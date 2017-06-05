def personator(person):
    for k,v in person.iteritems():
        print "My "+k+" is "+str(v)
brook={"name":"Brook","age":30,"country of birth":"Ethiopia","favorite language":"Python"}
personator(brook)
