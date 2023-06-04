import GithubBot
# import TemplateGeneratorYattag
# import GetGithubInfo
from pprint import pprint
import inquirer

import time
import typer
from rich.progress import track

app = typer.Typer()

userData = {}
reposData = []
githubUserData = {}

##### Github Setup #####
@app.command("start")
def start():
    """Starts the program"""
    print("Welcome!")
    print("Authenticating")
    GithubBot.auth()

@app.command("new")
def new():
    """Creates a new repo: Portfolio"""
    GithubBot.create_repo()

@app.command("push")
def push():
    """Pushes the files in the util folder to your GitHub repository"""
    files = ['index.html']
    GithubBot.update(files)
    print("Success!")

##### Template Setup #####

@app.command("create")
def createTemplate():
    """Creates a new html template if not already exists"""

    for value in track(range(100), description="Processing..."):
        time.sleep(0.01)
        if value == 10:
            print(f"Checking for existing template")

        if value == 30:
            print(f"Creating new template")

        if value == 50:
            print(f"Creating new template")

    print(f"Template successfully created")

##### Data Selection #####

@app.command("getRepos")
def getRepos():
    '''Gets all the repositories in your Github account'''
    reposData = GithubBot.getRepoInfo()
    print(reposData)

@app.command("getInfo")
def getInfo():
    '''Gets your Github account information'''
    githubUserData = GithubBot.getGithubInfo()
    print(githubUserData)

@app.command("selectRepos")
def selectRepos():
    '''Selects the repositories to be displayed in your portfolio'''
    print("Selecting repos... ")

    if len(reposData) == 0:
        print("You have no repos!")
        return
    
    repoNames = []
    for repo in reposData:
        repoNames.append(repo['name'])

    # Use Inquirer to ask the user if they want to include the repo in their portfolio
    questions = [
        inquirer.Checkbox('repos',
                            message="Select the repos you want to include in your portfolio",
                            choices=repoNames,
                        ),
    ]

    answers = inquirer.prompt(questions)
    # print(answers["repos"])

    for repo in reposData:
        if repo['name'] in answers["repos"]:
            repo['display'] = True
        else:
            repo['display'] = False

    print("Selection Updated!")


@app.command("updateWholeProfile")
def updateUserData():
    '''Updates the user data'''
    print("Updating profile... ")
    for value in track(range(len(8)), description="Processing..."):
        if value == 0:
            print("Enter your name: ")
            userData['name'] = input()
        elif value == 1:
            print("Enter your email: ")
            userData['email'] = input()
        elif value == 2:
            print("Enter your phone number: ")
            userData['phone'] = input()
        elif value == 3:
            print("Enter your bio: ")
            userData['bio'] = input()
        elif value == 4:
            print("Enter your about: ")
            userData['about'] = input()
        elif value == 5:
            print("Enter your twitter: ")
            userData['socialMedia']['twitter'] = input()
        elif value == 6:
            print("Enter your facebook: ")
            userData['socialMedia']['facebook'] = input()
        elif value == 7:
            print("Enter your instagram: ")
            userData['socialMedia']['instagram'] = input()


    print("Profile Updated!")


@app.command("updateProfileDetails")
def updateUserDataIndividually():
    '''Lets the user select which data to update'''
    questions = [
        inquirer.List(
            "value",
            message="Select which data field to update",
            choices=["name", "email", "phone", "bio", "about", "twitter", "facebook", "instagram"],
        ),
    ]

    answers = inquirer.prompt(questions)
    pprint(answers)

@app.command("cut")
def selectComamand():
    '''Shortcut to select the command to be executed instead of typing it'''
    commandNames = []
    for command in app.registered_commands:
        commandNames.append(command.name)

    questions = [
        inquirer.List(
            "value",
            message="Select which command to execute",
            choices=commandNames,
        ),
    ]

    answers = inquirer.prompt(questions)

    for i in range(len(app.registered_commands)):
        if answers["value"] == app.registered_commands[i].name:
            app.registered_commands[i].callback()


if __name__ == "__main__":
    app()
