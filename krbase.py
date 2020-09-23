# CONVERTER: ALLOWS YOU TO CONVERT STRING, LIST, AND TUPLES
# TO LIST OR TUPLE
# Thank you -> alizain :)

# The converter function with item as a requirement
def converter(item):
    # First print the type of that item and also ask which type the users
    # wants it to convert into
    print(type(item), 'Convert to list or tuple (l/t) ?')
    # Decision would be taken from the user as raw text
    decision = input('')

    # Try to do this
    try:

        # if the decision is l
        if decision == 'l':
            # Convert it to list and print the type and the item itself
            item = list(item)
            print(type(item), item)

        # if the decision is t
        elif decision == 't':
            # Convert it to tuple and print the type and the item itself
            item = tuple(item)
            print(type(item), item)

        # Else print this error and recall the function
        else:
            print('Invalid option.')
            converter()

    # Except for invalid value input or type errors, print these error messages
    except ValueError:
        print('Invalid value type input. Please put a valid item.')

    except TypeError:
        print('Invalid value type input. Please put a valid item.')

    # Open the file with append permissions
    open_file = open('output.txt', 'a')
    # Ask if the person wants to log or not
    write_permit = input('Log output? (y/n) ')

    # If the user agrees
    if write_permit == 'y':

        temp_output_lst = [item, type(item)]
        temp_output = str(temp_output_lst)

        # Write the output to output.txt
        open_file.write(temp_output + '\nl')
        print('Log file -> output.txt in this directory!')

    # if the user doesnt
    elif write_permit == 'n':
        # Say ok and exit
        print('Ok.')
        exit()

    # Else print an error
    else:
        print('Invalid value. recalling..')
        converter()

    # Close the file after all the operations
    open_file.close()


# Example variable (of course can be replaced for experimental purposes)
my_list = 'this is thie boy'

# Call that function using that my_list variable as an input
converter(my_list)
