# PushLunch: Push Notifications via Pushover

<div align="center">
    <p float="center">
        <img src=https://pushover.net/images/pushover-logo.svg
            width="35%" alt="lunchable">
        <img src=https://i.imgur.com/FyKDsG3.png
            width="60%" alt="lunchable">
    </p>
</div>

---

`PushLunch` supports Push Notifications via [Pushover](https://pushover.net). Pushover supports iOS
and Android Push notifications. To get started just provide your Pushover
`User Key` directly or via the `PUSHOVER_USER_KEY` environment variable.

## Run via the Lunchable CLI

The below command checks for un-reviewed transactions in the current period
and sends them as Push Notifications. The `--continuous` flag tells it to run
forever which will only send you a push notification once for each transaction.
By default it will check every 60 minutes, but this can be changed using the
`--interval` argument.

```shell
lunchable plugins pushlunch notify --continuous
```

## Run via Docker

```shell
docker run --rm \
    --env LUNCHMONEY_ACCESS_TOKEN=${LUNCHMONEY_ACCESS_TOKEN} \
    --env PUSHOVER_USER_KEY=${PUSHOVER_USER_KEY} \
    juftin/lunchable:latest \
    lunchable plugins pushlunch notify --continuous
```

## Run via Python

```python
from lunchable.plugins.pushlunch import PushLunch
```

::: lunchable.plugins.pushlunch.PushLunch
    handler: python
    options:
        show_bases: false
        allow_inspection: true
        heading_level: 3
