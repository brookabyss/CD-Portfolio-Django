def tupler(dicti):
    return zip(dicti.keys(),dicti.values())
    # result=[]
    # for k,v in dicti.iteritems():
    #     result+=[(k,v)]
    # return result


a={"kangaroo":"jack",1:20,"hello":"bob"}
print tupler(a)
