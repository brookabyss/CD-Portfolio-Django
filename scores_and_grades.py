def scores_and_grades(start,end,nums):
    print"Scores and Grades"
    #define grader function to assign grades to scores
    def grader(score):
        grade=""
        if 60 <= score and score < 70:
            grade="D"
        elif 70 <= score and score < 80:
            grade="C"
        elif 80 <= score and score < 90:
            grade="B"
        elif 90<= score and score <= 100:
            grade="A"
        return grade
    #populate scores array with nums number of random scores start-end
    scores=[]
    import random
    for i in range(0,nums):
        scores+=[random.randint(start,end+1)]
    for score in scores:
        print "Score: "+ str(score)+ " Your grade is " +grader(score)

scores_and_grades(60,100,10)
