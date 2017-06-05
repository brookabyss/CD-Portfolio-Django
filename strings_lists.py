def find_replace(string,word,replacement):
    print "here is the first instance of the word "+str(string.index(word))
    print "here is the string with the word replcaced:\n"+string.replace(word,replacement)
find_replace("The brown fox jumps again","fox","ostrich")


def min_max(l):
    print "Max num in list:"+str(max(l))
    print "Min num in list:"+str(min(l))
min_max([1,2,43,4])



def first_last(l):
    print "here is the first element in the list:" +str(l[0])
    print "here is the last elemnt in the list:" +str(l[-1])
first_last([1,2,4,4,5,5,5])



def new_list(l):
    l=sorted(l)
    a=l[:len(l)/2]
    b=l[len(l)/2:]
    print a
    print b
    b.insert(0,a)
    print b
new_list([2,3,5,6,-1])
