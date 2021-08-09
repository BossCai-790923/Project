import pprint
candidate_number_in_list=[]
print_dict={
    '0':0,
    '1':0,
    '2':0,
    '3':0,
    '4':0,
    '5':0,
    '6':0,
    '7':0,
    '8':0,
    '9':0

}
#generate all needed number in string
for i in range(1,2001):

    if len(str(i))==1:
        candidate_number_in_list+=list('000'+str(i))
    if len(str(i))==2:
        candidate_number_in_list+=list('00'+str(i))
    if len(str(i))==3:
        candidate_number_in_list+=list('0'+str(i))
    if len(str(i))==4:
        candidate_number_in_list+=list(str(i))
print(candidate_number_in_list)

# for x in range(10):
#     print('there should be ',candidate_number_in_list.count(str(x)),'of',x)
for i in candidate_number_in_list:

    print_dict[str(i)]+=1
pprint.pprint(print_dict)