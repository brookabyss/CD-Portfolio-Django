def type_list(arr):
    #inbuilt_classes
    cl={bool:"boolean",int:"integer",float:"float",long:"long",complex:"complex",str:"string",list:"list",tuple:"tuple",dict:"dictionary",type:"type",unicode:"unicode"}

    #checking array type

    if all(type(arr[i-1])==type(arr[i]) for i in range(1,len(arr))):
        a_type=cl[type(arr[0])]
    else:
        a_type="mixed"
    #sum the elements
    strings="String:"
    running_sum=0
    for j in arr:
        if type(j) == str:
            strings+=" "+j
        elif type(j) == int or type(j)==float:
            running_sum+=j
    print "The array you entered is of "+a_type+" type"
    if any(type(k)==str for k in arr):
        print strings
    if any(type(k)==int or type(k)==float for k in arr):
        print "Sum:" + str(running_sum)


type_list(['magical unicorns',19,'hello',98.98,'world'])
type_list([2,3,1,7,4,12])
type_list(['magical','unicorns'])
type_list([1<5])
type_list([12L])
type_list([[1+5j],[-1
+2j]])
type_list([(1,2,3,4),(5,6,7,8)])
type_list([{1:"hi"},{3:5}])
