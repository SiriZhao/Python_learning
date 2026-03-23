print("Hello, World!")

print(1500 * 1.15 == 1500 + 1500 * 0.15) #由于浮点数的精度问题，1500 * 1.15的结果可能不是精确的1725，而是一个接近1725的数，所以这个表达式的结果可能是False

from decimal import Decimal #使用Decimal类进行精确的十进制计算，避免浮点数的精度问题
print(Decimal("1500") * Decimal("1.15") == Decimal("1500") + Decimal("1500") * Decimal("0.15")) #使用Decimal类进行精确的十进制计算，避免浮点数的精度问题，所以这个表达式的结果是True

print(80 >= 60 and '12' == 12)

count = 0
i = 0
while count < 50: #当count小于50时，循环继续执行
    print("傻逼")
    count += 1
print(f"循环结束，我已经叫了{count}次傻逼了！")

word = "Hello" 
for letter in word: #遍历字符串中的每个字符，把每个字符依次赋值给变量letter，直到遍历完整个字符串
    print("遍历结束了！")
    print(letter) #输出字符串中的每个字符，结果是H、e、l、l、o，每个字符占一行

for number_item in range(1, 11, 2): #使用range函数生成一个从1到10（不包括10）的数字序列，步长为2，即生成1、3、5、7、9这五个数字，然后遍历这个数字序列，把每个数字依次赋值给变量number_item，直到遍历完整个数字序列
    print(number_item)

day = 0
while True:
    day += 1
    if day >= 7:
        break
    count = 0
    while True:
        print(f"第{day}天，叫了{count}次傻逼了！")
        count += 1
        if count >= 5:
            break
else:   
    print("循环结束了！")

def check_unsafe_word(comments):
    unsafe_words = ["傻逼", "垃圾", "滚犊子"]
    for word in unsafe_words:
        if word in comments:
            return "评论中包含敏感词，请重新输入！"
    return "评论发布成功！"

str_1 = "这个人真傻逼！"
str_2 = "这个人真棒！"

print(check_unsafe_word(str_1))
print(check_unsafe_word(str_2))

def function_a(a):
    a += 1
    return a #把a的值加1后返回
def function_b(b):
    b = b ** 2
    result = function_a(b) #把b的值平方后传递给function_a函数，function_a函数会把这个值加1后返回，然后把这个返回值赋值给result变量
    return result
print(function_b(3))

# 函数的多返回值
def calc_square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube
result_1 , result_2 = calc_square_and_cube(3) #调用函数calc_square_and_cube，传递参数3，函数会返回3的平方和3的立方，然后把这两个返回值分别赋值给result_1和result_2变量
print(f"平方是{result_1}，立方是{result_2}")

# 位置传参和关键词传参，函数可定义默认参数
def creat_game_character( account ,email , username = "傻逼" , password = "123456" , initial_payment = 1000):
    """创建游戏角色的函数，包含默认参数
    参数:
    account: 账号
    email: 邮箱
    username: 用户名，默认为"傻逼"
    password: 密码，默认为"123456"
    initial_payment: 初始支付金额，默认为1000
    """
    print(f"角色创建成功！账号：{account}，邮箱：{email}，用户名：{username}，密码：{password}，初始支付金额：{initial_payment}")
creat_game_character(account="ShaFu", email="shafu@example.com")

# 函数作为参数传递
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "除数不能为零！"
    return a / b
def add_and_subtract(a , b):
    c = add(a, b)
    d = subtract(c, a)
    return d
def calculate(a, b, function):
    """
    计算函数，接受两个数字和一个函数作为参数
    参数:
    a: 第一个数字
    b: 第二个数字
    function: 要执行的函数，可以是add、subtract、multiply或divide
    """
    result = function(a, b)
    return result
print(calculate(10, 5, add_and_subtract))

#函数作为参数传递
my_list = ["吃饭", "睡觉", "打豆豆"]
for item in my_list:
    print(item, end="，")

my_list = ["吃饭", "睡觉", "打豆豆", "玩游戏", "看电影"]
print(my_list[0])
print(my_list[-1])

