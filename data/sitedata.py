# Site-wide data for the CLIAVE portal.
# Module titles and UI strings in cs, ro, sr, sl were translated for this site and should be
# checked by the partners (see REVIEW.md).

LANGS = ['en', 'tr', 'cs', 'ro', 'sr', 'sl']
LANG_NAMES = {'en': 'English', 'tr': 'Türkçe', 'cs': 'Čeština', 'ro': 'Română', 'sr': 'Српски', 'sl': 'Slovenščina'}
HTML_LANG = {'en': 'en', 'tr': 'tr', 'cs': 'cs', 'ro': 'ro', 'sr': 'sr-Cyrl', 'sl': 'sl'}

PARTNERS = {
    'AHCRI': dict(name='Atatürk Horticultural Central Research Institute', country='Türkiye', city='Yalova', role='Coordinator',
                  people=['Erdinç Uysal', 'Emre Bilen', 'Özlem Boztepe'], logo='ahcri.png', url='https://arastirma.tarimorman.gov.tr/ataturkbahce'),
    'BSEU': dict(name='Bilecik Şeyh Edebali University', country='Türkiye', city='Bilecik', role='Partner',
                 people=['Burçin Atılgan Türkmen', 'Levent Burgu'], logo='bseu.png', url='https://www.bilecik.edu.tr'),
    'JCU': dict(name='University of South Bohemia in České Budějovice', country='Czech Republic', city='České Budějovice', role='Partner',
                people=['Jaroslav Bernas', 'Petr Konvalina', 'Jaroslav Neumann'], logo='jcu.png', url='https://www.jcu.cz'),
    'UASVM': dict(name='Iași University of Life Sciences', country='Romania', city='Iași', role='Partner',
                  people=['Iuliana Motrescu', 'Daniel Bucur', 'Vasile Stoleru'], logo='iuls.png', url='https://www.iuls.ro'),
    'KGZS': dict(name='Institute of Agriculture and Forestry Maribor', country='Slovenia', city='Maribor', role='Partner',
                 people=['Katarina Kresnik', 'Jože Miklavc', 'Stanka Klemenčič'], logo='kgzs.png', url='https://www.kgz-maribor.si'),
    'IAH': dict(name='Institute for Animal Husbandry', country='Serbia', city='Belgrade-Zemun', role='Partner',
                people=['Dušica Ostojić Andrić', 'Ljiljana Samolovac', 'Dragan Nikšić'], logo='iah.png', url='https://www.istocar.bg.ac.rs'),
}

