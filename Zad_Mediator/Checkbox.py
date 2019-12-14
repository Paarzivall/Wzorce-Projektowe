from Component import Component


class Checkbox(Component):
    def __init__(self, action, label):
        self.action = action
        self.label = label
        self.Checked = False

    def __str__(self):
        if self.Checked:
            return f'{self.label}: X'
        else:
            return f'{self.label}:  '

    def Check(self):
        return self._mediator.Notify(self.action)
