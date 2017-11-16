from cmath import pi, exp
def evaluate(x):
  approximation = 0
  for i in range(-10000, 10000):
    if i != 0:
      approximation += 1j*(-1)**i/i*exp(1j*i*x)
  return approximation
print(evaluate(1)) # fancy way of running f(x)=x, 2pi periodic :-)