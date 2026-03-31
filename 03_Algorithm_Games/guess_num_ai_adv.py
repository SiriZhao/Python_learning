"""
在以下区间：[1, 10000000]（1000万）实现机器猜数字，规则：
1. 代码生成区间内一个随机的整数
2. 用代码猜这个随机的整数是几，并且输出已猜的次数
3. 思考：第二步中如何更快让代码猜到这个数字，而不是每次都瞎猜
"""

import random
import math

# 机器生成一个1-10000000的随机数
right_number = random.randint(1, 10000000)
print(f"【系统】已生成随机数（答案隐藏），开始猜测...\n")

low = 1
high = 10000000
count = 0
guessed_number = None

# 理论最少猜测次数
max_guesses = math.ceil(math.log2(high - low + 1))
print(f"【提示】二分查找理论最多需要 {max_guesses} 次即可猜中\n")

while guessed_number != right_number:
    # 二分查找：每次猜中间值
    guessed_number = (low + high) // 2
    count += 1

    print(f"第 {count:>2} 次猜测：{guessed_number:>10}", end="  →  ")

    if guessed_number == right_number:
        print("✅ 猜对了！")
        break
    elif guessed_number > right_number:
        print(f"太大了！调整范围：[{low}, {guessed_number - 1}]")
        high = guessed_number - 1
    else:
        print(f"太小了！调整范围：[{guessed_number + 1}, {high}]")
        low = guessed_number + 1

print(f"\n🎉 恭喜！正确答案是 {right_number}，共猜了 {count} 次！")