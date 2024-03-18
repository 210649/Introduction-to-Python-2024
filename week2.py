# 第2章 变量和简单数据类型
# 2.1 hello world
print("Hello Python world!")

# 2.2 变量
message = "Hello Python world!"
print(message)

message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)

message = "Hello Python Crash Course reader!"
print(message)

# 2.3 字符串
#2.3.1
name = "ada lovalace" 
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#2.3.2
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
print(full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
print(f"Hello,{full_name.title（）}!")

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
message = f"Hello,{full_name.title（）}!"
print(message)

#2.3.3
print("Python")
print("\tPython")

print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#2.3.4
favorite_language = 'python '
favorite_language.rstrip()
favorite_language = favorite_language.rstrip()

favorite_language = ' python '
favorite_language = favorite_language.lstrip()
favorite_language = favorite_language.rstrip()

#2.3.5
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://') 
simple_url = nostarch_url.removeprefix('https://')

#2.3.6
message = "One of Python's strengths is its diverse community"
print(message)

# 2.4 数
#2.4.1
2+3
3-2
2*3
3/2
3**2
3**3
10**6
2+3*4
(2+3)*4

#2.4.2
0.1+0.1
0.2+0.2
2*0.1
2*0.2
0.2+0.1
3*0.1

#2.4.3
4/2
1+2.0
2*3.0
3.0**2

#2.4.4
universe_age = 14_000_000_000
print(universe_age)

#2.4.5
x,y,z = 0,0,0

#2.4.6
MAX_CONNECTIONS = 5000

# 2.5 注释
#向大家问好
print("Hello Python people!")

#2.6
import this
