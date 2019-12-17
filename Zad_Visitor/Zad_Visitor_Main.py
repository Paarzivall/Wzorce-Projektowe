from Bird import Bird
from Fish import Fish
from Mammal import Mammal
from Reptile import Reptile
from OfficialPrice import OfficialPrice
from BlackMarketPrice import BlackMarketPrice
from VetDiagnosis import VetDiagnosis


if __name__ == '__main__':
    bird = Bird('Ptak', 100, True, 150)
    fish = Fish('Ryba', 10, False)
    mammal = Mammal('Ssak', 1000, False)
    raptile = Reptile('Gad', 999, True)
    bird2 = Bird('Ptak', 100, False, 110)

    animals = [bird, fish, mammal, raptile, bird2]

    for animal in animals:
        print(animal)

    officialPrice = OfficialPrice()
    blackMarketPrice = BlackMarketPrice()
    vetDiagnosis = VetDiagnosis()

    for animal in animals:
        animal.Accept(officialPrice)
        animal.Accept(blackMarketPrice)

    print('\n\n\t\tCeny odwiedzonych zwierzat')

    officialPrice.PrintVisitorResult()
    blackMarketPrice.PrintVisitorResult()

    print('\n\n\t\tStan zdrowia odwiedzonych zwierzat')
    for animal in animals:
        animal.Accept(vetDiagnosis)