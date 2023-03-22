FROM python:3.11.2-slim-bullseye

WORKDIR /bulk-check-github-actions

COPY requirements.txt .
RUN pip install --no-cache-dir --root-user-action=ignore --disable-pip-version-check -r requirements.txt

COPY . .
