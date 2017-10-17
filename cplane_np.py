me: Aly Baughman, Cynthia Parks
# Student ID: 1923165, 2303535
# Email: baugh107@mail.chapman.edu, cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 6
###

from abscplane import AbsComplexPlane
import numpy as np
import pandas as pd

class ArrayComplexPlane(AbsComplexPlane):
    """Complex Plane Creation
    $ python
    >>> import cplane
    >>> help(cplane)
    The ListComplexPlane class is meant to create a nested list grid of complex numbers.  It initializes with the min and max points
    of both axis, their lengths, the plane of points, and an empty list of functions applied to said points.  It contains functions
    to refresh and zoom in the grid, a function to create the plane itself, and a function to apply mathematical functions to the points.
    """

from abscplane import AbsComplexPlane

class ArrayComplexPlane(AbsComplexPlane):
    """This class creates a complex plane and uses different functions to edit the plane.
     Attributes:
        xmax (float) : maximum horizontal axis value
        xmin (float) : minimum horizontal axis value
        xlen (int)   : number of horizontal points
        ymax (float) : maximum vertical axis value
        ymin (float) : minimum vertical axis value
        ylen (int)   : number of vertical points
        plane        : stored complex plane implementation
        fs (list[function]) : function sequence to transform plane
    """
    #initializing the attributes
    def __init__(self, xmin, xmax, xlen, ymin, ymax, ylen):
        """The class constructor that initializes the complex plane
        
        Args:
            xmin (float): Minimum x value
            xmax (float): Maximum x value
            xlen (int): Number of horizontal points
            ymin (float): Minimum y value
            ymax (float): Maximum y value
            ylen (int): Number of vertical points
        """
        self.xmin = float(xmin)
        self.xmax = float(xmax)
        self.xlen = int(xlen)
        self.ymin = float(ymin)
        self.ymax = float(ymax)
        self.ylen = int(ylen)
        self.plane = self.__create_plane(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)
        self.fs = []
        
    ##creates plane of complex points    
    def __create_plane(self, xmin, xmax, xlen, ymin, ymax, ylen):
       
        """This function creates a list of lists that contains the points for the complex plane.  It does so by
           starting at the minimum point, and moves towards the maximum point in equal intervals based on the xlen
           and ylen values.
        
        Args:
            xmin (float): Minimum x value
            xmax (float): Maximum x value
            xlen (int): Number of horizontal points
            ymin (float): Minimum y value
            ymax (float): Maximum y value
            ylen (int): Number of vertical points
        Returns:
            plane[]: The list of complex points
        """
        
        #Gives us evenly spaced numbers over the min/max intervals for x and y
        xp = np.linspace(self.xmin, self.xmax, self.xlen)
        yp = np.linspace(self.ymin, self.ymax, self.ylen)
        
        #returns coordinate matrices from coordinate vectors
        x,y = np.meshgrid(xp,yp)
        
        #creates complex plane using vectors from meshgrid
        self.plane = x + y*1j
        
        print(self.plane)
        
        return self.plane
                
        
    
    def refresh(self):
        """Regenerates the complex plane and replaces all the attribute values.  
           It also removes any functions stored in the attribute fs.
        """
        self.plane = self.__create_plane(self, xmin, xmax, xlen, ymin, ymax, ylen)
        self.fs = []

    def apply(self, f):
        """Adds a function f to the attribute fs.  Then it applies that function to every
           point in the plane.
        """

        #adds f to fs
        self.fs.append(f)
        
        self.plane = f(self.plane)
        return self.plane
        
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """Resets the x and y attributes and recreates the plane with new x and y values.
        Then it goes through all the transformations in fs and applies them in order to 
        the new values.
        """
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        
        self.plane = self.__create_plane(self.xmin, self.xmax, self.xlen, self.ymin, self.ymax, self.ylen)
        #applies the transformations in fs in order
        for f in self.fs:
            self.apply(f)
            
        return self.plane    
