import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print(self):
        print self.x, self.y

    def distance(self,other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Circle:
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius

    def in_circle(self,point):
        return self.center.distance(point) < self.radius

    def cirumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius**2

    def move(self,dx,dy):
        self.center.x += dx
        self.center.y += dy

    def strech(self, dr):
        self.radius *= dr
