from math import exp

# Definer initialverdiene og steglengden.
x, y, h = 0, 1, 1 / 10

def f(x, y): return x * y ** 2

# Kjør tre runder av Eulers metode.
for i in range(3):
  # Oppdater approksimasjonene.
  y, x = y + h * f(x, y), x + h
  # Regn ut differansen fra den analytiske løsningen.
  error = 1 / (1 - x ** 2 / 2) - y
  # Skriv ut verdiene og feilen.
  print(x, y, error)

# Definer initialverdiene og steglengden.
x, y, h = 0, 1, 1 / 10

# Kjør tre runder av Eulers forbedrede metode.
for i in range(3):
  # Bruker snittet av de to tangentene for å approksimere. 
  y, x = y + h * (f(x, y) + f(x + h, y + h * f(x, y))) / 2, x + h
  # Regner ut differansen fra den analytiske løsningen.
  error = 1 / (1 - x ** 2 / 2) - y
  # Skriv ut verdiene og feilen.
  print(x, y, error)

# 4-ordens Runge-Kutta.
x, y, h = 0, 1, 1 / 10
for i in range(3):
  k1 = f(x, y)
  k2 = f(x + h / 2, y + h / 2 * k1)
  k3 = f(x + h / 2, y + h / 2 * k2)
  k4 = f(x + h, y + h * k3)
  y, x = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4), x + h
  error = 1 / (1 - x ** 2 / 2) - y
  print(x, y, error)

def g(y): return -3*y-exp(y)
x, y = 0, 1
for i in range(3):
  y, x = y + h * g(y), x + h
  print(x, y)

x, y = 0, 1
for i in range(3):
  y, x = y + h / 2 * (g(y) + g(g(y) * h)), x + h
  print(x, y)

def f1(y1, y2): return -y1 + y2
def f2(y1, y2): return -y1 - y2
y1, y2, h = 0, 4, 0.2
for i in range(3):
  y1, y2 = y1 + h * f1(y1, y2), y2 + h * f2(y1, y2)
  print(y1, y2)