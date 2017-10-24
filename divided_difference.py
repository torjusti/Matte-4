def divided_difference(values):
  """Calculates the divided difference using the given samples."""
  if len(values) == 1:
    return values[0][1]

  if len(values) == 2:
    return (values[0][1] - values[1][1]) / (values[0][0] - values[1][0])

  return (divided_difference(values[1:]) - divided_difference(values[0:-1])) / (values[-1][0] - values[0][0])

print(divided_difference([(-2, -2), (-1, 1), (0, 2)]))