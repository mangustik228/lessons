import requests 

url = "https://my-json-server.typicode.com/typicode/demo/posts"

def getting_post(url):
    response = requests.get(url)
    if response.status_code == 200: 
        return response.json() 
    raise 

def main():
    result = getting_post()
    print(result)

if __name__ == '__main__':
    main()