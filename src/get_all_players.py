import string

import requests
from bs4 import BeautifulSoup

from classes.player import Player
from helper_methods import merge_dictionaries, flatten_list

LETTERS = list(string.ascii_lowercase)

BASE_PLAYERS_URL = 'https://www.basketball-reference.com/players/'


def request_html_file(letter):
    request_string = BASE_PLAYERS_URL + letter
    return requests.get(request_string).text


def create_player_instance_from_table(player_entry):
    player_dictionary = {}
    for attribute in player_entry:
        if (attribute.get('data-append-csv')):
            player_dictionary['bref_id'] = attribute.get('data-append-csv')
        player_dictionary[attribute.get('data-stat')] = attribute.get_text()
    return player_dictionary


def parse_players_from_html_file(html_txt):
    bs_instance = BeautifulSoup(html_txt, 'html.parser')
    table_rows = bs_instance.find(id="players").find_all('tr')
    html_columns = list(map(lambda entry: entry.find_all('td') + entry.find_all('th'), table_rows))[1:]
    return list(map(lambda entry: create_player_instance_from_table(entry), html_columns))


def add_id_to_player_obj(player_list, letter):
    return list(map(lambda entry, i: merge_dictionaries(entry, {'id': letter + '-' + str(i), 'bref_letter': letter}),
                    player_list, range(len(player_list))))


def get_all_players():
    all_players = list(
        map(lambda letter: add_id_to_player_obj(parse_players_from_html_file(request_html_file(letter)), letter),
            LETTERS))
    flattened_list = flatten_list(all_players)
    return list(map(lambda player_info: Player(player_info), flattened_list))
