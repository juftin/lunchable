# LunchMoney API Clients

## Generating API Clients

## Docker

```shell
docker run --rm \
  --volume ${PWD}:/work \
  --workdir /work \
  timbru31/java-node \
  /bin/bash -c "npm install && npm run generate"
```

### MacOS

1. Install Base Dependencies (Java)

    ```bash
    brew install openjdk
    sudo ln -sfn \
        ${HOMEBREW_PREFIX}/opt/openjdk/libexec/openjdk.jdk \
        /Library/Java/JavaVirtualMachines/openjdk.jdk
    ```

2. Install Generator

    ```bash
    npm install
    ```

3. Generate Clients

    ```bash
    npm run generate
    ```
