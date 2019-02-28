import subprocess
import sys


def get_history(filename):
    #add file to executable
    command = ['ipconfig','/displaydns']

    subprocess.Popen(command, shell=True, stdout=open(filename,'w'))
    #send the text file somewhere with smtp

if __name__ == '__main__':
    get_history(sys.argv[1])
    
