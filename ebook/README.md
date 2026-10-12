# SehaNova ebook — «ذاكرة أقوى في 30 يومًا»

A 37-page illustrated Arabic (RTL) ebook in A5 format for the SehaNova | صحة نوفا YouTube channel.

- **Ready-to-sell PDF:** `ذاكرة-أقوى-في-30-يوما-SehaNova.pdf`
- **Cover image** for the sales page and thumbnails: `cover.png` (1680×2382)
- **How to sell it** (audience, pricing, platforms, funnel, Arabic sales copy): `MARKETING.md`

## Edit and rebuild

| File | What it holds |
|---|---|
| `ebook.html` | All text and page layout, one `<section class="page">` per page |
| `style.css` | Design: colours, typography, components |
| `illustrations.py` | Every illustration, as inline SVG |
| `fonts/` | Cairo, Tajawal and Amiri (Google Fonts, OFL), bundled for offline builds |

```bash
python3 build.py                                   # -> build/ebook.full.html
PLAYWRIGHT_PATH=/path/to/node_modules/playwright \
  node render.mjs "ذاكرة-أقوى-في-30-يوما-SehaNova.pdf" --previews --cover
```

`render.mjs` prints a warning for any page whose content overflows. Shorten that page's text until it reports `overflowing: none`.

### Use your AI presenter's image

Save it as `img/avatar.png` (or `.jpg` / `.webp`) and rebuild. It then appears on the cover and in the welcome letter, replacing the drawn doctor illustration.
