
#  problem 5  
class Duration:
    def __init__(self, seconds: int): 
        self.seconds = seconds

    def __init__(self, minutes: int, seconds: int):
        self.seconds = minutes * 60 + seconds
        self.minutes = minutes

    def  __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = hours * 3600 + minutes * 60 + seconds
        self. hours = hours

    def __str__(self): return f"{self.hours}:{self.minutes:02d}:{self.seconds:02d}"

    def __repr__(self): return f"{self.hours} {self.minutes} {self.seconds}s"

__len__ = lambda self: self.seconds
__getitem__ = lambda self, unit: (
    self.hours if unit == "hours" else
    self.minutes if unit == "minutes" else
    self.seconds if unit == "seconds" else
    None
)

__bool__ = lambda self: bool(self.seconds)

__add__ = lambda self, other: Duration(0, 0, self.seconds + other.seconds)
__sub__ = lambda self, other: Duration(0, 0, self.seconds - other.seconds)
__mul__ = lambda self, factor: Duration(0, 0, self.seconds * factor)

a = Duration(1, 5, 9)
b = Duration(0, 59, 51)

print(a) #1:05:09
print(b) #0:59:51
print(repr(a)) #1 5 9s

print(len(a))
print(a(minutes))
print(bool(Duration()))
