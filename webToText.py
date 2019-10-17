import re
import urllib.request
from bs4 import BeautifulSoup

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    elif '\n' == element:
        return False
    return True


output = open("text.txt", "w+")
while True:
    print("HTML: ", end="")
    try:
        url = input().strip()
        if url == "exit":
            break
        print("URL:", url)
        html = urllib.request.urlopen(url)
        soup = BeautifulSoup(html)
        print("reading...")
        data = soup.findAll(text=True)
        print("filtering...")
        result = filter(visible, data)
        print("writing...")
        for string in list(result):
            output.write(string)
        output.flush()
    except Exception:
        print("Hek something went wrong")
output.close()
