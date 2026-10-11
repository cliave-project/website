"""Build the static CLIAVE portal into _site/.
Usage: python tools/build.py [--base-url https://www.cliave.net]
"""
import os, sys, json, shutil, re, math, glob, datetime, html
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'data'))
from sitedata import LANGS, LANG_NAMES, HTML_LANG, PARTNERS, MODULES, DISCLAIMER, T, ABOUT, PROJECT_FACTS  # noqa
from news import NEWS  # noqa

BASE_URL = 'https://www.cliave.net'
if '--base-url' in sys.argv: BASE_URL = sys.argv[sys.argv.index('--base-url') + 1].rstrip('/')
OUT = os.path.join(ROOT, '_site')
CONTENT = os.path.join(ROOT, 'content', 'modules')
INDEX = json.load(open(os.path.join(CONTENT, 'index.json')))
NEWS_MAP = json.load(open(os.path.join(ROOT, 'data', 'news_map.json')))
NEWS_PHOTOS = json.load(open(os.path.join(ROOT, 'data', 'news_photos.json'))) if os.path.exists(os.path.join(ROOT, 'data', 'news_photos.json')) else {}
DOWNLOADS = json.load(open(os.path.join(ROOT, 'data', 'downloads.json'))) if os.path.exists(os.path.join(ROOT, 'data', 'downloads.json')) else {}
CH_ORDER = [str(i) for i in range(1, 9)]

env = Environment(loader=FileSystemLoader(os.path.join(ROOT, 'templates')), autoescape=select_autoescape(['html']))

def t(key, lang):
    v = T[key]
    return v.get(lang) or v['en']

def chapter(mod, lang, ch):
    return INDEX.get(str(mod), {}).get(lang, {}).get(str(ch))

def chapter_title(mod, lang, ch):
    c = chapter(mod, lang, ch)
    if c and c['title']: return c['title'], lang
    for l in ['en'] + LANGS:
        c = chapter(mod, l, ch)
        if c and c['title']: return c['title'], l
    return '', lang

def read_minutes(words): return max(1, math.ceil(words / 200))

def langs_for(mod, ch):
    return [l for l in LANGS if chapter(mod, l, ch)]

PAGES = []  # (path, lang) for sitemap

