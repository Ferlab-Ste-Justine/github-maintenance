import argparse
import os
from git import Repo
from github import Github

parser = argparse.ArgumentParser(description='Bulk List GitHub Actions')
parser.add_argument('-o', '--githuborg', help='set github organization', required=True)
parser.add_argument('-t', '--githubtkn', help='set github token', required=True)
args = parser.parse_args()


def get_reused_actions(repos):
    dir_repos = os.getcwd() + '/repos'
    os.mkdir(dir_repos)
    reused_actions = []
    for repo in repos:
        print(f"\nRepo '{repo.name}'...")
        if not repo.archived:
            os.chdir(dir_repos)
            repo_url_withtoken = repo.clone_url.replace('https://', f'https://{args.githubtkn}@')
            Repo.clone_from(repo_url_withtoken, repo.name, depth=1)
            workflows_dir = f'{repo.name}/.github/workflows'

            if os.path.exists(workflows_dir):
                print("Workflow(s) found.")
                os.chdir(workflows_dir)
                reused_actions_found = 0
                for file in os.listdir(os.getcwd()):
                    for line in open(file, 'r'):
                        search_string = ' uses: '
                        if search_string in line:
                            reused_actions_found += 1
                            reused_action = line.split(search_string)[1].strip()
                            if reused_action not in reused_actions:
                                reused_actions.append(reused_action)

                if reused_actions_found > 0:
                    print("Reused action(s) found.")
                else:
                    print("No reused actions found.")
            else:
                print("No workflows found.\nSkipped.")
        else:
            print("Archived repo.\nSkipped.")

    reused_actions.sort()

    print("\nHere are all the reused actions that were found:")
    print("------------------------------------------------")
    print(*reused_actions, sep='\n')
    print("\nAll done.")


if __name__ == '__main__':
    repos = Github(args.githubtkn).get_organization(args.githuborg).get_repos()
    print(f"\n{repos.totalCount} repos in total.")
    get_reused_actions(repos)
