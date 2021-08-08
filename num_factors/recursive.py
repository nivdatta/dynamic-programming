def count_ways(n):
  # Base Cases
  if n==0:
    return 1
  if n==1:
    return 1
  if n==2:
    return 1
  if n==3:
    return 2
  if n==4:
    return 4
  return count_ways(n-1) + count_ways(n-3) + count_ways(n-4) 


def main():

  print(count_ways(4))
  print(count_ways(5))
  print(count_ways(6))

main()
