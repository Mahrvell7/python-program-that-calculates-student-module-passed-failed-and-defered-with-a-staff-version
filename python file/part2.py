


def progress_outcome(pass_credits, defer_credits, fail_credits):

    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
        print("Progress")
    elif pass_credits == 100 and defer_credits == 20 and fail_credits ==0:
        print("Progress (module trailer)")
    elif pass_credits == 100 and defer_credits == 0 and fail_credits == 20:
        print("Progress (module trailer)")
    elif pass_credits == 80 and defer_credits == 40 and fail_credits == 0:
        print("Do not progress - module retriever")
    elif pass_credits == 80 and defer_credits == 20 and fail_credits == 20:
        print("Do not progress - module retriever")
    elif pass_credits == 80 and defer_credits == 0 and fail_credits == 40:
        print("Do not progress - module retriever")
    elif pass_credits == 60 and defer_credits == 60 and fail_credits == 0:
        print("Do not progress - module retriever")
    elif pass_credits == 60 and defer_credits == 40 and fail_credits == 20:
        print("Do not progress - module retriever")
    elif pass_credits == 60 and defer_credits == 20 and fail_credits == 40:
        print("Do not progress - module retriever")
    elif pass_credits == 60 and defer_credits == 0 and fail_credits == 60:
        print("Do not progress - module retriever")
    elif pass_credits == 40 and defer_credits == 80 and fail_credits == 0:
        print("Do not progress - module retriever")
    elif pass_credits == 40 and defer_credits == 60 and fail_credits == 20:
        print("Do not progress - module retriever")
    elif pass_credits == 40 and defer_credits == 40 and fail_credits == 40:
        print("Do not progress - module retriever")
    elif pass_credits == 40 and defer_credits == 20 and fail_credits == 60:
        print("Do not progress - module retriever")
    elif pass_credits == 40 and defer_credits == 0 and fail_credits == 80:
        print("Exclude")
    elif pass_credits == 20 and defer_credits == 100 and fail_credits == 0:
        print("Do not progress - module retriever")
    elif pass_credits == 20 and defer_credits == 80 and fail_credits == 20:
        print("Do not progress - module retriever")
    elif pass_credits == 20 and defer_credits == 60 and fail_credits == 40:
        print("Do not progress - module retriever")
    elif pass_credits == 20 and defer_credits == 40 and fail_credits == 60:
        print("Do not progress - module retriever")
    elif pass_credits == 20 and defer_credits == 20 and fail_credits == 80:
        print("Exclude")
    elif pass_credits == 20 and defer_credits == 0 and fail_credits == 100:
        print("Exclude")
    elif pass_credits == 0 and defer_credits == 120 and fail_credits == 0:
        print("Do not progress - module retriever")
    elif pass_credits == 0 and defer_credits == 100 and fail_credits == 20:
        print("Do not progress - module retriever")
    elif pass_credits == 0 and defer_credits == 80 and fail_credits == 40:
        print("Do not progress - module retriever")
    elif pass_credits == 0 and defer_credits == 60 and fail_credits == 60:
        print("Do not progress - module retriever")
    elif pass_credits == 0 and defer_credits == 40 and fail_credits == 80:
        print("Exclude")
    elif pass_credits == 0 and defer_credits == 20 and fail_credits == 100:
        print("Exclude")
    elif pass_credits == 0 and defer_credits == 0 and fail_credits == 120:
        print("Exclude")


def validation():

    range =[0, 20, 40, 60, 80, 100, 120]

    global  pass_credits, defer_credits, fail_credits
    while True:
        try:
            pass_credits = int(input("Please enter your credits at pass: "))
        except ValueError:
            print("Interger required")
            continue
        else:
            if pass_credits not in range:
                print("Out of range")
            elif pass_credits in range:
                break
    while True:
        try:
            defer_credits = int(input("Please enter your credit at defer: "))
        except ValueError:
            print("Integer required")   
            continue
        else:
            if defer_credits not in range:
                print("Out of range")
            elif defer_credits in range:
                break    
    while True:
        try:
             fail_credits = int(input("Please enter your credit at fail: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if fail_credits not in range:
                print("Out of range")
            elif defer_credits in range:
             break    
    while True:
        t_credits= pass_credits + defer_credits + fail_credits
        if t_credits != 120:
            print("Total incorrect")   
            validation()
        else:
            progress_outcome(pass_credits, defer_credits, fail_credits)
            break 

