from Mediator import Mediator


class WindowMediator(Mediator):
    def __init__(self, checkbox1, checkbox2, checkbox3):
        self.checkbox1 = checkbox1
        self.checkbox2 = checkbox2
        self.checkbox3 = checkbox3

    def Notify(self, action):
        if action == '1':
            if not self.checkbox1.Checked:
                self.checkbox1.Checked = True
            else:
                self.checkbox1.Checked = False
                self.checkbox2.Checked = False
                self.checkbox3.Checked = False
        elif action == '2':
            if not self.checkbox2.Checked:
                self.checkbox1.Checked = True
                self.checkbox2.Checked = True
            else:
                self.checkbox2.Checked = False
                self.checkbox3.Checked = False
        elif action == '3':
            if not self.checkbox3.Checked:
                self.checkbox1.Checked = True
                self.checkbox2.Checked = True
                self.checkbox3.Checked = True
            else:
                self.checkbox3.Checked = False
