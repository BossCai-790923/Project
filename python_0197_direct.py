from collections import defaultdict
from itertools import permutations
from itertools import combinations
from pprint import pprint

# PREPARE DATA BEGIN =================================

green_line = (
    'Pasir Ris', 'Tampines', 'Simei', 'Tanah Merah', 'Bedok', 'Kembangan', 'Eunos', 'Paya Lebar', 'Aljunied', 'Kallang',
    'Lavender', 'Bugis', 'City Hall', 'Raffles Place', 'Tanjong Pagar', 'Outram Park', 'Tiong Bahru', 'Redhill',
    'Queenstown', 'Commonwealth', 'Buona Vista', 'Dover', 'Clementi', 'Jurong East', 'Chinese Garden', 'Lakeside',
    'Boon Lay', 'Pioneer', 'Joo Koon', 'Gul Circle', 'Tuas Crescent', 'Tuas West Road', 'Tuas Link')
green_sub_line = ('Tanah Merah', 'Expo', 'Changi Airport')

red_line = (
    'Jurong East', 'Bukit Batok', 'Bukit Gombak', 'Choa Chu Kang', 'Yew Tee', 'Kranji', 'Marsiling', 'Woodlands',
    'Admiralty', 'Sembawang', 'Canberra', 'Yishun', 'Khatib', 'Yio Chu Kang', 'Ang Mo Kio', 'Bishan', 'Braddell',
    'Toa Payoh', 'Novena', 'Newton', 'Orchard', 'Somerset', 'Dhoby Ghaut', 'City Hall', 'Raffles Place', 'Marina Bay',
    'Marina South Pier')

yellow_line = (
    'Dhoby Ghaut', 'Bras Basah', 'Esplanade', 'Promenade', 'Nicoll Highway', 'Stadium', 'Mountbatten', 'Dakota',
    'Paya Lebar', 'MacPherson', 'Tai Seng', 'Bartley', 'Serangoon', 'Lorong Chuan', 'Bishan', 'Marymount', 'Caldecott',
    'Botanic Gardens', 'Farrer Road', 'Holland Village', 'Buona Vista', 'one-north', 'Kent Ridge', 'Haw Par Villa',
    'Pasir Panjang', 'Labrador Park', 'Telok Blangah', 'HarbourFront')
yellow_sub_line = ('Marina Bay', 'Bayfront', 'Promenade')

purple_line = (
    'HarbourFront', 'Outram Park', 'Chinatown', 'Clarke Quay', 'Dhoby Ghaut', 'Little India', 'Farrer Park',
    'Boon Keng',
    'Potong Pasir', 'Woodleigh', 'Serangoon', 'Kovan', 'Hougang', 'Buangkok', 'Sengkang', 'Punggol')

brown_line = (
    'Woodlands North', 'Woodlands', 'Woodlands South', 'Springleaf', 'Lentor', 'Mayflower', 'Bright Hill',
    'Upper Thomson',
    'Caldecott', 'Mount Pleasant', 'Stevens', 'Napier', 'Orchard Boulevard', 'Orchard', 'Great World', 'Havelock',
    'Outram Park', 'Maxwell', 'Shenton Way', 'Marina Bay', 'Marina South', 'Gardens by the Bay')

'''
Requirement: Your task is find out all the transit stations among all the lines.
'''

list_all_station = green_line + green_sub_line + red_line + yellow_line + yellow_sub_line + purple_line + brown_line
l = ['green_line', 'green_sub_line', 'red_line', 'yellow_line', 'yellow_sub_line', 'purple_line', 'brown_line']
# 1) I want to give a number to each of the 7 lines
# The name and line are 1 to 1 mapping, so I use a dictionary to define it.
line_name_dict = {'green_line': green_line,
                  'green_sub_line': green_sub_line,
                  'red_line': red_line,
                  'yellow_line': yellow_line,
                  'yellow_sub_line': yellow_sub_line,
                  'purple_line': purple_line,
                  'brown_line': brown_line}

transit_station_lines_dict = defaultdict(set)


def populate_transit_station_to_lines_dict():
    line_combination_set = set(combinations(line_name_dict, 2))

    for line1_n, line2_n in line_combination_set:
        line1_stations_set = set(line_name_dict[line1_n])
        line2_stations_set = set(line_name_dict[line2_n])
        transit_stations = line1_stations_set & line2_stations_set

        if len(transit_stations) > 0:  #
            for transit_station in transit_stations:
                transit_station_lines_dict[line1_n].add(transit_station)
                transit_station_lines_dict[line2_n].add(transit_station)


populate_transit_station_to_lines_dict()
pprint(transit_station_lines_dict)

lineslist = []
st = input('start')
st_line = input('startline')
end = input('end:')
endline = input('endline:')


if st_line == endline:
    print(f'{st}  and {end} both are on {st_line}')
listcomb = []
listcomb += list(permutations(l, 3))
listcomb += list(permutations(l, 2))
print(listcomb)
for i in listcomb:
    print(i)
    if i[0] != st_line:

        listcomb.remove(i)
        continue

    elif i[-1] != endline:
        listcomb.remove(i)
        continue
print(listcomb)
def cangoif(listcomb):
    de=listcomb
    for i in listcomb:
        print(i)
        for a in range(len(transit_station_lines_dict[st_line])):
            for b in range(len(transit_station_lines_dict[endline])):
                if tuple(transit_station_lines_dict[st_line])[a]==tuple(transit_station_lines_dict[endline])[b]:
                    c=True
                else:
                    c=False
                if tuple(transit_station_lines_dict[st_line])[a]==tuple(transit_station_lines_dict[st_line])[-1] and c==False:
                    de[de.index(i)]='*%&'
    for i in range(de.count('*%&')):
        de.remove('*%&')

    listcomb=de[:]
    pprint(listcomb)


cangoif(listcomb)
