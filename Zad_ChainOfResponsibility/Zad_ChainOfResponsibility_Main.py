from Application import Application
from Dialog import Dialog
from Button import Button


if __name__ == '__main__':
    anApplication = Application()
    aSaveDialog = Dialog()
    aPrintDialog = Dialog()
    aPrintButton = Button()
    anOkButton = Button()

    anOkButton.SetSuccesor(aPrintDialog)
    aPrintButton.SetSuccesor(aPrintDialog)
    aPrintDialog.SetSuccesor(anApplication)
    aSaveDialog.SetSuccesor(anApplication)

    anOkButton.HandleHelp()
    print("\n")
    aPrintButton.HandleHelp()
    print("\n")
    aSaveDialog.HandleHelp()