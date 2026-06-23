import httpx
import requests

def run_httpx(url:str):
    print("-"*50)
    response = httpx.get(url)

    print(response.url)
    # если нет json(a) то выдает исключение json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    # print(response.json())
    # httpx использует исключения python

def run_requests(url:str):
    print("-"*50)
    response = requests.get(url)

    print(response.url)
    # если нет json(a) то выдает исключение requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    # print(response.json())
    # requests использует своё исключение



def main():
    url = "https://google.com/"
    run_httpx(url)
    run_requests(url)


if __name__ == "__main__":
    main()