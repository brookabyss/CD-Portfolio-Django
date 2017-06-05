def odd_even(start,end):
    for i in range(start,end+1):
        num_type="even" if i%2==0 else "odd"
        print "Number is "+str(i)+". This is an "+num_type+"number."
# odd_even(1,2000)

def multiply(li,x):
    return map(lambda i: i*x,li)
# print multiply([2,4,10,16],5)


def layered_multiples(func,li,x):
    altered=func(li,x)
    new_li=[]
    for i in range(0,len(li)):
        row=[]
        for j in range(0,altered[i]):
            row+=[1]
        new_li+=[row]
    return new_li
# print layered_multiples(multiply,[2,4,5],3)
