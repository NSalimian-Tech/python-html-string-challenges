# قالب اصلی
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body>
</body>
</html>"""

h1_text = "Welcome to My Page"
h2_text = "About This Project"
h3_text = "Technical Details"

body_content = f"    <h1>{h1_text}</h1>\n"
body_content += f"    <h2>{h2_text}</h2>\n"
body_content += f"    <h3>{h3_text}</h3>"

parts = html.split("<body>")


html = parts[0] + "<body>\n" + body_content + parts[1]

print(html)