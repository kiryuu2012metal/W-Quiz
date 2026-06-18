import os
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

files = sorted(
    f for f in os.listdir(ROOT)
    if f.endswith(".html") and f != "index.html"
)


def display_name(filename):
    name = filename.rsplit(".html", 1)[0]
    return name.replace("_", " ")


items_html = ""
for fn in files:
    href = urllib.parse.quote(fn)
    label = display_name(fn)
    items_html += f'    <a class="quiz-link" href="{href}">{label}</a>\n'

template = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>K-Quiz 모음</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Pretendard', 'Apple SD Gothic Neo', sans-serif; background: #f5f4f0; color: #1a1a18; min-height: 100vh; padding: 2.5rem 1rem; }}
  .container {{ max-width: 640px; margin: 0 auto; }}
  header {{ text-align: center; margin-bottom: 2rem; }}
  header h1 {{ font-size: 1.6rem; font-weight: 700; margin-bottom: 0.4rem; color: #0F6E56; }}
  header p {{ font-size: 0.875rem; color: #5f5e5a; }}
  .quiz-list {{ display: flex; flex-direction: column; gap: 0.7rem; }}
  .quiz-link {{
    display: block;
    background: #fff;
    border: 0.5px solid #d3d1c7;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    font-size: 0.95rem;
    font-weight: 500;
    color: #1a1a18;
    text-decoration: none;
    transition: all 0.15s;
  }}
  .quiz-link:hover {{ background: #E1F5EE; border-color: #1D9E75; color: #085041; }}
  .quiz-link::before {{ content: "📘 "; }}
  footer {{ text-align: center; margin-top: 2rem; font-size: 0.8rem; color: #9a988f; }}
</style>
</head>
<body>
<div class="container">
  <header>
    <h1>K-Quiz 모음</h1>
    <p>학예사 시험 준비 — 분야별 점검 퀴즈 목록</p>
  </header>
  <div class="quiz-list">
{items_html}  </div>
  <footer>총 {len(files)}개 퀴즈 — 새 파일을 올리면 이 목록이 자동으로 갱신됩니다.</footer>
</div>
</body>
</html>
"""

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(template)

print(f"index.html generated with {len(files)} quizzes")
