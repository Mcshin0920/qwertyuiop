import re
import graph


def main():

    user_input = input("Type in your equation in y=mx+b format: ")
    user_input.replace(" ", "")

    slope = float(get_slope(user_input))
    y_intercept = float(get_y(user_input))
    yValue = 100*slope + y_intercept

    screen = 250

    graph.grid(screen, yValue, y_intercept)
    


def get_slope(list1):
    fallback = []
    slope = re.findall(r'-?\d+', list1)
    print(slope)
    try:
      return slope[0]
    except IndexError:
      fallback.append(1)
      return fallback[0]


def get_y(list1):
    fallback = [0]
    yintercept = re.findall(r'-?\d+', list1)
    print(yintercept)
    try:
      return yintercept[1]
    except IndexError:
      return yintercept[0]
    if IndexError:
      return fallback[0]

    


if __name__ == "__main__":
    main()
