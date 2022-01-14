# PushLunch

## Lunch Money Push Notifications via Pushover

<div align="center">
    <p float="center">
        <img src=https://pushover.net/images/pushover-logo.svg
            width="195" alt="lunchable">
        <img src=https://i.imgur.com/FyKDsG3.png
            width="300" alt="lunchable">
    </p>
</div>

[![Lunchable Version](https://img.shields.io/pypi/v/lunchable?color=blue&label=lunchable)](https://github.com/juftin/lunchable)
[![PyPI](https://img.shields.io/pypi/pyversions/lunchable)](https://pypi.python.org/pypi/lunchable/)
[![Testing Status](https://github.com/juftin/lunchable/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/juftin/lunchable/actions/workflows/tests.yml?query=branch%3Amain)
[![GitHub License](https://img.shields.io/github/license/juftin/lunchable?color=blue&label=License)](https://github.com/juftin/lunchable/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/lunchable/badge/?version=latest)](https://lunchable.readthedocs.io/en/latest/?badge=latest)

`PushLunch` supports Push Notifications via [Pushover](https://pushover.net). Pushover supports iOS
and Android Push notifications. To get started just provide your Pushover
`User Key` directly or via the `PUSHOVER_USER_KEY` environment variable.

```shell
pip install lunchable
```

The below command checks for un-reviewed transactions in the current period and sends them as Push
Notifications. The `–-continuous` flag tells it to run forever which will only send you a push
notification once for each transaction. By default, it will check every 60 minutes - but this can be
changed using the `-–interval` argument.

```shell
lunchable plugins pushlunch notify --continuous --user-key <PUSHOVER_USER_KEY>
```

### Run via Docker

```shell
docker run --rm \
    --env LUNCHMONEY_ACCESS_TOKEN=${LUNCHMONEY_ACCESS_TOKEN} \
    --env PUSHOVER_USER_KEY=${PUSHOVER_USER_KEY} \
    juftin/lunchable:latest \
    lunchable plugins pushlunch notify --continuous
```

### More info on the [ReadTheDocs](https://lunchable.readthedocs.io/en/latest/pushlunch.html)
