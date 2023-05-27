import Load
from Interpolations import *
import matplotlib.pyplot as plt
import numpy as np



def Kolorado(N):
    x_raw, y_raw,all_x,all_y = Load.Kolorado(N)


    plot1 = plt.subplot2grid((2, 1), (0, 0))
    plot2 = plt.subplot2grid((2, 1), (1, 0))

    plot1.scatter(all_x, all_y, color='r', label="all measured", marker="o")
    plot2.scatter(all_x, all_y, color='r', label="all measured")
    plot1.scatter(x_raw, y_raw, color='g', label="taken", marker="o")
    plot2.scatter(x_raw, y_raw, color='g', label="taken")

    x, y = LaGrange(x_raw, y_raw, 3)
    plot1.plot(x, y, color='b', label="interpolated")
    plot1.set_xlabel("x")
    plot1.set_ylabel("y")
    plot1.set_title("Kolorado")
    plot1.grid()
    plot1.legend()

    x, y = Splines(x_raw, y_raw, 10)
    plot2.plot(x, y, color='b', label="splines")
    plot2.legend()
    plot2.grid()
    plot2.set_xlabel("x")
    plot2.set_ylabel("y")
    plot2.set_title("Kolorado")




    plt.show()
def Stale(N):
    x_raw, y_raw,all_x,all_y = Load.Stale(N)


    plot1 = plt.subplot2grid((2, 1), (0, 0))
    plot2 = plt.subplot2grid((2, 1), (1, 0))

    plot1.scatter(all_x, all_y, color='r', label="all measured", marker="o")
    plot2.scatter(all_x, all_y, color='r', label="all measured")
    plot1.scatter(x_raw, y_raw, color='g', label="taken", marker="o")
    plot2.scatter(x_raw, y_raw, color='g', label="taken")

    x, y = LaGrange(x_raw, y_raw, 3)
    plot1.plot(x, y, color='b', label="interpolated")
    plot1.set_xlabel("x")
    plot1.set_ylabel("y")
    plot1.set_title("Stałe")
    plot1.grid()
    plot1.legend()

    x, y = Splines(x_raw, y_raw, 10)
    plot2.plot(x, y, color='b', label="splines")
    plot2.legend()
    plot2.grid()
    plot2.set_xlabel("x")
    plot2.set_ylabel("y")
    plot2.set_title("Stałe")

    plt.show()


def Everest(N):
    x_raw, y_raw,all_x,all_y = Load.Everest(N)


    plot1 = plt.subplot2grid((2, 1), (0, 0))
    plot2 = plt.subplot2grid((2, 1), (1, 0))

    plot1.scatter(all_x, all_y, color='r', label="all measured", marker="o")
    plot2.scatter(all_x, all_y, color='r', label="all measured")
    plot1.scatter(x_raw, y_raw, color='g', label="taken", marker="o")
    plot2.scatter(x_raw, y_raw, color='g', label="taken")

    plot1.set_xlabel("x")
    plot1.set_ylabel("y")
    plot1.set_title("Everest")

    x, y = LaGrange(x_raw, y_raw, 3)
    plot1.plot(x, y, color='b', label="interpolated")
    plot1.legend()
    plot1.grid()

    x, y = Splines(x_raw, y_raw, 10)
    plot2.plot(x, y, color='b', label="splines")
    plot2.legend()
    plot2.grid()
    plot2.set_xlabel("x")
    plot2.set_ylabel("y")
    plot2.set_title("Everest")

    plt.show()