import requests


def main():
    locations = ['Лондон',
                 'аэропорт Шереметьево',
                 'Череповец',]
    options = '3nqT'
    units = 'M'
    lang = 'ru'

    for location in locations:
        url_template = f'https://wttr.in/{
            location}?{options}{units}&lang={lang}'
        response = requests.get(url_template, timeout=10)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
