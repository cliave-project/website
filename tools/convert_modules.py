"""Convert CLIAVE learning-module .docx files into HTML fragments + JSON metadata.
Usage: python convert_modules.py <Learning Modules dir> <output repo dir>
Output: content/modules/m{N}/{lang}/{ch}.html, content/modules/index.json, static/img/lm/*.webp
"""
import sys, os, re, json, glob, hashlib, subprocess, tempfile, shutil, unicodedata
from bs4 import BeautifulSoup, NavigableString
from PIL import Image

SRC, OUT = sys.argv[1], sys.argv[2]
LANG = {'ces':'cs','eng':'en','ron':'ro','srp':'sr','srb':'sr','slv':'sl','tur':'tr','еng':'en'}
MOD = {'PR-2':1,'PR-3':2,'PR-4':3,'PR-5':4,'PR-6':5,'PR-7':6}
IMGDIR = os.path.join(OUT,'static','img','lm'); os.makedirs(IMGDIR, exist_ok=True)
REF_WORDS = ('reference','kaynak','literatur','literatúr','bibliograf','литератур','izvor','viri','zdroj','referin','referenc')

def lower_lang(s, lang):
    if lang=='tr': s = s.replace('I','ı').replace('İ','i')
    return s.lower()

def tidy_title(t, lang):
    t = ' '.join(t.split())
    letters = [c for c in t if c.isalpha()]
    if letters and sum(c.isupper() for c in letters)/len(letters) > 0.8:
        low = lower_lang(t, lang)
        first = low[0].upper() if not (lang=='tr' and low[0]=='i') else 'İ'
        t = first + low[1:]
        # keep chemical formulae / acronyms that were uppercase in context
        t = re.sub(r'\b(ghg|ipm|co2|n2o|ch4|dss|eu|fao|ipcc|gis|ict)\b', lambda m: m.group(0).upper(), t, flags=re.I)
    return t

def save_img(path):
    data = open(path,'rb').read()
    h = hashlib.sha1(data).hexdigest()[:14]
    dst = os.path.join(IMGDIR, h + '.webp')
    if not os.path.exists(dst):
        try:
            im = Image.open(path)
            if im.mode in ('P','LA','RGBA'): im = im.convert('RGBA')
            else: im = im.convert('RGB')
            im.thumbnail((1400, 1400))
            im.save(dst, 'WEBP', quality=80, method=5)
        except Exception as e:
            print('  img fail', path, e); return None, None
    w, hgt = Image.open(dst).size
    return 'img/lm/' + h + '.webp', (w, hgt)

