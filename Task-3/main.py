# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

#   ###############################################################################

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення


# ###############################################################################

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

# Приклад:

# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))

#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()
    

# для перевірки ксассів використовуємо метод isinstance, приклад:


# user = User('Max', 15)
# shape = Shape()

# isinstance(max, User) -> True
# isinstance(shape, User) -> False

class Rectangle:
    
    def __init__(self,x ,y) -> None:
        self.x= x
        self.y= y
       
    @staticmethod   
    def area(rectangle):
        return rectangle.x * rectangle.y
    
    
    def __add__(self, other: object) -> float:
        return Rectangle.area(self) + Rectangle.area(other) 
    
    def __sub__(self, other: object) -> float:
        return Rectangle.area(self) - Rectangle.area(other) 
    
    def __eq__(self, other: object) -> bool:
        return Rectangle.area(self) == Rectangle.area(other) 

    def __ne__(self, other: object) -> bool:
        return Rectangle.area(self) != Rectangle.area(other) 

    def __gt__(self, other: object) -> bool:
        return Rectangle.area(self) > Rectangle.area(other) 

    def __lt__(self, other: object) -> bool:
        return Rectangle.area(self) < Rectangle.area(other) 

    def __len__(self) -> float:
        return self.x+self.y


rec = Rectangle(4,5)
rec1 = Rectangle(4,5)

# print(len(rec))



class Human:
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
        
class Prince(Human):
    def __init__(self, name, age, size) -> None:
        super().__init__(name, age)
        self.size = size
    
    
    def find_love(self, arr:list[object]):
        return [i for i in arr if i.feet == self.size]
        
            

class Cinderella(Human):
    count = 0
    def __init__(self, name, age, feet) -> None:
        super().__init__(name, age)
        self.feet = feet
        Cinderella.count +=1
    @classmethod
    def getter(cls):
        return cls.count
   

    def __repr__(self) -> str:
        return f" \n Name:{self.name} \n Age: {self.age} \n Feet:{self.feet}"
    
prince = Prince('Max', 25, 36)

olha = Cinderella('Olha', 36, 36)
masha = Cinderella('Masha', 18, 36)
ira = Cinderella('Ira', 26, 39)
tanya = Cinderella('Tanya', 22, 37)


# print(prince.find_love([olha, masha, ira, tanya]))

from abc import ABC, abstractmethod
class Printable(ABC):
    def __init__(self, name) -> None:
            self.name = name

    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def __str__(self):
        return self.name
    
class Book(Printable):
    def print(self):
        print(f"Name: {self.name}")
    
    def __str__(self):
        return self.name
    
class Magazine(Printable):
    def print(self):
        print(f"Name: {self.name}")

    def __str__(self):
        return self.name
class Main:
    __printable_list = []
    
    def add(self, other):
        if isinstance(other, Book) or isinstance(other, Magazine):
            Main.__printable_list.append(other)
            
    @classmethod
    def show_all_magazines(cls):
        print(' '.join([str(i) for i in cls.__printable_list if isinstance(i, Magazine)]))
        
    @classmethod
    def show_all_books(cls):
        print(' '.join([str(i) for i in cls.__printable_list if (isinstance(i, Book))]))
        
  
Main = Main()      

Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()

