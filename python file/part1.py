def progress_outcome(pass_credits, defer_credits, fail_credits):

    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
        print("Progress")
    elif pass_credits == 100 and defer_credits == 20 and fail_credits ==0:
        print("Progress (module trailer)")
    elif pass_credits == 100 and defer_credits == 0 and fail_credits == 20:
        print("Progress (module trailer)")
    elif  pass_credits == 80 and defer_credits == 40 and fail_credits == 0:
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