def convert(docx, lang):
    tmp = tempfile.mkdtemp()
    html = subprocess.run(['pandoc', docx, '-t', 'html5', '--wrap=none', f'--extract-media={tmp}'],
                          capture_output=True, text=True).stdout
    soup = BeautifulSoup(html, 'html.parser')
    # images
    for img in soup.find_all('img'):
        src = img.get('src','')
        if src.lower().endswith(('.emf','.wmf')):
            png = os.path.splitext(src)[0] + '.png'
            subprocess.run(['soffice','--headless','--convert-to','png','--outdir',os.path.dirname(src),src], capture_output=True)
            src = png if os.path.exists(png) else src
        rel, size = save_img(src) if os.path.exists(src) else (None, None)
        if not rel: img.decompose(); continue
        new = soup.new_tag('img', src='{{ROOT}}' + rel, loading='lazy', alt='')
        new['width'], new['height'] = size
        img.replace_with(new)
    # figure + caption: paragraph containing an img, caption text in same/next paragraph
    for p in list(soup.find_all('p')):
        imgs = p.find_all('img')
        if not imgs: continue
        cap_html = ''.join(str(c) for c in p.contents if not (getattr(c,'name',None)=='img')).strip()
        nxt = p.find_next_sibling()
        if not BeautifulSoup(cap_html,'html.parser').get_text(strip=True) and nxt is not None and nxt.name=='p' and not nxt.find('img'):
            txt = nxt.get_text(' ', strip=True)
            if re.match(r'^(fig|slika|obr|şekil|sekil|figura|grafikon|слика|graf|diagram|imagine|chart)', txt, re.I) and len(txt) < 400:
                cap_html = nxt.decode_contents(); nxt.decompose()
        fig = soup.new_tag('figure')
        for im in imgs: fig.append(im.extract())
        if BeautifulSoup(cap_html,'html.parser').get_text(strip=True):
            fc = soup.new_tag('figcaption'); fc.append(BeautifulSoup(cap_html,'html.parser')); fig.append(fc)
        p.replace_with(fig)
    # table captions (paragraph right before a table starting with Table/Tablo/...)
    for t in soup.find_all('table'):
        for a in ['style','class']: t.attrs.pop(a, None)
        for el in t.find_all(True): el.attrs.pop('style', None)
        wrap = soup.new_tag('div', attrs={'class':'table-wrap'})
        t.wrap(wrap)
    for el in soup.find_all(['col','colgroup']): el.decompose()
    for el in soup.find_all(True):
        if el.attrs: el.attrs.pop('style', None)
    # headings: first h1 is chapter title; drop module-name h1s ("PR-5 ...")
    for h in soup.find_all('h1'):
        if re.match(r'^\s*PR-\d', h.get_text()): h.decompose()
    def is_caps(t):
        L=[c for c in t if c.isalpha()]
        return len(L)>=4 and sum(c.isupper() for c in L)/len(L)>0.85 and len(t)<220
    top = [el for el in soup.contents if getattr(el,'name',None)]
    if top and not soup.find('h1'):
        t0 = top[0].get_text(' ',strip=True)
        if top[0].name in ('h2','h3','h4') or (top[0].name=='p' and (is_caps(t0) or (len(t0)<160 and not t0.endswith('.')))):
            top[0].name='h1'
    for mk in soup.find_all(['mark','span','u']): mk.unwrap()
    for p_ in soup.find_all('p', recursive=False):
        t=p_.get_text(' ',strip=True)
        if is_caps(t) and len(t)<120 and not p_.find('img'): p_.name='h2'
    h1 = soup.find(['h1'])
    title = tidy_title(h1.get_text(' ', strip=True), lang) if h1 else ''
    if h1: h1.decompose()
    # demote: h1->h2, h2->h3, h3->h4
    for lvl in (3,2,1):
        for h in soup.find_all(f'h{lvl}'): h.name = f'h{lvl+1}'
    toc, used = [], set()
    top_lvl = 'h2' if soup.find('h2') else 'h3'
    for h in soup.find_all(['h2','h3','h4']):
        txt = tidy_title(h.get_text(' ', strip=True), lang)
        h.string = txt
        base = re.sub(r'[^\w]+','-', ''.join(c for c in unicodedata.normalize('NFKD', txt.lower()) if unicodedata.category(c)!='Mn')).strip('-')[:50] or 's'
        hid, k = base, 2
        while hid in used: hid = f'{base}-{k}'; k += 1
        used.add(hid); h['id'] = hid
        if any(w in txt.lower() for w in REF_WORDS) and h.name==top_lvl:
            h['class'] = 'refs-heading'
            sib = h.find_next_sibling()
            if sib is not None and sib.name in ('ol','ul'): sib['class'] = 'refs'
        if h.name==top_lvl: toc.append({'id':hid,'t':txt})
    # remove empty paragraphs
    for p in soup.find_all('p'):
        if not p.get_text(strip=True) and not p.find(['img','figure']): p.decompose()
    words = len(soup.get_text(' ').split())
    shutil.rmtree(tmp, ignore_errors=True)
    return title, str(soup), toc, words

index = {}
files = sorted(glob.glob(os.path.join(SRC, 'PR-*', '*.docx')))
for f in files:
    b = os.path.basename(f)
    m = re.match(r'(PR-\d) - (\d)\s+\[(\S+)\]\.docx', b)
    if not m: print('skip', b); continue
    mod, ch, lang = MOD[m.group(1)], int(m.group(2)), LANG.get(m.group(3))
    if not lang: print('skip lang', b); continue
    title, body, toc, words = convert(f, lang)
    if words < 60: print('  empty', b, words); continue
    d = os.path.join(OUT, 'content', 'modules', f'm{mod}', lang); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, f'{ch}.html'), 'w').write(body)
    index.setdefault(str(mod), {}).setdefault(lang, {})[str(ch)] = {'title': title, 'toc': toc, 'words': words}
    print(f'm{mod} ch{ch} {lang} {words}w "{title[:60]}"')
json.dump(index, open(os.path.join(OUT,'content','modules','index.json'),'w'), ensure_ascii=False, indent=1)
