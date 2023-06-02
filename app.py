import typer

app = typer.Typer()


@app.command("hello")
def hello(username: str):
    print(f"Hello: {username}")


@app.command("bonjour")
def bonjour(username: str):
    print(f"Bonjour: {username}")


if __name__ == "__main__":
    app()
