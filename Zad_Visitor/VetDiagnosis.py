from Visitor import Visitor


class VetDiagnosis(Visitor):
    def VisitAnimal(self, animal):
        if(animal.ill):
            diagnosis = 'zdrowy'
            treatment = 'niewymagane'
        else:
            diagnosis = 'choroba'
            treatment = 'antybiotyki'
        print(f'Odwiedzone zwierze: {animal.name}, Diagnoza: {diagnosis}, Leczenie: {treatment}')

    def VisitBird(self, bird):
        if(bird.ill):
            diagnosis = 'zdrowy'
            treatment = 'niewymagane'
        else:
            diagnosis = 'choroba'
            if(bird.blackMarketPrice >= 2* bird.Price):
                treatment = 'klinika'
            else:
                treatment = 'antybiotyki, dieta'
        print(f'Odwiedzone zwierze: {bird.name}, Diagnoza: {diagnosis}, Leczenie: {treatment}')
