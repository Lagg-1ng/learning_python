print("hi world")

#переменные
x = 2
y = 3
print("x = ", x, "y = ", y)

#строку в переменную
str = 'Строка в переменной'
print(str)

#логическое значение(boolean)
#(важно что с заглавной и без ковычек,камон не глупи)
t = True
f = False

#float (плавующая точка, дроби)

a_float = 3.87
#type позволяет узнать тип переменной
print(type(str))

#none(отсутствие чего-либо)
a_non = None
#в идеале если большое имя переменной то записываем через "_" каждое слово
super_long_name = True

#упорядоченные списки
days = "mon, tue, web, thu, fri, sat,sun"
print(type(days))

#не лист глупо и неудобно
#day_one = 'mon'
#day_two = 'tue'
#tuple

days = ['mon', 'tue', 'web', 'thu', 'fri', 'sat', 'sun']
print(type(days), days)
#nonmutable операторы
print(days[2])  #по класике с 0
print(len(days))

#mutable операторы
days.append('second_sun')
print(days)
days.reverse()
print(days)

#tuple не упорядоченные последовательности

days = ('mon', 'tue', 'web', 'thu', 'fri', 'sat', 'sun')
print(type(days))  #не изменяемый!

#словари dictionary
#название ключа всегда в ковычках
human = {
    'name': 'Человек',
    'age': 22,
    'russian': True,
    'fav_food': ['суп', 'пельмени']
}
print(human['fav_food'])
#созданный нужный нам набор данных

#добавление новых записей
human['developer'] = False
print(human)

#функции

age_f = '128'
print(type(age_f), age_f)

age_f2 = int(age_f)
print(type(age_f2), age_f2)


#собственные функции
def seyHello(  #могут быть пармаетры
):
  print('Привет')


print('Пока')
seyHello()

#параметры функции


def seyHello1(name):
  print('Привет', name)


seyHello1('Валера')


def plus(a, b=0):
  print(a + b)


plus(110)
plus(4, 6)


def plus1(a, b):
  return (a + b)
  print('эта строкан икогда не выполниться', True)


p_sum = plus1(2, 3)
print(p_sum)


#позиционные функции
def r_plus(a, b):
  return b - a


r_sum = r_plus(b=2, a=4)
print(r_sum)


def seyHello1(name, age, city, fav_food):
  return f'Привет {name}, тебе {age} лет, ты из {city}, твоя любимая еда {fav_food}'


hello = seyHello1(name='Антон', age='28', city='Пенза', fav_food='рис')
print(hello)

#условие
#def dz(a,b):
#  return a+ b
#
#result = dz(2,"3")
#print(result)


def dz(a, b):
  if type(b) is int or type(b) is float:
    return a + b
  else:
    return None


result = dz(2, 3.5)
print(result)
