#Task10
class Rectangle():
    def __init__(a, l, w):
        a.len = l
        a.wid  = w

    def RectangleArea(a):
        return a.len*a.wid

newRectangle = Rectangle(5,6)
print(newRectangle.RectangleArea())