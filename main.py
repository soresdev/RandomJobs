from Job import Job

# Start
print("Hello, this is a game where you will be assigned a random job.")
print("Let's start by inputting your name.")

# Get their name
user_name = str(input('\nTell us your name: '))

# Get their age
user_age = int(input('\nTell us your age: '))

print(f'Ok {user_name}, we will now find you a job!')

# Create the job object
job = Job(user_name, user_age)

# Hire them
job.hire()