my_list = ["吃饭", "睡觉", "打豆豆", "玩游戏", "吃饭" , "看电影"]
for i in range(0 , 5): 
    print(my_list[i]) 

print(len(my_list)) #列表的长度是6，索引范围是0-5，访问my_list[6]会报错
print(len(my_list[0])) #"吃饭"这个字符串的长度是2
print(my_list.index("打豆豆")) #返回"打豆豆"在列表中的索引位置，结果是2

my_list.append("运动") #在列表末尾添加一个元素"运动"
print(my_list) 

print(my_list.count("吃饭")) #统计列表中"吃饭"出现的次数，结果是2

my_list.insert(2, "学习") #在索引位置2插入一个元素"学习"
my_list.insert(-1, "刷视频") #在倒数第1个元素之前插入一个元素"刷视频"
my_list.append("睡觉") #在列表末尾添加一个元素"睡觉"
print(my_list) 

my_list_2 = ["吃早餐" , "午餐" , "晚餐"]
print(my_list + my_list_2) #列表拼接，结果是一个包含my_list和my_list_2所有元素的新列表

my_list.extend(my_list_2) #在my_list末尾添加my_list_2中的所有元素
print(my_list) 
#上述二者一致

my_list.remove("吃饭") #从列表中删除第一个出现的"吃饭"
print(my_list) 

my_list.append("吃饭")
print(my_list)
if "吃饭" in my_list:
    print("吃饭在列表中！")

while "吃饭" in my_list:
    my_list.remove("吃饭") #从列表中删除所有的"吃饭"
print(my_list)

my_list.pop(0)  #从列表中删除索引位置0的元素，并返回该元素
del my_list[0]  #从列表中删除索引位置0的元素，但不返回该元素
#上述两种写法等价

my_list.clear() #清空列表中的所有元素
print(my_list)

my_list = [1, 2, 3, 4, 5]
for index in range(len(my_list)):
    print(index)

# 元组
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0]) #访问元组中的第一个元素，结果是1
a , b , c , d , e = my_tuple #元组解包，把my_tuple中的元素依次赋值给变量a、b、c、d、e
print(a, b, c, d, e)

# 字符串
my_name = "My name is ShaFu. Hi, ShaFu!" 
new_name = my_name.replace("ShaFu", "傻逼") #把字符串中的"ShaFu"替换成"傻逼"
print(new_name)
print(my_name) #原字符串my_name没有被修改，仍然是"My name is ShaFu. Hi,ShaFu!"，说明字符串是不可变类型

my_list = [1, 2, 3, 4, 5]
print(my_list.remove(3)) #remove方法没有返回值，直接修改了my_list列表，删除了第一个出现的元素3，所以结果是None，my_list变成了[1, 2, 4, 5]

my_name = "My name is ShaFu. Hi, ShaFu!"
my_name_split = my_name.split(" ") #把字符串按照空格分割成一个列表，结果是['My', 'name', 'is', 'ShaFu.', 'Hi,', 'ShaFu!'] 
print(my_name_split)
count = 0
for i in range(len(my_name_split)):
    if my_name_split[i] == "ShaFu.":
        count += 1
    if count == 2:     
        my_name_split[i] = "傻逼." 
        #把列表中的"ShaFu."替换成"傻逼."
print(("、").join(my_name_split)) #把列表中的元素用"、"连接成一个字符串，结果是"My、name、is、傻逼.、Hi,、ShaFu!"，注意列表中的"ShaFu."被替换成了"傻逼."

my_name = "My name is ShaFu. Hi, ShaFu!"
my_name_new = my_name.strip("Fu") #把字符串两端的"F"和"u"都去掉，结果是"My name is ShaFu. Hi, ShaF"，注意字符串中间的"ShaFu"没有被修改，说明strip方法只会去掉字符串两端的指定字符，而不会修改字符串中间的内容
print(my_name_new)
print(my_name[::-1]) #把字符串反转，结果是"!uFaS ,iH .uFaS si eman yM"
print(my_name[-6:-1:1]) #切片操作，从索引-6到索引-1（不包括-1），步长为1，结果是"ShaFu"
print(my_name[-1:-7:-1]) #切片操作，从索引-1到索引-7（不包括-7），步长为-1，结果是"!uFaS "

