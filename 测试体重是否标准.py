'''
8.身体质量指数(BMI),是目前国际上常用的衡量人体胖瘦程度以及是否健康的一个标准。
它的计算公式:BMI=体重 - 身高* 身高 。
其中,体重的单位是kg,身高的单位是 m。中国人的 BMI参考标准:BMI<18.5 为偏瘦;
18.5≤BMI<24为正常;
24<BMI<28 为偏胖;
BMI>28 为肥胖。
编写一个程序,输入一个人的体重和身高,计算 BMI并指出体重是否正常。

'''
BMI = 0

G = input("你的体重(kg):")
L = input("你的升高(cm):")
BMI = float(G)  /((float(L)/100) **2)
print(BMI)

if BMI >= 28:
    print("肥胖")
elif BMI >=24 and BMI <18:
    print("正常")
else:
    print("偏瘦")
