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

def Factorial(n):
    if n < 2 :
        return 1
    else:
        return n * Factorial(n-1)
    
print(Factorial(int(input())))