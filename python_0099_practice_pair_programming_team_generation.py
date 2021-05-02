#NOOOOOOOOOO!
import random
girls = ['吕昕桐','胡倚菡','刘仲妮','又心','郑雅文','玟希','金柏芳','周杰麟']
boys = ['郑敬衡','蔡博斯','刘子睿','任浩','家豪','陈宇洋','吴彦均','周锐麒','林家锐','周煜庭']
for girl in girls:
    boy_index=random.randint(0,len(boys)-1)
    print(girl,boys[boy_index])
    boys.pop(boy_index)
print(boys[0],boys[1])