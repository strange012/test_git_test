import sys

def recfib(n):
    if n == 1:
        return (0, 1)
    a, b = recfib(n-1)
    return b, a + b

def main(argv):
    return recfib(int(argv[1]))
    
if __name__ == '__main__':
    main(sys.argv)