class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.eventList = [0]
        self.index = 1
        self.redoAmount = 0

    def add(self, num: int):
        self.value += num
        self.eventList = self.eventList[:self.index]
        self.eventList.append(self.value)
        self.index += 1
        self.redoAmount = 0
        pass

    def subtract(self, num: int):
        self.value -= num
        self.eventList = self.eventList[:self.index]
        self.eventList.append(self.value)
        self.index += 1
        pass

    def undo(self):
        if self.index > 1:
            self.index -= 1
            self.value = self.eventList[self.index-1]
            self.redoAmount += 1
        pass

    def redo(self):
        if self.redoAmount > 0:
            self.index += 1
            self.value = self.eventList[self.index-1]
            self.redoAmount -= 1
        pass

    def bulk_undo(self, steps: int):
        if self.index > steps:
            self.index -= steps
            self.value = self.eventList[self.index-1]
            self.redoAmount += steps
        else:
            self.redoAmount = self.index-1
            self.index = 1
            self.value = self.eventList[self.index-1]
        pass

    def bulk_redo(self, steps: int):
        if self.redoAmount > steps-1:
            self.index += steps
            self.value = self.eventList[self.index-1]
            self.redoAmount -= steps
        else:
            self.index += self.redoAmount
            self.value = self.eventList[self.index-1]
            self.redoAmount = 0
        pass