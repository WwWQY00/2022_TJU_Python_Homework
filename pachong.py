import requests
from bs4 import BeautifulSoup

layer = 0

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        return ""

def getURL(text):
    global layer
    if layer < 5:
        layer += 1
        soup = BeautifulSoup(text, 'html.parser')
        links = soup.find_all('a')
        url_lst = []
        for item in links:
            url = item.get('href')
            url_lst.append(url)
            url_lst = list(filter(lambda url_str: 'http' in url_str, url_lst))
        return url_lst
    else:
        return 0

def paChong(url):
    text = getHTMLText(url)
    lst = getURL(text)
    if lst != 0:
        print(lst)
        for u in lst:
            paChong(u)
    else:
        return 0

def main():
    url = "https://cn.fflogs.com/"
    paChong(url)

if __name__ == "__main__":
    main()