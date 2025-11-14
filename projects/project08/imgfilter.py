# Put the required comment for your python programs here. See the Comment Guide on Canvas.

from cs1.ppm import display_ppm
from cs1.notebooks import *

#This function returns a new filename based on the original and a filter.
#Parameters:
#    original_filename: The original name of the file: something.ppm
#    filter: The filter that was applied (an integer 1-9)
#Returns:
#    A new filename based on the filter.
#    
#  Examples:
#    make_output_filename('rhodes.ppm', 9) returns rhodes_grayscale.ppm
#    make_output_filename('lynx.ppm', 8) returns lynx_flipped.ppm
#
def make_output_filename(original_filename, filter):
    mods = ['negate_red', 'negate_green', 'negate_blue',
            'negate_all', 'remove_red', 'remove_green',
            'remove_blue', 'flip_horizontally', 'grayscale']
    # YOUR CODE HERE
  
  
# This function takes in a list and negates each value in the list
# To negate a value, subtract the value from 255
# Parameters: lst, a 1-D list of integers
# Returns: a list with the modified values (negatives of the original values)
def negate(lst):
    pass # remove this line (including the 'pass') when you start to write this function.

# This function takes in a list and flattens each value in the list
# To flatten a value, set it equal to zero 
# Parameters: lst, a 1-D list of integers
# Returns: a list of the same length as (lst) with all zeros
def flatten(lst):
    pass # remove this line (including the 'pass') when you start to write this function.

# This function takes in a list and reverses the order of the list
# Parameters: lst, a 1-D list of integers
# Returns: the original list in reverse order
def flip(lst):
    pass # remove this line (including the 'pass') when you start to write this function.

# This function takes in three 1-D lists, and returns 3 lists that contain the average 
# of the original values at each index
# To calculate the new value for each list, we need to take the average of the values
# and replace the value with the average in all 3 lists (these values must be integers)
# Example: red[0] = 30, green[0] = 100, blue[0] = 74, average = (30 + 100 + 74) / 3 = 68
# so we set red[0] = 68, green[0] = 68 and blue[0] = 68.
# Hint: Use parallel lists
# Parameters: red, green, blue (3 1-D lists with the same number of elements in them)
# Returns: a list of the same length, whose values are averages.
def grayscale(red, green, blue):
    pass # remove this line (including the 'pass') when you start to write this function.

# This function copies the first 3 lines of input into output
# Parameters: input_file (fileObject that you're reading from),
#             output_file (fileObject that you're writing to)
# Returns: None
def process_header(input_file, output_file):
    # Read the first three lines from the input file and write them to the output file.
    # These file objects were already opened in main() for you.
    pass # remove this line (including the 'pass') when you start to write this function.

# This function applies the specified filter to each pixel in input, writing it to output.
# Hint: Recall that the split function for strings allows you to either specify exactly
# how many variables to create, or if you don't know, you can return the result into
# a single variable, which will be a list of strings
# Example:   s = "5,4,2,5,6,7"
#            values = s.split(',') #values is now equal to ['5','4','2','5','6','7']
# 
# Parameters: input_file: the input file with the header already read
#             output_file: the output file with the header already written
#             filter: the filter to apply
# Returns: None
def process_body(input_file, output_file, filter):
    pass # remove this line (including the 'pass') when you start writing this function.
    # Remove these comments when you're done...
    # Algorithm:
    # Loop over the input file, one line at a time.
    # For each line,
    # ..strip off the whitespace
    # ..create three empty lists for red, blue, and green values
    # ..use the split function to split the line into a list of strings
    #
    # ..With the list of strings,
    #   ..put each red value in the red list,
    #   ..each green value in the green list,
    #   ..and each blue value in the blue list.
    # ..finally call the appropriate filter on the appropriate lists.
    #
    # For example, if you are negating the red channel, your code
    # should call negate on the red list to get the new red channel.
    #
    # ..Now, after processing the colors for the line, create a new string variable that is empty
    # ..write the output RGB values to the output file by looping over the lists 
    # ..(Hint: do this by writing a loop that iterates over each index in the red list)
    #   ..and writing each of the red, blue, and green values to the file
    #   ..(Hint: use string concatenation to put together the red, green, and blue values in the appropriate order, 
    #      with spaces in between, into the new string you created)
    # ..separate each line by a newline. (Add a newline character at the end of your string variable)
    # ..write this new string out to output_file

    # If you are having trouble with this section, try the sample, small input files.
    # test.ppm is the 4x4 image. This is a good way to start.
    # Remember to run through the algorithm on pen and paper _before_ you
    # start coding. It won't do you any good to just start writing Python without
    # thinking about and _understanding_ what you need to do here.
    # Hint: if you're having trouble, print out the string before you write it to the file and if you haven't done any modifications
    # it should be the exact same string as the original line from the infile


# The main function is mostly written for you.
# Add an input validation loop where specified to ensure valid input from the user
def main():
    # get input from user
    input_filename = input('PPM file? ')
    mod = int(input("""Select a filter:
    1. Negate red
    2. Negate green
    3. Negate blue
    4. Negate all
    5. Remove red
    6. Remove green
    7. Remove blue
    8. Flip horizontally
    9. Grayscale
    """))
    # TODO: ADD input validation loop here to ensure valid input from the user 

    # open the file
    input_file = open(input_filename, 'r')

    # get output filename
    output_filename = make_output_filename(input_filename, mod)
    output_file = open(output_filename, 'w')

    # process the file
    process_header(input_file, output_file)
    process_body(input_file, output_file, mod)

    # close both files, print filename, and display image
    input_file.close()
    output_file.close()
    print('Output file with filter', mod, 'applied is named', output_filename)
    display_ppm(output_filename)
    

    

main()
