from python_0210_practice_mrt_data_basic import line_name_dict
from python_0213_practice_mrt_data_line_to_transit_stations import *
from collections import defaultdict
from itertools import permutations
from pprint import pprint

change_line_possibilities_dict = defaultdict(list)
def populate_change_lines_possibilities_dict():
    line_name_list = list(line_name_dict.keys()) * 2
    possible_set = set(permutations(line_name_list, 2))
    for start_line, stop_line in possible_set:
        if start_line == stop_line:
            change_line_possibilities_dict[start_line, stop_line].append([start_line])
            for transit_line in line_name_dict.keys():

                if transit_line == start_line:
                    continue

                start_line_transit_stations_set = line_to_transit_stations_dict[start_line]
                transit_line_transit_stations_set = line_to_transit_stations_dict[transit_line]
                common_transit_station_set = start_line_transit_stations_set & transit_line_transit_stations_set
                if len(common_transit_station_set) <= 1:
                    continue
                change_line_possibilities_dict[start_line, stop_line].append([start_line, transit_line, stop_line])
        else:

            start_line_transit_stations_set = line_to_transit_stations_dict[start_line]
            stop_line_transit_stations_set = line_to_transit_stations_dict[stop_line]
            common_transit_stations_between_start_line_stop_line_set = start_line_transit_stations_set & stop_line_transit_stations_set
            if len(common_transit_stations_between_start_line_stop_line_set) > 0:
                change_line_possibilities_dict[start_line, stop_line].append([start_line, stop_line])
            for transit_line in line_name_dict.keys():
                if transit_line == start_line or transit_line == stop_line:
                    continue
                transit_line_transit_stations_set = line_to_transit_stations_dict[transit_line]
                common_transit_stations_between_start_line_transit_line_set = start_line_transit_stations_set & transit_line_transit_stations_set
                if len(common_transit_stations_between_start_line_transit_line_set) < 1:
                    continue
                common_transit_stations_between_stop_line_transit_line_set = stop_line_transit_stations_set & transit_line_transit_stations_set
                if len(common_transit_stations_between_stop_line_transit_line_set) < 1:
                    continue
                if common_transit_stations_between_start_line_transit_line_set == common_transit_stations_between_stop_line_transit_line_set and len(common_transit_stations_between_stop_line_transit_line_set) == 1:
                    continue
                change_line_possibilities_dict[start_line, stop_line].append([start_line, transit_line, stop_line])

if __name__ == '__main__':
    populate_line_to_transit_station_dict()
    populate_change_lines_possibilities_dict()
    pprint(change_line_possibilities_dict)