def write(path, html_text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf-8').write(html_text)
    if path.endswith('index.html'): PAGES.append(path[:-10])

def render(tpl, path, lang, **ctx):
    depth = path.count('/')
    root = '/' if path == '404.html' else '../' * depth
    page_url = path[:-10] if path.endswith('index.html') else path
    alt = ctx.pop('alternates', None)
    if alt is None:
        alt = {l: re.sub(r'^[a-z]{2}/', f'{l}/', page_url) for l in LANGS}
    html_text = env.get_template(tpl).render(
        lang=lang, html_lang=HTML_LANG[lang], root=root, t=lambda k: t(k, lang), LANGS=LANGS, LANG_NAMES=LANG_NAMES,
        MODULES=MODULES, PARTNERS=PARTNERS, disclaimer=DISCLAIMER[lang], base_url=BASE_URL, page_url=page_url,
        alternates=alt, year=datetime.date.today().year, **ctx)
    write(path, html_text)

def module_card(mod, lang):
    m = MODULES[mod]
    chs = [c for c in CH_ORDER if chapter(mod, lang, c)]
    words = sum(chapter(mod, lang, c)['words'] for c in chs)
    return dict(n=mod, title=m['title'].get(lang, m['title']['en']), partner=PARTNERS[m['partner']], icon=m['icon'],
                chapters=len(CH_ORDER), available=len(chs), minutes=read_minutes(words), authors=m['authors'])

def load_body(mod, lang, ch):
    p = os.path.join(CONTENT, f'm{mod}', lang, f'{ch}.html')
    return open(p, encoding='utf-8').read() if os.path.exists(p) else None

def quiz_for(mod, lang, ch):
    p = os.path.join(ROOT, 'data', 'quizzes', f'm{mod}', f'{ch}.{lang}.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    shutil.copytree(os.path.join(ROOT, 'static'), OUT)
    for lang in LANGS:
        cards = [module_card(m, lang) for m in MODULES]
        total_ch = len(MODULES) * len(CH_ORDER)
        news_latest = sorted(NEWS, key=lambda n: NEWS_MAP[str(n['i'])][1], reverse=True)[:3]
        render('home.html', f'{lang}/index.html', lang, cards=cards, total_ch=total_ch,
               news=[news_item(n) for n in news_latest])
        render('modules.html', f'{lang}/modules/index.html', lang, cards=cards)
        render('book.html', f'{lang}/book/index.html', lang)
        render('about.html', f'{lang}/about/index.html', lang, about=ABOUT.get(lang, ABOUT['en']),
               facts=PROJECT_FACTS, cards=cards)
        render('news.html', f'{lang}/news/index.html', lang,
               news=[news_item(n) for n in sorted(NEWS, key=lambda n: NEWS_MAP[str(n['i'])][1], reverse=True)])
        for mod in MODULES:
            card = module_card(mod, lang)
            chs = []
            for c in CH_ORDER:
                title, tl = chapter_title(mod, lang, c)
                info = chapter(mod, lang, c) or chapter(mod, tl, c)
                chs.append(dict(n=int(c), title=title, title_lang=tl, here=bool(chapter(mod, lang, c)),
                                minutes=read_minutes(info['words']) if info else None))
            intro = load_body(mod, lang, '0') or load_body(mod, 'en', '0')
            intro_lang = lang if load_body(mod, lang, '0') else 'en'
            dl = DOWNLOADS.get(f'm{mod}', {})
            render('module.html', f'{lang}/modules/{mod}/index.html', lang, card=card, chapters=chs,
                   intro=fix_body(intro, f'{lang}/modules/{mod}/index.html') if intro else None, intro_lang=intro_lang,
                   slides=dl.get(lang) or None, slides_fallback=dl.get('en'))
            for i, c in enumerate(CH_ORDER):
                path = f'{lang}/modules/{mod}/{c}/index.html'
                info = chapter(mod, lang, c)
                avail = langs_for(mod, c)
                body = fix_body(load_body(mod, lang, c), path) if info else None
                title, tl = chapter_title(mod, lang, c)
                prev = dict(n=int(CH_ORDER[i-1]), title=chapter_title(mod, lang, CH_ORDER[i-1])[0]) if i > 0 else None
                nxt = dict(n=int(CH_ORDER[i+1]), title=chapter_title(mod, lang, CH_ORDER[i+1])[0]) if i < len(CH_ORDER) - 1 else None
                render('chapter.html', path, lang, card=card, chapters=chs, ch=int(c), title=title, title_lang=tl,
                       body=body, toc=info['toc'] if info else [], minutes=read_minutes(info['words']) if info else None,
                       avail=avail, prev=prev, next=nxt, quiz=quiz_for(mod, lang, c))
    # root redirect + 404
    render('root.html', 'index.html', 'en', alternates={l: f'{l}/' for l in LANGS})
    render('404.html', '404.html', 'en', alternates={l: f'{l}/' for l in LANGS})
    # sitemap, robots, CNAME
    with open(os.path.join(OUT, 'sitemap.xml'), 'w') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in PAGES:
            if p: f.write(f'  <url><loc>{BASE_URL}/{p}</loc></url>\n')
        f.write('</urlset>\n')
    open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n')
    if BASE_URL.endswith('cliave.net'): open(os.path.join(OUT, 'CNAME'), 'w').write(BASE_URL.split('//')[1] + '\n')
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    print('pages:', len(PAGES))

def fix_body(body, path):
    root = '../' * path.count('/')
    return body.replace('{{ROOT}}', root)

def news_item(n):
    folder, date = NEWS_MAP[str(n['i'])]
    d = datetime.date.fromisoformat(date)
    return dict(n, date=date, date_h=d.strftime('%-d %B %Y'), photos=NEWS_PHOTOS.get(str(n['i']), []), slug=f'news-{n["i"]}')

if __name__ == '__main__':
    build()
