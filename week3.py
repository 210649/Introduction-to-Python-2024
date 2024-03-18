#第3章 列表简介
# 3.1 列表是什么
#3.1.1
bicycles = ['trek','cannodale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

#3.1.2
bicycles = ['trek','cannodale','redline','specialized']
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

#3.1.3
bicycles = ['trek','cannodale','redline','specialized']
messsage = f"My first bicrcle was a {bicycles[0].title()}"
print(messsage)

# 3.2 修改、添加和删除元素
#3.2.1
motorbicycles = ['honda','yamaha','suzuki']
print(motorbicycles)

motorbicycles[0] = 'ducati'
print(motorbicycles)

#3.2.2
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorbicycles = []
motorbicycles.append('honda')
motorbicycles.append('yamaha')
motorbicycles.append('suzuki')
print(motorbicycles)

motorcycles = ['honda','yamaha','suzuki']
motorbicycles.insert(0,'ducati')
print(motorbicycles)

#3.2.3
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned}.title()")

motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# 3.3 管理列表
#3.3.1
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#3.3.2
cars = ['bmw','audi','toyota','subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list:")
print(cars)

#3.3.3
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#3.3.4
cars = ['bmw','audi','toyota','subaru']
len(cars)

# 3.4 使用列表时避免索引错误
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles[-1])


