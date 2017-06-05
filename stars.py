def draw_stars(li):
    for i in li:
        stars=""
        if type(i)==int:
            for j in range(1,i+1):
                stars+="*"
            print stars
        elif type(i)==str:
            for j in range(0,len(i)):
                stars+=i[0].lower()
            print stars


draw_stars([1, 6, 0, "hello", 5, "Boogie", 25])
