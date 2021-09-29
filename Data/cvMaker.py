import requests
from bs4 import BeautifulSoup


def information_getter(string: str) -> []:
    try:
        url = "https://www.merinfo.se/search?who=" + string + "&where="
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='result-list')
        name = results.a.text
        ssn = results.p.text
        ssn_last_char = string[-4:]
        ssn = ssn.replace('-XXXX', ssn_last_char)
        address = results.find_all('p')[1].text.strip()
        zip_code_city = address.split("\n", 1)[1].split()
        zip_code = zip_code_city[0]+zip_code_city[1]
        city = zip_code_city[2]
        print(address.split("\n", 1)[0].split())
        info_dic = {'name': name.strip(),
                    'ssn': ssn.strip(),
                    'address': address,
                    'zip_code': zip_code,
                    'city': city}
        return info_dic
    except AttributeError:
        return None


if __name__ == '__main__':
    pass
