import requests 

url = "https://gorest.co.in/public/v1/users"

def some_func(url: str) -> dict:
    return requests.get(url).json()


def main():
    r = some_func(url)
    print(r)


if __name__ == '__main__':
    main()