dp = [0] * 20
def count_ways(n):
  # base case
  dp[0] = dp[1] = dp[2] = 1
  dp[3] = 2
  dp[4] = 4
  if dp[n] == 0:
    dp[n] = count_ways(n-1) + count_ways(n-3) + count_ways(n-4) 
  return dp[n]

def main():

  print(count_ways(4))
  print(count_ways(5))
  print(count_ways(6))


main()
