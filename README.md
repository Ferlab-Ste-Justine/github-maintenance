# About

This repo purpose is to gather useful scripts for different sporadic maintenance operations on GitHub repositories.

# Scripts

## bulk-update-github

This script is to replace a string on every file under a certain directory on the default branch of all non-archived repositories in a GitHub organization.

Run the following commands to execute the script:
```
cd bulk-update-github
docker build -t bulk-update-github .
docker run --rm -t bulk-update-github python bulk-update-github.py [-d] -o GITHUBORG -t GITHUBTKN -l DIRLOOKUP -s STRINGOLD -r STRINGNEW -m MSGCOMMIT
```
