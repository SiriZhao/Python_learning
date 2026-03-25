"""
从键盘接受两个值：1. 是否是新顾客（可以用是/否） 2. 充值金额
然后执行如下逻辑：
单次充值[1000,2000)元的，按照充值金额的15%进行额外赠送
单次充值[2000,5000)元的，按照充值金额的18%进行额外赠送
单次充值5000元及以上的，按照充值金额的20%进行额外赠送，并且补贴500元
单次充值10000元及以上的，不进行额外赠送，而是直接补贴10000元
如果该顾客是新顾客，则赠送总金额的10%作为首充福利
    最后，以f-string的方式，输出如下内容：尊敬的 新/老 客户，您好！您充值的金额是 XXXX 元，实际到账 XXXX 元!
"""

def main(): #定义一个主函数，作为程序的入口点
    customer_type = input("请输入顾客类型(新/老)：")
    if customer_type not in ["新", "老"]: #判断输入的顾客类型是否有效，如果不是"新"或"老"，则输出提示信息并返回
        print("输入的顾客类型无效，请输入'新'或'老'。")
        return
    
    try: #使用try-except块来捕获用户输入的充值金额可能引发的异常，如果用户输入的不是一个整数，程序会抛出一个ValueError异常，这时我们可以捕获这个异常并输出一个提示信息，告诉用户输入的充值金额无效，并要求用户输入一个整数。
        input_money = int(input("请输入充值金额："))
    except Exception as error: #捕获所有异常，并把异常对象赋值给变量error，这样我们就可以在except块中使用这个变量来获取异常的详细信息，或者在调试时查看异常对象的属性和方法，以便更好地理解和处理异常。
        print("输入的充值金额无效，请重新输入。")
        return

    result_money = 0

    if 2000 > input_money >= 1000:
        result_money = input_money + input_money * 0.15 
    elif 5000 > input_money >= 2000:
        result_money = input_money + input_money * 0.18
    elif 10000 > input_money >= 5000:
        result_money = input_money + input_money * 0.2 + 500
    elif input_money >= 10000:
        result_money = input_money + 10000
    else:
        result_money = input_money

    if customer_type == "新":
        result_money += result_money * 0.1

    print(f"尊敬的 {customer_type} 客户，您好！您充值的金额是 {input_money} 元，实际到账 {result_money} 元!")

main() #调用主函数，开始执行程序