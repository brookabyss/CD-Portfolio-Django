
def namer(person_li):
    mapper=[]
    for i in person_li:
        result=""
        count=0
        for v in i.itervalues():
            count+=len(v)
            result+=v+" "
        mapper+=[[result,count]]
    return mapper
# for Assignment # 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
x= namer(students)
for i in x:
    print i[0]

# for Assignment #2

def fielder(user_obj):
    for obj_keys,obj_val in user_obj.iteritems():
        #print the title of the person
        print obj_keys
        # use the namer method to iterate through the values and get back [["string",lettercount]]
        b=namer(obj_val)
        for p_no in range(0,len(b)):
            print str(p_no+1)+" - "+ b[p_no][0]+" - " +str(b[p_no][1])

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
fielder(users)
