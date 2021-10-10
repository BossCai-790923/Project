import random



class Game2048:

    def __init__(self):
        self.grid = []
        for i in range(4):
            self.grid.append(['_'] * 4)

        self.generate_number()
        self.generate_number()
        self.print_me()



    @staticmethod
    def merge_number(*row):

        # Step 1) create 2 lists
        numbers = [n for n in row if n != '_']
        spaces =  [n for n in row if n == '_']

        # Step 2) merge numbers
        # if len(numbers) == 1; you can't merge a single number, so you do nothing

        if len(numbers) == 2:
            if numbers[0] == numbers[1]:
                numbers[0] *= 2
                numbers.pop(1)
                spaces.append('_')

        elif len(numbers) == 3:
            if numbers[0] == numbers[1]:
                numbers[0] *= 2
                numbers.pop(1)
                spaces.append('_')
            elif numbers[1] == numbers[2]:
                numbers[1] *= 2
                numbers.pop(2)
                spaces.append('_')

        elif len(numbers) == 4:

            hasMerged = False

            if numbers[0] == numbers[1]:
                numbers[0] *= 2
                numbers.pop(1)
                spaces.append('_')
                hasMerged = True

            if hasMerged == False and numbers[1] == numbers[2]:
                numbers[1] *= 2
                numbers.pop(2)
                spaces.append('_')
                hasMerged = True

            if hasMerged == False and numbers[-1] == numbers[-2]:
                numbers[-2] *= 2
                numbers.pop(-1)
                spaces.append('_')

        return tuple(numbers + spaces)



    def up(self):


        # handle the 1st column: self.grid[0][0], self.grid[1][0], self.grid[2][0], self.grid[3][0]
        # handle the 2nd column: self.grid[0][1], self.grid[1][1], self.grid[2][1], self.grid[3][1]
        # handle the 3rd column: self.grid[0][2], self.grid[1][2], self.grid[2][2], self.grid[3][2]
        # handle the 4th column: self.grid[0][3], self.grid[1][3], self.grid[2][3], self.grid[3][3]

        for y in range(4):

            # handle self.grid[0][y], self.grid[1][y], self.grid[2][y], self.grid[3][y]
            if self.grid[0][y] == '_' and self.grid[1][y] == '_' and self.grid[2][y] == '_' and self.grid[3][y] == '_':
                continue

            self.grid[0][y], self.grid[1][y], self.grid[2][y], self.grid[3][y] = Game2048.merge_number(self.grid[0][y], self.grid[1][y], self.grid[2][y], self.grid[3][y])

        self.generate_number()
        self.print_me()
        self.check_win_or_lose()



    def down(self):

        for y in range(4):

            # handle self.grid[0][y], self.grid[1][y], self.grid[2][y], self.grid[3][y]
            if self.grid[0][y] == '_' and self.grid[1][y] == '_' and self.grid[2][y] == '_' and self.grid[3][y] == '_':
                continue

            self.grid[3][y], self.grid[2][y], self.grid[1][y], self.grid[0][y] = Game2048.merge_number(self.grid[3][y], self.grid[2][y], self.grid[1][y], self.grid[0][y])

        self.generate_number()
        self.print_me()
        self.check_win_or_lose()



    def left(self):

        for x in range(4):

            # handle self.grid[0][y], self.grid[1][y], self.grid[2][y], self.grid[3][y]
            if self.grid[x][0] == '_' and self.grid[x][1] == '_' and self.grid[x][2] == '_' and self.grid[x][3] == '_':
                continue

            self.grid[x][0], self.grid[x][1], self.grid[x][2], self.grid[x][3] = Game2048.merge_number(self.grid[x][0], self.grid[x][1], self.grid[x][2], self.grid[x][3])

        self.generate_number()
        self.print_me()
        self.check_win_or_lose()



    def right(self):

        for x in range(4):

            # handle self.grid[0][y], self.grid[1][y], self.grid[2][y], self.grid[3][y]
            if self.grid[x][0] == '_' and self.grid[x][1] == '_' and self.grid[x][2] == '_' and self.grid[x][3] == '_':
                continue

            self.grid[x][3], self.grid[x][2], self.grid[x][1], self.grid[x][0] = Game2048.merge_number(self.grid[x][3], self.grid[x][2], self.grid[x][1], self.grid[x][0])

        self.generate_number()
        self.print_me()
        self.check_win_or_lose()



    def print_me(self):
        print('---------------------')
        for line in self.grid:
            print(*line)



    def generate_number(self):
        '''
        Game starts with 2 random numbers ( being 2 or 4) at random position.
        After each user's move, a new random number (being 2 or 4) will appear in a random position.
        '''
        new_number = random.randint(1, 2) * 2 # random.randint(1, 2) generates either 1 or 2
        x, y = self.generate_random_available_position()
        self.grid[x][y] = new_number


    def generate_random_available_position(self):
        x = random.randint(0, 3)
        y = random.randint(0, 3)

        while self.grid[x][y] != '_':
            x = random.randint(0, 3)
            y = random.randint(0, 3)

        return x, y



    def check_win_or_lose(self):
        dis=0
        for i in range(4):
            for y in range(4):

                if self.grid[i][y]==2048:
                    print('you win!')
                    exit()
                if self.grid[i][y]!='_':
                    dis+=1
                if dis==16:
                    print('you loose')
                    exit()







# MAIN PROGRAM BEGIN ==============================


if __name__ == '__main__':

    game = Game2048()

    while True:

        action = input("Action: ")

        if 'up' == action or 'w' == action:
            game.up()

        elif 'down' == action or 's' == action:
            game.down()

        elif 'left' == action or 'a' == action:
            game.left()

        elif 'right' == action or 'd' == action:
            game.right()

        else:
            print("Unrecognized operation!")