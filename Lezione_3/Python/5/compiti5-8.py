'''5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'. 
Imagine you are writing code that will print a greeting to each user after they log in to a website. 
Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.'''

usernames : list = ["Admin", "Francesco", "Federico", "Riccardo", "Jacopo"]

for name in usernames: 
    if name == "Admin":
        print("Hello Admin you rock")
    else:
        print(f"Hello {name}")

i = 0

while i < len(usernames):
    if usernames[i] == "Admin":
        print("Hello Admin you rock")
    else:
        print(f"Hello {usernames[i]}")
    i += 1