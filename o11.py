import numpy as np
import matplotlib.pyplot as plt
from math import pi

F = np.fft.fft([0, 2, 3, 7])

def interpolate(F, x):
  """Vektoren som beskriver den diskrete Fouriertransformasjonen er
  skalerte, så vi må dele med antallet elementer i vektoren for å
  finne koeffisientene i interpolasjonspolynomet."""
  return np.real(np.sum(F[i] * np.exp(i * x * 1j)
                 for i in range(len(F)))) / len(F)

interpolation_points = [2 * pi * k / 4 for k in range(len(F))]

for point in interpolation_points:
  print(interpolate(F, point))

X = np.linspace(0, 2 * pi, 256, endpoint=True)
plt.plot(X, interpolate(F, X))
plt.show()

error_matrix = [
  [0, 1 / 5, 2 / 5],
  [1 / 4, 0, -1 / 2],
  [1 / 4, 3 / 8, 0],
]

eigenvalues = np.linalg.eigvals(error_matrix)
spectral_radius = max(abs(max(eigenvalues)), abs(min(eigenvalues)))
print(spectral_radius)

A = np.array([
  [5, 1, 2],
  [1, 4, -2],
  [2, 3, 8],
])

b = np.array([19, -2, 39])

x = [1, 1, 1]

D = np.diag(np.diag(A))
D_inverse = np.linalg.inv(D)
R = A - D

for i in range(len(A)):
  x = D_inverse.dot(b - R.dot(x))

print(x)

x_gs = [1, 1, 1]

for i in range(4):
  for j in range(len(x)):
    x_gs[j] = D_inverse[j].dot(b - R[j].dot(x_gs))

print(x_gs)