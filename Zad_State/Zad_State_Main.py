from File import File


if __name__ == '__main__':
    plik = File()
    plik.Open()
    plik.Read()
    plik.Open()
    plik.Write()
    plik.Close()
    plik.Write()
    plik.Read()
    plik.Close()