from question import Ask, If, AND, OR
from rules import rules


class KnowledgeBase():
    def __init__(self, rules):
        self.rules = rules
        self.memory = {}

    def get(self, name):
        if ':' in name:
            k, v = name.split(':')
            vv = self.get(k)
            return 'y' if v == vv else 'n'
        if name in self.memory.keys():
            return self.memory[name]
        for fld in self.rules.keys():
            if fld == name or fld.startswith(name + ":"):
                # print(" + proving {}".format(fld))
                value = 'y' if fld == name else fld.split(':')[1]
                res = self.eval(self.rules[fld], field=name)
                if res != 'y' and res != 'n' and value == 'y':
                    self.memory[name] = res
                    return res
                if res == 'y':
                    self.memory[name] = value
                    return value
        # field is not found, using default
        res = self.eval(self.rules['default'], field=name)
        self.memory[name] = res
        return res

    def eval(self, expr, field=None):
        # print(" + eval {}".format(expr))
        if isinstance(expr, Ask):
            print(field)
            return expr.ask()
        elif isinstance(expr, If):
            return self.eval(expr.x)
        elif isinstance(expr, AND) or isinstance(expr, list):
            expr = expr.x if isinstance(expr, AND) else expr
            for x in expr:
                if self.eval(x) == 'n':
                    return 'n'
            return 'y'
        elif isinstance(expr, OR):
            for x in expr.x:
                if self.eval(x) == 'y':
                    return 'y'
            return 'n'
        elif isinstance(expr, str):
            return self.get(expr)
        else:
            print("Unknown expr: {}".format(expr))


kb = KnowledgeBase(rules)
print(kb.get("car"))
