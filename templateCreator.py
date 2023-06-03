'''
Creates a new html template if not already exists
'''


from tinyhtml import html, h
import tinyhtml

tinyhtml.set_doctype("html5") # setting doctype to html5
tinyhtml.set_indent(4) # setting indentation to 4 spaces

# Add external stylesheet links
tinyhtml.add_external_stylesheet("https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css")
tinyhtml.add_external_stylesheet("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")
tinyhtml.add_external_stylesheet("https://fonts.googleapis.com/css?family=Roboto")
tinyhtml.add_external_stylesheet("https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/css/bootstrap.min.css")

# Constructing HTML using html() and h()
# nested h() is also supported
html_content = html(lang="en")(
	h("head")(
		(h("h1")("hello Geeks!!")),
	),
).render()

# printing html formed on console.
print(html_content)

# html_content = html(lang="en")()  
# print(html_content.render()) 