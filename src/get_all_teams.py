import requests
from bs4 import BeautifulSoup

from classes.season_entry import SeasonEntry

# HtmlFile = open('src/data/test_player_txt.html', 'r', encoding='utf-8')
# source_code = HtmlFile.read()

BASE_PLAYERS_URL = 'https://www.basketball-reference.com/players'
REQUIRED_SEASON_KEYS = {'season', 'team_id', 'lg_id'}


def request_player_html_page(player):
    request_url = f'{BASE_PLAYERS_URL}/{player.bref_letter}/{player.bref_id}.html'
    return requests.get(request_url).text

def safe_create_season_entry(season):
    season_dict = extract_season_info_from_table(season)
    if season_dict.keys() >= REQUIRED_SEASON_KEYS:
        return SeasonEntry(season_dict)

    return None


def extract_season_info_from_table(season_entry):
    season_dictionary = {}
    for attribute in season_entry:
        season_dictionary[attribute.get('data-stat')] = attribute.get_text()
    return season_dictionary


def parse_per_game_seasons_from_html_file(html_txt):
    bs_instance = BeautifulSoup(html_txt, 'html.parser')
    table_rows = bs_instance.find(id="per_game").tbody.find_all('tr') if bs_instance.find(id="per_game") is not None else []
    return table_rows


def parse_season_values_from_row(html_text):
    season_headers = html_text.find_all('th')
    season_stats = html_text.find_all('td')
    return season_headers + season_stats


def parse_season_entry_list(player):
    player_html_page = request_player_html_page(player)
    seasons_info_html = list(map(lambda season: parse_season_values_from_row(season),
                                 parse_per_game_seasons_from_html_file(player_html_page)))
    season_info_dictionary_list = list(map(lambda season: safe_create_season_entry(season), seasons_info_html))
    filtered_list = [season for season in season_info_dictionary_list if season is not None]
    return filtered_list

def add_season_info_to_player(player, season_info):
    for season in season_info:
        player.add_season(season)

def add_team_info_to_player(player, season_info):
    for season in season_info:
        player.add_team(season)

def add_team_and_season_info_to_player(player):
    season_info = parse_season_entry_list(player)
    add_season_info_to_player(player, season_info)
    add_team_info_to_player(player, season_info)
    return player