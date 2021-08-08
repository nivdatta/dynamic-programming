def count_ways(n):
  dp = [0] * (n+1)
  
  if n in [0, 1, 2]:
    return 1
  if n == 3:
    return 2
  if n == 4:
    return 4
  for i in range(5, n+1):
    dp[i] = count_ways(n-1) + count_ways(n-3) + count_ways(n-4) 
  return dp[n]

def main():

  print(count_ways(4))
  print(count_ways(5))
  print(count_ways(6))


main()
