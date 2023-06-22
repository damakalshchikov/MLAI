class Ask():
    def __init__(self, choices=['y', 'n']):
        self.choices = choices

    def ask(self):
        if max([len(x) for x in self.choices]) > 1:
            for i, x in enumerate(self.choices):
                print("{0}. {1}".format(i, x), flush=True)
            x = int(input())
            return self.choices[x]
        else:
            print("/".join(self.choices), flush=True)
            return input()


class Content():
    def __init__(self, x):
        self.x = x


class If(Content):
    pass


class AND(Content):
    pass


class OR(Content):
    pass
