"""Build the website version of notes/terminology.md with Quarto's Pandoc."""
from pathlib import Path
import shutil
import subprocess
import re

root = Path(__file__).resolve().parents[1]
quarto = shutil.which('quarto')
if not quarto:
    raise SystemExit('Install Quarto before building the terminology page.')
bundled = Path(quarto).parent / 'tools' / 'pandoc.exe'
command = [str(bundled)] if bundled.exists() else [quarto, 'pandoc']
source = root / 'notes' / 'terminology.md'
body = subprocess.run(command + [str(source), '--from=gfm', '--to=html5'], check=True, capture_output=True, encoding='utf-8').stdout
body = re.sub(r'<table>.*?</table>', lambda m: '<div class="table-scroll" role="region" aria-label="術語比較表" tabindex="0">'+m[0]+'</div>', body, flags=re.S)
html = '''<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="比較 StreamAtt 2024 與 TACL 2025 的 SimulST／StreamST 用語，整理輸入、分段、架構、輸出與評估的判斷規則。">
  <title>共用術語筆記 · Streaming Speech Research</title>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
<main class="notes-content">
  <nav class="reading-nav" aria-label="閱讀入口"><a class="home-button" href="../index.html">← 回首頁</a> <a href="../StreamST/index.html">StreamST</a> <a href="../SimulST/index.html">SimulST 簡報</a></nav>
''' + body + '''
  <footer>Streaming Speech Research · <a href="https://github.com/tc9305/streaming-speech-research/blob/main/notes/terminology.md">GitHub Markdown 原稿</a></footer>
</main>
</body>
</html>
'''
out = root / 'docs' / 'notes' / 'terminology.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html, encoding='utf-8')
print('Built docs/notes/terminology.html from notes/terminology.md')
