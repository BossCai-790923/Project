def tower_of_hanoi(n, from_rod, to_rod, help_rod):

    # base case:
    if n == 1:
        print(f'Move disk {n} from {from_rod} to {to_rod}')


    # recursive call
    else:
        # step 1) Move n-1 disks from 'from_rod' to 'help_rod' via 'to_rod'
        tower_of_hanoi(n-1, from_rod, help_rod, to_rod)

        # step 2) Move disk n from 'from_rod' to 'to_rod'
        print(f'Move disk {n} from {from_rod} to {to_rod}')

        # step 3) Move n-1 disks from 'help_rod' to 'to_rod' via 'from_rod'
        tower_of_hanoi(n - 1, help_rod, to_rod, from_rod)



tower_of_hanoi(6, 'A', 'C', 'B')