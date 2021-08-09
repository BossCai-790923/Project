from python_0212_practice_mrt_data_transit_station_to_lines import populate_transit_station_to_lines_dict # Import a function
from python_0212_practice_mrt_data_transit_station_to_lines import transit_station_to_lines_dict # Import a dict
from collections import defaultdict
from pprint import pprint


line_to_transit_stations_dict = defaultdict(set)

def populate_line_to_transit_station_dict():

    populate_transit_station_to_lines_dict()
    for station, lines in transit_station_to_lines_dict.items():
        for line in lines:
            line_to_transit_stations_dict[line].add(station)





if __name__ == '__main__':

    populate_line_to_transit_station_dict()

    pprint(line_to_transit_stations_dict)
