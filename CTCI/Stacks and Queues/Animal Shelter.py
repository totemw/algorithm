"""
AnimalShelter - FIFO, receive the oldest animal of that type
enqueue, dequeueAny, dequeueDog, dequeueCat
"""


class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal):
        if animal.__class__ == Cat:
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueAny(self):
        if self.cats:
            return self.dequeueCat()
        return self.dequeueDog()

    def dequeueCat(self):
        if not self.cats:
            return None
        cat = self.cats[0]
        self.cats = self.cats[1:]
        return cat

    def dequeueDog(self):
        if not self.dogs:
            return None
        dog = self.dogs[0]
        self.dogs = self.dogs[1:]
        return dog


class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Cat(Animal):
    pass

class Dog(Animal):
    pass

