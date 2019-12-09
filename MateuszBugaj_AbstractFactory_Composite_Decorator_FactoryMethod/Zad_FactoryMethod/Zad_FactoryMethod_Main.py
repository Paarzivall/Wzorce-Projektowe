from ZapytanieSqlServer import ZapytanieSqlServer
from ZapytanieOracle import ZapytanieOracle

if __name__ == '__main__':
    zapytanie = 'DROP TABLE Risitas'
    zapytanie1 = ZapytanieSqlServer()
    zapytanie1.WykonajZapytanie('SQL_SERVER_1', zapytanie)

    zapytanie2 = ZapytanieOracle()
    zapytanie2.WykonajZapytanie('Oracle_1', zapytanie)