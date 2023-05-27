from SolveMethod import *

def Polynomial(x,coefficients):
    otp=0
    for i in range(len(coefficients)):
        if i != 0:
            otp += coefficients[i] * (x**i)
        else:
            otp = coefficients[i] + otp
    return otp
def SplinePolynomial(x,x_n,coefficients):
    otp=0
    h=x-x_n
    for i in range(len(coefficients)):
        if i != 0:
            otp += coefficients[i] * (h**i)
        else:
            otp = coefficients[i] + otp
    return otp

def GetSplineCoefficient(coefficients):
    splineCofficients=[]
    for i in range(int(len(coefficients)/4)):
        splineCofficients.append(coefficients[:4])
        coefficients=coefficients[4:]
    return splineCofficients



def LaGrange(x, y, N):
    '''
    :param N: liczba punktów dodatkowych pomiędzy każdą parą sąsiednich
    :return:
    '''
    N +=1 # bo trzeba podzielić na N+1 części by było N punktów pomiedzy
    size = len(x)
    matrix = Matrix(size,size)
    vector = Matrix(size,1)

    #  Przypisanie wartości w macierzy i wektorze
    for i in range(size):
        for j in range(size):
            matrix[i][j] = x[i]**j
        vector[i] = y[i]

    coefficients = Gauss(matrix, vector)  # rozwiązanie układu równań


    x_interpolated = []
    y_interpolated = []
    for i in range(size-1):
        x_interpolated.append(x[i])  # dodanie oryginalnych punktów
        y_interpolated.append(y[i])
        dist = x[i + 1] - x[i]  # odległość pomiędzy dwoma oryginalnymi punktami
        for j in range(1,N):
            x_temp = x[i]+dist * j / N
            x_interpolated.append(x_temp)  # dodanie interpolowoanych punktów
            y_interpolated.append(Polynomial(x_temp,coefficients))
    x_interpolated.append(x[size-1])
    y_interpolated.append(y[size-1])
    return x_interpolated,y_interpolated


def FillSplinesMatrix(matrix,vector,x,y):
    splinesNumb = len(x) - 1
    size = splinesNumb * 4
    #warunki na wartość
    for i in range(0,splinesNumb):#kazdy spline

        matrix[2*i][4*i] = 1  #S_n(x_n)=f(x_n)
        vector[2*i + 0] = y[i]

        h = x[i+1]-x[i]  # odległość pomiędzy punktami
        for j in range(4): #4 kolumny
            matrix[i*2+1][i*4 + j] = h ** j  #S_n(x_n+1)=f(x_n+1)
        vector[2*i + 1] = y[i+1]

    ofst=splinesNumb * 2
    for i in range(1,splinesNumb):#kazdy punkt wewnatrz
        h = x[i + 1] - x[i]  # odległość pomiędzy punktami
        # S_n'(x_n+1)=S_n+1'(x_n+1)
        matrix[ofst + 2*(i-1)][4*i - 4] = 0  #a
        matrix[ofst + 2*(i-1)][4*i - 3] = 1  #b0
        matrix[ofst + 2*(i-1)][4*i - 2] = 2*h  #c
        matrix[ofst + 2*(i-1)][4*i - 1] = 3*h**2  #d

        matrix[ofst + 2*(i-1)][4*i + 1] = -1  #b1

        vector[ofst + 2*(i-1) + 0] = 0

        # S_n''(x_n+1)=S_n+1''(x_n+1)
        matrix[ofst + 2 * (i-1) + 1][4 * i - 4] = 0  # a
        matrix[ofst + 2 * (i-1) + 1][4 * i - 3] = 0  # b0
        matrix[ofst + 2 * (i-1) + 1][4 * i - 2] = 2  # c
        matrix[ofst + 2 * (i-1) + 1][4 * i - 1] = 6 * h  # d

        matrix[ofst + 2 * (i-1) + 1][4 * i + 2] = -2  # b1

        vector[ofst + 2 * (i-1) + 1] = 0

    #ostatnie 2 warunki na krawedziach
    #lewa
    i=size-2
    matrix[i][0] = 0  # a
    matrix[i][1] = 0  # b0
    matrix[i][2] = 2  # c
    matrix[i][3] = 0 # d

    i = size - 1
    h = x[len(x)-1] - x[len(x)-2]
    #prawa
    matrix[i][size - 4] = 0  # a
    matrix[i][size - 3] = 0  # b0
    matrix[i][size - 2] = 2  # c
    matrix[i][size - 1] = 6*h  # d


def Splines(x, y, N):

    splinesNumb = len(x)-1
    N += 1  # bo trzeba podzielić na N+1 części by było N punktów pomiedzy
    size = splinesNumb * 4
    matrix = Matrix(size, size)
    vector = Matrix(size, 1)

    FillSplinesMatrix(matrix,vector,x,y)

    coefficients = GaussNorm1(matrix, vector)  # rozwiązanie układu równań
    splineCoefficients = GetSplineCoefficient(coefficients)  # wydobycie poszczególnych współczynników


    x_interpolated = []
    y_interpolated = []
    for i in range(len(x)-1):
        x_interpolated.append(x[i])  # dodanie oryginalnych punktów
        y_interpolated.append(y[i])
        dist = x[i + 1] - x[i]  # odległość pomiędzy dwoma oryginalnymi punktami
        for j in range(1, N):
            x_temp = x[i] + dist * j / N
            x_interpolated.append(x_temp)  # dodanie interpolowoanych punktów
            y_interpolated.append(SplinePolynomial(x_temp,x[i], splineCoefficients[i]))
    x_interpolated.append(x[len(x) - 1])
    y_interpolated.append(y[len(x) - 1])
    return x_interpolated, y_interpolated