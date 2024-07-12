from googlesearch import search


results = search("Google", num_results=10)
for res in results:
    print(res)