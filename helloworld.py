# print("Hello World!"); ##输出hello

# a = "Hello";
# print("ello5" in a);

# a = 15;
# b = "12";
# # print (a + b);
# print(a + int(b))

# a = complex(1,2);
# print(a);
# print(a.real);
# print(a.imag);


# print(input("请输入你的名字：") + ",你好！");
# a = int(input());
# b = int(input());
# print(a + b);
# print(a - b);

# s = input();
# numbers = s.split();
# a = int(numbers[0]);
# b = int(numbers[1]);
# print(a + b);




# 函数-阶乘递归

# def Factorial(n):
#     if n < 2 :
#         return 1
#     else:
#         return n * Factorial(n-1)
    
# print(Factorial(int(input())))


# a = [1,2,3,4]
# c = a
# a[2] = 6
# print(a)
# print(c)

#!/usr/bin/python3
 
# import sys         # 引入 sys 模块
 
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
 
# while True:
#     try:
#         print (next(it))
#     except StopIteration:
#         sys.exit()

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
 
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
 
# myclass = MyNumbers()
# myiter = iter(myclass)
 
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
 
# # 创建生成器对象
# generator = countdown(5)
 
# # 通过迭代生成器获取值
# print(next(generator))  # 输出: 5
# print(next(generator))  # 输出: 4
# print(next(generator))  # 输出: 3
 
# # 使用 for 循环迭代生成器
# for value in generator:
#     print(value)  # 输出: 2 1

# 

def square(x):
    return x*x
def print_running(f,x):
    print(f'{f.__name__} is running.')
    return f(x)

result = print_running(square, 2)
print(result)