FROM python:3.11.2-slim-bullseye

WORKDIR /bulk-update-github

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN mkdir /root/.ssh && ssh-keyscan github.com >> /root/.ssh/known_hosts

COPY requirements.txt .
RUN pip install --no-cache-dir --root-user-action=ignore --disable-pip-version-check -r requirements.txt

COPY . .
