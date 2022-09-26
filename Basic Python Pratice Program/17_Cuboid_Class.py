#    ------------ For Circle Class -------------------



# class circle:
#     def __init__ (self,radius):
#         self.radius = radius
    
#     def area(self,radius):
#         return 3.14*self.radius*self.radius
#     def circum(self,radius):
#         return 2*3.14*self.radius

# radius = int(input("Enter Radius of Circle "))
# cir1= circle(radius)
# print(cir1.area(radius))
# print(cir1.circum(radius))


# ------------------ For Cubiod Class --------------------
class cubiod:
    def __init__ (self,length,width,height):
        self.length = length
        self.width = width
        self.height = height
    
    def volume(self,length,width,height):
        return length*width*height
    def total_surface_area(self,length,width,height):
        return (2*length*width) + (2*length*height) + (2*height*width)

length= float(input("Enter Length  of Cubiod : "))
width= float(input("Enter Width  of Cubiod : "))
height= float(input("Enter Height  of Cubiod : "))

#  Creating Object
cube1= cubiod(length,width,height)
print(" Volume of Cubiod is : ",cube1.volume(length,width,height))
print(" Total Surface Area  of Cubiod is : ",cube1.total_surface_area(length,width,height))



