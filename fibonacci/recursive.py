def calculateFibonacci(n):
  if n < 2:
    return n
  return calculateFibonacci(n - 1) + calculateFibonacci(n - 2)


def main():
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))

main()
