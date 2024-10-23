import requests


def main():
    locations = ['Лондон',
                 'аэропорт Шереметьево',
                 'Череповец',]
    parameters = {'3': '', 'n': '', 'q': '', 'T': '', 'M': '', 'lang': 'ru'}

    for location in locations:
        response = requests.get(
            f'https://wttr.in/{location}', params=parameters, timeout=20)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
