def foo_bar(start,stop):
    def primo(n):
            num=n
            if n<2:
                return False
            elif n==2:
                return True
            while n > 2:
                if num%(n-1)==0:

                    return False
                n-=1
            return True

    def squaro(n):
        for i in range(1,n/2+1):
            if i*i==n:
                return True
        return False
    for digit in range(start,stop+1):
        if squaro(digit):
            print digit
            print"Bar"
        elif primo(digit):
            print"Foo"
        else:
            print digit
            print "Foobar"

foo_bar(1,100)
