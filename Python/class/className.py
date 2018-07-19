#https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance-in-python

class Spam:
    def meth(self):
        pass
    class Bar:
        pass

>>> s = Spam()
>>> type(s).__name__
'Spam'
>>> type(s).__qualname__
'Spam'
>>> type(s).Bar.__name__       # type not needed here
'Bar'
>>> type(s).Bar.__qualname__   # type not needed here
'Spam.Bar'
>>> type(s).meth.__name__
'meth'
>>> type(s).meth.__qualname__
'Spam.meth'
