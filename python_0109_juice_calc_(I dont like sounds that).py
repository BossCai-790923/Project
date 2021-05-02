import math

'''
Requirement:

A juice factory produces apple juice and orange juice in 2 containers - cube size and ball size
cube container has a edge length 10cm
ball container has a radius 6 cm s=4Pr^2 v=4/3 π r^3

The factory use 2 materials - plastic / metal
So in total, the factory produces 8 kinds of beverage:
1) apple juice - cube container - plastic material#
2) apple juice - cube container - metal material#
3) apple juice - ball container - plastic material#
4) apple juice - ball container - metal material#
5) orange juice - cube container - plastic material
6) orange juice - cube container - metal material
7) orange juice - ball container - plastic material
8) orange juice - ball container - metal material

orange juice cost: 0.14 cent / cm^3
apple juice cost: 0.11 cent / cm^3
plastic material cost: 0.08 cent / cm^2
metal material cost: 0.18 cent / cm^2



These 8 kinds of juice are sold in NTUC supermarket and Cold Storage supermarket.
NTUC charges 10% of your juice price, meaning if your juice is sold at $2, you need to pay NTUC 20 cent.
Cold Storage changes 15% of your juice price, meaning if your juice is sold at $2, you need to pay Code Storage 30 cent.

There are in total 16 situations.

Remember: the factory also needs to make profit 30%

The factory manager asks you to help them to calculate the price for the above 16 situations, how much they should sell 
for each case.
'''
Pi = math.pi
'''
So the --area-- of the ball is 
'''
S_ball = 4 * Pi * (6 ** 2)
V_ball = 4 / 3 * Pi * (6**3)
S_cube = 10 * 10 * 6
V_cube = 10 ** 3

# cp=(0.14*V_cube+S_cube*0.08)*1.1
# cm=(0.11*V_cube+S_cube*0.18)*1.1
# bp=(0.14*V_ball+S_ball*0.08)*1.1
# bm=(0.11*V_ball+S_ball*0.18)*1.1
# cp01=(0.14*V_cube+S_cube*0.08)*1.15
# cm01=(0.11*V_cube+S_cube*0.18)*1.15
# bp01=(0.14*V_ball+S_ball*0.08)*1.15
# bm01=(0.11*V_ball+S_ball*0.18)*1.15
# print(cp)
# print(cm)
# print(bp)
# print(bm)
print(S_ball,'s')
print(V_ball,'v')
print(S_cube,'s')
print(V_cube,'v')
def calc():
    '''
    this calculate money!!!

    orange juice cost: 0.14 cent / cm^3
    apple juice cost: 0.11 cent / cm^3
    plastic material cost: 0.08 cent / cm^2
    metal material cost: 0.18 cent / cm^2
    '''

    orange_cube_plastic_NTUC = (0.14 * V_cube + S_cube * 0.08) * 1.1 *1.3
    orange_cube_metal_NTUC = (0.14 * V_cube + S_cube * 0.18) * 1.1   *1.3
    orange_ball_plastic_NTUC = (0.14 * V_ball + S_ball * 0.08) * 1.1 *1.3
    orange_ball_medal_NTUC = (0.14 * V_ball + S_ball * 0.18) * 1.1   *1.3
                                                                     
    apple_cube_plastic_NTUC= (0.11 * V_cube + S_cube * 0.08) * 1.1   *1.3
    apple_cube_metal_NTUC= (0.11 * V_cube + S_cube * 0.18) * 1.1     *1.3
    apple_ball_plastic_NTUC= (0.11 * V_ball + S_ball * 0.08) * 1.1   *1.3
    apple_ball_medal_NTUC= (0.11 * V_ball + S_ball * 0.18) * 1.1     *1.3

    orange_cube_plastic_cold = (0.14 * V_cube + S_cube * 0.08) * 1.15*1.3
    orange_cube_metal_cold = (0.14 * V_cube + S_cube * 0.18) * 1.15  *1.3
    orange_ball_plastic_cold = (0.14 * V_ball + S_ball * 0.08) * 1.15*1.3
    orange_ball_medal_cold = (0.14 * V_ball + S_ball * 0.18) * 1.15  *1.3

    apple_cube_plastic_cold= (0.11 * V_cube + S_cube * 0.08) * 1.15  *1.3
    apple_cube_metal_cold= (0.11 * V_cube + S_cube * 0.18) * 1.15    *1.3
    apple_ball_plastic_cold= (0.11 * V_ball + S_ball * 0.08) * 1.15  *1.3
    apple_ball_medal_cold= (0.11 * V_ball + S_ball * 0.18) * 1.15    *1.3

    print(orange_cube_plastic_NTUC/100,'|Dollar','  orange_cube_plastic_NTUC')
    print(orange_cube_metal_NTUC/100,'  |Dollar','  orange_cube_metal_NTUC    ')
    print(orange_ball_plastic_NTUC/100,'|Dollar','  orange_ball_plastic_NTUC')
    print(orange_ball_medal_NTUC/100,'  |Dollar','  orange_ball_medal_NTUC    ')

    print(apple_cube_plastic_NTUC/100,' |Dollar','  apple_cube_plastic_NTUC  ')
    print(apple_cube_metal_NTUC/100,'   |Dollar','  apple_cube_metal_NTUC      ')
    print(apple_ball_plastic_NTUC/100,' |Dollar','  apple_ball_plastic_NTUC  ')
    print(apple_ball_medal_NTUC/100,'   |Dollar','  apple_ball_medal_NTUC     ')

    print(orange_cube_plastic_cold/100,'|Dollar','  orange_cube_plastic_cold')
    print(orange_cube_metal_cold/100,'  |Dollar','  orange_cube_metal_cold    ')
    print(orange_ball_plastic_cold/100,'|Dollar','  orange_ball_plastic_cold')
    print(orange_ball_medal_cold/100,'  |Dollar','  orange_ball_medal_cold  ')

    print(apple_cube_plastic_cold/100,' |Dollar','  apple_cube_plastic_cold ')
    print(apple_cube_metal_cold/100,'   |Dollar','  apple_cube_metal_cold     ')
    print(apple_ball_plastic_cold/100,' |Dollar','  apple_ball_plastic_cold  ')
    print(apple_ball_medal_cold/100,'   |Dollar','  apple_ball_medal_cold      ')
calc()