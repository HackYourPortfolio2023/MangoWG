from typing import Annotated

import typer
from util import bot

app = typer.Typer()


@app.command("hello")
def hello(username: str):
    print(f"Hello: {username}")


@app.command()
def start():
    print("Welcome!")
    print("Authenticating")
    bot.auth()


@app.command()
def push():
    files = ['util/text.txt']
    bot.update(files)
    print("Success!")


if __name__ == "__main__":
    app()
