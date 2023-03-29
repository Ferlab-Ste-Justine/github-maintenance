import argparse
from datetime import datetime, timedelta
from github import Github

parser = argparse.ArgumentParser(description='Bulk Check GitHub Actions')
parser.add_argument('-o', '--githuborg', help='set github organization', required=True)
parser.add_argument('-t', '--githubtkn', help='set github token', required=True)
parser.add_argument('-f', '--timeframe', type=int, help='set time frame (in hours)', required=True)
args = parser.parse_args()


def check_actions(repos):
    time_period = datetime.now() - timedelta(hours=args.timeframe)
    for repo in repos:
        print(f"\nRepo '{repo.name}'...")
        if not repo.archived:
            workflows = repo.get_workflows()
            if workflows.totalCount > 0:
                for workflow in workflows:
                    runs = workflow.get_runs()
                    if runs.totalCount > 0:
                        for run in runs:
                            if run.head_branch == repo.default_branch:
                                if run.created_at >= time_period:
                                    print(f"Last run conclusion is '{run.conclusion}' for workflow '{workflow.name}'.")
                                else:
                                    print(f"Last run is older than {args.timeframe}h for workflow '{workflow.name}'. Skipped.")
                                break
                    else:
                        print(f"No runs found for workflow '{workflow.name}'. Skipped.")
            else:
                print("No workflows found.\nSkipped.")
        else:
            print("Archived repo.\nSkipped.")

    print("\nAll done.")


if __name__ == '__main__':
    repos = Github(args.githubtkn).get_organization(args.githuborg).get_repos()
    print(f"\n{repos.totalCount} repos in total.")
    check_actions(repos)
