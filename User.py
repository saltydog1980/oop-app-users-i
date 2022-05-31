class User:
    def __init__(self, name, age, phone_number, email_address):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email_address = email_address

bob = User('Bob', 42, '(123)-222-4444', 'bob@mail.com')
cindy = User('Cindy', 55, '(123)-222-4444', 'cindy@mail.com')
tim = User('Tim', 32, '(123)-222-4444', 'tim@mail.com')
chuck = User('Chuck', 59, '(123)-222-4444', 'chuck@mail.com')


print(tim.phone_number)