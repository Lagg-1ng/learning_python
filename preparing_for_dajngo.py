#аргументы и именнованные аргументы
def plus(a, b, *args, **kwargs): #такая конструкция позволяет нам
    # получить *args-бесконечное количество позиционных аругментво
    #или бесконечное кол-во именнованных аргументов
    print(args)
    print(kwargs)
    return a+b
plus(1,2,1,1,1,1,1,1,1,1,1,1,
hello = True, goodbye = False, byebye=123)

def calc(*args):
    result = 0
    for x in args:
        result +=x
    return result
summa = calc(1,2,1,1,2,1,1,1,1,1,1,2,3)
print(summa)

#ООП
class Car():
   # wheels = 4
    #doors = 4
   #windows = 6
    #seets = 4
    def start(self): #если внутри класса, то метод, если нет то функция self - объект класса
        print('Двигатель запущен')
#это мы заменили стандартный str на свой
    def __str__(self):
        return f'автомоболь с {self.wheels} колесами'

    def __init__(self, *args, **kwargs):
        #print(kwargs)
        self.wheels = 4
        self.doors = 4
        self.windows = 6
        self.seets = 4
        self.color = kwargs.get('color', 'black')#первая '' это считываем, а 2 это если ничего не пришло то по умолчанию
        self.price = kwargs.get('price','1000')



#встроенные методы класса
print(dir(Car))

# __str__ - строковое отображение класса

#porshe = Car()
#porshe.color = 'black'
#porshe.windows = 4
#porshe.start()
porshe = Car(color = 'black',price = 10000)

print(porshe)# то что сделал str <__main__.Car object at 0x00000239A7B2FF50>


ferrari = Car()
ferrari.color = 'red'

mini = Car()
mini.color = 'yellow'

print(porshe.windows)
print('porshe',porshe.color, porshe.price)
print('ferrari',ferrari.color, ferrari.price)

#наследование
class Convertible(Car):
    #добавление к уже готовому
    def __init__(self, *args, **kwargs):
        # позволяет оперировать родительским классом
        self.time_to_take_off = 30
        super().__init__(*args, **kwargs)

    def take_off(self):
        print('Крыша убрана')

    #изменение метода в дачернем классе
    def __str__(self):
        return f'Кабриолет с {self.wheels} олесами и убираемой крышей'

porshe = Convertible(color = 'red',price=100000)
print(porshe.time_to_take_off)

porshe = Convertible(color = 'green',price=100000)
porshe.take_off()
print(porshe)

class Coupe(Convertible):
    def smth(self):
        print('большая матрешка')

vaz = Coupe(color =  'red', price = 100)
print('vaz',vaz.color)

