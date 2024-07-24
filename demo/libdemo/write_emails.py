
emails = ("scott@gmail.com", "larry@google.com", "bill@microsot.com",
          "ellison@oracle.com", "marks@facebook.com", "steve@gmail.com",
          "allen@microsoft.com")

f = open("emails.txt", "wt")

for email in emails:
    f.write(email + "\n")

f.close()


