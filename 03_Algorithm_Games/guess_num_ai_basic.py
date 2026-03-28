import random

low_number = 0
high_number = 10000000

right_number = random.randint(low_number, high_number)

middle_number = int((low_number + high_number) / 2)
new_low_number = low_number
new_high_number = high_number

guess_count = 1
while middle_number != right_number:
    print(f"第{guess_count}次猜测，猜测的数字是{middle_number}")
    if middle_number > right_number:
        print("你猜的太大了！")
        new_high_number = middle_number
    elif middle_number < right_number:
        print("你猜的太小了！")
        new_low_number = middle_number
    middle_number = int((new_low_number + new_high_number) / 2)
    guess_count += 1

print(f"第{guess_count}次猜测，猜测的数字是{middle_number}")
print("恭喜你，猜对了！")
