# httpx имеет существеный минус, он не умеет декодировать 
# json с разными кодировками(это я только предпологаю а как оно 
# на самом деле работает я не знаю), типо от вк приходит 
# json который не мог декодировать httpx я думаю что это
# вк такие молодцы что  json приходит в разных кодировках
# с requsts такого нет

import httpx
import requests
# синтаксис у них один и тот же просто, что httpx асинхроный 
# и подерживает http2

def run_httpx(url:str):
    print("-"*50)
    # в httpx переадрицацию надо вкл самому
    response = httpx.get(url, follow_redirects=True)

    print(response.url, response.status_code, response.reason_phrase)

    # если нет json(a) то выдает исключение json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    # print(response.json())
    # httpx использует исключения python

    # выводит тело ответа
    # print(response.text)

def run_requests(url:str):
    print("-"*50)
    # requests по умолчанию имеет вкл переадрицацию
    response = requests.get(url)

    # url, статус код, 
    print(response.url, response.status_code, response.reason)

    
    # если нет json(a) то выдает исключение requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
    # print(response.json())
    # requests использует своё исключение

    # выводит тело ответа
    # print(response.text)


def main():
    url = "https://google.com/"
    run_httpx(url)
    run_requests(url)


if __name__ == "__main__":
    main()
    # я тут подумал и понял что я не то учу что надо 
    # я учу httpx хоть мне надо учить как работать с API
    # используя httpx