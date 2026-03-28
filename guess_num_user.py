from random import randint

# 机器生成一个1-100的随机数
right_number = randint(1, 100)
user_number = None
count = 0  # 用户最多可以猜10次

while user_number != right_number and count < 10:
    print(f"欢迎来到猜数字游戏！这已经是你第{count + 1}次猜了！")
    # 用户输入一个1-100的数字，带校验
    try:
        user_number = int(input("请输入你猜的数字（1-100）："))
    except ValueError:
        print("请输入有效的整数。")
        continue

    count += 1

    if user_number == right_number:
        break
    elif user_number > right_number:
        print("你猜的数字太大了！")
    else:
        print("你猜的数字太小了！")

# 比较用户输入的数字与机器生成的随机数并输出最终结果
if user_number == right_number:
    print("恭喜你，猜对了！")
else:
    print(f"很遗憾，你没有在10次之内猜到正确数字。正确答案是{right_number}。")