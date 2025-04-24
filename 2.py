class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.line = ""

    def add_word(self, word):
        if not self.line:
            self.line = word
        elif len(self.line) + 1 + len(word) <= self.width:
            self.line += " " + word
        else:
            print(self.line)
            self.line = word

    def end(self):
        if self.line:
            print(self.line)
            self.line = ""

class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.line = ""

    def add_word(self, word):
        if not self.line:
            self.line = word
        elif len(self.line) + 1 + len(word) <= self.width:
            self.line += " " + word
        else:
            print(self.line.rjust(self.width))
            self.line = word

    def end(self):
        if self.line:
            print(self.line.rjust(self.width))
            self.line = ""
