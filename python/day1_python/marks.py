marks = int(input("enter your marks: "))
if marks >= 90:
    print("Excellent")
elif 90 > marks >= 75:
    print("Very Good")
elif 75 > marks >= 60:
    print("Good")
elif 60 > marks >= 40:
    print("Pass")
else:
    print("Fail")