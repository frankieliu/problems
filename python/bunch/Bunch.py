
"""
https://stackoverflow.com/questions/2827623/how-can-i-create-an-object-and-add-attributes-to-it

https://stackoverflow.com/questions/2827623/how-can-i-create-an-object-and-add-attributes-to-it
"""


class BunchDict(dict):
    def __init__(self, **kw):
        dict.__init__(self, kw)
        self.__dict__ = self


class Pass(object):
    pass


if __name__ == "__main__":
    b = BunchDict()
    b.a = 1
    b.b = 2
    print(b)

    import types
    c = types.SimpleNamespace()
    c.a = 1
    c.b = 1
    print(c)

    p = Pass()
    p.a = 1
    p.b = 2
    print(p.a)

    # You can set arbitrary attributes to lamda functions in python
    l = lambda: None
    setattr(l, 'a', 1)
    print(l.a)
