// Render build/ebook.full.html -> PDF + page previews, and report overflowing pages.
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)(process.env.PLAYWRIGHT_PATH || 'playwright');
import path from 'node:path';
import fs from 'node:fs';

const root = path.dirname(new URL(import.meta.url).pathname);
const src = 'file://' + path.join(root, 'build/ebook.full.html');
const pdfOut = path.join(root, process.argv[2] || 'build/ebook.pdf');
const previews = process.argv.includes('--previews');

const browser = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
const page = await browser.newPage({ viewport: { width: 560, height: 794 }, deviceScaleFactor: 2 });
await page.goto(src, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);

const report = await page.evaluate(() => [...document.querySelectorAll('.page')].map((p, i) => {
  const box = p.getBoundingClientRect();
  let over = 0;
  for (const el of p.querySelectorAll('*')) {
    if (el.closest('.opener') || el.classList.contains('folio')) continue;
    const r = el.getBoundingClientRect();
    over = Math.max(over, r.bottom - (box.bottom - 13 * 3.78)); // keep clear of the folio
  }
  return { page: i + 1, over: Math.round(over) };
}));
const bad = report.filter(r => r.over > 0);
console.log(`${report.length} pages; overflowing:`, bad.length ? bad : 'none');
const fonts = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight));
console.log('fonts loaded:', [...new Set(fonts)].join(', '));

if (previews) {
  fs.mkdirSync(path.join(root, 'build/pages'), { recursive: true });
  const els = await page.$$('.page');
  for (let i = 0; i < els.length; i++)
    await els[i].screenshot({ path: path.join(root, `build/pages/p${String(i + 1).padStart(2, '0')}.png`) });
}
await page.emulateMedia({ media: 'print' });
await page.pdf({ path: pdfOut, preferCSSPageSize: true, printBackground: true });
console.log('wrote', pdfOut);
await browser.close();

// High-res cover image for the sales page / thumbnails.
if (process.argv.includes('--cover')) {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM || undefined });
  const pg = await b.newPage({ viewport: { width: 560, height: 794 }, deviceScaleFactor: 3 });
  await pg.goto(src, { waitUntil: 'networkidle' });
  await pg.evaluate(() => document.fonts.ready);
  await (await pg.$('.page.cover')).screenshot({ path: path.join(root, 'cover.png') });
  console.log('wrote cover.png');
  await b.close();
}
