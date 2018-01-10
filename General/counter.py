class Counter :
    value = 0

    def set(self,value):
        self.value = value

    def up(self):
        self.value = self.value + 1

    def down(self):
        self.value = self.value - 1

count = Counter()

set,up,down = count.up, count.up,count.down


