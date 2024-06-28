import requests
import json


def get_ship_url_by_name(name: str):
    star_wars_ships = requests.get('https://swapi.dev/api/starships')
    ships_data = json.loads(star_wars_ships.text)
    for ship in ships_data['results']:
        if ship['name'] == name:
            return ship['url']


def get_info_ship_by_url():
    result_dict = dict()
    required_fields = ["max_atmosphering_speed", "pilots", "starship_class", "name"]
    ship_url = get_ship_url_by_name(name='X-wing')
    get_info_x_wing = requests.get(url=ship_url)
    get_info_json = json.loads(get_info_x_wing.text)
    for field in get_info_json:
        if field in required_fields:
            result_dict[field] = get_info_json[field]
    return get_pilot_by_url(result_dict)


def get_pilot_by_url(ship: dict):
    pilots = list()
    pilot = dict()
    requires_fields_for_pilots = ['height', 'homeworld', 'mass', 'name']

    for url_pilots in ship['pilots']:
        info_pilots = requests.get(url=url_pilots)
        info_pilots_json = json.loads(info_pilots.text)

        for field in info_pilots_json:
            if field in requires_fields_for_pilots:
                pilot[field] = info_pilots_json[field]
        pilots.append(pilot)
        pilot = {}

    ship['pilots'] = pilots
    return get_name_homeworld_by_url(ship)


def get_name_homeworld_by_url(ship: dict):
    for pilots in ship['pilots']:
        get_name = requests.get(url=pilots['homeworld'])
        name_json = json.loads(get_name.text)
        pilots['homeworld_url'] = pilots['homeworld']
        pilots['homeworld'] = name_json['name']
    return ship


if __name__ == "__main__":
    info_ship = get_info_ship_by_url()

    print(info_ship)
    with open(file='starwars.json', mode='w') as file:
        json.dump(info_ship, file, ensure_ascii=False, indent=4)
