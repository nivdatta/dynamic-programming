def count_ways(n):
  dp = [0 for x in range(n+1)]
  return count_ways_recursive(dp, n)

def count_ways_recursive(dp, n):
  if n == 0:
    return 1  # base case, we don't need to take any step, so there is only one way

  if n == 1:
    return 1  # we can take one step to reach the end, and that is the only way

  if n == 2:
    return 2  # we can take one step twice or jump two steps to reach at the top

  # if we take 1 step, n-1 steps left
  # if we take 2 step, n-2 steps left
  # if we take 3 step, n-3 steps left
  if dp[n] == 0:
    dp[n] = count_ways_recursive(dp, n - 1) + count_ways_recursive(dp, n - 2) + count_ways_recursive(dp, n - 3)

  return dp[n]


def main():
  print(count_ways(5))

main()