MODULES = {
    1: dict(partner='JCU', pr='PR-2', icon='crop', authors='Jaroslav Bernas, Petr Konvalina, Jaroslav Neumann', title={
        'en': 'Climate Resilient Cropping Systems',
        'tr': 'İklime Dayanıklı Bitkisel Üretim Sistemleri',
        'cs': 'Systémy pěstování plodin odolné vůči změně klimatu',
        'ro': 'Sisteme de cultură rezistente la schimbările climatice',
        'sr': 'Системи гајења усева отпорни на климатске промене',
        'sl': 'Na podnebne spremembe odporni sistemi pridelave'}),
    2: dict(partner='AHCRI', pr='PR-3', icon='soil', authors='Erdinç Uysal', title={
        'en': 'Greenhouse Gas Emissions from Land and Fertilizer Use and Protection Measures Against Climate Change',
        'tr': 'Arazi ve Gübre Kullanımından Kaynaklanan Sera Gazı Emisyonları ve İklim Değişikliğine Karşı Koruma Önlemleri',
        'cs': 'Emise skleníkových plynů z využívání půdy a hnojiv a ochranná opatření proti změně klimatu',
        'ro': 'Emisiile de gaze cu efect de seră din utilizarea terenurilor și a îngrășămintelor și măsuri de protecție împotriva schimbărilor climatice',
        'sr': 'Емисије гасова са ефектом стаклене баште из коришћења земљишта и ђубрива и мере заштите од климатских промена',
        'sl': 'Emisije toplogrednih plinov zaradi rabe zemljišč in gnojil ter ukrepi za zaščito pred podnebnimi spremembami'}),
    3: dict(partner='UASVM', pr='PR-4', icon='water', authors='Iuliana Motrescu', title={
        'en': 'Use of New Technologies in Irrigation for Sustainable Production and Protection of Water Resources under Climate Change Conditions',
        'tr': 'İklim Değişikliği Koşullarında Sürdürülebilir Üretim ve Su Kaynaklarının Korunması için Sulamada Yeni Teknolojiler',
        'cs': 'Nové technologie v zavlažování pro udržitelnou produkci a ochranu vodních zdrojů v podmínkách změny klimatu',
        'ro': 'Noi tehnologii de irigare pentru o producție durabilă și protecția resurselor de apă în condițiile schimbărilor climatice',
        'sr': 'Нове технологије у наводњавању за одрживу производњу и заштиту водних ресурса у условима климатских промена',
        'sl': 'Nove tehnologije namakanja za trajnostno pridelavo in varstvo vodnih virov v razmerah podnebnih sprememb'}),
    4: dict(partner='KGZS', pr='PR-5', icon='leaf', authors='Boštjan Matko, Stanka Klemenčič', title={
        'en': 'Integrated Pest Management Recommendations to Cope with Climate Change Challenges',
        'tr': 'İklim Değişikliğinin Getirdiği Sorunlarla Başa Çıkmak için Entegre Mücadele Önerileri',
        'cs': 'Doporučení integrované ochrany rostlin pro zvládání výzev změny klimatu',
        'ro': 'Recomandări de management integrat al dăunătorilor pentru a face față provocărilor schimbărilor climatice',
        'sr': 'Препоруке интегралне заштите биља за суочавање са изазовима климатских промена',
        'sl': 'Priporočila za integrirano varstvo rastlin ob izzivih podnebnih sprememb'}),
    5: dict(partner='IAH', pr='PR-6', icon='cow', authors='Dušica Ostojić Andrić, Ljiljana Samolovac, Dragan Nikšić', title={
        'en': 'Livestock under Climate Change Conditions: Impacts, Mitigation and Adaptation',
        'tr': 'İklim Değişikliği Koşullarında Hayvancılık: Etkiler, Azaltım ve Uyum',
        'cs': 'Hospodářská zvířata v podmínkách změny klimatu: dopady, zmírňování a adaptace',
        'ro': 'Creșterea animalelor în condițiile schimbărilor climatice: impact, atenuare și adaptare',
        'sr': 'Сточарство у условима климатских промена: утицаји, ублажавање и прилагођавање',
        'sl': 'Živinoreja v razmerah podnebnih sprememb: vplivi, blaženje in prilagajanje'}),
    6: dict(partner='BSEU', pr='PR-7', icon='sun', authors='Burçin Atılgan Türkmen, Levent Burgu', title={
        'en': 'Energy Efficiency Improvements and Renewable Energy Supply in the Agricultural Sector',
        'tr': 'Tarım Sektöründe Enerji Verimliliğinin Artırılması ve Yenilenebilir Enerji Arzı',
        'cs': 'Zvyšování energetické účinnosti a dodávky obnovitelné energie v zemědělství',
        'ro': 'Îmbunătățirea eficienței energetice și aprovizionarea cu energie regenerabilă în sectorul agricol',
        'sr': 'Унапређење енергетске ефикасности и снабдевање обновљивом енергијом у пољопривреди',
        'sl': 'Izboljšanje energetske učinkovitosti in oskrba z obnovljivo energijo v kmetijstvu'}),
}

