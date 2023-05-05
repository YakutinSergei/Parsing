import requests
import lxml

from bs4 import BeautifulSoup


def load_soup(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    res = requests.get(url=url, headers=header)
    res.encoding = 'utf-8'

    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def main():
    soup = load_soup('https://gg240.bet/ru/live?sportIds[]=esports_dota_2&sportIds[]=esports_counter_strike&tournamentIds[]=gin%3A9c157b43-909b-4281-b1b9-c66176472eba&tournamentIds[]=gin%3Aa30e9f66-271c-49f0-a81f-fd222b81f898&tournamentIds[]=gin%3A3c4bb034-6c39-4f47-a898-aa875d0b7f56&tournamentIds[]=gin%3A4468a241-829a-4eb7-8514-10948c5b8758&tournamentIds[]=gin%3A05534c02-86ac-4aa3-823c-d2d293316b7f&tournamentIds[]=gin%3A01e725f5-6b8c-49c8-be74-b24ebb93a2fb&tournamentIds[]=gin%3Ada6c160d-c13e-43fc-92ca-5f2c10a2a340&tournamentIds[]=gin%3A56e43df7-6cb5-492a-84dd-70ecc4367b6d&tournamentIds[]=gin%3Aa76ad8af-2aa4-49c8-b37d-1d8dcf8eb6be&tournamentIds[]=gin%3Ab46c88be-6c1c-406e-bd2f-fd05896b4ab9&tournamentIds[]=gin%3A9b3b3380-7452-4750-b0f1-adaec44b6c75&tournamentIds[]=gin%3A563fa90e-3dbe-4407-a9ae-1582e6e79056&tournamentIds[]=gin%3A7c8cf788-e0d8-4da5-a360-2cf9ea9ae73a&tournamentIds[]=gin%3A9b1b1086-44c7-43cb-92e9-b6d8af88ebd6&tournamentIds[]=gin%3Aa3c27be4-a2f2-4a87-a3db-7a6720678cad&tournamentIds[]=gin%3Ab738f41c-82bd-4511-929b-075c8b969205&tournamentIds[]=gin%3A3b88db7b-67f2-4427-926e-5da5f0dfa54d&tournamentIds[]=gin%3Abe5147a4-a2af-4962-b3b2-2c3afd404db4')
    players = soup.find('a', class_='__app-SmartLink-link __app-OverviewRow-container overviewRow__container___2uPYc')
    print(soup)

if __name__ == '__main__':
    main()