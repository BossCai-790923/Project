from python_0211_practice_mrt_data_station_to_lines import populate_station_to_lines_dict
from python_0211_practice_mrt_data_station_to_lines import station_to_lines_dict
from collections import defaultdict
from pprint import pprint
transit_station_to_lines_dict = defaultdict(set)

def populate_transit_station_to_lines_dict():

    populate_station_to_lines_dict()
    for station, lines in station_to_lines_dict.items():
        if len(lines) > 1:
            transit_station_to_lines_dict[station] = lines


if __name__ == '__main__':

    populate_transit_station_to_lines_dict()

    pprint(transit_station_to_lines_dict)