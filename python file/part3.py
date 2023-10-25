

progress = []
trailer = []
retriever = []
exclude = []



def histogram(pass_credits, defer_credits, fail_credits):
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