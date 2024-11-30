def handle_index(lcs, x_index, y_index):
  if x_index < 0 or y_index < 0:
    return 0
  return lcs[x_index][y_index]    

def longest_common_subsequence (x, y):
  x_size = len(x)
  y_size = len(y)
  lcs = [[0] * (y_size) for _ in range(x_size)]
  for i in range(x_size):
    for j in range(y_size):
      if x[i] == y[j]:
        lcs[i][j] = handle_index(lcs, i-1, j-1) + 1
      else:
        lcs[i][j] = max(handle_index(lcs, i-1, j-1),
            handle_index(lcs, i, j-1),
            handle_index(lcs, i-1, j))

  i = x_size - 1
  j = y_size - 1
  str = ''
  while i >= 0 and j >= 0:
    if x[i] == y[j]:
      str += x[i]
      i -= 1
      j -= 1
    else:
      if handle_index(lcs, i, j - 1) > handle_index(lcs, i - 1, j):
        j -= 1
      else:
        i -= 1

  return (lcs[x_size-1][y_size-1], str[::-1])
