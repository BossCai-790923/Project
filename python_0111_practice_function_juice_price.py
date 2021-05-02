import math
container01=['cube',10]
container02=['sphere',6]
containers=[container01,container02]
#
juice01=['orange',0.14]
juice02=['apple',0.11]
juice=[juice01,juice02]
#
material01=['plastic',0.08]
material02=['medal',0.18]
material=[material01,material02]
#
ntuc=['NTUC',0.1]
coldstorage=['Cold Storage',0.15]
supermarkets=[ntuc,coldstorage]
################################################################
# list can help you to group all relater information together. #
################################################################

'''
-------------------------------------
step 2) CLogic:
-------------------------------------
conclusion 1) 
Total situation = 2 juice * 2 container * material * 2 supermarket
                = 16 situations

I use nested loop to cover all 16 situations
for container in containers: 
    for current_juice in juice:
        for current_material in material:
            for supermarket in supermarkets:
                # here, we have 4 variables: container / current_juice / current_material / supermarket
                # my core logic is here

conclusion 2)                                 
Inside the loop body, what shall we do? 
Step 1) calculate the container's surface and volume.
        So we define a function:
        def surface_and_volume(container):
            pass
Step 2) use container's surface and volume / juice / material to calculate the cost of the juice to the factory
       so we define a function:
       def calculate_cost(container_data, juice, material):
           pass            

Step 3) because the factory needs to make 30% profit, so based on the cost to the factory, we can calculate the price so the supermarket.
      so we define a function:
      def sold_price_to_supermarket(cost):
         pass

Step 4) because ntuc and coldstorage need to make profit, so same import price from factory has a different selling price to customer。
     So we define a function:
     def sold_price_to_customer(cost, supermarket):
        pass                    
'''

def surface_and_volume(container):
    '''
    this function calculates the surface and volume\n
    of the container\n
    :param: container: list container (ball(sphere) or square)
    :return: cm^3 of the container
    '''
    result=[]
    if container[0]=='cube':
        result.append((container[1]**2*6))
        result.append(container[1]**3)
    elif container[0]=='sphere':
        result.append(4*math.pi*container[1]**2)
        result.append(4/3 * math.pi * container[1]**3)
    else:
        print(f'Unknown object type{container[0]}')
    return result

def calculate_cost(container_data,juice,material):
    '''
    calculate the cost for the juice
    :param: container_data: is a list \n
           container_data[0] is the surface area of the container 
           container_data[1] is the volume of the container. 
    :param: juice: is a list \n
           juice[0] is the juice type, it can be either 'apple' or 'orange'
           juice[1] is the juice price, how much does it cost per cm^3
    :param: material: is a list \n
           material[0] is the material type, it can be either 'plastic' or 'metal'
           material[1] is the material price, how much does it cost per cm^2
    :return:  the total cost of the juice. Including juice cost + container cost
    '''
    container_cost=container_data[0]*material[1]
    juice_cost=container_data[1]*juice[1]
    total_cost=container_cost+juice_cost
    return total_cost

def sold_price_to_supermarket(cost):
    '''
    this calculate profit+30%
    :param cost: container+juice
    :return: 130% cost
    '''
    return cost*1.3
def sold_price_to_cusotmer(cost,supermarket):
    '''
    the shop make profit
    :param: cost:130%(container+juice)
    :param: supermarket:ntuc/cold
    :return:profit*cost+cost
    '''
    return cost*(1+supermarket[1])

for container in containers:
    for current_juice in juice:
        for current_material in material:
            for supermarket in supermarkets:
                print(f"For juice type: container: {container}, juice: {current_juice}, material: {current_material}, supermarket: {supermarket}")
                container_info = surface_and_volume(container)
                print(f"Surface area: {container_info[0]:.2f} cm^2")
                print(f"Volume: {container_info[1]:.2f} cm^3")
                original_cost = calculate_cost(container_info, current_juice,current_material)
                print(f"Cost for the factory to produce the juice: ${original_cost/100:.2f}")
                selling_price_to_supermarket = sold_price_to_supermarket(original_cost)
                print(f"Selling price to the supermarket: ${selling_price_to_supermarket/100:.2f}")
                selling_price_to_customer = sold_price_to_cusotmer(selling_price_to_supermarket, supermarket)
                print(f"Selling price to the cusomter: ${selling_price_to_customer*0.01}")
                print('-' * 100)