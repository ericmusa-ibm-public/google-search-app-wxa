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




### pushing to Container Registry

*Note* see https://cloud.ibm.com/registry/start
```sh
ibmcloud plugin install container-registry -r 'IBM Cloud'
ibmcloud login --sso
ibmcloud cr region-set us-south  # my techzone reservation region is "us-south"
ibmcloud target -g itz-watson-apps-xxxxxxxx
# ibmcloud cr namespace-add itz-watson-apps-xxxxxxxx-cr
## NOTE namespace is found in IBM Cloud > Resources > Container Registry > Namespaces
## no write permissions to create new namespaces


IMAGE_NAME=gsearch
NAMESPACE=itz-watson-apps-xxxxxxxx-cr
podman tag localhost/${IMAGE_NAME}:latest us.icr.io/${NAMESPACE}/${IMAGE_NAME}:latest
ibmcloud cr login --client podman
podman push us.icr.io/${NAMESPACE}/${IMAGE_NAME}:latest
ibmcloud cr image-list
```


### Creating Application in Code Engine
1. go to Code Engine in IBM Cloud
2. go to "Applications" and click the "Create" button to create a new application (...)
3. click "Configure image":
    - select your registry server from the list (may start with "private")
    - select/create a registry secret
    - if Server and Secret are correct, Namespace options will auto-populate - select from list
    - if Server, Secret, and Namespace are correct, Images will auto-populate - select from list
    - ":latest" tag default option, select from list
4. set concurrency/scaling options
5. *Important* scroll all the way down, open the "Image start options", and double check the Listening port is correct


### Exporting OpenAPI spec .json file
1. run the image locally, either in a container or on baremetal
2. open http://0.0.0.0:8000/docs to see the automated FastAPI documentation page
3. click the link to http://0.0.0.0:8000/openapi.json and save the openapi.json file


### modifying the openapi.json file to connect to watsonx Assistant
0. helpful to open the openapi.json file in VSCode text editor and click `ctrl + shift + f` to format the document to pretty-printed JSON
1. the very first line, `"openapi":"3.1.0"` --change to--> `"openapi":"3.0.0"` 
2. delete the following:
```
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
```
as well as the referenced `HTTPValidationError` and the reference within that, `ValidationError`. 
This is because there are some type arguments in these schemata whose syntax is incompatible with watsonx Assistant.
3. between the `info` and `paths` objects at the top of the file, add the following:
```
    "servers": [
        {
            "url": "https://<app-name>.xxxxxxxxxxxx.us-south.codeengine.appdomain.cloud/",
            "description": "<description>"
        }
    ],
```
where `<app-name>` refers to the name of an Application running in Code Engine.
Extensions in wxA require at least one `url` in `servers` to point to where the extension's service is located.