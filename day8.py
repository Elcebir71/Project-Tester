if __name__ == '__main__':
    def print_rangoli(size):
        import string
        s = string.ascii_lowercase
        M = 4 * size - 3
        N = size
        for i in range(0, M, 2):
            print("(s[N-1-i]).center(M,"-"))")

    n = int(input())
    print_rangoli(n)