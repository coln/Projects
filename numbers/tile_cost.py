"""Find Cost of Tile to Cover W x H Floor
Calculate the total cost of tile it would take to cover a floor plan of width 
and height, using a cost entered by the user.
"""

def main():
    print("Price of tiling a WxH (in square feet) floor")
    while True:
        print("Enter '0' to quit at anytime")
        cost = getInput("cost", "Cost per square foot (in dollars): ")
        if cost == 0:
            break
        
        width = getInput("width", "Floor width (in feet): ")
        if width == 0:
            break
        
        height = getInput("height", "Floor height (in feet): ")
        if height == 0:
            break
        
        total = cost * width * height
        print("It would cost $%.2f to tile that floor." % total)
        print("")



def getInput(name, input_msg):
    number = -1
    while True:
        number = input(input_msg)
        try:
            number = float(number)
        except ValueError:
            print("Invalid " + name)
            continue
        
        if number < 0.0:
            print(name.title() + " must be a positive number")
            continue
        break
    return number

if __name__ == "__main__":
    main()