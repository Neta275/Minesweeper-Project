# -*- coding: utf-8 -*-
"""
Student: Netanel Azoviv
ID: 313152209
Assignment no. 6
Program: lines.py
"""

class Point: # a point in the plan
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self._x},{self._y})"

   

    @property
    def x(self): #function that get x
        return self.__x

    @x.setter
    def x(self, Value):#function that set the x
         if(not isinstance(Value,int)):
             raise Exception("not an integer")
         if Value < 0:
            raise Exception("negative number")
         self.__x = Value

    @property
    def y(self):#function that get y
        return self.__y

    @y.setter
    def y(self, Value): #function that set the y
        if (not isinstance(Value,int)):
            raise Exception("not an integer")
        self.__y = Value

class Line(): # a Line in the plane
    def __init__(self, point1, point2):
        if not isinstance(point1,Point):
            raise ValueError("this is not a Point",point1)
        self.point1 = point1
        if not isinstance(point2,Point):
            raise ValueError("this is not a Point",point2)
        self.point2 = point2


    @property
    def point1(self):#function gets point1
        return self.__point1

    @point1.setter
    def point1(self, Value):#function sets the point1
        self.__point1 = Value

    @property
    def point2(self):#function gets point2
        return self.__point2

    @point2.setter
    def point2(self, Value): #function sets the point2

        self.__point2 = Value
    def is_vertical(self):#function return true if line is vertical
        if self.point1.x==self.point2.x:
            return True
        return False
    def slope(self): # function return the slope of the given line
        if self.is_vertical():
            return None
        return (self.point2.y-self.point1.y)/(self.point2.x-self.point1.x)
    def y_intersect(self): #function returns the intersect with y
        if self.is_vertical():
            return None
        return self.slope()*(-self.point1.x)+self.point1.y
    
        
    def __str__(self):
        b=self.slope()
        if self.is_vertical():
            return f'(x={self.point1.x})'
        return f'y={b}x+{b*self.point1.x}+{self.point1.y}'
        
        
    def parallel(self,other):# function returns true if 2 lines are parallel
        if self.slope()==other.slope:
            return True
        return False

    def equals(self,other):#return if 2 lines are equal
        return self.__str__()==other.__str__()
    def intersection(self,other):
       #the function return intersection between 2 lines
       if self.parallel(other)==True:
           return 1
       if self.y_intersect()==None:
           return 2
       if other.y_intersect()==None:
           return 3
       x=(other.y_intersect()-self.y_intersect())/(self.slope()-other.slope())
       y=self.slope()*x+self.y_intersect()
       return "(%.2f,%.2f)"%(x,y)    
def main():
    f=open("input4.txt","r")
    f=f.read().split("\n")
    f=[i.split() for i in f if len(i)>=1] #split every line in the file to sublist
    f=[[(f[i][0],f[i][1]),(f[i][2],f[i][3])] for i in range(len(f))] # making the list into pairs (x,y)
    sub=[]
    for i in range(len(f)):  

          if f[i][0][0].isalpha() or f[i][1][0].isalpha():
              sub.append("xError")
          elif f[i][0][1].isalpha() or f[i][1][1].isalpha():
             sub.append("yError")
          else:
              x1=Point(float(f[i][0][0]),float(f[i][0][1]))
              x2=Point(float(f[i][1][0]),float(f[i][1][1]))
              y=Line(x1,x2)
              sub.append(y)
    s=open("output4444.txt","w")  
    for i in range(len(sub)): 
        
        if sub[i]=="xError":
            s.write(f"Line {i+1} error: x coordinate must be a number\n\n")
            continue
        if sub[i]=="yError":
            s.write(f"Line {i+1} error: x coordinate must be a number\n\n")
            continue
        else:
            s.write(f"Line {i+1}: "+str(sub[i]))
            s.write("\n")
            for x in range(i):
                if type(sub[x])==str:
                    s.write(f"line {i+1} cant calculate intersections with line {x+1}\n")
                    continue
                if sub[i].intersection(sub[x])==1:
                    s.write(str(f"Line {i+1} is parallel to line {x+1}")) 
                elif sub[i].intersection(sub[x])==2:
                    s.write("line %d with line %d: (%.2f,%.2f)"%(i+1,x+1,sub[i].q.x,sub[x].slope()*(sub[i].q.x)+sub[x].y_intersect()))
                elif sub[i].intersection(sub[x])==3:
                    s.write("line %d with line %d: (%.2f,%.2f)"%(i+1,x+1,sub[x].q.x,sub[i].slope()*(sub[x].q.x)+sub[i].y_intersect()))
                else:   
                    s.write(f"Line {i+1} with line {x+1}: {sub[i].intersection(sub[x])}")
                
                s.write("\n")
        s.write("\n")
          
main()
