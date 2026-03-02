with open("template.html", "r") as file:
    html_template = file.read()

new_content = "<h2>This content came from Python!</h2>"

final_html = html_template.replace("", new_content)

print(final_html)