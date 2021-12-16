class Restaurant:
    def __init__(self):
        self.drinks = {
            'coca cola': 20,
            'star ship': 25
        }


class FoodCourt(Restaurant):
    def __init__(self):
        super().__init__()
        self.items = {
            'breakfast': {
                'dim khichuri': 50,
                'chicken khichuri': 70,
            },
            'lunch': {
                'kacci': 100,
                'tehari': 70,
                'morog polaw': 80
            },
            'dinner': {
                'kacci': 100,
                'tehari': 70,
                'morog polaw': 80
            }
        }


class GreenGarden(Restaurant):
    def __init__(self):
        super().__init__()
        self.items = {
            'breakfast': {
                'plan porota': 10,
                'omelet': 15,
                'vegetable  curry': 10,
                'dal': 10
            },
            'lunch': {
                'rice': 10,
                'alu vorta': 10,
                'mach vorta': 10,
                'chachcahri': 20,
                'dim curry': 20,
                'fish curry': 50,
                'chicken curry': 50,
                'beef curry': 80,
                'tehari': 100,
                'morog polow': 100
            },
            'dinner': {
                'rice': 10,
                'alu vorta': 10,
                'mach vorta': 10,
                'chachcahri': 20,
                'dim curry': 20,
                'fish curry': 50,
                'chicken curry': 50,
                'beef curry': 80,
                'tehari': 100,
                'morog polow': 100
            }
        }


class Cafeteria(Restaurant):
    def __init__(self):
        super().__init__()

        self.items = {
            'breakfast': {
                'plan porota': 10,
                'omelet': 15,
                'vegetable  curry': 10,
                'dal': 10
            },
            'lunch': {
                'rice': 10,
                'alu vorta': 10,
                'mach vorta': 10,
                'chachcahri': 20,
                'dim curry': 20,
                'fish curry': 50,
                'chicken curry': 50,
                'beef curry': 80
            },
            'dinner': {
                'rice': 10,
                'alu vorta': 10,
                'mach vorta': 10,
                'chachcahri': 20,
                'dim curry': 20,
                'fish curry': 50,
                'chicken curry': 50,
                'beef curry': 80
            }
        }
