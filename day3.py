# Write a Python program that takes a student's marks in three subjects as input.
# If the average is greater than or equal to 90, print "Grade: A".
# If the average is between 80 and 89, print "Grade: B".
# If the average is between 70 and 79, print "Grade: C".
# Otherwise, print "Grade: Fail".
s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
avg = (s1 + s2 + s3) / 3
if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")   
else:
    print("Grade: Fail")

    