DISCLAIMER = {
    'en': "The European Commission's support for the production of this publication does not constitute an endorsement of the contents, which reflect the views only of the authors, and the Commission cannot be held responsible for any use which may be made of the information contained therein.",
    'tr': "Erasmus+ Programı kapsamında Avrupa Komisyonu tarafından desteklenmektedir. Ancak burada yer alan görüşlerden Avrupa Komisyonu ve Türkiye Ulusal Ajansı sorumlu tutulamaz.",
    'cs': "Podpora Evropské komise pro produkci této publikace nepředstavuje souhlas s obsahem, který odráží pouze názory autorů, a Komise nenese odpovědnost za jakékoli použití informací v ní obsažených.",
    'ro': "Conținutul prezentului material reprezintă responsabilitatea exclusivă a autorilor, iar Comisia Europeană nu este responsabilă pentru modul în care va fi folosit conținutul informației.",
    'sr': "Подршка Европске комисије за производњу ове публикације не представља одобрење за садржај који одражава само ставове аутора и Комисија не може бити одговорна за било какву употребу информација садржаних у њој.",
    'sl': "Podpora Evropske komisije pri pripravi te publikacije ne pomeni odobritve vsebine, ki odraža zgolj stališča avtorjev, in Komisija ne odgovarja za kakršno koli uporabo informacij, ki jih vsebuje.",
}

