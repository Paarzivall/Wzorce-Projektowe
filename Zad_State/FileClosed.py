from FileState import FileState



class FileClosed(FileState):
    def __init__(self):
        self._instance = None
        self._context = None

    def GetInstance(self):
        if self._instance== None:
            self._instance = FileClosed()
        return self._instance

    def Open(self):
        print('Otwieram plik')
        from FileOpened import FileOpened
        fileOpen = FileOpened()
        self._context.ChangeState(fileOpen.GetInstance())

    def Close(self):
        print('Plik jest już zamknięty')

    def Read(self):
        print('Plik zamkniety - nie moge czytac z pliku')

    def Write(self):
        print('Plik zamkniety - nie moge pisac do pliku')

    def SetContext(self, context):
        self._context = context