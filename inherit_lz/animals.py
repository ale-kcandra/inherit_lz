class Animal: # родительский класс, в котором общие свойства животных
    def __init__(self, name, age, species): # конструктор, в котором вызывается при создании объекта
        self.name = name # сохраняем имя в объект
        self.age = age # сохраняем возраст
        self.species = species # сохраняем вид животного

    def make_sound(self): # метод, который издает звук
        print(f"{self.name} издает звук") # выводим "имя издает звук"

    def info(self): # метод,который выводит информацию об объекте
        print(f"имя: {self.name}, возраст: {self.age}, вид: {self.species}") # все данные через self (это ссылка на тот конкретный объект, с которым сейчас работает метод)

    def __del__(self): # деструктор, который вызывается при удалении объекта
        print(f"объект: {self.name} удален") # выводим, что удалили объект


class Dog(Animal): # дочерний класс, который наследует Animal
    def __init__(self, name, age, species, breed, guard_status): # конструктор Dog 
        super().__init__(name, age, species) # super() вызывает конструктор родителя (через него дочерний класс обращается к методам родительского класса)
        self.breed = breed # доп. атрибут, который отвечает за породу
        self.guard_status = guard_status # доп. атрибут, который отвечает за статус охраны (True/False)

    def make_sound(self): # переопределение, где своя версия звука
        print(f"{self.name} Гав!")  # собака гавкает

    def info(self): # переопределение,где более расширенная информация
        super().info() # сначала выводим данные родителя
        print(f"порода: {self.breed}, охрана: {self.guard_status}") # потом добавляем свои поля

    def guard_house(self): # новый метод (нет у Animal)
        if self.guard_status: # если статус охраны True
            print(f"{self.name} охрана дома") # охраняет дом
        else: # иначе (False)
            print(f"{self.name} не охраняет дом") # не охраняет дом