T = {
 'tagline': {'en':'Climate Focused Agricultural Vocational Education','tr':'İklim Odaklı Tarımsal Mesleki Eğitim','cs':'Odborné zemědělské vzdělávání zaměřené na klima','ro':'Educație profesională agricolă axată pe climă','sr':'Пољопривредно стручно образовање усмерено на климу','sl':'Na podnebje osredotočeno kmetijsko poklicno izobraževanje'},
 'nav_modules': {'en':'Learning modules','tr':'Eğitim modülleri','cs':'Výukové moduly','ro':'Module de învățare','sr':'Модули за учење','sl':'Učni moduli'},
 'nav_book': {'en':'Book','tr':'Kitap','cs':'Kniha','ro':'Carte','sr':'Књига','sl':'Knjiga'},
 'nav_about': {'en':'About','tr':'Proje','cs':'O projektu','ro':'Despre proiect','sr':'О пројекту','sl':'O projektu'},
 'nav_news': {'en':'News','tr':'Haberler','cs':'Novinky','ro':'Noutăți','sr':'Вести','sl':'Novice'},
 'hero_title': {'en':'Agriculture in a changing climate','tr':'Değişen iklimde tarım','cs':'Zemědělství v měnícím se klimatu','ro':'Agricultura într-un climat în schimbare','sr':'Пољопривреда у клими која се мења','sl':'Kmetijstvo v spreminjajočem se podnebju'},
 'hero_text': {'en':'Six open learning modules for agricultural students and professionals. Free, in six languages, no registration needed.',
               'tr':'Tarım öğrencileri ve profesyonelleri için altı açık eğitim modülü. Ücretsiz, altı dilde, kayıt gerektirmez.',
               'cs':'Šest otevřených výukových modulů pro studenty a odborníky v zemědělství. Zdarma, v šesti jazycích, bez registrace.',
               'ro':'Șase module de învățare deschise pentru studenți și profesioniști din agricultură. Gratuit, în șase limbi, fără înregistrare.',
               'sr':'Шест отворених модула за учење намењених студентима и стручњацима у пољопривреди. Бесплатно, на шест језика, без регистрације.',
               'sl':'Šest odprtih učnih modulov za študente in strokovnjake v kmetijstvu. Brezplačno, v šestih jezikih, brez registracije.'},
 'start': {'en':'Start learning','tr':'Öğrenmeye başla','cs':'Začít studovat','ro':'Începe să înveți','sr':'Почни да учиш','sl':'Začni z učenjem'},
 'get_book': {'en':'Download the book','tr':'Kitabı indir','cs':'Stáhnout knihu','ro':'Descarcă cartea','sr':'Преузми књигу','sl':'Prenesi knjigo'},
 'stat_modules': {'en':'learning modules','tr':'eğitim modülü','cs':'výukových modulů','ro':'module de învățare','sr':'модула','sl':'učnih modulov'},
 'stat_chapters': {'en':'chapters','tr':'bölüm','cs':'kapitol','ro':'capitole','sr':'поглавља','sl':'poglavij'},
 'stat_langs': {'en':'languages','tr':'dil','cs':'jazyků','ro':'limbi','sr':'језика','sl':'jezikov'},
 'stat_partners': {'en':'partners in 5 countries','tr':'ortak, 5 ülke','cs':'partnerů z 5 zemí','ro':'parteneri din 5 țări','sr':'партнера из 5 земаља','sl':'partnerjev iz 5 držav'},
 'module': {'en':'Module','tr':'Modül','cs':'Modul','ro':'Modulul','sr':'Модул','sl':'Modul'},
 'chapter': {'en':'Chapter','tr':'Bölüm','cs':'Kapitola','ro':'Capitolul','sr':'Поглавље','sl':'Poglavje'},
 'chapters_in': {'en':'chapters','tr':'bölüm','cs':'kapitol','ro':'capitole','sr':'поглавља','sl':'poglavij'},
 'min': {'en':'min','tr':'dk','cs':'min','ro':'min','sr':'мин','sl':'min'},
 'overview': {'en':'Module overview','tr':'Modüle genel bakış','cs':'Přehled modulu','ro':'Prezentarea modulului','sr':'Преглед модула','sl':'Pregled modula'},
 'contents': {'en':'On this page','tr':'Bu sayfada','cs':'Na této stránce','ro':'Pe această pagină','sr':'На овој страници','sl':'Na tej strani'},
 'chapters_list': {'en':'Chapters','tr':'Bölümler','cs':'Kapitoly','ro':'Capitole','sr':'Поглавља','sl':'Poglavja'},
 'prev': {'en':'Previous','tr':'Önceki','cs':'Předchozí','ro':'Anterior','sr':'Претходно','sl':'Prejšnje'},
 'next': {'en':'Next','tr':'Sonraki','cs':'Další','ro':'Următorul','sr':'Следеће','sl':'Naslednje'},
 'authors': {'en':'Authors','tr':'Yazarlar','cs':'Autoři','ro':'Autori','sr':'Аутори','sl':'Avtorji'},
 'prepared_by': {'en':'Prepared by','tr':'Hazırlayan','cs':'Připravil','ro':'Elaborat de','sr':'Припремио','sl':'Pripravil'},
 'downloads': {'en':'Downloads','tr':'İndirmeler','cs':'Ke stažení','ro':'Descărcări','sr':'Преузимања','sl':'Prenosi'},
 'slides': {'en':'Presentation slides (PDF)','tr':'Sunum slaytları (PDF)','cs':'Prezentace (PDF)','ro':'Prezentare (PDF)','sr':'Презентација (PDF)','sl':'Predstavitev (PDF)'},
 'book_full': {'en':'Book of CLIAVE (PDF)','tr':'CLIAVE Kitabı (PDF)','cs':'Kniha CLIAVE (PDF)','ro':'Cartea CLIAVE (PDF)','sr':'Књига CLIAVE (PDF)','sl':'Knjiga CLIAVE (PDF)'},
 'not_available': {'en':'This chapter is not yet available in English. You can read it in:','tr':'Bu bölüm henüz Türkçe olarak hazır değil. Şu dillerde okuyabilirsiniz:','cs':'Tato kapitola zatím není k dispozici v češtině. Můžete si ji přečíst v jazyce:','ro':'Acest capitol nu este încă disponibil în limba română. Îl puteți citi în:','sr':'Ово поглавље још није доступно на српском. Можете га прочитати на:','sl':'To poglavje še ni na voljo v slovenščini. Preberete ga lahko v jeziku:'},
 'unavailable_badge': {'en':'other language','tr':'başka dilde','cs':'jiný jazyk','ro':'altă limbă','sr':'други језик','sl':'drug jezik'},
 'read_in': {'en':'Read this page in','tr':'Bu sayfayı oku:','cs':'Číst v jazyce','ro':'Citește în','sr':'Читај на','sl':'Beri v jeziku'},
 'all_modules': {'en':'All modules','tr':'Tüm modüller','cs':'Všechny moduly','ro':'Toate modulele','sr':'Сви модули','sl':'Vsi moduli'},
 'modules_intro': {'en':'Each module has eight chapters, written by specialists from the partner institutions and translated into all project languages. Read online, download the slides, or use them in your own teaching.',
                   'tr':'Her modül, ortak kurumların uzmanlarınca yazılmış ve tüm proje dillerine çevrilmiş sekiz bölümden oluşur. Çevrimiçi okuyabilir, slaytları indirebilir ya da kendi derslerinizde kullanabilirsiniz.',
                   'cs':'Každý modul má osm kapitol, které napsali odborníci z partnerských institucí a které byly přeloženy do všech jazyků projektu. Čtěte online, stáhněte si prezentace nebo je využijte ve vlastní výuce.',
                   'ro':'Fiecare modul are opt capitole, scrise de specialiști din instituțiile partenere și traduse în toate limbile proiectului. Citiți online, descărcați prezentările sau folosiți-le în propriile cursuri.',
                   'sr':'Сваки модул има осам поглавља која су написали стручњаци партнерских институција и која су преведена на све језике пројекта. Читајте на мрежи, преузмите презентације или их користите у сопственој настави.',
                   'sl':'Vsak modul ima osem poglavij, ki so jih napisali strokovnjaki partnerskih ustanov in so prevedena v vse jezike projekta. Berite na spletu, prenesite predstavitve ali jih uporabite pri svojem poučevanju.'},
 'book_intro': {'en':'All six learning modules are also published as a single open-access book with an ISBN, for offline reading and printing.',
                'tr':'Altı eğitim modülünün tamamı, çevrimdışı okuma ve baskı için ISBN numaralı, açık erişimli tek bir kitap olarak da yayımlanmıştır.',
                'cs':'Všech šest výukových modulů je také vydáno jako jedna volně dostupná kniha s ISBN pro čtení offline a tisk.',
                'ro':'Toate cele șase module sunt publicate și ca o singură carte în acces deschis, cu ISBN, pentru citire offline și tipărire.',
                'sr':'Свих шест модула објављено је и као једна књига отвореног приступа са ISBN бројем, за читање ван мреже и штампу.',
                'sl':'Vseh šest učnih modulov je objavljenih tudi kot ena prosto dostopna knjiga z ISBN za branje brez povezave in tiskanje.'},
 'book_langs_note': {'en':'Available in English and Romanian.','tr':'İngilizce ve Romence olarak mevcuttur.','cs':'K dispozici v angličtině a rumunštině.','ro':'Disponibilă în engleză și română.','sr':'Доступно на енглеском и румунском.','sl':'Na voljo v angleščini in romunščini.'},
 'news_note': {'en':'Project news, 2022–2024.','tr':'Proje haberleri, 2022–2024 (İngilizce).','cs':'Novinky z projektu, 2022–2024 (anglicky).','ro':'Noutăți despre proiect, 2022–2024 (în engleză).','sr':'Вести о пројекту, 2022–2024 (на енглеском).','sl':'Novice projekta, 2022–2024 (v angleščini).'},
 'latest_news': {'en':'From the project','tr':'Projeden','cs':'Z projektu','ro':'Din proiect','sr':'Из пројекта','sl':'Iz projekta'},
 'all_news': {'en':'All news','tr':'Tüm haberler','cs':'Všechny novinky','ro':'Toate noutățile','sr':'Све вести','sl':'Vse novice'},
 'partners': {'en':'Partners','tr':'Ortaklar','cs':'Partneři','ro':'Parteneri','sr':'Партнери','sl':'Partnerji'},
 'funded': {'en':'Funded by the European Union','tr':'Avrupa Birliği tarafından finanse edilmektedir','cs':'Financováno Evropskou unií','ro':'Finanțat de Uniunea Europeană','sr':'Финансира Европска унија','sl':'Financira Evropska unija'},
 'license': {'en':'Open access. Content may be reused for non-commercial educational purposes with attribution.','tr':'Açık erişim. İçerik, kaynak gösterilerek ticari olmayan eğitim amaçlarıyla kullanılabilir.','cs':'Volně dostupné. Obsah lze s uvedením zdroje využít k nekomerčním vzdělávacím účelům.','ro':'Acces deschis. Conținutul poate fi reutilizat în scopuri educaționale necomerciale, cu citarea sursei.','sr':'Отворени приступ. Садржај се може користити у некомерцијалне образовне сврхе уз навођење извора.','sl':'Prosto dostopno. Vsebino je mogoče ob navedbi vira uporabiti v nekomercialne izobraževalne namene.'},
 'selfcheck': {'en':'Check your understanding','tr':'Kendini dene','cs':'Ověřte si porozumění','ro':'Verifică-ți cunoștințele','sr':'Проверите своје разумевање','sl':'Preverite svoje razumevanje'},
 'check': {'en':'Check','tr':'Kontrol et','cs':'Zkontrolovat','ro':'Verifică','sr':'Провери','sl':'Preveri'},
 'correct': {'en':'Correct.','tr':'Doğru.','cs':'Správně.','ro':'Corect.','sr':'Тачно.','sl':'Pravilno.'},
 'incorrect': {'en':'Not quite.','tr':'Tam değil.','cs':'Ne úplně.','ro':'Nu chiar.','sr':'Не баш.','sl':'Ne povsem.'},
 'about_title': {'en':'About the project','tr':'Proje hakkında','cs':'O projektu','ro':'Despre proiect','sr':'О пројекту','sl':'O projektu'},
 'skip': {'en':'Skip to content','tr':'İçeriğe geç','cs':'Přejít na obsah','ro':'Salt la conținut','sr':'Пређи на садржај','sl':'Preskoči na vsebino'},
 'language': {'en':'Language','tr':'Dil','cs':'Jazyk','ro':'Limba','sr':'Језик','sl':'Jezik'},
 'menu': {'en':'Menu','tr':'Menü','cs':'Menu','ro':'Meniu','sr':'Мени','sl':'Meni'},
 'search_ph': {'en':'Search the modules…','tr':'Modüllerde ara…','cs':'Hledat v modulech…','ro':'Caută în module…','sr':'Претражи модуле…','sl':'Išči po modulih…'},
}

