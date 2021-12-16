from SFD import SFD

selects = SFD()


def selectOption():
    ask = input('What do you want to eat?\n1.Breakfast\n2.Lunch\n3.Dinner\n\n:::').lower()

    if ask == 'breakfast':
        option = input('Which restaurant you prefer?\n1.Food Court\n2. Green Garden\n3.Cafeteria\n:::').lower()
        if option == 'food court':
            selects.breakfast(option)
            selects.showInvoice(ask, option)
        elif option == 'green garden':
            selects.breakfast(option)
            selects.showInvoice(ask, option)
        elif option == 'cafeteria':
            selects.breakfast(option)
            selects.showInvoice(ask, option)

        else:
            print('Please choose those option :)')

    elif ask == 'lunch' or ask == '2':
        option = input('Which restaurant you prefer?\n1.Food Court\n2. Green Garden\n3.Cafeteria\n:::').lower()
        if option == 'food court' or option == '1':
            selects.lunch(option)
            selects.showInvoice(ask, option)
        elif option == 'green garden' or option == '2':
            selects.lunch(option)
            selects.showInvoice(ask, option)
        elif option == 'cafeteria' or option == '3':
            selects.lunch(option)
            selects.showInvoice(ask, option)
    elif ask == 'dinner' or ask == '3':
        option = input('Which restaurant you prefer?\n1.Food Court\n2. Green Garden\n3.Cafeteria\n:::').lower()
        if option == 'food court' or option == '1':
            selects.dinner(option)
            selects.showInvoice(ask, option)
        elif option == 'green garden' or option == '2':
            selects.dinner(option)
            selects.showInvoice(ask, option)
        elif option == 'cafeteria' or option == '3':
            selects.dinner(option)
            selects.showInvoice(ask, option)

    else:
        print('Please choose those option :)')
        selectOption()


selectOption()
