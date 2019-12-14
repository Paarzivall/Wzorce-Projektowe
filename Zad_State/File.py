from FileClosed import FileClosed


class File(object):
    def __init__(self):
        self.FileClosed = FileClosed()
        self._state = self.FileClosed.GetInstance()
        self._state.SetContext(self)

    def Open(self):
        self._state.Open()

    def Close(self):
        self._state.Close()

    def Write(self):
        self._state.Write()

    def Read(self):
        self._state.Read()

    def ChangeState(self, state):
        self._state = state
        self._state.SetContext(self)