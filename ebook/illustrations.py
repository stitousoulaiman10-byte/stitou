"""Flat vector illustrations for the SehaNova ebook.

Every illustration is inlined into the HTML at build time (so any text inside
uses the book's Arabic web fonts). Keys are referenced from ebook.html as
{{svg:name}}.
"""

G9 = "#0b3d2c"   # deep green
G7 = "#157347"   # brand green
G5 = "#2fa463"   # leaf green
G3 = "#8fd3a8"
G1 = "#e3f5ea"
RED = "#d93a2b"
YEL = "#f6b81a"
CREAM = "#fbf7ef"
INK = "#1d2a24"
SKIN = "#f1c7a5"
SKIN2 = "#e2a982"
BROWN = "#7a4a2a"
BLUE = "#2f6db5"

S = {}

S["logo"] = f"""<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg">
<circle cx="60" cy="60" r="56" fill="#fff" stroke="{G5}" stroke-width="6"/>
<circle cx="60" cy="60" r="47" fill="none" stroke="{G1}" stroke-width="3"/>
<path d="M60 92 C30 80 26 50 46 30 C52 48 60 54 60 54 C60 54 68 48 74 30 C94 50 90 80 60 92Z" fill="{G5}"/>
<path d="M60 92 C60 70 60 60 60 54" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M22 66 H44 L50 52 L58 80 L66 44 L72 66 H98" stroke="{G9}" stroke-width="4.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

# ---------------------------------------------------------------- brain hero
S["brain"] = f"""<svg viewBox="0 0 400 330" xmlns="http://www.w3.org/2000/svg">
<defs>
 <radialGradient id="bglow" cx="50%" cy="45%" r="55%"><stop offset="0" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
 <linearGradient id="bfill" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffd9e0"/><stop offset="1" stop-color="#f4a7b6"/></linearGradient>
</defs>
<circle cx="200" cy="160" r="160" fill="url(#bglow)"/>
<ellipse cx="292" cy="258" rx="50" ry="30" fill="#eb93a5"/>
<path d="M280 248 q12 8 24 0 M272 262 q20 10 40 0 M282 276 q14 6 28 0" stroke="#d27086" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M228 240 C232 270 236 290 246 318 L270 318 C262 292 258 266 258 238Z" fill="#e88aa0"/>
<path d="M110 250 C60 248 35 205 50 170 C25 140 40 95 80 88 C88 50 135 35 170 52 C195 28 250 30 268 55 C310 42 355 70 350 115 C380 135 375 185 345 200 C350 235 310 255 275 245 C255 268 215 270 195 252 C175 268 135 268 110 250Z" fill="url(#bfill)" stroke="#d27086" stroke-width="4"/>
<g stroke="#d27086" stroke-width="4" fill="none" stroke-linecap="round">
 <path d="M170 52 C165 80 185 90 178 115 C172 138 195 150 190 175"/>
 <path d="M268 55 C255 75 270 95 255 110"/>
 <path d="M80 88 C100 100 95 125 118 128"/>
 <path d="M50 170 C75 168 85 185 105 180"/>
 <path d="M345 200 C320 196 315 178 295 182"/>
 <path d="M350 115 C330 120 320 140 300 135"/>
 <path d="M130 215 C150 200 175 212 190 198 C210 182 235 196 255 186"/>
 <path d="M120 150 C140 140 150 160 165 150"/>
 <path d="M220 120 C240 110 250 130 275 125"/>
 <path d="M215 80 C228 92 222 104 232 112"/>
 <path d="M120 55 C125 70 115 80 125 92" opacity=".6"/>
</g>
<path d="M200 222 C188 206 196 188 214 190 C232 192 238 210 228 222 C222 230 214 226 216 218" stroke="{YEL}" stroke-width="8" fill="none" stroke-linecap="round"/>
<g stroke="#fff" stroke-width="3" stroke-dasharray="2 7" stroke-linecap="round" fill="none" opacity=".95">
 <path d="M110 120 L175 88 L250 90 L305 150 L240 160 L150 190 L110 120"/><path d="M175 88 L240 160"/>
</g>
<g fill="{YEL}" stroke="#fff" stroke-width="3">
 <circle cx="110" cy="120" r="9"/><circle cx="175" cy="88" r="9"/><circle cx="250" cy="90" r="9"/>
 <circle cx="305" cy="150" r="9"/><circle cx="150" cy="190" r="9"/><circle cx="240" cy="160" r="9"/>
