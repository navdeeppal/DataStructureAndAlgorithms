######### Assignment 9 ##########
######### Navdeep Pal ###########
######### Date : 04/11/2015 #####


def fib(num): 
    print ("Computing fib(%d)" % num)
    if num < 3: 
        print ("Leaving fib(%d) returning 1" % num )
        return 1
    else: 
        nplus = fib(num-1) + fib(num-2) 
        print ("Leaving fib(%d) returning %d" % (num, nplus) )
        return nplus
fib(6)  