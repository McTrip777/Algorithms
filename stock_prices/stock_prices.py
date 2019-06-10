#!/usr/bin/python

# import argparse

def find_max_profit(prices):
  profitArr = []
  highest = prices[1]-prices[0]
  for i in range(0, len(prices)):
    for j in range(0, len(prices)): 
      if i < j:
        profit = prices[j] - prices[i]
        profitArr.append(profit)
  j+=1     
  for k in range(0, len(profitArr)):
    if highest < profitArr[k]:
      highest = profitArr[k]
  return highest


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))


prices = [200, 100, 90, 20, 5]

print(find_max_profit(prices))