
import argparse
  # loop through arr
    # for each element loop through the rest of the array
    # find the difference between first element vs the next elements
    # if the difference is greater than max_profit
        # replace max_profit with current difference
      # elif difference is less than min_profit
        # replace min_profit with current difference

def find_max_profit(prices):

  # variable for max_profit
  max_profit = -999

  for i in prices:

    for j in prices[prices.index(i) + 1:]:

      current_difference = j - i
      print(f"i({i}), j({j}), current difference({current_difference})")

      if max_profit < current_difference:
        max_profit = current_difference
        print(f"max Profit ({max_profit})")

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))