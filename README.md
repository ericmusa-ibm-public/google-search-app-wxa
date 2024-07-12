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
