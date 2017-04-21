# HoneypotCF
Code to deploy an Honeypot to Cloud Foundry for project Titanium Crucible.

How to deploy (example)

```

 cf push

 ```

## Environment Variables

The variables embedded are set to connect to an ELK stack available over internet for demo purposes.

Change these variables in manifest.yml to connect to your own stack:

```

    LOG_HOST: tcteam.ddns.net
    LOG_PORT: 5000

 ```
 
 ## Output
 This is how an example log should show up on Kibana:
 
 ![Alt text](/images/HoneypotCFLogELK.png "HoneypotCFLogELK")

The code that can be used to start this App on docker is here:

https://github.com/FabioChiodini/titaniumcrucible


@FabioChiodini
