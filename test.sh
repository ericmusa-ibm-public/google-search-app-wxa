curl --location --request POST 'http://127.0.0.1:8000/search' \
--header 'Content-Type: application/json' \
--data '{"query": "hospitals in Miami"}' | jq

