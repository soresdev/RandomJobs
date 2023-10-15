import random

# List of jobs to choose from
jobs = ["Fry Cook",
        "Police Officer",
        "Doctor",
        "Construction Worker",
        "Teacher",
        "Vet",
        "Truck Driver",
        "Stripper",
        "Pizza Delivery Driver"]

# Create a random job
random_job = jobs[random.randint(0, len(jobs))]
random_salary = None


class Job:
    def __init__(self, name: str = "sores", age: int = 18):
        self.name = name
        self.age = age
        self.jobs = jobs

    # Hire the person to a random job making a random salary
    def hire(self):
        age = self.age
        global random_salary

        # If age is 25-35, set their pay between 1400-2200
        if 25 < age <= 35:
            random_salary = random.randint(1400, 2200)

        # If age is 18-25, set their pay between 800-1250
        elif 18 < age <= 25:
            random_salary = random.randint(800, 1250)

        elif age > 35:
            random_salary = random.randint(2500, 3200)

        # If they're under 18 don't hire them
        elif age < 18:
            return print(f'Sorry {self.name}, you are under 18 and cannot be hired.')

        print(f'Congratulations {self.name}, you have been hired as a {random_job}.')
        print(f'You will be making ${random_salary} weekly!')

        chosen_value = jobs.index(random_job, 0, len(jobs))
        print(f'\nYou were assigned job {chosen_value + 1} out of {len(jobs)} other jobs.')