# 集合
my_set = {1, 2, 3, 4, 5} #集合是花括号。集合是无序的，所以定义时元素的顺序不重要，输出时元素的顺序也可能和定义时不同
print(my_set) #集合是无序的，所以输出的元素顺序可能和定义时不同，结果是{1, 2, 3, 4, 5}，但元素的内容是一样的
my_set.add(6) #在集合中添加一个元素6
my_set.update([7, 8, 9]) #在集合中添加多个元素7、8、9
print(my_set) #集合是无序的，所以输出的元素顺序可能和定义时不同，结果是{1, 2, 3, 4, 5, 6, 7, 8, 9}，但元素的内容是一样的
my_set.remove(2) #从集合中删除一个元素2，如果元素不存在会报错
my_set.pop() #从集合中随机删除一个元素，并返回该元素
print(my_set) #集合是无序的，所以输出的元素顺序可能和定义
my_set.clear() #清空集合中的所有元素
print(my_set) #输出空集合，结果是set()  

"""
# 并集差集和交集
set_3 = set_1 | set_2  #set 1 和 set 2 的并集，包含 set 1 和 set 2 中的所有元素，重复的元素只保留一个
set_3 = set_1 .union(set_2) #set 1 和 set 2 的并集，包含 set 1 和 set 2 中的所有元素，重复的元素只保留一个
# 上述两种写法等价，都为并集写法

set_3 = set_1 & set_2 #set 1 和 set 2 的交集，包含 set 1 和 set 2 中都存在的元素
set_3 = set_1 .intersection(set_2) #set 1 和 set 2 的交集，包含 set 1 和 set 2 中都存在的元素
# 上述两种写法等价，都为交集写法

set_3 = set_1 - set_2  #set 1 和 set 2 的差集，包含 set 1 中存在但 set 2 中不存在的元素
set_3 = set_1 .difference(set_2)  #set 1 和 set 2 的差集，包含 set 1 中存在但 set 2 中不存在的元素
# 上述两种写法等价，都为差集写法
"""

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}
set_3 = set_1 | set_2 #set 1 和 set 2 的并集
print(set_3)

my_list = ["Alice", "Bob", "Charlie", "Alice", "Bob"]
list(set(my_list)) #把列表转换成集合，去掉重复的元素，然后再把集合转换成列表
print(list(set(my_list)))

# 字典
score_dict = {
    20250108847:{
        "姓名":"张三",
        "总分": 638
    },
    20250108848:{
        "姓名":"李四",
        "总分": 365
    },
    20250108848:{
        "姓名":"李四",
        "总分": 665
    }
}
print(score_dict) #字典是无序的，所以输出的键值对顺序可能和定义时不同
print(score_dict[20250108847]) #访问字典中键为20250108847的值
score_dict[20250108849] = {"姓名":"王五", "总分": 520} #在字典中添加一个键值对
print(score_dict) #字典是无序的，所以输出的键值对顺序可能和定义时不同
score_dict[20250108847]["总分"] = 650 #修改字典中键为20250108847的值中的"总分"键对应的值
print(score_dict) #字典是无序的，所以输出的键值对顺序可能和定义时不同
print(score_dict) #字典是无序的，所以输出的键值对顺序可能和定义时不同
print(score_dict.keys()) #获取字典中的所有键
print(score_dict.values()) #获取字典中的所有值
print(score_dict.items()) #获取字典中的所有键值对

for item in score_dict.items():
    print(item) #遍历字典中的所有键值对
    print(item[0]) #遍历字典中的所有键

for key, value in score_dict.items():
    print(f"学号：{key}，姓名：{value['姓名']}，总分：{value['总分']}") #遍历字典中的所有键值对

print("a" > "B") #字符串比较是按照ASCII码进行比较的，"a"的ASCII码是97，"B"的ASCII码是66，所以"a" > "B"的结果是True