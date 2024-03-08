class Rectangle:
    def __init__(self, side1:int, side2:int) -> None:
        if type(side1) not in [int, float] or type(side2) not in [int, float]:
            raise TypeError('sides must be an integer or float')
        if side1 < 0 or side2 < 0:
            raise ValueError("Side lengths must be positive")
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1*self.side2
    
    def perimeter(self):
        return (self.side1+self.side2)*2


class Square:
    def __init__(self, length) -> None:
        if type(length) not in [int, float]:
            raise TypeError('Length must be an integer or float')
        if length < 0:
            raise ValueError("Length must be positive")
        self.length = length

    def area(self):
        return self.length**2
    
    def perimeter(self):
        return self.length*4


if __name__ == "__main__":

    mysquare = Square(4)
    print(mysquare.area())
    print(mysquare.length)
