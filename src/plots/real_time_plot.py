from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.animation import FuncAnimation

def fibonacci_increment(series, fibonacci):
    series.append(series[-1] + 1)
    fibonacci.append(fibonacci[-1] + fibonacci[-2])


def fibonacci_plot():
    series = [0, 1]
    fibonacci = [1, 1]

    def animate(i):  ## has to give an i as input
        fibonacci_increment(series, fibonacci)
        print(series)
        print(fibonacci)

        plt.cla()
        plt.plot(series, fibonacci)

    ani = FuncAnimation(plt.gcf(), animate, interval=500, save_count=10)
    plt.tight_layout()
    plt.show()

def basic_plot():
    from itertools import count
    import random

    plt.style.use('fivethirtyeight')

    x_vals = []
    y_vals = []

    index = count()

    def animate(i):
        x_vals.append(next(index))
        y_vals.append(random.randint(0, 5))

        plt.cla()
        plt.plot(x_vals, y_vals)

    ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

    plt.tight_layout()
    plt.show()


# basic_plot()
fibonacci_plot()