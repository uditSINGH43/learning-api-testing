from faker import Faker


class TestdataGenerator:
    def test_fake_data(self):
        faker = Faker()  # local Variable
        fullname = faker.name()
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.safe_email()
        password = faker.password(length=6)
        phone_number = faker.phone_number()

        print("Full name: ", fullname)
        print("First Name: ", first_name)
        print("Last Name: ", last_name)
        print("Email: ", email)
        print("Password: ", password)
        print("Phone Number: ", phone_number)
