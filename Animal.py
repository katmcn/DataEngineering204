from Cat import hiss


class Animal:

    def __init__(self, name=str, breed=str, colour=str, age=int, domesticated=bool):
        self.__name = name
        self.__breed = breed
        self.__colour = colour
        self.__age = age
        self.__domesticated = domesticated

    # def set_species(self, species):
    # control flow
    # check input is characters
    # error handle for spelling mistakes/caps etc
    # put answers into categories e.g. if dog or Dog or spaniel is entered, it is a dog
    # self.__species = species

    # def get_species(self):
    #    return self.__species

    def set_name(self, name):
        # control flow
        self.__name = name

    def get_name(self):
        return self.__name

    def speak(self):  # override with specifications
        print(f'{self.__name} *made a noise*')

    def move(self):  # override with specifications
        print(f'{self.__name} ran away')

    def eat(self):
        print(f'{self.__name} ate')

    def sleep(self):
        print(f'{self.__name} fell asleep....ZZZZzzzzzzzzZZZZZZZzzzzzz')


class Cat(Animal):

    def __init__(self, name, breed, colour, age, domesticated):
        super().__init__(name, breed, colour, age, domesticated)

    def hiss(self):
        print(f'{self.get_name()} hissed at you')

    def speak(self):  # override parent method
        print(f'{self.get_name()} meowed!')


my_cat = Cat("Lisa", "Siberian", 'Brown Tabby', 13, True)
print(f'Your cats name is {my_cat.get_name()}')
my_cat.hiss()
my_cat.move()
my_cat.speak()
my_cat.sleep()


class Dog(Animal):

    def __init__(self, name, breed, colour, age, domesticated, best_trick):
        super().__init__(name, breed, colour, age, domesticated)
        self.best_trick = best_trick

    def spin(self):
        print(f'{self.get_name()} spun in circles')

    def speak(self):  # override with specifications
        print(f'{self.get_name()} barked!')


my_dog = Dog("Max", "Spaniel", "Brown and White", 6, True, "Spin")
print(f'Your dogs name is {my_dog.get_name()}')
my_dog.spin()
my_dog.speak()
my_dog.spin()



