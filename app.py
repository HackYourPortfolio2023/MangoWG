import bot
import os
from typing import Annotated
import templateGeneratorYattag

import time
import typer
from rich.progress import track

app = typer.Typer()

@app.command()
def start():
    '''Starts the program'''
    print("Welcome!")
    print("Authenticating")
    bot.auth()


@app.command()
def new():
    bot.create_repo()


@app.command()
def push():
    '''Pushes the files in the util folder to your Github repository'''
    files = ['index.html']
    bot.update(files)
    print("Success!")


@app.command("create")
def createTemplate():
    '''Creates a new html template if not already exists'''

    for value in track(range(100), description="Processing..."):
        time.sleep(0.01)
        if value == 10:
            print(f"Checking for existing template")

        if value == 30:
            print(f"Creating new template")

        if value == 50:
            print(f"Creating new template")

    print(f"Template successfully created")


if __name__ == "__main__":
    app()
