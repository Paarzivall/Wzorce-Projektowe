from ZapytanieOracle import ZapytanieOracle
from ZapytanieSQLServer import ZapytanieSQLServer


if __name__ == '__main__':
    zapOracle = ZapytanieOracle()
    zapSQLServer = ZapytanieSQLServer()

    zapytanie = 'SELECT * FROM tabela'
    print(zapOracle.wykonajZapytanie('Oracle', zapytanie))
    print('\n')
    print(zapSQLServer.wykonajZapytanie('SQL Server', zapytanie))