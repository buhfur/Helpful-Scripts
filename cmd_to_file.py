#script to write the result of a cmd command to a text file
#2/27/19  N0d3
import subprocess
import time
import sys
"""
sys.argv[1] = 'ipconfig'
sys.argv[2] = ['other commands here']
command_to_file([ipconfig, '/flushdns',], filename=output.txt)
note: if echo = True, script will read and print the text file

"""
def command_to_file(*args, filename=None, echo=True, filetype=".txt"):

    try:

        #use current date as the file name

        if filename:

            if check_for_extension(filename):

                with open(str(filename), 'w') as output_file:

                    output_file.write(subprocess.call(args))

                if echo:

                    with open(str(filename), 'r') as output_file:

                        print(output_file.read())


            else:

                print("ERROR: NO FILE EXTENSION")

                sys.exit()

        else:
            #file name is the day of the month

            fname = time.asctime().split(' ')[2]

            with open(str(fname) + ".txt", 'w') as output_file:
                #DOES NOT SHOW ANY OUTPUT
                output_file.write(subprocess.call(args))

            if echo:

                with open(str(fname) + ".txt", 'r') as output_file:

                    print(output_file.read())

    except Exception as e:

        print(e)








def check_for_extension(string, type='.txt'):

    split_string = string.split('.')

    if len(split_string) > 2 or len(split_string) < 2:

        return False

    else:

        if split_string[1] == type:

            return True

        else:

            return False




if __name__ == '__main__':

    command_to_file(sys.argv, echo=True)
