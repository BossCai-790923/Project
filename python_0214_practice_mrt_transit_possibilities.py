from python_0210_practice_mrt_data_basic import line_name_dict
from python_0213_practice_mrt_data_line_to_transit_stations import populate_transit_station_to_lines_dict
from pprint import pprint
from collections import defaultdict
from itertools import permutations
from itertools import combinations
# line_name_dict = {  'green_line'        : green_line,
#                     'green_sub_line'    : green_sub_line,
#                     'red_line'          : red_line,
#                     'yellow_line'       : yellow_line,
#                     'yellow_sub_line'   : yellow_sub_line,
#                     'purple_line'       : purple_line,
#                     'brown_line'        : brown_line,
#                     'blue_line'         : blue_line}
transit_station_lines_dict = defaultdict(set)
#Max twice
change_line_possibilities_dict=defaultdict(tuple)
line_to_transit_stations_dict = defaultdict(set)
def populate_line_to_transit_station_dict():
    line_combination_set = set(combinations(line_name_dict, 2))

    for line1_n, line2_n in line_combination_set:
        line1_stations_set = set(line_name_dict[line1_n])
        line2_stations_set = set(line_name_dict[line2_n])
        transit_stations = tuple(line1_stations_set & line2_stations_set)

        if len(transit_stations) > 0:  #
            for transit_station in transit_stations:
                transit_station_lines_dict[line1_n].add(transit_station)
                transit_station_lines_dict[line2_n].add(transit_station)
populate_line_to_transit_station_dict()
pprint(transit_station_lines_dict)

st = input('start')
st_line = input('startline')
end = input('end:')
endline = input('endline:')

def populate_change_lines_possibilities_dict():
    line_name_list = tuple(line_name_dict.keys()) * 2
    pprint(line_name_list)

    possible_set0 = tuple(permutations(line_name_list, 2))
    possible_set1 = tuple(permutations(line_name_list, 3))
    possible_set=possible_set1+possible_set0
    # pprint(possible_set)
    for i in range(len(possible_set)):
        if possible_set[i][0]==st_line and possible_set[i][-1]==endline:
            if len(possible_set[i]) ==2:
                for x in range(len(line_name_dict[possible_set[i][0]])):
                    for y in range(len(line_name_dict[possible_set[i][1]])):

                        if line_name_dict[possible_set[i][0]][x]==line_name_dict[possible_set[i][0]][x]:
                            if len(possible_set[i]) == 2:
                                print(f'you need first get to {possible_set[i][0]},and get to {possible_set[i][1]}')
                                exit()
                            else:
                                print(f'you need first get to {possible_set[i][0]},and get to {possible_set[i][1]},finally get to {possible_set[i][2]}')
                                exit()

                        else:
                            if len(possible_set[i]) ==3:
                                for x in range(len(line_name_dict[possible_set[i][0]])):
                                    for y in range(len(line_name_dict[possible_set[i][1]])):

                                        if line_name_dict[possible_set[i][0]][x] == line_name_dict[possible_set[i][0]][x]:
                                            pass
                                for x in range(len(line_name_dict[possible_set[i][1]])):
                                    for y in range(len(line_name_dict[possible_set[i][2]])):

                                        if line_name_dict[possible_set[i][0]][x] ==line_name_dict[possible_set[i][0]][x]:
                                            if len(possible_set[i])==2:
                                                print(f'you need first get to {possible_set[i][0]},and get to {possible_set[i][1]}')
                                                exit()
                                            else:
                                                print(f'you need first get to {possible_set[i][0]},and get to {possible_set[i][1]},finally get to {possible_set[i][2]}')
                                                exit()
                                for x in range(len(line_name_dict[possible_set[i][0]])):
                                    for y in range(len(line_name_dict[possible_set[i][2]])):

                                        if line_name_dict[possible_set[i][0]][x] ==line_name_dict[possible_set[i][0]][x]:
                                            pass











populate_transit_station_to_lines_dict()


populate_change_lines_possibilities_dict()
