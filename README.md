# About

This repo purpose is to gather useful scripts for different sporadic maintenance operations on GitHub repositories.

# Docker Image

Run the following command to build the Docker image:
```
docker build -t github-maintenance .
```

# Scripts

## bulk-update-github.py

This script is to replace a string on every file under a certain directory on the default branch of all non-archived repositories in a GitHub organization.

Run the following command to execute the script:
```
docker run --rm -t github-maintenance python scripts/bulk-update-github.py [-d] -o GITHUBORG -t GITHUBTKN -l DIRLOOKUP -s STRINGOLD -r STRINGNEW -m MSGCOMMIT -n USERNAME -e USEREMAIL
```

## bulk-check-github-actions.py

This script is to check for the conclusion of the last run on the default branch for every workflow of all non-archived repositories in a GitHub organization.

Run the following command to execute the script:
```
docker run --rm -t github-maintenance python scripts/bulk-check-github-actions.py -o GITHUBORG -t GITHUBTKN -f TIMEFRAME
```

## bulk-list-github-actions.py

This script is to list all the reused actions on the default branch of all non-archived repositories in a GitHub organization.

Run the following command to execute the script:
```
docker run --rm -t github-maintenance python scripts/bulk-list-github-actions.py -o GITHUBORG -t GITHUBTKN
```
