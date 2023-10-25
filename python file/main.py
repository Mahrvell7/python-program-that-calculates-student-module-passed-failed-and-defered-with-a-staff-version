



# progress outcome for student

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



# student validation to test (out of range, integer required and total incorrect)

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



## staff version
progress = []
trailer = []
retriever = []
exclude = []

def histogram (pass_credits, defer_credits, fail_credits):
    if pass_credits == 120 and defer_credits == 0 and fail_credits == 0:
        progress.append(0)
    elif pass_credits == 100 and defer_credits == 20 and fail_credits == 0:
        trailer.append(0)
    elif pass_credits == 100 and defer_credits == 0 and fail_credits == 20:
        trailer.append(0)
    elif pass_credits == 80 and defer_credits == 40 and fail_credits == 0:
        retriever.append(0)
    elif pass_credits == 80 and defer_credits == 20 and fail_credits == 20:
        retriever.append(0)
    elif pass_credits == 80 and defer_credits == 0 and fail_credits == 40:
        retriever.append(0)
    elif pass_credits == 60 and defer_credits == 60 and fail_credits == 0:
        retriever.append(0)
    elif pass_credits == 60 and defer_credits == 40 and fail_credits == 20:
        retriever.append(0)
    elif pass_credits == 60 and defer_credits == 20 and fail_credits == 40:
        retriever.append(0)
    elif pass_credits == 60 and defer_credits == 0 and fail_credits == 60:
        retriever.append(0)
    elif pass_credits == 40 and defer_credits == 80 and fail_credits == 0:
        retriever.append(0)
    elif pass_credits == 40 and defer_credits == 60 and fail_credits == 20:
        retriever.append(0)
    elif pass_credits == 40 and defer_credits == 40 and fail_credits == 40:
        retriever.append(0)
    elif pass_credits == 40 and defer_credits == 20 and fail_credits == 60:
        retriever.append(0)
    elif pass_credits == 40 and defer_credits == 0 and fail_credits == 80:
        exclude.append(0)
    elif pass_credits == 20 and defer_credits == 100 and fail_credits == 0:
        retriever.append(0)
    elif pass_credits == 20 and defer_credits == 80 and fail_credits == 20:
        retriever.append(0)
    elif pass_credits == 20 and defer_credits == 60 and fail_credits == 40:
        retriever.append(0)
    elif pass_credits == 20 and defer_credits == 40 and fail_credits == 60:
        retriever.append(0)
    elif pass_credits == 20 and defer_credits == 20 and fail_credits == 80:
        exclude.append(0)
    elif pass_credits == 20 and defer_credits == 0 and fail_credits == 100:
        exclude.append(0)
    elif pass_credits == 0 and defer_credits == 120 and fail_credits == 0:
        retriever.append(0)
    elif pass_credits == 0 and defer_credits == 100 and fail_credits == 20:
        retriever.append(0)
    elif pass_credits == 0 and defer_credits == 80 and fail_credits == 40:
        retriever.append(0)
    elif pass_credits == 0 and defer_credits == 60 and fail_credits == 60:
        retriever.append(0)
    elif pass_credits == 0 and defer_credits == 40 and fail_credits == 80:
        exclude.append(0)
    elif pass_credits == 0 and defer_credits == 20 and fail_credits == 100:
        exclude.append(0)
    elif pass_credits == 0 and defer_credits == 0 and fail_credits == 120:
        exclude.append(0)



def histogram_output():
    print("\n")
    print("-" * 60)
    print("Horizontal Histogram\n")
    print("Progress", len(progress))
    print("Trailer", len(trailer))
    print("Retriever", len(retriever))
    print("Excluded", len(exclude))
    total_outcomes = len(progress) + len(trailer) + len(retriever) + len(exclude)
    print("\n")
    print(total_outcomes, "outcomes in total.")
    print("-" * 60)



# staff validation  for histograms

def staff_validation():

    range =[0, 20, 40, 60, 80, 100, 120]

    global pass_credits, defer_credits, fail_credits, close
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
            staff_validation()
        else:
            progress_outcome(pass_credits, defer_credits, fail_credits)
            histogram(pass_credits, defer_credits, fail_credits)
            break




#staff validation run again after exquition

def run_again():
    global muiltiple_outcomes
    while True:
        print("\n")
        try:
            muiltiple_outcomes = input("Would you like to enter another set of data?\n"
                          "Enter 'y' for yes or 'q' to quit and view results: ")
        except ValueError:
            print("Please Enter 'y' or 'q'")
        else:
            if muiltiple_outcomes == "q":
                histogram_output()
                break

            elif muiltiple_outcomes == "y":
                pass
                break

            else:
                print("Please Enter 'y' or 'q'")

    return muiltiple_outcomes





# main menu entry

def main_menu():
    while True:
        print("\n")
        try:
            menu = input("Enter '1' to open Student version: \n"
                              "Enter '2' to open Staff version: \n"
                              "Enter 'q' to Quit: ")
        except ValueError:
            print("Please enter 1 , 2 or q to quit.")
            continue
        else:
            if menu == "q":
                print("'q'  pressed, Quit programme")
                quit()
            elif menu == "1":
                print("-" * 60)
                print("Student Version\n")
                validation()

            elif menu == "2":
                print("-" * 60)
                print("Staff Version and Histogram\n")
                while True:
                    staff_validation()
                    muiltiple_outcomes = run_again()
                    if muiltiple_outcomes == "q":
                        break


main_menu()


