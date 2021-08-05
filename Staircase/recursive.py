def count_ways(n):
  # base cases
  if n == 0:
    return 1  # we don't need to take any step, so there is only one way

  if n == 1:
    return 1  # we can take one step to reach the end, and that is the only way

  if n == 2:
    return 2  # we can take one step twice or jump two steps to reach at the top

  # if we take 1 step,  'n-1' steps remaining
  # if we take 2 steps, 'n-2' steps remaining
  # if we take 3 steps, 'n-3' steps remaining
  return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


def main():
  print(count_ways(5))

main()
