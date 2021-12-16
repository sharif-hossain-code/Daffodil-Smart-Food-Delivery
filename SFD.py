from restaurant import *


class SFD(FoodCourt, GreenGarden, Cafeteria):
    def __init__(self):
        super().__init__()
        self.food_court = FoodCourt()
        self.green_garden = GreenGarden()
        self.cafeteria = Cafeteria()
        self.count = 1
        self.selectedItem = []
        self.done = True
        self.totalPrice = 0

    def breakfast(self, option):
        food_court_items = self.food_court.items['breakfast']
        green_garden_items = self.green_garden.items['breakfast']
        cafeteria_items = self.cafeteria.items['breakfast']

        if option == 'food court':
            for item, price in food_court_items.items():
                print(f'{self.count}. {item.title()}: {price} Tk.')
                self.count = self.count + 1
            while self.done:
                want_more = input('Do you Want any of this Items(yes or no): ').lower()
                if want_more == 'yes':
                    selectItem = input('Select your Item: ').lower()
                    self.selectedItem.append(selectItem)
                else:
                    print('Here is your Invoice...')
                    self.done = False

        elif option == 'green garden':
            for item, price in green_garden_items.items():
                print(f'{self.count}. {item.title()}: {price} Tk.')
                self.count = self.count + 1

            while self.done:
                want_more = input('Do you Want any of this Items(yes or no): ').lower()
                if want_more == 'yes':
                    selectItem = input('Select your Item: ').lower()
                    self.selectedItem.append(selectItem)
                else:
                    print('Here is your Invoice...')
                    self.done = False

        elif option == 'cafeteria':
            for item, price in cafeteria_items.items():
                print(f'{self.count}. {item.title()}: {price} Tk.')
                self.count = self.count + 1

            while self.done:
                want_more = input('Do you Want any of this Items(yes or no): ').lower()
                if want_more == 'yes':
                    selectItem = input('Select your Item: ').lower()
                    self.selectedItem.append(selectItem)
                else:
                    print('Here is your Invoice...')
                    self.done = False

        else:
            print("Invalid option")

    def lunch(self, option):
        food_court_items = self.food_court.items['lunch']
        green_garden_items = self.green_garden.items['lunch']
        cafeteria_items = self.cafeteria.items['lunch']

        if option == 'food court':
            for item, price in food_court_items.items():
                print(f'{self.count}. {item.title()}: \t\t\t💸{price} Tk.')
                self.count = self.count + 1
            while self.done:
                want_more = input('Do you Want any of this Items(yes or no): ').lower()
                if want_more == 'yes':
                    selectItem = input('Select your Item: ').lower()
                    self.selectedItem.append(selectItem)
                else:
                    print('Here is your Invoice...')
                    self.done = False
        elif option == 'green garden':
            for item, price in green_garden_items.items():
                print(f'{self.count}. {item.title()}: \t\t\t💸{price} Tk.')
                self.count = self.count + 1
            while self.done:
                want_more = input('Do you Want any of this Items(yes or no): ').lower()
                if want_more == 'yes':
                    selectItem = input('Select your Item: ').lower()
                    self.selectedItem.append(selectItem)
                else:
                    print('Here is your Invoice...')
                    self.done = False
        elif option == 'cafeteria':
            for item, price in cafeteria_items.items():
                print(f'{self.count}. {item.title()}: \t\t\t💸{price} Tk.')
                self.count = self.count + 1
            while self.done:
                want_more = input('Do you Want any of this Items(yes or no): ').lower()
                if want_more == 'yes':
                    selectItem = input('Select your Item: ').lower()
                    self.selectedItem.append(selectItem)
                else:
                    print('Here is your Invoice...')
                    self.done = False

    def dinner(self, option):
        food_court_items = self.food_court.items['dinner']
        green_garden_items = self.green_garden.items['dinner']
        cafeteria_items = self.cafeteria.items['dinner']
        if option == 'food court':
            for item, price in food_court_items.items():
                print(f'{self.count}. {item.title()}: {price} Tk.')
                self.count = self.count + 1
            while self.done:
                want_more = input('Do you Want any of this Items(yes or no): ').lower()
                if want_more == 'yes':
                    selectItem = input('Select your Item: ').lower()
                    self.selectedItem.append(selectItem)
                else:
                    print('Here is your Invoice...')
                    self.done = False
        elif option == 'green garden':
            for item, price in green_garden_items.items():
                print(f'{self.count}. {item.title()}: {price} Tk.')
                self.count = self.count + 1
            while self.done:
                want_more = input('Do you Want any of this Items(yes or no): ').lower()
                if want_more == 'yes':
                    selectItem = input('Select your Item: ').lower()
                    self.selectedItem.append(selectItem)
                else:
                    print('Here is your Invoice...')
                    self.done = False
        elif option == 'cafeteria':
            for item, price in cafeteria_items.items():
                print(f'{self.count}. {item.title()}: {price} Tk.')
                self.count = self.count + 1
            while self.done:
                want_more = input('Do you Want any of this Items(yes or no): ').lower()
                if want_more == 'yes':
                    selectItem = input('Select your Item: ').lower()
                    self.selectedItem.append(selectItem)
                else:
                    print('Here is your Invoice...')
                    self.done = False

    def showInvoice(self, ask, option):
        food_court_items = self.food_court.items[ask]
        green_garden_items = self.green_garden.items[ask]
        cafeteria_items = self.cafeteria.items[ask]
        print('-----------------------------------------------')
        if option == 'food court':
            for item in self.selectedItem:
                if item in food_court_items.keys():
                    self.totalPrice = self.totalPrice + food_court_items.get(item)
                    print(f'{item.title()}: {food_court_items.get(item)}')
        elif option == 'green garden':
            for item in self.selectedItem:
                if item in green_garden_items.keys():
                    self.totalPrice = self.totalPrice + green_garden_items.get(item)
                    print(f'{item.title()}: {green_garden_items.get(item)}')
        elif option == 'cafeteria':
            for item in self.selectedItem:
                if item in cafeteria_items.keys():
                    self.totalPrice = self.totalPrice + cafeteria_items.get(item)
                    print(f'{item.title()}: {cafeteria_items.get(item)}')
        print('-----------------------------------------------')
        print(f'Here is your Bill, sir: {self.totalPrice} Tk.')
