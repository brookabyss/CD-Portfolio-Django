def mult_table():
    table=[]
    for y in range (1,13):
        row=[]
        for x in range (1,13):
            row+=[x*y]
        table+=[row]

    return table
b=mult_table()
top_row=["x"]
for i in range(0,12):
    top_row.append(i+1)
    b[i].insert(0,i+1)
b.insert(0,top_row)
def printer(arr):
    for i in arr:
        print"\n"
        for k in i:
            if len(str(k))==1:
                print "  "+str(k),
            elif len(str(k))==2:
                print " "+str(k),
            elif len(str(k))==3:
                print ""+str(k)
printer(b)
