
###changes

num_terms = int(input("How many terms? "))

# first two terms
first_term, second_term = 0, 1
count = 0

# check if the number of terms is valid
if num_terms <= 0:
    print("Please enter a positive integer")
# if there is only one term, return first term
elif num_terms == 1:
    print("Fibonacci sequence up to", num_terms, ":")
    print(first_term)
# generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < num_terms:
        print(first_term)
        next_term = first_term + second_term
        # update values
        first_term = second_term
        second_term = next_term
        count += 1
