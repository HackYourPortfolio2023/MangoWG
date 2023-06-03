import time
import typer
from rich.progress import track

app = typer.Typer()


@app.command("hello")
def hello(username: str):
    print(f"Hello: {username}")


@app.command("bonjour")
def bonjour(username: str):
    print(f"Bonjour: {username}")

@app.command("create")
def create():
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
