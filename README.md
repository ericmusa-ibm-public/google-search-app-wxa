# google-search-app-wxa
A webservice to serve content to an IBM watsonx Assistant via a custom extension.


## Steps:
1. write the app locally as a script (single job/batch)
2. rewrite the functional script as a local server/webservice (application/long running)
3. containerize the webservice locally
4. deploy container to public/external service
--> web app is in the cloud or somewhere accessible to the cloud where wxA can access it



### assuming you have Python3.X installed:
1. `python3.12 -m venv .venv`
2. `source ./.venv/bin/activate`
3. `pip install googlesearch-python`
4. `python`
4.1 `with open('gsearch.py', 'r') as f: exec(f.read())`




### pushing to CR and then to CE

```
#!/bin/sh

# https://cloud.ibm.com/registry/start

ibmcloud plugin install container-registry -r 'IBM Cloud'
ibmcloud login --sso
ibmcloud cr region-set us-south  # my techzone reservation region is "us-south"
ibmcloud target -g itz-watson-apps-xxxxxxxx
# ibmcloud cr namespace-add itz-watson-apps-xxxxxxxx-cr
## NOTE namespace is found in IBM Cloud > Resources > Container Registry > Namespaces
## no write permissions to create new namespaces


## Documented example:
# docker pull hello-world
# docker tag hello-world us.icr.io/<my_namespace>/<my_repository>:<my_tag>
# docker push us.icr.io/<my_namespace>/<my_repository>:<my_tag>
# ibmcloud cr image-list


IMAGE_NAME=gsearch
NAMESPACE=itz-watson-apps-eby1zl6u-cr
podman tag localhost/${IMAGE_NAME}:latest us.icr.io/${NAMESPACE}/${IMAGE_NAME}:latest
ibmcloud cr login --client podman
podman push us.icr.io/${NAMESPACE}/${IMAGE_NAME}:latest
ibmcloud cr image-list

# ibmcloud ce application create --name APP_NAME --image IMAGE_REF [--concurrency CONCURRENCY] [--concurrency-target CONCURRENCY_TARGET] [--cpu CPU] [--env ENV] [--env-from-configmap ENV_FROM_CONFIGMAP] [--env-from-secret ENV_FROM_SECRET] [--ephemeral-storage EPHEMERAL_STORAGE] [--force] [--max-scale MAX_SCALE] [--memory MEMORY] [--min-scale MIN_SCALE] [--mount-configmap MOUNT_CONFIGMAP] [--mount-secret MOUNT_SECRET] [--no-cluster-local] [--no-wait] [--output OUTPUT] [--port PORT] [--probe-live PROBE_LIVE] [--probe-ready PROBE_READY] [--quiet] [--registry-secret REGISTRY_SECRET] [--request-timeout REQUEST_TIMEOUT] [--revision-name REVISION_NAME] [--scale-down-delay SCALE_DOWN_DELAY] [--service-account SERVICE_ACCOUNT] [--user USER] [--visibility VISIBILITY] [--wait] [--wait-timeout WAIT_TIMEOUT]


## NOTE see [this](redo_erm/code-engine_config.png) for an example of a successful Code Engine App deployment
```