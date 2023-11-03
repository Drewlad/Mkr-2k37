name =input("Enter your name!")
which_class =input("Enter your class!")
marks =input("Enter your score!")
marks = int(marks)
if marks > 100:
    print("THE TOTEL AT YOUR LEVEL IS 100 PLS!")
if marks  <= 50  >= 45:
    print("you got a C-")
elif marks  <= 59 >= 50:
    print("you got a C+")
elif marks  <=69 >= 60:
    print("you got a B-")  
elif marks  <=79 >= 70:
    print("you got a B+")
elif marks  <= 89 >= 80:
    print("you got an A-")
elif marks <= 100 >= 90:
    print("you got an A+")
else:
    print("FAILED")

