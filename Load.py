import csv
from decimal import Decimal
from re import sub

def Kolorado(N):
    file = open("Punkty/WielkiKanionKolorado.csv")
    csvreader = csv.reader(file)
    header= next(csvreader)
    x=[]
    y=[]
    all_x=[]
    all_y=[]
    n=0
    for row in csvreader:
        n+=1
        if n == N:
            x.append(Decimal(sub(r'[^\d.]', '', row[0]))) #konwersja na liczbe
            y.append(Decimal(sub(r'[^\d.]', '', row[1]))) #konwersja na liczbe
            n = 0
        all_x.append(Decimal(sub(r'[^\d.]', '', row[0])))  # konwersja na liczbe
        all_y.append(Decimal(sub(r'[^\d.]', '', row[1])))  # konwersja na liczbe

    return x, y,all_x,all_y
def Stale(N):
    file = open("Punkty/Stale.txt")
    csvreader = csv.reader(file)
    header= next(csvreader)
    x=[]
    y=[]
    all_x = []
    all_y = []
    n=0
    for row in csvreader:
        n+=1
        if n == N:
            x.append(Decimal(sub(r'[^\d.]', '', row[0]))) #konwersja na liczbe
            y.append(Decimal(sub(r'[^\d.]', '', row[1]))) #konwersja na liczbe
            n = 0
        all_x.append(Decimal(sub(r'[^\d.]', '', row[0])))  # konwersja na liczbe
        all_y.append(Decimal(sub(r'[^\d.]', '', row[1])))  # konwersja na liczbe

    return x, y,all_x,all_y
def Everest(N):
    file = open("Punkty/MountEverest.csv")
    csvreader = csv.reader(file)
    header= next(csvreader)
    x=[]
    y=[]
    all_x = []
    all_y = []
    n=0
    for row in csvreader:
        n+=1
        if n == N:
            x.append(Decimal(sub(r'[^\d.]', '', row[0]))) #konwersja na liczbe
            y.append(Decimal(sub(r'[^\d.]', '', row[1]))) #konwersja na liczbe
            n = 0
        all_x.append(Decimal(sub(r'[^\d.]', '', row[0])))  # konwersja na liczbe
        all_y.append(Decimal(sub(r'[^\d.]', '', row[1])))  # konwersja na liczbe

    return x, y,all_x,all_y
