want_intructions =input("Do you want to see the intructions?") . lower ()

# check the user says yes / no
if want_intructions == "yes" or want_intructions == "y":
    print("you said yes")
elif want_intructions =="no" or want_intructions == "n":
    print("you said no")
else:
    print("please enter yes / no")

