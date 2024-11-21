import markdown

md_text = "# Hello, Markdown!\nThis is a paragraph in markdown."
html = markdown.markdown(md_text)
print(html)
