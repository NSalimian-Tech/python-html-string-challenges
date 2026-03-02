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

new_style = "main.min.css"
new_script = "bundle.js"


start_index = html.find("styles.css")
end_index = start_index + len("styles.css")

html = html[:start_index] + new_style + html[end_index:]


start_script = html.find("app.js")
end_script = start_script + len("app.js")

html = html[:start_script] + new_script + html[end_script:]


print(html)