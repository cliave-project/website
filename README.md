# CLIAVE — Climate Focused Agricultural Vocational Education

Open learning portal of the Erasmus+ project CLIAVE (2021-1-TR01-KA220-VET-000032974), 2022–2024.
Six learning modules × eight chapters, in English, Turkish, Czech, Romanian, Serbian and Slovenian. No registration.

Live site: https://www.cliave.net

## Structure

| Path | What it is |
|---|---|
| `content/modules/m{N}/{lang}/{ch}.html` | Chapter texts converted from the original Word files (chapter 0 = module overview) |
| `content/modules/index.json` | Chapter titles, headings and word counts |
| `data/sitedata.py` | Partners, module titles, interface texts in six languages |
| `data/news.py` | Project news migrated from the old Google Sites page |
| `data/quizzes/` | Self-check questions per chapter (optional) |
| `templates/` | Page templates (Jinja2) |
| `static/` | CSS, JavaScript, images, PDF downloads |
| `tools/build.py` | Builds the site into `_site/` |
| `tools/convert_modules.py` | Re-converts the original .docx modules (needs pandoc, LibreOffice) |

## Build locally

```
pip install jinja2
python tools/build.py --base-url http://localhost:8000
cd _site && python -m http.server
```

Every push to `main` is built and published by GitHub Actions (`.github/workflows/pages.yml`).

## Licence and funding

Funded by the European Union. The European Commission's support for the production of this publication does not constitute an endorsement of the contents, which reflect the views only of the authors, and the Commission cannot be held responsible for any use which may be made of the information contained therein.
