from PIL import Image

import turtle as t


def leave(path):


    img = Image.open(path)  # 读取图像

    global size

    size = img.size

    pix = img.load()

    list = [[] for i in range(size[1])]  # 构造空列表

    for i in range(0, size[1]):  # 从第一行开始循环

        k = 0

        for j in range(0, size[0] - 1):

        # 如果当前像素与下一个像素值不同且两者有一为背景色，则记录坐标

            if pix[j, i] != pix[j + 1, i] and (255, 255, 255) in [pix[j, i], pix[j + 1, i]]:

                if k == 0:  # index值为0说明是像素条起始坐标

                    list[i].append([j + 1, ])

                    k += 1

                else:  # index值为1说明记录的是像素条结束坐标

                    list[i][-1].append(j)

                    k = 0

    return list



def draw(path):

    l=leave(path)

    # 绘图窗口大小

    t.screensize(canvwidth=size[0], canvheight=size[1],bg='white')

    t.speed(1000)

    for i in range(0, size[1]):



        t.pencolor('orange')

        for line in l[i]:




            t.penup()
            t.goto(line[0] - size[0] // 2, (size[1] - i) - size[1] // 2)
            t.pendown()
            t.goto(line[1] - size[0] // 2, (size[1] - i) - size[1] // 2)
            t.speed(0)
            

            
draw('枫叶.jpg')
t.mainloop()