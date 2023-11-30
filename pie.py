'''
Pie
Group: Taylor Eskew and Maya Federico
'''
class Pie:
    # __init__ method
    def __init__(self, flavor, slices, preparation):
        self.flavor = flavor
        self.slices = slices
        self.preparation = preparation   # frozen or cooked
        self.slices_eaten = 0

    # String method
    def __str__(self):
        return f'{self.slices} slices of {self.preparation} {self.flavor} pie \nSlices eaten: {self.slices_eaten}'

    def cook(self):
        # cooks the pie
        self.preparation = 'cooked'
    
    def eat(self):
        # subtracts a slice
        # and increments the number of slices eaten
        self.slices -= 1
        self.slices_eaten += 1


if __name__ == "__main__":
    # main program
    apple_pie = Pie('apple', 5, 'frozen')
    pumpkin_pie = Pie('pumpkin', 7, 'cooked')

    print(apple_pie)
    print(pumpkin_pie)

    apple_pie.cook()
    pumpkin_pie.eat()
    
    print()
    print(apple_pie)
    print(pumpkin_pie)