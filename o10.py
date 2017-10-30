from fractions import Fraction

def divided_difference(values):
  """Calculates the divided difference using the given samples."""
  if len(values) == 1:
    return values[0][1]

  if len(values) == 2:
    return (values[0][1] - values[1][1]) / (values[0][0] - values[1][0])

  return (divided_difference(values[1:]) - divided_difference(values[0:-1])) / (values[-1][0] - values[0][0])

tups = [(0, 4), (1, -1), (2, -3), (4, -6), (6, 9), (3, -5)]

for i in range(0, len(tups)):
  print(tups[:i+1], Fraction(divided_difference(tups[:i+1])).limit_denominator())
