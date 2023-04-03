Hot = input("Select a hot drink: ")

if input == Hot:
    print("Coffee")
else:
    print("Tea")


class Coffee:
    def __init__(self, no_milk, milk, sugar):
        self.no_milk = no_milk
        self.milk = milk
        self.sugar = sugar


class Tea:
    def __init__(self, no_milk, milk, sugar):
        self.no_milk = no_milk
        self.milk = milk
        self.sugar = sugar


class Hot(Coffee):
    def __init__(self, no_milk, milk):
        super().__init__(self, no_milk, milk)

    def __str__(self):
        return f'Selected drink is {self.no_milk}, with: {self.milk} and {self.sugar}'


class Hot(Tea):
    def __init__(self, no_milk, milk):
        super().__init__(self, no_milk, milk)

    def __str__(self):
        return f'Selected drink is {self.no_milk}, with: {self.milk} and {self.sugar}'


spoons_of_sugar = [int(spoons_of_sugar) for spoons_of_sugar in input("Adjust dose of sugar: ").split()]
print("Dose of sugar is: ", spoons_of_sugar)
