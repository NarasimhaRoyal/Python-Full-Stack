import smtplib

# Get student details
name = input("Enter student name: ")
course = input("Enter course: ")
marks = int(input("Enter marks: "))

# Decide result
if marks >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Write details into a file
with open("student.txt", "w") as file:
    file.write("STUDENT REPORT\n")
    file.write("----------------\n")
    file.write("Name: " + name + "\n")
    file.write("Course: " + course + "\n")
    file.write("Marks: " + str(marks) + "\n")
    file.write("Result: " + result + "\n")

print("\nStudent details saved to file.")


# Read the file
with open("student.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)


# Email details
sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "your_app_password"

subject = "Student Report"

message = f"""
Hello,

Please find the student report below:

{content}

Thank you.
"""

email = "Subject: " + subject + "\n\n" + message


# Send email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender, password)

    server.sendmail(sender, receiver, email)

    server.quit()

    print("Email sent successfully!")

except Exception as e:
    print("Email error:", e)    