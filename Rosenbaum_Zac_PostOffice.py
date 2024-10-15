'''
Author: Zac Rosenbaum
Date: 9/30/2024
Description: Generates a price for shipping a piece of mail when the user gives the dimension and the starting and ending zipcode
Features: None9
Bugs: None
Sources: w3 schools
'''
import sys #brings in the sys libray to exit the program if user doesn't meet the parameters
#package type code
def get_size(length, height, thickness):    # defines the get_size function that finds the size of the package that takes in variable length, height, and thickness
    """
    Calculates the type of package

    Args:
        length, hieght, thickness (int): The number for which the zipcode zone needs for calculation.

    Returns:
       The cost of the packaging and the cost of shipping through each zipcode zone
"""
    if length >= 3.5 and length <= 4.25 and height >= 3.5 and height <= 6.0 and thickness >= .007 and thickness <= .016:            #if length is between, 3.5, 4.25, and height is between, 3.5, 6, and thickness is between, .007, .016, then,
        return [.20, .03] #reg post card    # returns the values .20 (steady price) and .03 (price per zipcode zone hop)
    elif length >= 4.25 and length <= 6.0 and height >= 6.0 and height <= 11.5 and thickness >= .007 and thickness <= .015:         #if the prev conditional was not met, check if length is between, 4.25, 6, and height is between, 6, 11.5, and thickness is between, .007, .015, if so, then,
        return [.37, .03] #large post card  # returns the values .37 (steady price) and .03 (price per zipcode zone hop)
    elif length >= 3.5 and length <= 6.125 and height >= 5.0 and height <= 11.5 and thickness >= .016 and thickness <= .25:         #if the prev conditionals are not met, check if length is between, 3.5, 6.125, and height is between, 5, 11.5, and thickness is between, .016, .25, if so, then,
        return [.37, .04] #envelope         # returns the values .37 (steady price) and .04 (price per zipcode zone hop)
    elif length >= 6.125 and length <= 24.0 and height >= 11.0 and height <= 18.0 and thickness >= .25 and thickness <= .5:         #if the prev conditionals are not met, check if length is between, 6.125, 24, and height is between, 11, 18, and thickness is between, .25, .5, if so, then,
        return [.60, .05] #large envelope   # returns the values .60 (steady price) and .05 (price per zipcode zone hop)
    elif length + 2*thickness + 2*height <= 84.0:      #if the prev conditionals are not met, check if the length plus the distance around the other sides is less than or equal to 84, if so, then,
        return [2.95, .25] #package          # returns the values 2.95 (steady price) and .25 (price per zipcode zone hop)
    elif length + 2*thickness + 2*height <= 130.0:    #if the prev conditionals are not met, check if the length plus the distance around the other sides is less than or equal to 130, if so, then,
        return [3.95, .35] #large package    # returns the values 3.95 (steady price) and .35 (price per zipcode zone hop)
    else:                                              #if the prev conditionals are not met, then,
        sys.exit("Package is UNMAILABLE because it does not fit the size requirments")  # the code exits and displays that the package is unmailable
#zip zone code 
def get_zip(zipcode):
    """
    Calculates the zipcode zone of a zipcode

    Args:
        zipcode (int): The number for which the zipcode zone needs for calculation.

    Returns:
        the value of the zipcode ex. 2
    """
    if zipcode < 6999 and zipcode > 1:      #if the parameter zipcode is less than 06999 and greater than 00001 then, 
        return 1                            #returns the value 1 to the function (zone 1)
    elif zipcode <19999 and zipcode > 7000: #if the prev conditional was not met, check if the parameter zipcode is less than 19999 and greater than 07000, if so, then,
        return 2                            #returns the value 2 to the function
    elif zipcode <35999 and zipcode > 20000:#if the prev conditional was not met, check if the parameter zipcode is less than 35999 and greater than 20000, if so, then,
        return 3                            #returns the value 3 to the function
    elif zipcode <62999 and zipcode > 36000:#if the prev conditional was not met, check if the parameter zipcode is less than 62999 and greater than 36000, if so, then,
        return 4                            #returns the value 4 to the function
    elif zipcode <84999 and zipcode > 63000:#if the prev conditional was not met, check if the parameter zipcode is less than 84999 and greater than 63000, if so, then,
        return 5                            #returns the value 5 to the function
    elif zipcode <99999 and zipcode > 85000:#if the prev conditional was not met, check if the parameter zipcode is less than 99999 and greater than 85000, if so, then,
        return 6                            #returns the value 6 to the function
    else:                                   #if all of the prev conditionals were not met, then
        sys.exit("GIVEN ZIPCODE IS NOT A REAL ZIPCODE") #exits the code and displays that the zipcode given is not an actual zip code. 

