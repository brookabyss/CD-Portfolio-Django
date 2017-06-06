def list_to_dict(list_one,list_two):
    new_dict=dict(zip(list_one,list_two)) if len(list_one)> len(list_two) else dict(zip(list_two,list_one))
    return new_dict
print list_to_dict([1,2,3,4,5,100,200,300,500],["hello","greetings","Boogie",5,7,6])
