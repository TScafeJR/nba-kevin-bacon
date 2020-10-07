import json
from helper_methods import create_split_list_vals


player_data_file = open('src/data/output.json')
player_data = json.load(player_data_file)


def get_nodes(file_data):
    return [{'id': i, 'label': player['name'].replace('*', '') + ' ' + player['bref_id'], 'bref_id': player['bref_id']} for i,player in enumerate(file_data)]


def get_edges(file_data):
    edge_list = []
    for player in file_data:
        for teammate in player['teammates']['py/set']:
            edge_list.append({'source': player['bref_id'], 'target': teammate, 'value': 1})
    return edge_list

def get_edge_dict(file_data):
    edge_dict = {}
    for node in get_nodes(file_data):
        edge_dict[node['bref_id']] = {'id': node['id'], 'label': node['label']}
    return edge_dict


def create_set_of_edges(file_data):
    edges = get_edges(file_data)
    edges_list = list(map(lambda edge: sorted([edge['source'], edge['target']]), edges))
    edges_str_sorted_list = list(map(lambda entry: f'{entry[0]}-{entry[1]}', edges_list))
    edges_set = list(set(edges_str_sorted_list))
    formatted_edge_list = create_split_list_vals(edges_set, '-')
    return list(map(lambda edge: {'source': edge[0], 'target': edge[1], 'value': 1},formatted_edge_list))

def convert_vals_to_id(edges_list, edges_dict):
    return list(map(lambda edge: {
        'source': edges_dict[edge['source']]['id'],
        'target': edges_dict[edge['target']]['id'],
        'value': 1
    }, edges_list))

def print_gml_element(element, type):
    print(' ', type)
    print('  [')
    for key in element.keys():
        if (isinstance(element[key], str)):
            print('    ', key, f'"{element[key]}"')
        else:
            print('    ', key, element[key])
    print('  ]')


def print_gml_file(file_data):
    nodes = get_nodes(file_data)
    edges_dict = get_edge_dict(file_data)
    edges_list = create_set_of_edges(file_data)
    edges_with_ids = convert_vals_to_id(edges_list, edges_dict)

    print('graph')
    print('[')
    print('  directed 0')

    for node in nodes:
        print_gml_element(node, 'node')

    for edge in edges_with_ids:
        print_gml_element(edge, 'edge')

    print(']')


print_gml_file(player_data)

# print(convert_vals_to_id(get_edges(player_data), get_edge_dict(player_data)))
player_data_file.close()
