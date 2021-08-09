# Requirment:
# Implement a simple database using dictionary.
# The dictionary uses person names as keys.
# Each person is represented as another dictionary with keys 'phone' and 'addr' referring to their phone number and address repectively.

people = {

    'Alice': {
        'phone': '2341',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9012',
        'addr': 'Bar street 42'
    },

    'Cecil': {
        'phone': '2158',
        'addr': 'Baz avenue 90'
    }

}

labels = {
    'phone': 'phone number',
    'addr': 'address'
}
key=''
name = str(input("Name: "))
request = str(input("'Phone number (p) or address (a) ? "))
if request == 'p':
    key ='phone'

if request == 'a':
    key = 'addr'

if name in people:
    # print(f"{name}'s {labels[key]} is {people.get(name).get(key)}")
    print(f"{name}'s {labels[key]} is {people[name][key]}")
else:
    print("No such persons:", name)

