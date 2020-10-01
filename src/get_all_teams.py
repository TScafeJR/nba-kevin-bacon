import requests

BASE_PLAYERS_URL = 'https://www.basketball-reference.com/players'

def request_player_html_page(player):
    request_url = f'{BASE_PLAYERS_URL}/{player.bref_letter}/{player.bref_id}'
    