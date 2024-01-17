import sys # this allows us to figure out what the first argument is

def parseArguments():
    arguments = {
        "price" : int(sys.argv[1]),
        "quantity" : 1,
        "province" : "ON"
    }
    return arguments

def taxRate (province):
    tax = {
        "ON" : 0.13,
    }
    return tax[province]

def mcmerchCalculator():
    arguments = parseArguments()
    tax = taxRate(arguments['province'])
    result = arguments['price'] * arguments['quantity'] * (1 + tax)
    rounded_result = round(result, 2)  # Round the result to 2 decimal places
    print(rounded_result)
#thisguy
mcmerchCalculator()