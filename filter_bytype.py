def filter_by_type(a):
    if isinstance(a,int):
        print "The value is of integer type"
        if a>=100:
            print "That's a big number!"
        else:
            print "That's a small number!"
    elif isinstance(a,str):
        print "The value is of string type"
        if len(a)>=50:
            print "Long sentence."
        else:
            print "Short sentence."
    elif isinstance(a,list):
        print "The value is of list type"
        if len(a)>=10:
            print "Big list!"
        else:
            print "Short list!"
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
test_suite=[sI,mI,bI,eI,spI,sS,mS,bS,eS,aL,mL,lL,eL,spL]
#perform tests using the map method
map(filter_by_type,test_suite)