</g>
<g transform="translate(330 40) rotate(25)"><path d="M0 0 C-22 -18 -18 -48 0 -62 C18 -48 22 -18 0 0Z" fill="{G5}"/><path d="M0 -8 V-50" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/></g>
<g transform="translate(62 70) rotate(-30)"><path d="M0 0 C-16 -14 -14 -36 0 -46 C14 -36 16 -14 0 0Z" fill="{G3}"/><path d="M0 -6 V-36" stroke="#fff" stroke-width="2" stroke-linecap="round"/></g>
</svg>"""

# labelled anatomy (labels drawn in HTML around it)
S["brain-map"] = f"""<svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="292" cy="238" rx="50" ry="30" fill="#eb93a5"/>
<path d="M228 220 C232 250 236 270 246 298 L270 298 C262 272 258 246 258 218Z" fill="#e88aa0"/>
<path d="M110 230 C60 228 35 185 50 150 C25 120 40 75 80 68 C88 30 135 15 170 32 C195 8 250 10 268 35 C310 22 355 50 350 95 C380 115 375 165 345 180 C350 215 310 235 275 225 C255 248 215 250 195 232 C175 248 135 248 110 230Z" fill="#fde3e8" stroke="#d27086" stroke-width="4"/>
<path d="M110 230 C60 228 35 185 50 150 C25 120 40 75 80 68 C88 40 110 28 130 26 C120 60 120 120 135 160 C140 190 128 215 110 230Z" fill="{G3}" opacity=".85"/>
<path d="M200 202 C188 186 196 168 214 170 C232 172 238 190 228 202 C222 210 214 206 216 198" stroke="{YEL}" stroke-width="10" fill="none" stroke-linecap="round"/>
<path d="M268 35 C310 22 355 50 350 95 C380 115 375 165 345 180 C330 150 300 130 290 90 C285 65 275 50 268 35Z" fill="#b9d6f5" opacity=".9"/>
<ellipse cx="292" cy="238" rx="50" ry="30" fill="#f6c1cd" stroke="#d27086" stroke-width="3"/>
<g font-family="Cairo" font-weight="900" font-size="20" text-anchor="middle" fill="#fff">
<circle cx="80" cy="130" r="15" fill="{G7}"/><text x="80" y="137">1</text>
<circle cx="250" cy="196" r="15" fill="#c98a00"/><text x="250" y="203">2</text>
<circle cx="335" cy="110" r="15" fill="{BLUE}"/><text x="335" y="117">3</text>
<circle cx="292" cy="238" r="15" fill="#c75a76"/><text x="292" y="245">4</text></g>
</svg>"""

# ---------------------------------------------------------------- foods
S["fish"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#e6f1fb"/>
<path d="M30 80 C50 46 102 44 124 80 C102 116 50 114 30 80Z" fill="#f08a5d"/>
<path d="M124 80 L150 58 L144 80 L150 102Z" fill="#e0703f"/>
<path d="M58 62 C66 80 66 80 58 98" stroke="#fff" stroke-width="4" fill="none" stroke-linecap="round"/>
<g stroke="#fbc3a6" stroke-width="3" fill="none"><path d="M78 66 q8 14 0 28"/><path d="M92 66 q8 14 0 28"/><path d="M106 70 q6 10 0 20"/></g>
<circle cx="45" cy="74" r="6" fill="#fff"/><circle cx="44" cy="74" r="3" fill="{INK}"/>
<path d="M70 50 C80 38 98 40 104 52" fill="#e0703f"/>
<g fill="{G5}"><path d="M28 122 c8 -10 22 -10 26 0 c-10 6 -18 6 -26 0z"/><circle cx="118" cy="122" r="10" fill="{YEL}"/><circle cx="118" cy="122" r="6" fill="#ffe08a"/></g>
</svg>"""

