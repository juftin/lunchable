ARG BASE_IMAGE
FROM ${BASE_IMAGE:-python:3.11-slim}

MAINTAINER Justin Flannery "juftin@juftin.com"

RUN apt-get update && apt-get install -y jq && apt-get clean

COPY requirements.txt /tmp/project/requirements.txt
COPY README.md /tmp/project/README.md
COPY pyproject.toml /tmp/project/pyproject.toml
COPY lunchable /tmp/project/lunchable

RUN pip install -r /tmp/project/requirements.txt
RUN pip install /tmp/project && \
    rm -rf /tmp/project

SHELL ["/bin/bash", "-c"]

RUN _LUNCHABLE_COMPLETE=bash_source lunchable > ${HOME}/.lunchable-complete.bash && \
    echo "[[ ! -f ${HOME}/.lunchable-complete.bash ]] || source ${HOME}/.lunchable-complete.bash" >> /root/.bashrc

CMD ["lunchable", "--help"]
