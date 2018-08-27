import click
import libbackup

@click.command()
@click.argument('username')
@click.option('--backup-repositories', '-r', is_flag=True, help='Backup GitHub Repositories.')
@click.option('--backup-gists', '-g', is_flag=True, help='Backup GitHub Gists.')

def main(backup-repositories, backup-gists):
    if not(backup-repositories or backup-gists):
        noargs()
    
if __name__ == "__main__":
    main()

def noargs():
    while True:
        username = input("Enter the GitHub account username to perform a backup of")
        if libbackup.siteexists("https://api.github.com/users/" + username):
            break
        else:
            print("Username does not exist")
    
    answerToBool = {"y": True, "n": False}

    while True:
        while True:
            answer = input("Backup Repositories? (y/n)")
            if answer.lower() in ["y", "n"]:
                backupRepos = answerToBool[answer]
                break
            else:
                print("Invalid answer")

        while True:
            answer = input("Backup Gists? (y/n)")
            if answer.lower() in ["y", "n"]:
                backupGists = answerToBool[answer]
                break
            else:
                print("Invalid answer")
        
        if backupRepos or backupGists:
            break
        else:
            print("Repositories, Gists or both must be selected")
    
    if backupGists == True:
        giststext = "--backup-repositories "
    else:
        giststext = ""
    
    if backupGists == True:
        giststext = "--backup-gists "
    else:
        giststext = ""
    print("Next time, use ") 

else:
    # Change your username here
    username = "Richienb"
