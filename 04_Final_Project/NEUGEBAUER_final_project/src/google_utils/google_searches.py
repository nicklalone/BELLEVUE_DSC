import googlesearch

search_results = []

def get_google_results(search_string):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found. This is really bad.")

    for j in search(search_string, tld="co.in", num=10, stop=1, pause=2):
        search_results.append(j)

    return j
