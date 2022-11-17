paragraph1 = 'This is my frist blog'

def paragraph_html(text):
    paragraph = f'<p>{text}</p>'
    return paragraph
paragraph1 = paragraph_html(paragraph1)
print(paragraph1)

def h2_html(text):
    h2 = f'<h2>{text.title()}</h2>'
    return h2
print(h2_html('Top 5 product review'))


