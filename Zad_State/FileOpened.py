from FileState import FileState


class FileOpened(FileState):
    def __init__(self):
        self._instance = None
        self._context = None

    def GetInstance(self):
        if self._instance == None:
            self._instance = FileOpened()
        return self._instance

    def Open(self):
        print('Plik jest otwarty')

    def Close(self):
        print('Zamykam plik')
        from FileClosed import FileClosed
        fileClose = FileClosed()
        self._context.ChangeState(fileClose.GetInstance())

    def Read(self):
        print('Czytam Plik')

    def Write(self):
        print('Pisze do pliku')

    def SetContext(self, context):
        self._context = context