"""
实现一个通用进度条，进度条的样式自定义
函数入参要求：
1. 进度条每进一格所需要的秒数 seconds
2. 进度条完成之后执行的函数 callback_function
函数功能要求：
1. 实现每seconds秒进度条进一步
2. 进度条达到100%之后，调用`callback_function`
函数返回要求：
None
备注：实际调用时，callback_function可以自己定义，至少定义两种callback_function，实际调用时也分别调用一次（传入不同的callback_function）
"""

import time
def progress_bar(seconds, callback_function):
    for i in range(101):
        print(f"\r进度：{i}%", end="")
        time.sleep(seconds)
    print("\n进度完成！")
    callback_function() 
def callback_function_1():
    print("这是回调函数1，进度条完成了！")

def callback_function_2():
    print("这是回调函数2，进度条完成了！")  

if __name__ == "__main__":    
    progress_bar(0.1, callback_function_1)
    progress_bar(0.1, callback_function_2)