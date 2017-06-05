def oddo():
    #loop between 1 and 1000, excluding 1000
    for i in range(1,1000):
        #check if i is odd
        if i%2!=0:
            #print i
            print i
oddo()

def fivos():
    #lloop between 1 and 1000, excluding 1000000
    for i in range(5,1000000):
        #check if i is a multiple of 5
        if i%5==0:
            #print i
            print i
fivos()

def sumo(l):
    #iterate through the list
    total=0
    for i in l:
    #incrememt by element
        total+=i
    return total
print(sumo([1, 2, 5, 10, 255, 3]))

def av(l):
    #using fucntion sumo declared above we can calculate the average:
    #the sum will be changed to a float value to get an accurate calculation:
    average=float(sumo(l))/(len(l))
    print average
av([1, 2, 5, 10, 255, 3])
