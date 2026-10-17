from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#ffd6e7">
  <meta name="description" content="A tiny pastel world full of cute characters, surprises and happy vibes.">
  <title>Little Cloud Club ♡</title>
  <style>
    :root { --ink:#74445f; --pink:#ff9fc7; --cream:#fffaf4; --lilac:#e8dcff; }
    * { box-sizing:border-box; }
    body { margin:0; min-height:100vh; color:var(--ink); font-family:system-ui,-apple-system,"Segoe UI",sans-serif;
      background:linear-gradient(145deg,#ffe0ed 0%,#fff6f8 48%,#e9e1ff 100%); overflow-x:hidden; }
    .top { text-align:center; padding:28px 16px 20px; }
    .pill { display:inline-block; background:#ffffffb8; border:1px solid white; border-radius:999px; padding:7px 13px; font-size:.86rem; }
    h1 { font-size:clamp(2.1rem,8vw,4rem); line-height:1.05; margin:14px 0 10px; letter-spacing:-1.5px; }
    .top p { margin:0 auto; max-width:500px; line-height:1.6; }
    main { width:min(920px,92%); margin:0 auto 40px; }
    .hero { display:grid; grid-template-columns:1fr; gap:18px; }
    .panel { background:#ffffffbd; border:2px solid #fff; border-radius:28px; padding:22px; box-shadow:0 12px 32px #b66b9820; }
    .scene { min-height:230px; display:flex; align-items:center; justify-content:center; gap:clamp(8px,3vw,26px); background:linear-gradient(135deg,#ffe5ef,#f1e7ff); position:relative; overflow:hidden; }
    .buddy { font-size:clamp(3.2rem,12vw,6rem); filter:drop-shadow(0 7px 3px #b87da322); animation:bob 2.8s ease-in-out infinite; }
    .buddy:nth-child(2) { animation-delay:.25s; } .buddy:nth-child(3) { animation-delay:.5s; }
    @keyframes bob { 0%,100%{transform:translateY(0) rotate(-3deg)} 50%{transform:translateY(-10px) rotate(3deg)} }
    .spark { position:absolute; font-size:1.4rem; opacity:.8; } .s1{top:20px;left:12%}.s2{top:28px;right:15%}.s3{bottom:20px;left:20%}.s4{bottom:18px;right:22%}
    h2 { margin:0 0 8px; font-size:1.45rem; } .muted { line-height:1.6; margin:0 0 16px; }
    .buttons { display:flex; flex-wrap:wrap; gap:10px; }
    button { font:inherit; font-weight:700; color:#fff; background:#f47eae; border:0; border-radius:999px; padding:12px 17px; cursor:pointer; box-shadow:0 5px 0 #d96396; transition:transform .15s,filter .15s; }
    button:hover { filter:brightness(1.04); transform:translateY(-2px); } button:active { transform:translateY(2px); box-shadow:0 2px 0 #d96396; }
    button.secondary { color:#74445f; background:#eee4ff; box-shadow:0 5px 0 #d1baf6; }
    #message { min-height:48px; margin:16px 0 0; padding:12px; border-radius:16px; background:#fff0f6; line-height:1.5; }
    .section-title { text-align:center; margin:30px 0 14px; }
    .tiles { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; }
    .tile { text-align:center; padding:18px 10px; border-radius:22px; background:#ffffffbd; border:2px solid white; }
    .tile .emoji { display:block; font-size:2.2rem; margin-bottom:7px; }
    .tile strong { display:block; margin-bottom:4px; } .tile small { line-height:1.4; }
    footer { text-align:center; padding:8px 16px 28px; font-size:.9rem; }
    @media(min-width:680px) { .hero { grid-template-columns:1fr 1fr; align-items:stretch; } .scene { min-height:300px; } .tiles { grid-template-columns:repeat(4,minmax(0,1fr)); } }
    @media(prefers-reduced-motion:reduce) { *,*::before,*::after { animation:none!important; transition:none!important; scroll-behavior:auto!important; } }
  </style>
</head>
<body>
  <header class="top">
    <span class="pill">✿ a tiny happy place ✿</span>
    <h1>Little Cloud Club <span aria-hidden="true">♡</span></h1>
    <p>Soft colours, tiny friends, and little surprises to make your day sweeter.</p>
  </header>
  <main>
    <section class="hero" aria-label="Welcome">
      <div class="panel scene" aria-label="Cute animal characters">
        <span class="spark s1">✦</span><span class="spark s2">♡</span><span class="spark s3">✧</span><span class="spark s4">✿</span>
        <span class="buddy" role="img" aria-label="bunny">🐰</span>
        <span class="buddy" role="img" aria-label="teddy bear">🧸</span>
        <span class="buddy" role="img" aria-label="chick">🐥</span>
      </div>
      <div class="panel" style="display:flex;flex-direction:column;justify-content:center">
        <h2>Hey, little sunshine! ☁️</h2>
        <p class="muted">Welcome to your own pastel corner of the internet. Pick a button and see what your tiny cloud has for you.</p>
        <div class="buttons">
          <button type="button" id="surprise">A tiny surprise 💌</button>
          <button type="button" class="secondary" id="mood">Change the vibe 🎨</button>
        </div>
        <p id="message" aria-live="polite">A little reminder: you deserve kind moments. ♡</p>
      </div>
    </section>
    <h2 class="section-title">Choose your little joy 🌷</h2>
    <section class="tiles" aria-label="Cute little things">
      <div class="tile"><span class="emoji">🍓</span><strong>Berry sweet</strong><small>For extra-sweet days</small></div>
      <div class="tile"><span class="emoji">🌙</span><strong>Dreamy moon</strong><small>For quiet moments</small></div>
      <div class="tile"><span class="emoji">🫧</span><strong>Bubble magic</strong><small>For a fresh start</small></div>
      <div class="tile"><span class="emoji">🌼</span><strong>Sunny flower</strong><small>For a little hope</small></div>
    </section>
  </main>
  <footer>Made with lots of ♡ and a sprinkle of magic ✨</footer>
  <script>
    (() => {
      const messages = [
        'You are allowed to take life one little step at a time. 🌷',
        'Sending a pocket-sized hug your way! 🧸',
        'Tiny progress is still progress. ⭐',
        'May something lovely surprise you today. 🍓',
        'You bring your own kind of sparkle. ✨'
      ];
      const palettes = [
        'linear-gradient(145deg,#ffe0ed 0%,#fff6f8 48%,#e9e1ff 100%)',
        'linear-gradient(145deg,#dffff1 0%,#fff8dc 50%,#ffe0ed 100%)',
        'linear-gradient(145deg,#e4e0ff 0%,#fff0f7 50%,#dff7ff 100%)',
        'linear-gradient(145deg,#ffe7d6 0%,#fff7ef 50%,#f4e0ff 100%)'
      ];
      let messageIndex = 0;
      let paletteIndex = 0;
      const message = document.getElementById('message');
      document.getElementById('surprise').addEventListener('click', () => {
        message.textContent = messages[messageIndex];
        messageIndex = (messageIndex + 1) % messages.length;
      });
      document.getElementById('mood').addEventListener('click', () => {
        paletteIndex = (paletteIndex + 1) % palettes.length;
        document.body.style.background = palettes[paletteIndex];
      });
    })();
  </script>
</body>
</html>'''

@app.get('/')
def home():
    return render_template_string(PAGE)

if __name__ == '__main__':
    # The hosting platform supplies PORT; local testing defaults to 5000.
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', '5000')), debug=False)
