#实现倒序99乘法表的输出
for i in range(9,0,-1):
    for j in range(i,0,-1):
        print(f"{j}*{i}={i*j}",end="\t")
    print("\n")
