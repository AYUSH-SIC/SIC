'''PROBLEM STATEMENT :-
                    ACCEPT A NUMBER AND FIND THE NEXT SMALLEST POSSIBLE BIGGER NUMBER THAT MUST HAVE ALL DIGITS AS IN THE INPUT NUMBER '''

input_number = input("ENTER THE NUMBER : ")
input_list = list(input_number)
input_rev = input_list[::-1]
index = 0
for i in range(len(input_list) - 1):
    if (input_rev[i] > input_rev[i+1]):
        input_rev[i],input_rev[i+1] = input_rev[i+1],input_rev[i]
        index = i
        break

input_rev = input_rev[::-1]
if index < len(input_rev) & index > 0:
    index = len(input_list) - 2
    print(''.join(input_rev[0:index] + sorted(input_rev[index:])))
else :
    print(''.join(input_rev))
print(''.join(input_rev[0:index] + sorted(input_rev[index:])))