def coin_tosses(nums):
    print "Starting the program..."
    head_count=0
    tail_count=0
    import random
    for i in range(0,nums+1):
        print "Attempt #"+str(i)+": Throwing a coin...",
        if round(random.random())==1:
            print "It's a head! ...",
            head_count+=1
        else:
            print "It's a tail! ...",
            tail_count+=1
        print "Got " +str(head_count)+" heads(s) so far and "+str(tail_count)+" tails(s) so far"
    return
coin_tosses(5000)
