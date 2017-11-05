from fractions import Fraction

def divided_difference(values):
  """Calculates the divided difference using the given samples."""
  if len(values) == 1:
    return values[0][1]

  if len(values) == 2:
    return (values[0][1] - values[1][1]) / (values[0][0] - values[1][0])

  return (divided_difference(values[1:]) - divided_difference(values[0:-1])) / (values[-1][0] - values[0][0])

print('Divided differences for task 1')
tups = [(0, 4), (1, -1), (2, -3), (4, -6), (6, 9), (3, -5)]
for i in range(0, len(tups)):
  print(tups[:i+1], Fraction(divided_difference(tups[:i+1])).limit_denominator())

print('Divided differences for task 2')
tups = [(1.885, -1.101), (1.074, 0.549), (-0.074, 0.05), (-0.885, 0.496)]
for i in range(0, len(tups)):
  print(tups[:i+1], divided_difference(tups[:i+1]))
