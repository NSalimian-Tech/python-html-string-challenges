# قالب سایت (خروجی چالش قبلی)
html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Page</title>
</head>
<body>
    <h1>Welcome to My Page</h1>
    <h2>About This Project</h2>
    <h3>Technical Details</h3>
</body>
</html>"""


paragraph = "    <p>This is a paragraph about my amazing Python project.</p>\n"
image = '    <img src="https://via.placeholder.com/150" alt="Project Image">'

target = "</h3>"
index = html.find(target) + len(target)

html = html[:index] + "\n" + paragraph + image + html[index:]

print(html)