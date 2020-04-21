import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        c = self.g
        if self.h == 1:
            d = c[0][0]
        else:
            d = (c[0][0]*c[1][1]- c[1][0]*c[0][1])
        
        return d
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        total = 0
        for i in range(self.h):
            total += self[i][i]
            
        return total            

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inverse = []
    
        # Check if not square
        if not self.is_square():
            raise ValueError('The matrix must be square')
    
        # Check if matrix is larger than 2x2.
        if self.h > 2:
            raise NotImplementedError('this functionality is not implemented')
    
        # Check if matrix is 1x1 or 2x2.
        # Depending on the matrix size, the formula for calculating
        # the inverse is different. 
        det = self.determinant()
        if det == 0:
            raise ValueError('The matrix is not invertible.')
        
        if self.h == 1:
            inverse = Matrix([[1/det]])
        elif self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
            inverse = 1/det * Matrix([[d, -b],[-c, a]])
            
    
        return inverse
      
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        a = self.g
        b = zeroes(self.w,self.h)
        for i in range(self.h):
            for j in range(self.w):
                b[j][i] = a[i][j]
                
        return b

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        c = []
        a = self.g
        b = other.g
        for i in range(self.h):
            c_row = []
            for j in range(self.w):
                c_ij = a[i][j] + b[i][j]
                c_row.append(c_ij)
            c.append(c_row)
            
        return Matrix(c)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        a = self.g
        b = []
        
        for i in range(self.h):
            b_row = []
            for j in range(self.w):
                b_ij = -1*a[i][j]
                b_row.append(b_ij)
            b.append(b_row)

        return Matrix(b)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
            
        a = self.g
        b = other.g
        c = []
        for i in range(self.h):
            c_row = []
            for j in range(self.w):
                c_ij = a[i][j] - b[i][j]
                c_row.append(c_ij)
            c.append(c_row)    
            
        return Matrix(c)
      
   
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise(ValueError, "Matrices cannot be multiplied")
        
        a = self.g
        b = other.g
        c = []
        
        for i in range(self.h):
            c_row = []
            for j in range(other.w):
                c_ij = 0
                for k in range(self.w):
                    c_ij += a[i][k]*b[k][j]
                c_row.append(c_ij)
            c.append(c_row)    

                
        return Matrix(c)
       
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
        
        a = self.g
        b = []
        for i in range(self.h):
            b_row = []
            for j in range(self.w):
                b_ij = other*a[i][j]
                b_row.append(b_ij)
            b.append(b_row)    
                
        return Matrix(b)
        
            