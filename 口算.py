# ----------2021/06/18----------
# -------------v1.0-------------
# -----power by Oscar Zhu-------
from random import *
def random_text(a,b,c):
    print(a,b,c,"=")
    daan=input("请输入答案：")
    daan = int(daan)
    if b == "+":
        num = a+b
    if b == "-":
        num = a-b
    if b == "*":
        num = a*b
    if b == "/":
        num = a/b
    if daan==num:
        print("回答正确，恭喜你！")
    else:
        print("回答错误，继续加油哦！正确答案为：",num)
jia=input("请问是否要出加法题(输入y或者n)：")
jian=input("请问是否要出减法题(输入y或者n)：")
cheng=input("请问是否要出乘法题(输入y或者n)：")
chu=input("请问是否要出除法题(输入y或者n)：")
shuliang=input("请输入题目数量：")
shuliang=int(shuliang)
max=input("请输入数字最大值：")
max=int(max)
min=input("请输入数字最小值")
min=int(min)
for i in range(shuliang):
    n=randint(1,4)
    if n == 1:
        if jia=="y":
            random_text(randint(min,max),"+",randint(min,max))
    if n == 2:
        if cheng=="y":
            random_text(randint(min,max),"*",randint(min,max))
    if n == 3:
        if chu=="y":
            random_text(randint(min,max),"/",randint(min,max))
    if n == 4:
        if jian=="y":
            f=randint(max,min)
            m=randint(max,min)
            if f>=m:
                random_text(f,"-",m)
            if f<m:
                random_text(m,"-",f)
