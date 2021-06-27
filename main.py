# ----------2021/06/27----------
# -------------v3.0-------------
# -----power by Oscar Zhu-------
from random import *
jia=input("请问是否要出加法题(输入y或者n)：")
jian=input("请问是否要出减法题(输入y或者n)：")
cheng=input("请问是否要出乘法题(输入y或者n)：")
chu=input("请问是否要出除法题(输入y或者n)：")
max=input("请输入题目数字最大值:")
max=int(max)
min=input("请输入题目数字最小值:")
min=int(min)
shuliang=input("请输入题目数量：")
shuliang=int(shuliang)
bool=input("1.出题模式2.答题模式:")
bool=int(bool)
for i in range(shuliang):
    if bool==2:
        jjcc=randint(1,4)
        text1=randint(min,max)
        text2=randint(min,max)
        if jjcc==1 and jia=="y":
            print(text1,"+",text2)
            num=input("请写下你的答案：")
            num=int(num)
            if num == text1+text2:
                print("恭喜你答对了！")
            else:
                print("很遗憾答错了！")
        elif jjcc==2 and jian=="y":
            if text1>=text2:
                print(text1,"-",text2)
                num=input("请写下你的答案：")
                num=int(num)
                if num == text1-text2:
                    print("恭喜你答对了！")
                else:
                    print("很遗憾答错了！")
            else:
                print(text2,"-",text1)
                num=input("请写下你的答案：")
                num=int(num)
                if num == text2-text1:
                    print("恭喜你答对了！")
                else:
                    print("很遗憾答错了！")
        elif jjcc==3 and cheng=="y":
            print(text1,"x",text2)
            num=input("请写下你的答案：")
            num=int(num)
            if num == text1*text2:
                print("恭喜你答对了！")
            else:
                print("很遗憾答错了！")
        elif jjcc==4 and chu=="y":
            print(text1,"÷",text2)
            num=input("请写下你的答案：")
            num=int(num)
            if num == text1/text2:
                print("恭喜你答对了！")
            else:
                print("很遗憾答错了！")
        else:
            while True:
                jjcc=randint(1,4)
                text1=randint(min,max)
                text2=randint(min,max)
                if jjcc==1 and jia=="y":
                    print(text1,"+",text2)
                    num=input("请写下你的答案：")
                    num=int(num)
                    if num == text1+text2:
                        print("恭喜你答对了！")
                    else:
                        print("很遗憾答错了！")
                    break
                elif jjcc==2 and jian=="y":
                    if text1>=text2:
                        print(text1,"-",text2)
                        num=input("请写下你的答案：")
                        num=int(num)
                        if num == text1-text2:
                            print("恭喜你答对了！")
                        else:
                            print("很遗憾答错了！")
                    else:
                        print(text2,"-",text1)
                        num=input("请写下你的答案：")
                        num=int(num)
                        if num == text2-text1:
                            print("恭喜你答对了！")
                        else:
                            print("很遗憾答错了！")
                        break
                elif jjcc==3 and cheng=="y":
                    print(text1,"x",text2)
                    num=input("请写下你的答案：")
                    num=int(num)
                    if num == text1*text2:
                        print("恭喜你答对了！")
                    else:
                        print("很遗憾答错了！")
                    break
                elif jjcc==4 and chu=="y":
                    print(text1,"÷",text2)
                    num=input("请写下你的答案：")
                    num=int(num)
                    if num == text1/text2:
                        print("恭喜你答对了！")
                    else:
                        print("很遗憾答错了！")
                    break
                else:
                    jjcc=0
    elif bool==1:
        jjcc=randint(1,4)
        text1=randint(min,max)
        text2=randint(min,max)
        if jjcc==1 and jia=="y":
            print(text1,"+",text2)
        elif jjcc==2 and jian=="y":
            if text1>=text2:
                print(text1,"-",text2)
            else:
                print(text2,"-",text1)
        elif jjcc==3 and cheng=="y":
            print(text1,"x",text2)
        elif jjcc==4 and chu=="y":
            print(text1,"÷",text2)
        else:
            while True:
                jjcc=randint(1,4)
                text1=randint(min,max)
                text2=randint(min,max)
                if jjcc==1 and jia=="y":
                    print(text1,"+",text2)
                    break
                elif jjcc==2 and jian=="y":
                    if text1>=text2:
                        print(text1,"-",text2)
                    else:
                        print(text2,"-",text1)
                        break
                elif jjcc==3 and cheng=="y":
                    print(text1,"x",text2)
                    break
                elif jjcc==4 and chu=="y":
                    print(text1,"÷",text2)
                    break
                else:
                    jjcc=0
