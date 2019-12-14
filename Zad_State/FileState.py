from abc import ABC

class FileState(ABC):
    def Open(self):
        pass

    def Close(self):
        pass

    def Read(self):
        pass

    def Write(self):
        pass

    def SetContext(self, context):
        pass
