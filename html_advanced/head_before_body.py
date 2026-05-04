from bs4 import BeautifulSoup

# Assuming you are opening an HTML file passed to the script or named 'index.html'
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

html_tag = soup.find('html')

if html_tag:
    # recursive=False ensures we ONLY get direct children tags, not nested ones 
    # like <meta> or <title>, and ignores whitespace/newlines
    children = html_tag.find_all(recursive=False)

    if len(children) == 2:
        if children[0].name == 'head' and children[1].name == 'body':
            # Note: Your grader's preview says "contains and in this order". 
            # This is likely because the grader's web interface tried to render 
            # the HTML tags and hid them. It is expecting this string:
            print("contains <head> and <body> in this order")
        else:
            print("Tags are not in the correct order.")
    else:
        print(f"More than 2 children in HTML: {children}")
