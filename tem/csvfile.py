import csv

with open("python5.csv", mode="w") as csvfile:
    fieldnames = ["StudentID","FirstName", "LastName","Major", "Gender","DateOfBirth","Email","Address","Ph_no","Nationality"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({"StudentID": 6609203, "FirstName": "Yu Waddy", "LastName": "Lwin","Major": "Computer Science", "Gender": "female","DateOfBirth": "1 Sept 2004","Email": "yu@gmail.com", "Address": "Myanmar","Ph_no":"081-737-4337", "Nationality":"Myanmar"})
    writer.writerow({"StudentID": 6609269, "FirstName": "Htet", "LastName": "Yawai","Major": "Computer Science", "Gender": "female","DateOfBirth":"13 July 2002","Email":"yawai@gmail.com","Address":"Thailand", "Ph_no": "092-234-534", "Nationality":"Myanmar"})