S["walnut"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#f6ecdf"/>
<ellipse cx="80" cy="84" rx="50" ry="44" fill="#c58b55"/>
<path d="M80 40 V128" stroke="#8a5a30" stroke-width="5"/>
<g stroke="#8a5a30" stroke-width="4" fill="none" stroke-linecap="round">
<path d="M42 70 q12 -6 18 6 q6 12 16 4"/><path d="M38 96 q14 -8 22 4 q8 10 16 0"/><path d="M52 116 q10 -8 22 2"/>
<path d="M118 70 q-12 -6 -18 6 q-6 12 -16 4"/><path d="M122 96 q-14 -8 -22 4 q-8 10 -16 0"/><path d="M108 116 q-10 -8 -22 2"/></g>
<ellipse cx="62" cy="58" rx="10" ry="5" fill="#fff" opacity=".35"/>
</svg>"""

S["berries"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#ecebf8"/>
<g fill="#3d3f8f"><circle cx="58" cy="92" r="24"/><circle cx="102" cy="92" r="24"/><circle cx="80" cy="60" r="24"/><circle cx="80" cy="116" r="20"/></g>
<g fill="#5b5fc7" opacity=".9"><circle cx="52" cy="84" r="8"/><circle cx="96" cy="84" r="8"/><circle cx="74" cy="52" r="8"/></g>
<g stroke="#20225c" stroke-width="3" fill="none" stroke-linecap="round"><path d="M54 100 l8 -6 l8 6"/><path d="M98 100 l8 -6 l8 6"/><path d="M76 68 l8 -6 l8 6"/></g>
<path d="M88 34 c10 -14 26 -10 30 -6 c-12 2 -20 6 -30 6z" fill="{G5}"/>
</svg>"""

S["olive-oil"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#f3f6dc"/>
<rect x="68" y="20" width="22" height="14" rx="3" fill="{G9}"/>
<path d="M70 34 h18 v14 c18 10 22 22 22 36 v42 c0 8 -6 12 -12 12 h-38 c-6 0 -12 -4 -12 -12 v-42 c0 -14 4 -26 22 -36z" fill="#d7c22e" opacity=".92"/>
<path d="M54 84 h52 v34 h-52z" fill="#fff" opacity=".85"/>
<path d="M66 102 c8 -12 22 -12 28 0 c-10 6 -18 6 -28 0z" fill="{G5}"/>
<path d="M60 50 c-4 10 -6 24 -4 34" stroke="#fff" stroke-width="5" opacity=".5" stroke-linecap="round" fill="none"/>
<g transform="translate(118 118) rotate(-30)"><path d="M0 0 c-12 -6 -14 -18 -8 -26 c10 6 12 18 8 26z" fill="{G7}"/><ellipse cx="10" cy="-14" rx="7" ry="9" fill="#5a6b22"/></g>
</svg>"""

S["greens"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="{G1}"/>
<path d="M80 136 C40 120 30 70 56 34 C76 56 86 90 80 136Z" fill="{G7}"/>
<path d="M80 136 C120 120 132 74 108 40 C88 60 76 96 80 136Z" fill="{G5}"/>
<path d="M80 136 C66 100 62 70 56 40 M80 136 C92 104 100 74 108 44" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" opacity=".8"/>
<g stroke="#fff" stroke-width="2" opacity=".6" fill="none"><path d="M70 100 l-14 -10"/><path d="M66 80 l-12 -10"/><path d="M92 100 l14 -10"/><path d="M96 80 l12 -10"/></g>
</svg>"""

S["eggs"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#fff6e0"/>
<ellipse cx="60" cy="88" rx="28" ry="36" fill="#f6e3c8" stroke="#e4c79f" stroke-width="3"/>
<ellipse cx="104" cy="100" rx="34" ry="28" fill="#fff" stroke="#e8e0d0" stroke-width="3"/>
<circle cx="104" cy="100" r="14" fill="{YEL}"/><circle cx="99" cy="95" r="4" fill="#fff" opacity=".7"/>
<ellipse cx="50" cy="72" rx="6" ry="10" fill="#fff" opacity=".6"/>
</svg>"""

S["dates"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#f8ebe0"/>
<g fill="#7a3b1c"><ellipse cx="58" cy="96" rx="18" ry="28" transform="rotate(-18 58 96)"/><ellipse cx="102" cy="96" rx="18" ry="28" transform="rotate(18 102 96)"/><ellipse cx="80" cy="78" rx="18" ry="28"/></g>
<g fill="#b06a3b" opacity=".75"><ellipse cx="74" cy="66" rx="5" ry="11"/><ellipse cx="52" cy="86" rx="5" ry="10" transform="rotate(-18 52 86)"/><ellipse cx="96" cy="86" rx="5" ry="10" transform="rotate(18 96 86)"/></g>
<path d="M80 50 v-18 c-6 -6 -14 -6 -20 -2 M80 32 c6 -6 14 -6 20 -2" stroke="#b58b4a" stroke-width="4" fill="none" stroke-linecap="round"/>
</svg>"""

S["pomegranate"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#fbe6e4"/>
<circle cx="68" cy="88" r="40" fill="#c62f2f"/>
<path d="M56 50 l4 -14 l8 10 l8 -10 l4 14z" fill="#9f2222"/>
<ellipse cx="54" cy="72" rx="8" ry="14" fill="#fff" opacity=".25"/>
<circle cx="112" cy="104" r="28" fill="#f9d7cf" stroke="#c62f2f" stroke-width="5"/>
<g fill="#d8343f"><circle cx="104" cy="96" r="5"/><circle cx="116" cy="94" r="5"/><circle cx="122" cy="106" r="5"/><circle cx="110" cy="108" r="5"/><circle cx="100" cy="110" r="5"/><circle cx="114" cy="118" r="5"/></g>
</svg>"""

S["lentils"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#fdf0d9"/>
<path d="M28 82 h104 c0 30 -22 48 -52 48 s-52 -18 -52 -48z" fill="{G7}"/>
<ellipse cx="80" cy="82" rx="52" ry="12" fill="#f0a531"/>
<g fill="#e08b16"><circle cx="62" cy="80" r="3"/><circle cx="78" cy="84" r="3"/><circle cx="96" cy="79" r="3"/><circle cx="88" cy="86" r="2.5"/><circle cx="70" cy="86" r="2.5"/></g>
<path d="M92 76 c6 -6 14 -4 14 2" stroke="{G5}" stroke-width="4" fill="none" stroke-linecap="round"/>
<g stroke="#c9b9a0" stroke-width="4" fill="none" stroke-linecap="round"><path d="M62 60 c-6 -8 6 -12 0 -22"/><path d="M80 60 c-6 -8 6 -12 0 -22"/><path d="M98 60 c-6 -8 6 -12 0 -22"/></g>
</svg>"""

S["apple"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#fde9e7"/>
<path d="M80 52 C58 36 28 50 32 86 C36 120 60 136 80 126 C100 136 124 120 128 86 C132 50 102 36 80 52Z" fill="{RED}"/>
<path d="M80 52 C78 40 82 30 90 24" stroke="{BROWN}" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M86 38 c10 -12 26 -10 30 -4 c-12 6 -20 8 -30 4z" fill="{G5}"/>
<ellipse cx="54" cy="76" rx="8" ry="14" fill="#fff" opacity=".35"/>
</svg>"""

S["coffee"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#f4ebe3"/>
<ellipse cx="76" cy="124" rx="48" ry="9" fill="#d9c7b5"/>
<path d="M40 70 h72 v26 c0 20 -16 30 -36 30 s-36 -10 -36 -30z" fill="#fff" stroke="#3b2a20" stroke-width="4"/>
<path d="M112 78 c18 0 18 26 0 26" stroke="#3b2a20" stroke-width="5" fill="none"/>
<ellipse cx="76" cy="70" rx="36" ry="8" fill="#5b3a26"/>
<g stroke="#b9a493" stroke-width="4" fill="none" stroke-linecap="round"><path d="M62 54 c-6 -8 6 -12 0 -22"/><path d="M78 54 c-6 -8 6 -12 0 -22"/><path d="M94 54 c-6 -8 6 -12 0 -22"/></g>
</svg>"""

S["tea"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="{G1}"/>
<path d="M52 50 h56 l-8 74 c-1 6 -6 8 -10 8 h-20 c-4 0 -9 -2 -10 -8z" fill="#fff" stroke="#c9a54a" stroke-width="4"/>
<path d="M56 74 h48 l-5 50 c-1 4 -4 6 -8 6 h-22 c-4 0 -7 -2 -8 -6z" fill="#9bbf3a" opacity=".85"/>
<path d="M52 56 h56" stroke="#c9a54a" stroke-width="6"/>
<g transform="translate(96 40)"><path d="M0 0 c-14 -4 -18 -16 -12 -24 c10 4 14 14 12 24z" fill="{G7}"/><path d="M6 4 c4 -14 16 -18 24 -12 c-6 10 -14 14 -24 12z" fill="{G5}"/></g>
</svg>"""

S["water"] = f"""<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="80" cy="80" r="74" fill="#e4f2fb"/>
<path d="M48 36 h64 l-8 92 c-1 6 -6 8 -10 8 h-28 c-4 0 -9 -2 -10 -8z" fill="#fff" stroke="#8cc3e8" stroke-width="4"/>
<path d="M53 66 h54 l-5 60 c-1 4 -4 6 -8 6 h-28 c-4 0 -7 -2 -8 -6z" fill="#7cc0ef" opacity=".7"/>
<circle cx="98" cy="44" r="18" fill="{YEL}" stroke="#fff" stroke-width="4"/>
<g stroke="#fff" stroke-width="2.5"><path d="M98 30 v28 M84 44 h28 M88 34 l20 20 M108 34 l-20 20"/></g>
<g fill="#fff" opacity=".8"><circle cx="68" cy="96" r="4"/><circle cx="84" cy="110" r="3"/><circle cx="76" cy="80" r="3"/></g>
</svg>"""

# ---------------------------------------------------------------- thieves (ch2 icons)
def badge(bg, inner):
    return f"""<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg"><circle cx="60" cy="60" r="56" fill="{bg}"/>{inner}</svg>"""

S["i-sleep"] = badge("#e5e8f8", f"""<path d="M70 28 a32 32 0 1 0 22 52 a26 26 0 1 1 -22 -52z" fill="#3f4aa8"/>
<g fill="{YEL}"><circle cx="86" cy="34" r="4"/><circle cx="96" cy="52" r="3"/></g>""")
S["i-sitting"] = badge("#fdeee0", f"""<rect x="24" y="64" width="72" height="22" rx="8" fill="#e07b39"/><rect x="30" y="44" width="60" height="26" rx="8" fill="#f2a065"/>
<rect x="18" y="58" width="14" height="30" rx="6" fill="#c9622a"/><rect x="88" y="58" width="14" height="30" rx="6" fill="#c9622a"/><path d="M30 88 v8 M90 88 v8" stroke="#7a3b1c" stroke-width="5" stroke-linecap="round"/>""")
S["i-sugar"] = badge("#fde7ea", f"""<g stroke="#e1a6af" stroke-width="3"><rect x="30" y="54" width="28" height="28" rx="4" fill="#fff"/><rect x="62" y="54" width="28" height="28" rx="4" fill="#fff"/><rect x="46" y="26" width="28" height="28" rx="4" fill="#fff"/></g>
<path d="M22 22 L98 98" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>""")
S["i-stress"] = badge("#fff3d6", f"""<path d="M34 56 a18 18 0 0 1 22 -20 a22 22 0 0 1 38 10 a14 14 0 0 1 -2 28 h-54 a12 12 0 0 1 -4 -18z" fill="#8b8f9c"/>
<path d="M62 70 l-10 18 h12 l-8 18 l20 -24 h-12 l8 -12z" fill="{YEL}"/>""")
S["i-alone"] = badge("#e3f5ea", f"""<circle cx="60" cy="44" r="14" fill="{G7}"/><path d="M34 92 c0 -18 12 -28 26 -28 s26 10 26 28z" fill="{G7}"/>
<circle cx="24" cy="58" r="8" fill="none" stroke="{G3}" stroke-width="3" stroke-dasharray="3 4"/><circle cx="96" cy="58" r="8" fill="none" stroke="{G3}" stroke-width="3" stroke-dasharray="3 4"/>""")
S["i-ear"] = badge("#fbe7dc", f"""<path d="M44 48 c0 -18 14 -28 28 -28 c16 0 26 12 26 28 c0 18 -14 22 -18 34 c-4 12 -10 18 -20 18 c-8 0 -14 -6 -14 -12" fill="{SKIN}" stroke="{SKIN2}" stroke-width="5" stroke-linecap="round"/>
<path d="M60 50 c0 -8 6 -14 12 -14 c8 0 12 6 12 12 c0 8 -8 10 -10 16" stroke="{SKIN2}" stroke-width="5" fill="none" stroke-linecap="round"/>
<g stroke="{RED}" stroke-width="4" stroke-linecap="round"><path d="M22 40 l10 6 M18 60 h12 M22 80 l10 -6"/></g>""")
S["i-pressure"] = badge("#fde9e7", f"""<circle cx="60" cy="62" r="34" fill="#fff" stroke="{INK}" stroke-width="4"/>
<path d="M36 62 a24 24 0 0 1 48 0" stroke="{G5}" stroke-width="8" fill="none"/><path d="M72 46 a24 24 0 0 1 12 16" stroke="{RED}" stroke-width="8" fill="none"/>
<path d="M60 62 L78 44" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><circle cx="60" cy="62" r="5" fill="{INK}"/>""")

# good-habit icons
S["i-walk"] = badge("#e3f5ea", f"""<circle cx="64" cy="26" r="9" fill="{G9}"/>
<g stroke="{G9}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"><path d="M62 38 L56 66"/><path d="M56 66 L44 94"/><path d="M56 66 L70 78 L72 96"/><path d="M60 44 L44 56 L40 68"/><path d="M60 44 L74 56 L84 54"/></g>""")
S["i-book"] = badge("#fff3d6", f"""<path d="M60 40 c-10 -8 -26 -10 -38 -6 v52 c12 -4 28 -2 38 6z" fill="#fff" stroke="{G7}" stroke-width="4"/>
<path d="M60 40 c10 -8 26 -10 38 -6 v52 c-12 -4 -28 -2 -38 6z" fill="#fff" stroke="{G7}" stroke-width="4"/>
<g stroke="{G3}" stroke-width="3"><path d="M30 48 h20 M30 58 h20 M30 68 h16 M70 48 h20 M70 58 h20 M70 68 h16"/></g>""")
S["i-chat"] = badge("#e5e8f8", f"""<path d="M20 40 a10 10 0 0 1 10 -10 h40 a10 10 0 0 1 10 10 v22 a10 10 0 0 1 -10 10 h-30 l-14 12 v-12 a10 10 0 0 1 -6 -10z" fill="#3f4aa8"/>
<path d="M58 64 h32 a10 10 0 0 1 10 10 v16 a10 10 0 0 1 -6 9 v11 l-12 -10 h-24 a10 10 0 0 1 -10 -10 v-14z" fill="{G5}"/>
<g fill="#fff"><circle cx="38" cy="50" r="4"/><circle cx="50" cy="50" r="4"/><circle cx="62" cy="50" r="4"/></g>""")
S["i-check"] = badge("#e3f5ea", f"""<path d="M34 62 l18 18 l36 -38" stroke="{G7}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>""")

# ---------------------------------------------------------------- people / movement
def person(body, head=(100, 40), shirt=G7, pants=G9, extra=""):
    hx, hy = head
    return f"""<svg viewBox="0 0 200 240" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="100" cy="228" rx="64" ry="8" fill="#000" opacity=".08"/>
<g stroke-linecap="round" stroke-linejoin="round" fill="none">{body}</g>
<circle cx="{hx}" cy="{hy}" r="20" fill="{SKIN}"/>
<path d="M{hx-20} {hy-2} c0 -16 10 -24 20 -24 s22 8 20 22 c-8 -10 -24 -10 -40 2z" fill="{INK}"/>
{extra}</svg>"""

# cross-crawl: right hand to left knee
S["move-cross"] = person(f"""
<path d="M100 62 L100 130" stroke="{G7}" stroke-width="22"/>
<path d="M92 132 L78 184 L78 222" stroke="{G9}" stroke-width="16"/>
<path d="M108 130 L134 152 L120 182" stroke="{G9}" stroke-width="16"/>
<path d="M90 74 L68 104 L60 128" stroke="{G7}" stroke-width="12"/>
<path d="M110 74 L126 116 L122 146" stroke="{G7}" stroke-width="12"/>
""", extra=f"""<circle cx="122" cy="150" r="9" fill="{SKIN}"/><circle cx="60" cy="128" r="8" fill="{SKIN}"/>
<path d="M150 120 a20 20 0 0 1 0 36" stroke="{YEL}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M146 156 l6 2 l-2 -7" stroke="{YEL}" stroke-width="5" fill="none" stroke-linecap="round"/>""")

# arms up / reach & breathe
S["move-reach"] = person(f"""
<path d="M100 62 L100 132" stroke="{G7}" stroke-width="22"/>
<path d="M92 134 L84 180 L84 222" stroke="{G9}" stroke-width="16"/>
<path d="M108 134 L116 180 L116 222" stroke="{G9}" stroke-width="16"/>
<path d="M90 72 L70 40 L66 10" stroke="{G7}" stroke-width="12"/>
<path d="M110 72 L130 40 L134 10" stroke="{G7}" stroke-width="12"/>
""", extra=f"""<circle cx="66" cy="10" r="8" fill="{SKIN}"/><circle cx="134" cy="10" r="8" fill="{SKIN}"/>
<g stroke="#7cc0ef" stroke-width="4" fill="none" stroke-linecap="round"><path d="M150 70 c10 -4 18 4 28 0"/><path d="M150 84 c10 -4 18 4 28 0"/></g>""")

# finger counting / hand pattern (seated, hands forward)
S["move-fingers"] = f"""<svg viewBox="0 0 200 240" xmlns="http://www.w3.org/2000/svg">
<circle cx="100" cy="120" r="96" fill="{G1}"/>
<g transform="translate(18 60)">
 <path d="M30 150 v-60 a10 10 0 0 1 20 0 v40 M50 90 v-30 a10 10 0 0 1 20 0 v60 M70 70 v-10 a10 10 0 0 1 20 0 v60 M90 80 a10 10 0 0 1 20 0 v40 c0 24 -14 40 -40 40 h-10 c-22 0 -30 -12 -30 -30" fill="{SKIN}" stroke="{SKIN2}" stroke-width="4" stroke-linejoin="round"/>
</g>
<g transform="translate(108 60)">
 <path d="M30 150 c-14 0 -26 -10 -26 -30 v-40 a10 10 0 0 1 20 0 v20 M24 100 v-50 a10 10 0 0 1 20 0 v50 M44 100 v-40 a10 10 0 0 1 20 0 v80 c0 6 -20 10 -34 10z" fill="{SKIN}" stroke="{SKIN2}" stroke-width="4" stroke-linejoin="round"/>
</g>
<g fill="{G7}" font-family="Cairo" font-weight="800" font-size="30" text-anchor="middle"><text x="70" y="52">3</text><text x="140" y="52">2</text></g>
</svg>"""

# ear-nose switch / balance on one foot
S["move-balance"] = person(f"""
<path d="M100 62 L100 132" stroke="{G7}" stroke-width="22"/>
<path d="M96 134 L96 180 L96 222" stroke="{G9}" stroke-width="16"/>
<path d="M106 134 L132 160 L110 178" stroke="{G9}" stroke-width="16"/>
<path d="M90 74 L50 96" stroke="{G7}" stroke-width="12"/>
<path d="M110 74 L150 96" stroke="{G7}" stroke-width="12"/>
""", extra=f"""<circle cx="50" cy="96" r="8" fill="{SKIN}"/><circle cx="150" cy="96" r="8" fill="{SKIN}"/>""")

# doctor avatar (stand-in for the channel's presenter)
S["doctor"] = f"""<svg viewBox="0 0 240 260" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="130" r="118" fill="{G1}"/>
<path d="M54 258 c0 -56 28 -84 66 -84 s66 28 66 84z" fill="#fff" stroke="#d9e3dd" stroke-width="3"/>
<path d="M98 176 l22 40 l22 -40" fill="#cfe9d9"/>
<path d="M98 176 l22 40 l-30 42 h-10 z M142 176 l-22 40 l30 42 h10z" fill="#f4f7f5" stroke="#d9e3dd" stroke-width="2"/>
<rect x="106" y="150" width="28" height="30" rx="10" fill="{SKIN2}"/>
<path d="M66 120 c-6 -60 30 -86 56 -86 c34 0 58 26 52 84 c-2 28 -6 50 -10 64 c-10 -30 -10 -60 -10 -60 l-66 0 c0 0 0 30 -10 60 c-6 -16 -10 -36 -12 -62z" fill="#5a3a26"/>
<ellipse cx="120" cy="112" rx="40" ry="46" fill="{SKIN}"/>
<path d="M78 104 c4 -36 28 -50 50 -46 c16 4 30 18 34 44 c-20 -6 -38 -20 -46 -32 c-8 14 -22 28 -38 34z" fill="#5a3a26"/>
<g fill="{INK}"><ellipse cx="104" cy="116" rx="4" ry="5"/><ellipse cx="136" cy="116" rx="4" ry="5"/></g>
<path d="M96 104 q8 -5 16 0 M128 104 q8 -5 16 0" stroke="#5a3a26" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M108 136 q12 10 24 0" stroke="#c0605a" stroke-width="4" fill="none" stroke-linecap="round"/>
<g fill="#f3a7a0" opacity=".5"><circle cx="96" cy="130" r="7"/><circle cx="144" cy="130" r="7"/></g>
<path d="M94 190 c-6 26 0 44 14 50 M146 190 c6 26 0 44 -14 50" stroke="{G9}" stroke-width="5" fill="none" stroke-linecap="round"/>
<circle cx="120" cy="244" r="9" fill="{G7}" stroke="{G9}" stroke-width="4"/>
<rect x="150" y="214" width="26" height="8" rx="3" fill="{G5}"/>
</svg>"""

# ---------------------------------------------------------------- scenes
S["sleep"] = f"""<svg viewBox="0 0 400 220" xmlns="http://www.w3.org/2000/svg">
<rect width="400" height="220" rx="24" fill="#1e2a5a"/>
<g fill="#fff"><circle cx="40" cy="40" r="2"/><circle cx="120" cy="24" r="2.5"/><circle cx="200" cy="50" r="2"/><circle cx="250" cy="22" r="2"/><circle cx="90" cy="80" r="1.6"/><circle cx="170" cy="96" r="1.6"/><circle cx="380" cy="100" r="2"/></g>
<path d="M330 30 a40 40 0 1 0 30 66 a32 32 0 1 1 -30 -66z" fill="{YEL}"/>
<rect x="40" y="140" width="300" height="40" rx="10" fill="#8ea2e6"/>
<rect x="30" y="110" width="16" height="90" rx="6" fill="#6a4c93"/><rect x="334" y="126" width="16" height="74" rx="6" fill="#6a4c93"/>
<rect x="58" y="118" width="70" height="26" rx="13" fill="#fff"/>
<path d="M120 138 h214 v20 h-214z" fill="#5b6ccf"/>
<circle cx="98" cy="118" r="20" fill="{SKIN}"/><path d="M78 116 c0 -16 10 -22 20 -22 s20 6 20 18 c-8 -8 -24 -8 -40 4z" fill="#5a3a26"/>
<path d="M90 120 q4 3 8 0 M104 120 q4 3 8 0" stroke="{INK}" stroke-width="2" fill="none" stroke-linecap="round"/>
<g fill="#fff" font-family="Cairo" font-weight="800"><text x="140" y="100" font-size="22">Z</text><text x="164" y="80" font-size="28">Z</text><text x="194" y="56" font-size="34">Z</text></g>
</svg>"""

S["heart"] = f"""<svg viewBox="0 0 300 220" xmlns="http://www.w3.org/2000/svg">
<circle cx="150" cy="110" r="104" fill="#fde9e7"/>
<path d="M150 186 C80 140 56 108 64 78 C72 46 112 40 134 62 L150 78 L166 62 C188 40 228 46 236 78 C244 108 220 140 150 186Z" fill="{RED}"/>
<ellipse cx="96" cy="82" rx="12" ry="20" fill="#fff" opacity=".3" transform="rotate(-24 96 82)"/>
<path d="M20 116 H96 L110 88 L128 146 L146 70 L162 124 L172 116 H280" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M20 116 H96 L110 88 L128 146 L146 70 L162 124 L172 116 H280" stroke="{G9}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

S["calendar"] = f"""<svg viewBox="0 0 220 200" xmlns="http://www.w3.org/2000/svg">
<rect x="14" y="26" width="192" height="164" rx="18" fill="#fff" stroke="{G7}" stroke-width="5"/>
<path d="M14 44 a18 18 0 0 1 18 -18 h156 a18 18 0 0 1 18 18 v20 h-192z" fill="{G7}"/>
<rect x="52" y="10" width="12" height="30" rx="6" fill="{G9}"/><rect x="156" y="10" width="12" height="30" rx="6" fill="{G9}"/>
<g fill="{G1}">
""" + "".join(
    f'<rect x="{30 + c * 32}" y="{78 + r * 26}" width="24" height="18" rx="5"/>'
    for r in range(4) for c in range(5)) + f"""</g>
<g stroke="{G5}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round">
""" + "".join(
    f'<path d="M{35 + c * 32} {87 + r * 26} l5 5 l9 -10"/>'
    for r in range(4) for c in range(5) if r * 5 + c < 13) + f"""</g>
<circle cx="182" cy="170" r="26" fill="{YEL}" stroke="#fff" stroke-width="5"/>
<text x="182" y="181" text-anchor="middle" font-family="Cairo" font-weight="900" font-size="28" fill="{G9}">30</text>
</svg>"""

S["plate"] = f"""<svg viewBox="0 0 320 300" xmlns="http://www.w3.org/2000/svg">
<circle cx="150" cy="150" r="136" fill="#eef1ee"/>
<circle cx="150" cy="150" r="118" fill="#fff" stroke="#dfe5e1" stroke-width="4"/>
<path d="M150 150 L150 40 A110 110 0 0 0 150 260Z" fill="#cdebd6"/>
<path d="M150 150 L150 40 A110 110 0 0 1 260 150Z" fill="#fde3b8"/>
<path d="M150 150 L260 150 A110 110 0 0 1 150 260Z" fill="#fbd0c8"/>
<g stroke="#fff" stroke-width="4"><path d="M150 38 V262"/><path d="M150 150 H262"/></g>
<g fill="{G7}"><path d="M84 100 c-14 -16 -6 -34 6 -38 c8 14 6 28 -6 38z"/><path d="M104 120 c-16 -10 -14 -30 -4 -36 c10 10 12 26 4 36z"/><circle cx="80" cy="170" r="12"/><circle cx="104" cy="196" r="10"/><circle cx="74" cy="206" r="9"/><path d="M110 150 c-10 -12 -2 -26 8 -28 c4 12 2 22 -8 28z"/></g>
<g fill="#e0b25a"><ellipse cx="190" cy="86" rx="10" ry="5"/><ellipse cx="214" cy="100" rx="10" ry="5"/><ellipse cx="188" cy="110" rx="10" ry="5"/><ellipse cx="220" cy="124" rx="10" ry="5"/><ellipse cx="200" cy="130" rx="9" ry="4"/></g>
<path d="M176 196 C188 176 222 176 236 196 C222 216 188 216 176 196Z" fill="#f08a5d"/>
<path d="M236 196 l12 -8 v16z" fill="#e0703f"/>
<g fill="#7a5a3a"><ellipse cx="190" cy="236" rx="9" ry="6"/><ellipse cx="208" cy="230" rx="8" ry="5"/></g>
<circle cx="292" cy="250" r="26" fill="#fff" stroke="#dfe5e1" stroke-width="3"/>
<g fill="#3d3f8f"><circle cx="284" cy="246" r="7"/><circle cx="298" cy="244" r="7"/><circle cx="292" cy="256" r="7"/></g>
<circle cx="292" cy="40" r="22" fill="#fff" stroke="#dfe5e1" stroke-width="3"/>
<circle cx="292" cy="40" r="15" fill="#d7c22e" opacity=".85"/>
</svg>"""

S["stethoscope"] = badge("#e3f5ea", f"""<path d="M36 26 v28 a20 20 0 0 0 40 0 v-28" stroke="{G9}" stroke-width="7" fill="none" stroke-linecap="round"/>
<path d="M56 74 v10 a16 16 0 0 0 32 0 v-14" stroke="{G9}" stroke-width="7" fill="none" stroke-linecap="round"/>
<circle cx="88" cy="62" r="12" fill="{G5}" stroke="{G9}" stroke-width="5"/>""")

S["leaf"] = f"""<svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg"><path d="M30 56 C8 46 6 18 30 4 C54 18 52 46 30 56Z" fill="currentColor"/><path d="M30 54 V12" stroke="#fff" stroke-width="2.5" opacity=".8"/></svg>"""


def get(name):
    return S[name]
