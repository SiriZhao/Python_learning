"""
定义一个数列如下，你可以直接复制粘贴下面的代码，注意要把progress_function改为你自己函数的名字
my_list = [ "写完这段代码高考分数必如意", 750, ["计算机", "机器人", "自动化"],
           "", 12.9682, 6+9j, ["清华大学", "浙江大学"], "Apple", 
           progress_function, print("我是个print函数, 被执行了！"),
           progress_function(0.05, print("进度条函数执行完毕！"))]
注意，这里面的 progress_function 是作业2中自己实现的 progress_function
3.1 while遍历
通过while方法遍历列表，并删除所有元素，实现和.clear()同样的效果，也就是通过while循环实现.clear()方法
3.2 for遍历
( 1 ) 定义一个新的数列new_list
( 2 ) for遍历上面的循环my_list，把my_list按照倒序存入new_list中
( 3 ) 注意，存入的过程中，如果my_list中的元素是数列，则该序列也需要倒序存入
"""

from Progress import progress_bar

my_list = ["写完这段代码高考分数必如意", 750, ["计算机", "机器人", "自动化"],
           "", 12.9682, 6+9j, ["清华大学", "浙江大学"], "Apple",
           progress_bar, print("我是个print函数, 被执行了！")]

progress_bar(0.05)
print("进度条函数执行完毕！")


# 3.1 while 遍历：逐一删除所有元素，实现 .clear() 效果
while len(my_list) > 0:
    my_list.pop(0)

print("3.1 删除后 my_list =", my_list)


# 3.2 for 遍历：把 my_list 倒序存入 new_list，子列表也倒序
my_list = ["写完这段代码高考分数必如意", 750, ["计算机", "机器人", "自动化"],
           "", 12.9682, 6+9j, ["清华大学", "浙江大学"], "Apple",
           progress_bar, print("我是个print函数, 被执行了！")]

progress_bar(0.05)
print("进度条函数执行完毕！")

new_list = []

for i in range(len(my_list) - 1, -1, -1):   # 从最后一个索引倒着遍历到 0
    item = my_list[i]
    if isinstance(item, list):               # 如果元素是子列表，也倒序
        reversed_item = []
        for j in range(len(item) - 1, -1, -1):
            reversed_item.append(item[j])
        new_list.append(reversed_item)
    else:
        new_list.append(item)

print("3.2 new_list =", new_list)
