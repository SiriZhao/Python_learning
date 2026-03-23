# 类与对象
    # 动物信息——类
import re

class Animal: # type: ignore #定义一个Animal类，表示动物的信息
    name = None
    species = None
    age = 0
    sound = None
    diet = None
    health_status = None
    eat_times_every_day = None
    def make_sound(self): #定义一个方法，让动物发出叫声
        print(f"{self.name} 叫声：{self.sound}")
        return self.sound
    def age_in_human_years(self): #定义一个方法，计算动物的年龄相当于人类的多少岁
        human_age = self.age * 7
        return human_age

dog = Animal() #创建一个Animal类的实例，表示一只狗
dog.name = "旺财"  # type: ignore
dog.species = "狗" # type: ignore
dog.age = 3
dog.sound = "汪汪" # type: ignore
dog.diet = "狗粮" # type: ignore
dog.health_status = "健康" # type: ignore
dog.eat_times_every_day = 2 # type: ignore
print(dog.make_sound()) #调用make_sound方法，让狗发出叫声
print(f"{dog.name} 的年龄相当于人类的 {dog.age_in_human_years()} 岁") #调用age_in_human_years方法，计算狗的年龄相当于人类的多少岁

# 类的构造方法
class Animal:
    def __init__(self, name, age, sound, love_status, health_status="健康"):  # 定义构造方法，初始化对象的属性
        self.name = name
        self.age = age
        self.sound = sound
        self.health_status = health_status
        self.__love_status = love_status
    
    def __str__(self):  # 添加这个方法，当我们打印对象时，会调用这个方法来获取对象的字符串表示
        return f"动物名：{self.name}，年龄：{self.age}，健康状态：{self.health_status}"
    
    def make_sound(self):
        print(f"{self.name} 叫声：{self.sound}")
        return self.sound
    
    def age_in_human_years(self):
        return self.age * 7
    
    def __add__(self, other):
        if (self.__love_status): 
            print(f"{self.name} 已经有伴侣了，不能再交朋友了！")
            return f"已经有配偶了"
        print(f"{self.name} 和 {other.name} 在一起啦！")
        return f"孩子的名字叫：{self.name[0]}{other.name[0]}"
    
    def __sub__(self, other): 
        print(f"{self.name} 和 {other.name} 分手了！")
        return f"分手了。"
    
    def __call__(self): #当我们调用对象时，会调用这个方法来执行一些操作
        print(f"动物名：{self.name}，年龄：{self.age}，健康状态：{self.health_status}，恋爱状态：{self.__love_status}")
        self.make_sound()
        return
    

cat = Animal(name="咪咪", age=2, sound="喵喵", health_status="生病了", love_status=True) #创建一个Animal类的实例，表示一只猫
print(cat)  

dog = Animal(name="旺财", age=3, sound="汪汪", health_status="健康", love_status=True) #创建一个Animal类的实例，表示一只狗
print(dog)

new_animal = dog + cat  #调用__add__方法，让狗和猫交朋友
print(new_animal)

# 类的继承
class Phone: #定义一个Phone类，表示手机的信息
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    
    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}"
    
    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"

class Satellite(): #定义一个Satellite类，表示卫星电话的信息
    def satellite_call(self, number):
        return f"Satellite call to {number} is successful!"     

class Huawei(Phone, Satellite): #定义一个Huawei类，继承自Phone类，表示华为手机的信息，同时也继承了Satellite类，表示华为手机支持卫星电话功能
    def __init__(self, brand, model, price, harmony_version):
        super().__init__(brand, model, price) #调用父类的构造方法，初始化父类的属性
        self.harmony_version = harmony_version
    
    def fingerprint_unlock(self):
        return f"{self.brand} {self.model} 支持指纹解锁功能"
    
    def __str__(self):
        return f"HUAWEI 华为"

huawei_mate80_pro = Huawei(brand="HUAWEI", model="Mate 80 Pro", price=6999, harmony_version="HarmonyOS 6.0") #创建一个Huawei类的实例，表示一款华为手机
print(huawei_mate80_pro.satellite_call("1234567890")) #调用satellite_call方法，打印华为手机的卫星电话功能信息
print(huawei_mate80_pro.call("13800138000"))  #调用call方法，打印华为手机的信息
print(huawei_mate80_pro.fingerprint_unlock())  #调用fingerprint_unlock方法，打印华为手机的指纹解锁功能信息
print(huawei_mate80_pro)  #调用__str__方法，打印华为手机的信息


class Apple(Phone): #定义一个Apple类，继承自Phone类，表示苹果手机的信息
    def __init__(self, brand, model, price, ios_version):
        super().__init__(brand, model, price) #调用父类的构造方法，初始化父类的属性
        self.ios_version = ios_version
    
    def face_id_unlock(self):
        return f"{self.brand} {self.model} 支持面部识别解锁功能"
    
    def __str__(self):
        return f"APPLE 苹果"
    
iphone_17_pro = Apple("APPLE", "iPhone 17 Pro", "7999", "iOS 26") #创建一个Apple类的实例，表示一款苹果手机
print(iphone_17_pro.call("13800138000"))  #调用call方法，打印苹果手机的信息
print(iphone_17_pro.face_id_unlock())  #调用face_id_unlock方法，打印苹果手机的面部识别解锁功能信息
print(iphone_17_pro)  #调用__str__方法，打印苹果手机的信息

# 模块与库
# 1. 导入内置模块
import math          # 数学计算
import datetime      # 日期时间
import random        # 随机数
import os            # 操作系统交互（如文件路径）

# 使用 math 库进行高级运算
print(f"π 的值是：{math.pi}")
print(f"9 的平方根是：{math.sqrt(9)}")

# 使用 datetime 处理时间
now = datetime.datetime.now()
print(f"当前时间是：{now.strftime('%Y-%m-%d %H:%M:%S')}")

# 使用 random 生成随机数
fruits = ["苹果", "香蕉", "橘子", "葡萄"]
lucky_fruit = random.choice(fruits)
print(f"今天推荐吃的水果是：{lucky_fruit}")

# 2. 从模块中导入特定功能 (更简洁)
from time import sleep
print("程序准备休眠 1 秒...")
sleep(1)
print("休眠结束！")

# 3. 自定义模块 (原理说明)
# 如果你创建了一个名为 tools.py 的文件，内容为 add(a, b) 函数
# 你可以在这里使用：import tools; tools.add(1, 2)
