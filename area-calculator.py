import math

area = (input("Area calculator. Enter R for Rectagle, C for Circle or T for Triangle "))

if area == 'C':
    radius = float(input("Please enter the radius: "))
    total = 3.14159 * radius ** 2
    print(f"The area of your Circle is {total:.2f}" )
if area == 'R':
    lenght = float(input("Please enter length: "))
    width = float(input("Please enter width: "))
    totalR = lenght * width
    print(f"The area of your rectangle is {totalR:.2f}")
if area == 'T':
    base = float(input("Please enter base: "))
    height = float(input("Please enter height: "))
    areaT = 1 / 2 * base * height
    print(f"The area of your Triangle is {areaT:.2f}" )