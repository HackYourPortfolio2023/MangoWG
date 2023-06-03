from tinyhtml import html, h, link, script, title, body, nav, a, ul, li, div, img, h1, p, br, footer

page = html(
    h("head")(
        h("meta",charset="UTF-8"),
        h("meta",http_equiv="X-UA-Compatible", content="IE=edge"),
        h("meta", name="viewport", content="width=device-width, initial-scale=1.0"),
        script(
            src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/js/all.min.js",
            integrity="sha512-6PM0qYu5KExuNcKt5bURAoT6KCThUmHRewN3zUFNaoI6Di7XJPTMoT6K0nsagZKk2OB4L7E3q1uQKHNHd4stIQ==",
            crossorigin="anonymous",
            referrerpolicy="no-referrer",
        ),
        link(rel="stylesheet",
             href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"),
        script(src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"),
        script(
            src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"),
        script(src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"),
        link(rel="preconnect", href="https://fonts.googleapis.com"),
        link(rel="preconnect", href="https://fonts.gstatic.com",
             crossorigin="anonymous"),
        link(
            href="https://fonts.googleapis.com/css2?family=ABeeZee&display=swap",
            rel="stylesheet"
        ),
        link(
            href="https://fonts.googleapis.com/css2?family=Nunito&display=swap",
            rel="stylesheet"
        ),
        link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        ),
        script(
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
            integrity="sha384-geWF76RCwLtnZ8qwWowPQNguL3RmwHVBC9FhGdlKrxdiJJigb/j/68SIy3Te4Bkz",
            crossorigin="anonymous"
        ),
        script(
            src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js",
            integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r",
            crossorigin="anonymous"
        ),
        script(
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js",
            integrity="sha384-fbbOQedDUMZZ5KreZpsbe1LCZPVmfTnH7ois6mU1QK+m14rQ1l2bGBq41eYeM/fS",
            crossorigin="anonymous"
        ),
        title("My portfolio")
    ),
    body(
        nav(
            _class="navbar navbar-expand-sm bg-dark navbar-dark sticky-top",
            content=[
                a("Username", _class="navbar-brand", href="#"),
                ul(
                    _class="navbar-nav",
                    content=[
                        li(a("About", _class="nav-link", href="#about-section")),
                        li(a("Projects", _class="nav-link", href="#projects-section")),
                        li(a("Contact", _class="nav-link", href="#contact-section"))
                    ]
                )
            ]
        ),
        div(
            _class="jumbotron jumbotron-fluid",
            style="margin-bottom: 0",
            content=[
                div(
                    _class="d-flex align-items-center justify-content-center",
                    content=[
                        div(
                            _class="col-lg-4 d-flex align-items-center justify-content-center flex-wrap",
                            content=[
                                img(
                                    src="https://www.w3schools.com/bootstrap4/img_avatar3.png",
                                    alt="Avatar",
                                    _class="",
                                    style="width: 200px; height: 200px; border-radius: 50%"
                                ),
                                div(
                                    _class="d-flex flex-column align-items-center justify-content-center",
                                    content=[
                                        h1("Username"),
                                        p("Some text that represents \"Me\"...")
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        div(
            _class="row d-flex align-items-center justify-content-center",
            content=[
                div(
                    _class="col-sm-6",
                    content=[
                        img(
                            src="https://picsum.photos/600/600",
                            _class="card-img-top",
                            alt="...",
                            height="300px"
                        )
                    ]
                ),
                div(
                    _class="col-sm-6",
                    content=[
                        div(
                            style="padding: 20px",
                            content=[
                                h2("Heading"),
                                p(
                                    "Some representative placeholder content for the three columns of text "
                                    "below the carousel. This is the first column."
                                ),
                                p(
                                    a("View details »",
                                      _class="btn btn-secondary", href="#")
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        div(
            _class="row d-flex align-items-center justify-content-center",
            content=[
                div(
                    _class="col-sm-6",
                    content=[
                        div(
                            style="padding: 20px",
                            content=[
                                h2("Heading"),
                                p(
                                    "Some representative placeholder content for the three columns of text "
                                    "below the carousel. This is the first column."
                                ),
                                p(
                                    a("View details »",
                                      _class="btn btn-secondary", href="#")
                                )
                            ]
                        )
                    ]
                ),
                div(
                    _class="col-sm-6",
                    content=[
                        img(
                            src="https://picsum.photos/600/600",
                            _class="card-img-top",
                            alt="...",
                            height="300px"
                        )
                    ]
                )
            ]
        ),
        br(),
        div(
            _class="container",
            content=[
                div(
                    _class="col text-center",
                    content=h2("Projects")
                ),
                br(),
                div(
                    _class="row text-center",
                    content=[
                        div(
                            _class="col-lg-4",
                            style="padding: 10px",
                            content=[
                                img(
                                    src="https://picsum.photos/140/140",
                                    _class="card-img-top",
                                    style="width: 140px; height: 140px; border-radius: 50%",
                                    alt="..."
                                ),
                                h3(_class="fw-normal", content="Heading"),
                                p(
                                    "Some representative placeholder content for the three columns of text "
                                    "below the carousel. This is the first column."
                                ),
                                p(
                                    a("View details »",
                                      _class="btn btn-secondary", href="#")
                                )
                            ]
                        ),
                        div(
                            _class="col-lg-4",
                            style="padding: 10px",
                            content=[
                                img(
                                    src="https://picsum.photos/140/140",
                                    _class="card-img-top",
                                    style="width: 140px; height: 140px; border-radius: 50%",
                                    alt="..."
                                ),
                                h3(_class="fw-normal", content="Heading"),
                                p(
                                    "Some representative placeholder content for the three columns of text "
                                    "below the carousel. This is the first column."
                                ),
                                p(
                                    a("View details »",
                                      _class="btn btn-secondary", href="#")
                                )
                            ]
                        ),
                        div(
                            _class="col-lg-4",
                            style="padding: 10px",
                            content=[
                                img(
                                    src="https://picsum.photos/140/140",
                                    _class="card-img-top",
                                    style="width: 140px; height: 140px; border-radius: 50%",
                                    alt="..."
                                ),
                                h3(_class="fw-normal", content="Heading"),
                                p(
                                    "Some representative placeholder content for the three columns of text "
                                    "below the carousel. This is the first column."
                                ),
                                p(
                                    a("View details »",
                                      _class="btn btn-secondary", href="#")
                                )
                            ]
                        )
                    ]
                )
            ]
        ),
        br(),
        footer(
            content=[
                div(
                    _class="bg-dark text-white",
                    content=[
                        div(
                            _class="container",
                            style="padding: 20px",
                            content=[
                                div(
                                    _class="row",
                                    content=[
                                        div(
                                            _class="col-md-4",
                                            content=[
                                                h3("About"),
                                                p(
                                                    "I am a web developer with experience in HTML, CSS, JavaScript, "
                                                    "and PHP. I am passionate about creating beautiful and functional "
                                                    "websites."
                                                )
                                            ]
                                        ),
                                        div(
                                            _class="col-md-4",
                                            content=[
                                                h3("Contact"),
                                                p(
                                                    "Email: ",
                                                    a("youremail@example.com",
                                                      href="mailto:youremail@example.com")
                                                ),
                                                p("Phone: (123) 456-7890")
                                            ]
                                        ),
                                        div(
                                            _class="col-md-4",
                                            content=[
                                                h3("Social Media"),
                                                a(
                                                    _class="btn btn-outline-light",
                                                    href="#",
                                                    content=i(
                                                        class_="fab fa-twitter")
                                                ),
                                                a(
                                                    _class="btn btn-outline-light",
                                                    href="#",
                                                    content=i(
                                                        class_="fab fa-facebook")
                                                ),
                                                a(
                                                    _class="btn btn-outline-light",
                                                    href="#",
                                                    content=i(
                                                        class_="fab fa-instagram")
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ]
        )
    )
)

# Write the generated HTML to a file
with open("index.html", "w") as file:
    file.write(str(page))


# Print the generated HTML page
print(page)
