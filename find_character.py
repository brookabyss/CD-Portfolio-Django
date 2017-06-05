def find_character(li,l):
    result=[]
    for i in li:
        if i.find(l)!=-1:
            result+=[i]
    return result
print find_character(['hello','world','my','name','is','Anna'],"o")==["hello","world"]
