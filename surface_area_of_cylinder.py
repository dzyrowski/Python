# r = 1 h = 1 SA = 12.57
# r = 5 h = 15 SA = 628.32

#SA = 2 pi r h + 2 pi r squared 

#import math library
import math

#function for getting Surface area of right cylinder 
# 2 * pi * radius * height + 2 pi radius squared
def surface_area_cylinder(radius, height):
    SA = (2 * math.pi * radius * height) + (2 * math.pi * radius ** 2)
    return SA
    
print(abs(surface_area_cylinder(1, 1) - 12.57) < .01 )
print(abs(surface_area_cylinder(5, 15) - 628.32) < .01 )

r = float(input("Enter radius: "))
h = float(input("Enter height; "))


print(surface_area_cylinder(r, h))

