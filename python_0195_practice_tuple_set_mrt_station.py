'''
Introduction:
We are going to design a Singapore MRT transit app.
Right now, Singapore MRT system has green_line / red_line / yellow_line / purple_line / brown_line, 5 lines.
Green_line and yellow_line also have sub lines, meaning in total, we have 7 lines.

I've defined the 7 tuples as below:
'''

# PREPARE DATA BEGIN =================================

green_line= ('Pasir Ris', 'Tampines', 'Simei', 'Tanah Merah', 'Bedok', 'Kembangan', 'Eunos', 'Paya Lebar', 'Aljunied', 'Kallang', 'Lavender', 'Bugis', 'City Hall', 'Raffles Place', 'Tanjong Pagar', 'Outram Park', 'Tiong Bahru', 'Redhill', 'Queenstown', 'Commonwealth', 'Buona Vista', 'Dover', 'Clementi', 'Jurong East', 'Chinese Garden', 'Lakeside', 'Boon Lay', 'Pioneer', 'Joo Koon', 'Gul Circle', 'Tuas Crescent', 'Tuas West Road', 'Tuas Link')
green_sub_line= ('Tanah Merah', 'Expo', 'Changi Airport')

red_line= ('Jurong East','Bukit Batok','Bukit Gombak','Choa Chu Kang','Yew Tee','Kranji','Marsiling','Woodlands','Admiralty','Sembawang','Canberra','Yishun','Khatib','Yio Chu Kang','Ang Mo Kio','Bishan','Braddell','Toa Payoh','Novena','Newton','Orchard','Somerset','Dhoby Ghaut','City Hall','Raffles Place','Marina Bay','Marina South Pier')

yellow_line= ('Dhoby Ghaut', 'Bras Basah', 'Esplanade', 'Promenade', 'Nicoll Highway', 'Stadium', 'Mountbatten', 'Dakota', 'Paya Lebar', 'MacPherson', 'Tai Seng', 'Bartley', 'Serangoon', 'Lorong Chuan', 'Bishan', 'Marymount', 'Caldecott', 'Botanic Gardens', 'Farrer Road', 'Holland Village', 'Buona Vista', 'one-north', 'Kent Ridge', 'Haw Par Villa', 'Pasir Panjang', 'Labrador Park', 'Telok Blangah', 'HarbourFront')
yellow_sub_line= ('Marina Bay', 'Bayfront', 'Promenade')

purple_line= ('HarbourFront', 'Outram Park', 'Chinatown', 'Clarke Quay', 'Dhoby Ghaut', 'Little India', 'Farrer Park', 'Boon Keng', 'Potong Pasir', 'Woodleigh', 'Serangoon', 'Kovan', 'Hougang', 'Buangkok', 'Sengkang', 'Punggol')

brown_line = ('Woodlands North', 'Woodlands', 'Woodlands South', 'Springleaf', 'Lentor', 'Mayflower', 'Bright Hill', 'Upper Thomson', 'Caldecott', 'Mount Pleasant', 'Stevens', 'Napier', 'Orchard Boulevard', 'Orchard', 'Great World', 'Havelock', 'Outram Park', 'Maxwell', 'Shenton Way', 'Marina Bay', 'Marina South', 'Gardens by the Bay')

'''
Requirement: Your task is find out all the transit stations among all the lines.
'''
def transit():
    list_all_station=green_line+green_sub_line+red_line+yellow_line+yellow_sub_line+purple_line+brown_line
    dif=[]


    for i in list_all_station:
        if list_all_station.count(i)>1:
            dif.append(i)


    dif=set(dif)
    dif=list(dif)
    print(dif)

    for i in dif:
        if i in green_line:
            print(i,'is in green_line')
        if i in green_sub_line:
            print(i,'is in green_sub_line')
        if i in red_line:
            print(i,'is in red_line')
        if i in yellow_line:
            print(i,'is in yellow_line')
        if i in yellow_sub_line:
            print(i,'is in yellow_sub_line')
        if i in purple_line:
            print(i,'is in purple_line')
        if i in brown_line:
            print(i,'is in brown_line')
transit()


