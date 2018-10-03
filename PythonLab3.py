from abc import ABC, abstractmethod
 
class Person(ABC):
    name = str(None)
    weight = int(0)
    step = float(0)
    DailyCalories = int(0)
    eatCalories = int(0)

    def eat(self, eaten):
        self.eatCalories += eaten.Calories
    @abstractmethod
    def Heals(self):
        #Физическая активность
        steps_num = float(input('Сколько шагов вы сделали? '))
        steps_time = float(input('Какое время вы шли? (В минутах) ')) / 60

        V = self.step * steps_num / 1000 / steps_time 

        print("%.1f" % V)
        if 2 <= V < 4:
            print('Побольше ходи!!!')
        elif 4 <= V < 6:
            print('Продолжай в том же духе!')
        elif 6 <= V <= 10:
            print('А ты герой!')
        #Еда
        if (self.DailyCalories <= self.eatCalories):
            print('С калориями всё нормально, так держать')
        else: print('Ты мало ешь :(')

class Man(Person):
    step = 0.8
    DailyCalories = 3500

    def Heals(self):
        return super().Heals()
    
 
class Woman(Person):
    step = 0.5
    DailyCalories = 2500

    def Heals(self):
        return super().Heals()

class Product:
    name = str(None)
    Calories = int(0)

class Fruit(Product):
    pass
class Sweet(Product):
    pass
class Meat(Product):
    pass

class Program:
    user1 = Man()
    user1.name = 'Kirill'
    user1.weight = 79

    user2 = Woman()
    user2.name = 'Eva'
    user2.weight = 45

    f1 = Fruit()
    f1.name = 'Banana'
    f1.Calories = 300

    f2 = Fruit()
    f2.name = 'Авокадо'
    f2.Calories = 570

    s1 = Sweet()
    s1.name = 'Shokoladka'
    s1.Calories = 544

    m1 = Meat()
    m1.name = 'Shaslik'
    m1.Calories = 1485

    user1.eat(f1)
    user1.eat(m1)
    user1.eat(f2)
    user1.eat(f2)

    user2.eat(f1)
    user2.eat(f1)
    user2.eat(f1)
    user2.eat(s1)
    user2.eat(s1)
    user2.eat(f2)

    user1.Heals()
    user2.Heals()
