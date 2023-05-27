import math
import copy
from decimal import Decimal

class Row():
    def __init__(self, length):
        self.length = length
        self.values = [0]*length

    def SetValues(self, array):
        for i in range(self.length):
            self.values[i]=array[i]


    def __add__(self, other):
        result = Row(self.length)
        if type(other) == int or type(other) == float or type(other) == Decimal:
            if self.length == 1:
                result = self.values[0] + other
            else:
                for i in range(self.length):
                    result = self.values[i] + other
        else:
            for i in range(self.length):
                result = self.values[i] + other[i]
        return result

    def __iadd__(self, other):
        result = Row(self.length)
        if type(other) == int or type(other) == float or type(other) == Decimal:
            if self.length == 1:
                result = self.values[0] + other
            else:
                for i in range(self.length):
                    result = self.values[i] + other
        else:
            for i in range(self.length):
                result = self.values[i] + other[i]
        return result

    def __sub__(self, other):
        result = Row(self.length)
        if type(other) == int or type(other) == float or type(other) == Decimal:
            if self.length == 1:
                result = self.values[0] - other
            else:
                for i in range(self.length):
                    result = self.values[i] - other
        else:
            for i in range(self.length):
                result = self.values[i] - other[i]
        return result


    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __mul__(self, other):
        result = Row(self.length)
        if type(other) == int or type(other) == float or type(other) == Decimal:
            if self.length == 1:
                result = self.values[0] * Decimal(other)
            else:
                for i in range(self.length):
                    result = self.values[i]*other
        else:
            for i in range(self.length):
                result = self.values[i]*other[i]
        return result

    def __truediv__ (self, other):
        result = Row(self.length)
        if type(other) == int :
            if self.length == 1:
                result = self.values[0] / other
            else:
                for i in range(self.length):
                    result = self.values[i]/other
        else:
            for i in range(self.length):
                result = self.values[i]/other[i]
        return result

    def __str__(self):
        return self.values.__str__()

class Matrix():
    def __init__(self, rows,cols):
        self.rows = rows
        self.cols = cols
        self.values = []
        for i in range(rows):
            self.values.append(Row(cols))

    def SetValues(self,val):
        for row in range(self.rows):
            for col in range(self.cols):
                self.values[row][col]=val

    def SetIdentity(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if(col == row):
                    self.values[row][col]=1
                else:
                    self.values[row][col] = 0

    def SetDiagonal(self, a1, a2, a3):
        temp = [a3, a2, a1, a2, a3]
        for row in range(self.rows):
            for j in range(len(temp)):
                if 0 <= row + j - 2 < self.rows:
                    self.values[row][row + j - 2] = temp[j]
    def SetSinValues(self,f):
        for row in range(self.rows):
            for col in range(self.cols):
                self.values[row][col] = math.sin(row*(f+1))
    def GetDiagonal(self):
        # unused
        diag = copy.deepcopy(self)
        for i in range(self.rows):
            for j in range(self.rows):
                if i != j:
                    diag.values[i][j] = 0
        return diag

    def GetUpperTriangle(self):
        # unused
        upper = copy.deepcopy(self)
        for i in range(self.rows):
            for j in range(self.rows):
                if i > j:
                    upper.values[i][j] = 0
        return upper

    def GetLowerTriangle(self):
        #unused
        lower = copy.deepcopy(self)
        for i in range(self.rows):
            for j in range(self.rows):
                if i < j:
                    lower.values[i][j] = 0
        return lower

    def GetInverse(self):
        #unused
        return []

    def GetNorm(self):
        norm=0
        for i in range(self.rows):
            for j in range(self.cols):
                norm += self.values[i][j]**2
        return math.sqrt(norm)

    def GetNorm1(self):
        norm = 0
        for i in range(self.rows):
            for j in range(self.cols):
                norm += abs(self.values[i][j])
        return norm

    def __mul__(self, other ):
        result=Matrix(self.rows,other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum = 0
                for k in range(self.cols):
                    sum+=self.values[i][k]*other.values[k][j]
                result.values[i][j]=sum
        return result

    def __add__(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.values[i][j]=self.values[i][j]+other.values[i][j]
        return result


    def __iadd__(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.values[i][j]=self.values[i][j]+other.values[i][j]
        return result

    def __sub__(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.values[i][j] = self.values[i][j] - other.values[i][j]
        return result

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        if type(value) == Row:
            self.values[key] = value
        elif type(value) == int or type(value) == float or type(value) == Decimal:
            row = Row(1)
            row.SetValues([value])
            self.values[key] = row
        else:
            row = Row(len(value))
            row.SetValues([value])
            self.values[key] = row

    def __len__(self):
        '''zwraca liczbę wierszy!'''
        return len(self.values)
    def __str__(self):
        for i in range(self.rows):
            print(self.values[i])
        return ''