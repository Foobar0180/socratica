import datetime


class User:
    """
    Classes provide a means of bundling data and functionality together.
    Creating a new class creates a new type of object, allowing new
    instances of that type to be made. Each class instance can have
    attributes attached to it for maintaining its state. Class instances
    can also have methods (defined by its class) for modifying its state.
    """

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyymmdd

        # Extract first and last names
        name_split = full_name.split(" ")
        self.first_name = name_split[0]
        self.last_name = name_split[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2018, 4, 18)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        date_of_birth = datetime.date(yyyy, mm, dd)
        age_in_days = (today - date_of_birth).days
        age_in_years = age_in_days / 365

        return int(age_in_years)


user = User("Foo Bar", "19800124")
print(user.age())
