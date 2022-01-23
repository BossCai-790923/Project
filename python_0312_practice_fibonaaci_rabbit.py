month = int(input("What's the current month? "))
rabbit_1m_old = 2
rabbit_2m_old = 0
rabbit_3m_old = 0
rabbit_adult = 0

# here it describe the reproduce times:
for i in range(1, month):

    # step 1) 3 month old become adult
    rabbit_adult += rabbit_3m_old

    # step 2) adult rabbit reproduce
    temp = rabbit_adult

    # step 3)
    rabbit_3m_old = rabbit_2m_old

    rabbit_2m_old = rabbit_1m_old

    rabbit_1m_old = temp

    print(f'month {i} : {rabbit_1m_old + rabbit_2m_old + rabbit_3m_old + rabbit_adult}-------------------------------')
    print(f'1 month old: {rabbit_1m_old}')
    print(f'2 month old: {rabbit_2m_old}')
    print(f'3 month old: {rabbit_3m_old}')
    print(f'adult: {rabbit_adult}')