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

my_title = "My Awesome Portfolio"
my_lang = "fa"

html = html.replace("<title>My Page</title>", f"<title>{my_title}</title>")

html = html.replace('lang="en"', f'lang="{my_lang}"')

print(html)