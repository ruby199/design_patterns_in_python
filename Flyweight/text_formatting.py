class FormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.caps = [False] * len(plain_text)

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True
    
    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            result.append(c.upper() if self.caps[i] else c)
        return ''.join(result)

class BetterFormattedText:
    def __init__(self, plain_text):
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        def __init__(self, start, end, capitalize=False, bold=False, italic=False):
            self.end = end
            self.bold = bold
            self.capitalize = capitalize
            self.italic = italic
            self.start = start

        def covers(self, position):
            return self.start <= position <= self.end

    
    def get_range(self, start, end):
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range # return so that people can modify it

    def __str__(self):
        result = []
        # Go over every single position
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            result.append(c)
        return ''.join(result)

if __name__ == '__main__':
    ft = FormattedText('This is a fantastic new world')
    ft.capitalize(10, 19)
    print(ft)


    bft = BetterFormattedText('This is a fantastic new world')
    bft.get_range(10, 19).capitalize = True
    print(bft)