class Font:
    def __init__(self, color=-1, name="", size=0):
        self.color = color
        self.name = name
        self.size = size


class RepStr:
    def __init__(self, str="", color=-1, name="", size=0):
        self.str = str
        self.font = Font(color, name, size)


    def from_font(self,str="",font=Font()):
        return RepStr(str,font.color,font.name,font.size)