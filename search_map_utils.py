import requests


def get_organization(text, loclas='ru_RU', **params):
    search_api_server = "https://search-maps.yandex.ru/v1/"

    address_ll = "37.588392,55.734036"

    params['text'] = text
    params['lang'] = loclas
    params['apikey'] = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

    response = requests.get(search_api_server, params=params)
    if not response:
        raise RuntimeError(f'Ошибка выполнения запроса: {search_api_server}\n'
                           f'HTTP статус: {response.status_code} {response.reason}')

    organizations = response.json()['features']
    return organizations


def org_coord(organizations):
    return organizations[0]['geometry']['coordinates']


def org_info(organizations):
    data = organizations[0]['properties']['CompanyMetaData']
    return data['name'], data['address'], data['Hours']['text']
