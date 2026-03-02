html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Original Title</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <script src="app.js"></script>
</body>
</html>"""

html = html.replace('lang="en"', 'lang="es"').replace("<title>Original Title</title>", "<title>Full Page Challenge</title>")

css_start = html.find('href="') + 6
css_end = html.find('"', css_start)
html = html[:css_start] + "app.min.css" + html[css_end:]

js_start = html.find('src="') + 5
js_end = html.find('"', js_start)
html = html[:js_start] + "main.bundle.js" + html[js_end:]

if html.count("styles.css") == 0 and html.count("app.js") == 0:
    print("Step 3: Assets validated")
else:
    print("Step 3: Validation failed")

parts = html.split("<body>", 1)
headings = "\n    <h1>Main Title</h1>\n    <h2>Subtitle</h2>\n    <h3>Minor Details</h3>"
html = parts[0] + "<body>" + headings + parts[1]

tags = ["</h1>", "</h2>", "</h3>"]
positions = []
for t in tags:
    pos = html.rfind(t)
    if pos != -1:
        positions.append(pos + len(t))

max_pos = max(positions)
paragraph1 = "\n    <p>This is the first dynamic paragraph.</p>"
image = '\n    <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600" alt="Coding" style="width:100%; border-radius:10px; margin-top:20px;">'
html = html[:max_pos] + paragraph1 + image + html[max_pos:]

title_start = html.find("<title>") + 7
title_end = html.find("</title>")
extracted_title = html[title_start:title_end]

p2_index = html.find("</body>")
paragraph2 = f"\n    <p>The title of this page is: {extracted_title}</p>\n"
html = html[:p2_index] + paragraph2 + html[p2_index:]

print("\n--- Validation Report ---")
print("Title correct:", html.count("<title>Full Page Challenge</title>") == 1)
print("H1 found:", html.count("<h1>") == 1)
print("H2 found:", html.count("<h2>") == 1)
print("H3 found:", html.count("<h3>") == 1)
print("Img count 1:", html.count("<img") == 1)
print("P count 2:", html.count("<p>") == 2)
print("Starts with DOCTYPE:", html.strip().startswith("<!DOCTYPE html>"))
print("Ends with html:", html.strip().endswith("</html>"))
print("-------------------------\n")

print(html)

def extract_content(tag_name, source):
    start_tag = f"<{tag_name}>"
    end_tag = f"</{tag_name}>"
    start_idx = source.find(start_tag) + len(start_tag)
    end_idx = source.find(end_tag)
    return source[start_idx:end_idx]

print("--- Extraction Test ---")
for tag in ["title", "h1", "h2", "h3"]:
    print(tag + ": " + extract_content(tag, html))