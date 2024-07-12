from googlesearch import search


results = search("hospitals in Marietta, GA", num_results=10)
for res in results:
    print(res)

