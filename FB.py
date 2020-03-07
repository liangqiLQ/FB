class Fi():
    def FB(self, n):
        if n == 1:
            return [1]
        if n == 2:
            return [1, 1]
        fibs = [1, 1]
        for i in range(2, n):
            fibs.append(fibs[-1] + fibs[-2])
        return fibs

    def of(self, j):
        fibs = self.FB(201)
        tmp = fibs[j - 1]
        return tmp

def main():
    Fibonacci=Fi()
    for i in range(1,201):
        print("Fibonacci.of({})".format(i)+"="+str(Fibonacci.of(i)))
if __name__ == '__main__':
    main()
