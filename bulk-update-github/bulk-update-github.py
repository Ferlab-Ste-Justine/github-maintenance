import argparse
import os
from git import Repo
from github import Github

parser = argparse.ArgumentParser(description='Bulk Update GitHub')
parser.add_argument('-d', '--dryrun', action='store_true', help='run without adding/committing/pushing changes')
parser.add_argument('-o', '--githuborg', help='set github organization', required=True)
parser.add_argument('-t', '--githubtkn', help='set github token', required=True)
parser.add_argument('-l', '--dirlookup', help='set directory to lookup', required=True)
parser.add_argument('-s', '--stringold', help='set string to search for', required=True)
parser.add_argument('-r', '--stringnew', help='set string to replace with', required=True)
parser.add_argument('-m', '--msgcommit', help='set message for the commit', required=True)
args = parser.parse_args()


def update(repos):
    dir_repos = os.getcwd() + '/repos'
    os.mkdir(dir_repos)
    for repo in repos:
        print(f"\nRepo '{repo.name}'...")
        if not repo.archived:
            os.chdir(dir_repos)
            repo_url_withtoken = repo.clone_url.replace('https://', f'https://{args.githubtkn}@')
            repo_cloned = Repo.clone_from(repo_url_withtoken, repo.name, depth=1)
            os.chdir(repo.name)

            if os.path.exists(args.dirlookup):
                files_updated = 0
                for file_name in os.listdir(args.dirlookup):
                    file = os.path.join(args.dirlookup, file_name)

                    with open(file, 'r') as f:
                        content = f.read()

                    new_content = content.replace(args.stringold, args.stringnew)

                    if new_content != content:
                        with open(file, 'w') as f:
                            f.write(new_content)
                            files_updated += 1

                if files_updated > 0:
                    print(f"{files_updated} file(s) with changes.")
                    if args.dryrun:
                        print("Not updated as dry-run mode is enabled.")
                    else:
                        repo_cloned.index.add(args.dirlookup)
                        repo_cloned.index.commit(args.msgcommit)
                        repo_cloned.remotes.origin.push()
                        print("Updated.")
                else:
                    print("No files with changes.\nSkipped.")
            else:
                print("No directory to lookup.\nSkipped.")
        else:
            print("Archived repo.\nSkipped.")

    print("\nAll done.")


if __name__ == '__main__':
    repos = Github(args.githubtkn).get_organization(args.githuborg).get_repos()
    print(f"\n{repos.totalCount} repos in total.")
    update(repos)
