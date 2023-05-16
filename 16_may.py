'''
Create a program for me to caculate the cost neded for the columns errected for a new building
the base of the column can be either a square/circle/triangle in shape The user is supposed to enter the height as well as the number of columns
each column for circle will cost 156 * h * area * n
each column for square will cost 107 * h * area * n
each column for triangle will cost 246 * h * area * n
create new variable to input for the areas of the different shapes
def colomn(n,s) where n is the number of columns and s is the shape
 '''
 
from math import pi 
def column(n,s):
    def circle(n):
        radius = int(input("Enter the radius of your circle: \n"))
        height = int(input("Enter the height of each column: \n"))
        area = math.pi * radius * radius
        ccost = 156 * height * area * n
        return f"The cost for your new building is {ccost}"
        
    def square(n):
        length = int(input("Enter the radius of your circle: \n"))
        height = int(input("Enter the height of each column: \n"))
        area = length * height
        scost = 107 * height * area * n
        return f"The cost for your new building is {scost}"
        
    def triangle(n):
        length = int(input("Enter the radius of your circle: \n"))
        height = int(input("Enter the height of each column: \n"))
        area = 0.5 * length * height
        tcost = 246 * height * area * n
        return f"The cost for your new building is {tcost}"
        
    if (s == Triangle) or (s == triangle):
        triangle(n)
        
    if (s == Square) or (s == square):
        square(n)
        
    if (s == Circle) or (s == circle):
        circle(n)
        
    else:
        print("Invalid :(")
        
        
        
