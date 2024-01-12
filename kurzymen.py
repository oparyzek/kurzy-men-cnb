import requests
from bs4 import BeautifulSoup

def get_exchange_rates():
    # adresa webu kde budeme brat aktualni kurzy men
    url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/'

    # stahnuti obsahu
    response = requests.get(url)

    if response.status_code == 200:
        # vytvoreni objektu BeautifulSoap pro analyzu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # vyhledani tabulky s kurzy men
        table = soup.find('table', {'class': 'kurzy'})

        if table:
            # prochazime radky tabulky 
            for row in table.find_all('tr'):
                # ziskani jednotlivich budek v radku
                cells = row.find_all('td')

                if cells:
                    # ziskani nazvu meny a kurzu
                    currency = cells[2].text.strip()
                    rate = cells[4].text.strip()

                    # vypis informaci o mene
                    print(f"{currency}: {rate}")

        else:
            print("Nepodařilo se najít tabulku s kurzy měn.")
    else:
        print(f"Nepodařilo se stáhnout stránku. Kód chyby: {response.status_code}")

# zavoleni funkce pro ziskani aktualnich kurzu men
get_exchange_rates()