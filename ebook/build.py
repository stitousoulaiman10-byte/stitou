"""Assemble build/ebook.full.html from ebook.html + inline SVG illustrations.

Optional: drop your presenter image at img/avatar.png (or .jpg/.webp) and it
will be used on the cover and the welcome page.
"""
import base64, pathlib, re
from illustrations import S

ROOT = pathlib.Path(__file__).parent
html = (ROOT / "ebook.html").read_text(encoding="utf-8")

S["qr"] = (ROOT / "img/qr-channel.svg").read_text(encoding="utf-8").split("?>")[-1]

avatar = next((p for ext in ("png", "jpg", "jpeg", "webp")
               for p in [ROOT / f"img/avatar.{ext}"] if p.exists()), None)
if avatar:
    mime = "image/jpeg" if avatar.suffix in (".jpg", ".jpeg") else f"image/{avatar.suffix[1:]}"
    uri = f"data:{mime};base64,{base64.b64encode(avatar.read_bytes()).decode()}"
    cover = f'<img class="avatar-photo" src="{uri}" alt="">'
    small = f'<img src="{uri}" alt="" style="width:100%;aspect-ratio:1;object-fit:cover;border-radius:50%;border:1mm solid var(--g5)">'
else:
    cover, small = "", S["doctor"]

habits = ["تمرين الـ60 ثانية", "مشي (الدقائق)", "8 أكواب ماء", "خضار ورقية",
          "نوم 7 ساعات+", "حفظ / تمرين ذهني", "تواصل مع شخص"]

def tracker_block(start):
    days = range(start, start + 15)
    head = "<tr><th>العادة</th>" + "".join(f"<th>{d}</th>" for d in days) + "</tr>"
    rows = "".join(f'<tr><td class="h">{h}</td>' + "<td></td>" * 15 + "</tr>" for h in habits)
    return f'<table class="tracker">{head}{rows}</table>'

tracker = tracker_block(1) + tracker_block(16)

html = html.replace("{{tracker}}", tracker)
html = html.replace("{{avatar_cover}}", cover).replace("{{avatar_small}}", small)
html = re.sub(r"\{\{svg:([\w-]+)\}\}", lambda m: S[m.group(1)], html)
assert "{{" not in html, re.findall(r"\{\{.*?\}\}", html)

out = ROOT / "build" / "ebook.full.html"
out.write_text(html, encoding="utf-8")
print("wrote", out)
