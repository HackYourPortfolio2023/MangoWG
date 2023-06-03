'''
Creates a new html template if not already exists
'''

import tinyhtml

tinyhtml.set_doctype("html5") # setting doctype to html5
tinyhtml.set_indent(4) # setting indentation to 4 spaces

# Add external stylesheet links
tinyhtml.add_external_stylesheet_link("https://fonts.googleapis.com")
tinyhtml.add_external_stylesheet_link("https://fonts.gstatic.com")
tinyhtml.add_external_stylesheet_link("https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css")
tinyhtml.add_external_stylesheet_link("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css")
tinyhtml.add_external_stylesheet_link("https://fonts.googleapis.com/css2?family=ABeeZee&display=swap")
tinyhtml.add_external_stylesheet_link("https://fonts.googleapis.com/css2?family=Nunito&display=swap")

# Add external script links
tinyhtml.add_external_script_link("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/js/all.min.js")
tinyhtml.add_external_script_link("https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js")
tinyhtml.add_external_script_link("https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js")
tinyhtml.add_external_script_link("https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js")
tinyhtml.add_external_script_link("https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js")
tinyhtml.add_external_script_link("https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js")
tinyhtml.add_external_script_link("https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js")

# Add meta tags
tinyhtml.add_meta_tag("charset", "UTF-8")
tinyhtml.add_meta_tag("name", "viewport", "content", "width=device-width, initial-scale=1.0")


# Add title

# Add favicon

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