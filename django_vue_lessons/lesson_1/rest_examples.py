headers = [["URL Endpoint", "Http Verb", "Expected Outcome", "Status Code"]]

data = [
    ["/products/", "GET", "A list with all our products (JSON)", "200 OK"],
    ["/products/17/", "GET",
        "The details of the product with pk (JSON)", "200 OK"],
    ["/products/21/", "GET", "An Error Message and No Product", "404 Not Found"],
    ["/products/", "POST", "Creation of a New Product", "201 Created"],
    ["/products/15", "PUT", "An update to the product instance with pk 15", "200 OK"],
    ["/products/15", "DELETE",
        "Deletion of the product instance with pk 15", "204 No Content"],
]
result = headers + [*filter(lambda r: "GET" in r[1], data)]

lst_max = [max(*[len(datum[i]) for datum in result]) +
           3 for i in range(len(result[0]))]

for datum in result:
    info = "|"
    for txt, txt_len in zip(datum, lst_max):
        info += " " + txt + (" " * (txt_len - len(txt))) + "|"
    print(info)