ABOUT = {
 'en': [
  "Agriculture is one of the sectors most exposed to climate change, and also one that can do much to reduce it. Agricultural professionals who advise and train farmers are key to a fast adaptation process. CLIAVE was designed to train these trainers: to modernise agricultural vocational education so that students and professionals are prepared for production under changing climate conditions.",
  "Between 2022 and 2024, six institutions from Türkiye, the Czech Republic, Romania, Slovenia and Serbia surveyed 376 students and professionals on their knowledge of climate change, developed six learning modules based on the results, tested them in pilot trainings and multiplier events, and published them openly online and as a book.",
 ],
 'tr': [
  "Tarım, iklim değişikliğinden en çok etkilenen sektörlerden biri olduğu kadar, onu azaltmak için de en çok şey yapabilecek sektörlerden biridir. Üreticilere danışmanlık ve eğitim veren tarım profesyonelleri, hızlı bir uyum sürecinin anahtarıdır. CLIAVE, bu eğiticileri eğitmek; tarımsal mesleki eğitimi, öğrencileri ve profesyonelleri değişen iklim koşullarında üretime hazırlayacak biçimde güncellemek amacıyla tasarlandı.",
  "2022–2024 yıllarında Türkiye, Çekya, Romanya, Slovenya ve Sırbistan'dan altı kurum, 376 öğrenci ve profesyonelin iklim değişikliği bilgisini anketle ölçtü; sonuçlara dayanarak altı eğitim modülü geliştirdi, bunları pilot eğitimlerde ve yaygınlaştırma etkinliklerinde sınadı ve çevrimiçi ile kitap olarak açık erişimle yayımladı.",
 ],
}

PROJECT_FACTS = [
 ('Programme', 'Erasmus+ — KA220-VET, Cooperation partnerships in vocational education and training'),
 ('Project number', '2021-1-TR01-KA220-VET-000032974'),
 ('Duration', '28 February 2022 – 27 August 2024 (30 months)'),
 ('Coordinator', 'Atatürk Horticultural Central Research Institute, Yalova, Türkiye'),
 ('National Agency', 'Turkish National Agency (Centre for EU Education and Youth Programmes)'),
]
