from Checkbox import Checkbox
from WindowMediator import WindowMediator

if __name__ == '__main__':
    checkbox1 = Checkbox('1', 'Cwiczenia zaliczone')
    checkbox2 = Checkbox('2', 'Wyklad Zaliczony')
    checkbox3 = Checkbox('3', 'Przedmiot zaliczony (konkurs)')

    mediator = WindowMediator(checkbox1, checkbox2, checkbox3)

    checkbox1.SetMediator(mediator)
    checkbox2.SetMediator(mediator)
    checkbox3.SetMediator(mediator)

    while True:
        print(f'[1] {checkbox1}')
        print(f'[2] {checkbox2}')
        print(f'[3] {checkbox3}')
        print(f'[4] Wyjdz z programu ')
        action = str(input('Co chcesz zrobic?\t'))
        if action == '1':
            checkbox1.Check()
        elif action == '2':
            checkbox2.Check()
        elif action == '3':
            checkbox3.Check()
        else:
            break