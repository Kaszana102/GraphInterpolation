from MatrixClass import *


def Pivot(matrix,vector):
    for i in range(matrix.rows):
        highestIndex = i
        for j in range(i,matrix.rows):
            if(abs(matrix[j][i]) > abs(matrix[highestIndex][i])):
                highestIndex = j

        #swap
        temp = matrix[i]
        matrix[i] = matrix[highestIndex]
        matrix[highestIndex] = temp

        temp = vector[i]
        vector[i] = vector[highestIndex]
        vector[highestIndex] = temp


def ZeroLower(matrix,vector):
    for i in range(matrix.rows): #po przekątnej
        for j in range(i+1, matrix.rows): #idąc w dół
            if(matrix[i][i] != 0):
                numb = matrix[j][i] / matrix[i][i]
                for k in range(i,matrix.rows): #aktualizacja wiersza
                    matrix[j][k] -= Decimal(matrix[i][k]*numb)
                vector[j] -= vector[i]*numb


def Jacoby(matrix,vector):
    Pivot(matrix, vector)

    result = Matrix(matrix.rows, 1) #utworzenie wektora rozwiązań
    result.SetValues(1) #inicjalizacja jako same jedynki
    n = len(result)
    iterations = 0
    while (matrix * result - vector).GetNorm() > 10 ** -9 and iterations<400: #warunek na oczekiwaną dokładność, lub odgórną liczbę iteracji
        iterations += 1
        for i in range(n):
            sum = 0
            for j in range(n): #liczenie sumy
                if i != j:
                    sum += result[j] * matrix[i][j]
            result[i] = -1 / matrix[i][i] * sum + vector[i]/matrix[i][i] #aktualizacja szukanej wartości
    return result

def Gauss(matrix,vector):

    Pivot(matrix,vector)
    ZeroLower(matrix,vector)

    result = Matrix(matrix.rows, 1) #utworzenie wektora rozwiązań
    result.SetValues(1) #inicjalizacja jako same jedynki
    n=len(result)
    iterations = 0
    while (matrix * result - vector).GetNorm() > 10 ** -9 and iterations<400:
        iterations+=1
        for i in range(n):
            sum1=0
            sum2=0
            for j in range(i): #liczenie sumy1
                sum1 += result[j] * matrix[i][j]
            for j in range(i+1,n): #liczenie sumy2
                sum2 += result[j] * matrix[i][j]
            result[i] = 1/matrix[i][i] * (vector[i] - sum1 - sum2) #aktualizacja szukanej wartości

    return result


def GaussNorm1(matrix,vector):

    Pivot(matrix,vector)
    ZeroLower(matrix,vector)

    result = Matrix(matrix.rows, 1) #utworzenie wektora rozwiązań
    result.SetValues(1) #inicjalizacja jako same jedynki
    n=len(result)
    iterations = 0
    while (matrix * result - vector).GetNorm1() > 10 ** -3 and iterations<400:
        iterations+=1
        for i in range(n):
            sum1=0
            sum2=0
            for j in range(i): #liczenie sumy1
                sum1 += result[j] * matrix[i][j]
            for j in range(i+1,n): #liczenie sumy2
                sum2 += result[j] * matrix[i][j]
            result[i] = Decimal(1/matrix[i][i]) * Decimal(vector[i] - sum1 - sum2) #aktualizacja szukanej wartości

    return result

def LU(matrix,vector):
    result=[]

    U=matrix #kopiowanie macierzy wejściowej
    L=Matrix(matrix.rows,matrix.cols) #utworzenie macierzy L
    L.SetIdentity() #ustawienie jako macierzy jednostkowej

    n=len(vector)
    for k in range(n):
        for j in range(k+1,n):
            L[j][k]=U[j][k]/U[k][k]
            for l in range(k,n):
                U[j][l]-= L[j][k]*U[k][l]
    return U