"""
1.1 实现一个函数，完成如下功能：
函数入参要求：
两个参数low_number，height_number，low_number默认为0，height_number默认为10000
函数功能要求：
  a. 先生成一个 [low_number, height_number] 区间的随机整数 answer
  b. 通过二分法让计算机快速定位(猜)自己生成的数字
  c. 需要记录猜的次数guess_count
函数返回要求：
函数返回两个值 answer和guess_count
1.2 调用函数
调用上述函数，用解包的方法接受函数的两个返回值，并打印：
猜的数字是：XXXX, 共猜了 XXXX 次
"""

import random
def guess_number(low_number=0, height_number=10000):
    answer = random.randint(low_number, height_number)
    guess_count = 0
    low = low_number
    high = height_number
    while low <= high:
        guess_count += 1
        mid = (low + high) // 2
        if mid < answer:
            low = mid + 1
        elif mid > answer:
            high = mid - 1
        else:
            break
    return answer, guess_count

answer, guess_count = guess_number()
print(f"猜的数字是：{answer}, 共猜了 {guess_count} 次")