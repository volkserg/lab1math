# import PyGnuplot as gp
# import numpy as np
import matplotlib.pyplot as plt

class Derivative:
    def __init__(self, f, h=1E-9):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h


class Task1:

    def __init__(self, a, b):
        assert (a > 0 and a < 1 and b > 0 and b < 1)
        self.a = a
        self.b = b
        self.inA = 1 - a
        self. inB = 1 - b
        self.p = self.a/self.b
        self.delta = self.a * self.inB / (self.inA * self.b)

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def increase_a(self, n):
        self.a += n

# ---------------------------------1st-----------------------------
    # 1-2
    def calculate_p(self, i):
        assert (i >= 0)
        p0 = 1 - self.p
        if i == 0:
            return p0
        elif i > 0:
            return (1/self.b) * (self.delta ** i) * p0

    # 3-4
    def calculate_px(self, i):
        assert (i >= 0)
        if i == 0:
            return 1 - self.delta
        elif i >= 1:
            return (1 - self.delta)*(self.delta**i)

    # 5-6
    def calculate_vk(self, k):
        assert (k >= 1)
        return (1 - self.inB / self.inA) * (self.inB / self.inA)**(k - 1)

    # 7-8
    def calculate_wk(self, k):
        assert (k >= 0)
        if k == 0:
            return self.calculate_px(0)
        elif k >= 1:
            return (1 - self.calculate_px(0)) * self.calculate_vk(k)
    # ---------------------------------2nd-----------------------------

    # 9
    def calculate_n(self):
        return (self.inA * self.p) / (1 - self.p)

    # 10
    def calculate_q(self):
        return (self.inB * (self.p**2)) / (1 - self.p)

    # 11
    def calculate_nx(self):
        return (self.inB * self.p) / (1 - self.p)

    # 12
    def calculate_qx(self):
        return (self.inB * (self.p**2)) / (self.inA * (1 - self.p))

    # 13 не получилось (деление на ноль)
    def calculate_P(self, z):
        return ((((z - 1) * self.inA * self.b) + z * (z - 1) * self.a * self.b) / (((z - 1) * self.inA * self.b) - z * (z - 1) * self.a * self.inB)) * self.calculate_p(0)

    def calculate_VarN(self):
        h = 0.00001
        df = Derivative(self.calculate_P)

        return df(1) + self.calculate_n() - self.calculate_n()**2
    # 15
    def calculate_w(self):
        return (self.a * self.inB) / (self.b * (self.inA - self.inB))

    # 16
    def calculate_v(self):
        return self.calculate_w() + 1 / self.b

# ---------------------------------3rd-----------------------------

class Graphics():


    def draw_Na(self, a, b, dx):
        x = []
        y = []
        while a < b:
            t = Task1(a, b)
            x.append(a)
            y.append(t.calculate_n())
            a += dx
        plt.scatter(x, y)
        plt.show()

# t = Task1(0.1,0.5)
# print(t.calculate_p(3))
# print(t.calculate_VarN())

g = Graphics()
g.draw_Na(0.1, 0.7, 0.001)