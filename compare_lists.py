def compare_lists(list_one,list_two):
    result="The lists are not the same."
    test1=any(list_one[i]!=list_two[i] for i in range(0,len(list_two)))
    test2=len(list_one)!=len(list_two)
    if test1 or test2:
        print result
    else:
        print result.replace("not","")
compare_lists([1,2,3,4],[1,2,3,4])
compare_lists(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])
compare_lists([1,2,3],[1,2])