def main(): # defines the main function to run to carry out the code
    """
    Carries out the whole program to find the cost of shipping something

    Returns:
        the cost of shipping
    """
    dimension = input('''enter length,height,thickness,zip1,zip2 of your package (l,h,t IN INCHES):
                ''').split(',')          #asks the user to give length,height,thickness,zip1,zip2 and turns into a list by spliting input into elements at each comma 
    try:                                 #checks if the following indented code works
        length = float(dimension[0])     #sets the variable 'length' to a float of the first element of the dimension list
    except:                              #excepts the following error from the code
        ValueError                       #excepts value error(if someone inputs in letters instead of numbers into the dimension variable)
        sys.exit("the length of the package must only conatain numbers") #tells the user that the package must solely contain numbers and exits the program

    try:                                 #checks if the following indented code works
        height = float(dimension[1])     #sets the variable 'height' to a float of the second element of the dimension list
    except:                              #excepts the following error from the code
        ValueError                       #excepts value error(if someone inputs in letters instead of numbers into the dimension variable)
        sys.exit("the height of the package must only contain numbers")  #tells the user that the package must solely contain numbers and exits the program
    
    try:                                 #checks if the following indented code works
        thickness = float(dimension[2])  #sets the variable 'thickness' to a float of the third element of the dimension list
    except:                              #excepts the following error from the code
        ValueError                       #excepts value error(if someone inputs in letters instead of numbers into the dimension variable)
        sys.exit("the thickness of the package must only contain numbers")  #tells the user that the package must solely contain numbers and exits the program
    
    try:                                 #checks if the following indented code works
        zip1 = int(dimension[3])         #sets the variable 'zip1' to a integer of the 4th element of the dimension list
    except:                              #excepts the following error from the code
        ValueError                       #excepts value error(if someone inputs in letters instead of numbers into the dimension variable)
        sys.exit("the starting zipcode of the package must only contain numbers") #tells the user that the package must solely contain numbers and exits the program      
    try:                                 #checks if the following indented code works
        zip2 = int(dimension[4])         #sets the variable 'zip2' to a integer of the 5th element of the dimension list
    except:                              #excepts the following error from the code
        ValueError                       #excepts value error(if someone inputs in letters instead of numbers into the dimension variable)
        sys.exit("the ending zipcode of the package must only contain numbers")   #tells the user that the package must solely contain numbers and exits the program

    start_zone = get_zip(zip1)              #sets the output of the get_zip function that takes in the variable zip1 to a new variable 'start_zone'
    end_zone = get_zip(zip2)                #sets the output of the get_zip function that takes in the variable zip2 to a new variable 'end_zone'
    zone_hops = (abs(start_zone-end_zone))  #sets zone hops variable to the absolute value of the variable start_zone subtracted by end_zone
    

    size_cost = get_size(length, height, thickness)[0]  #sets the variable size cost to the first element of the list output of the get size function when taking in variable h,l,t
    zone_rate = get_size(length, height, thickness)[1]  #sets the variable zone rate to the second element of the list output of the get size function when taking in variable h,l,t

    cost = round(zone_hops*zone_rate+size_cost, 2)       #sets cost equal to the formula for the shipping cost
    final_cost = "{:,.2f}".format(cost).lstrip("0")                   #gets rid of the leading 0 and makes cost a string
    print (final_cost)                 #prints final cost



 
main()                      #runs the main function to carry out all the functions of the code
