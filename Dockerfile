# library/python:3-alpine
FROM library/python@sha256:ebcb1714a8f5abbf0b03262e518ca0453131cf720ea0a0f85e9bf3bfd7c1d53d

RUN apk --update add bash
RUN pip install flake8

WORKDIR /usr/local/src/stacker_blueprints
COPY . .

