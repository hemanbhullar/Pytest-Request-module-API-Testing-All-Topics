from faker import Faker

class TestFakeDataGeneration:
    def test_fake_data_generation(self):
        faker = Faker() # local variable
        fullname = faker.name()
        firstname = faker.first_name()
        lastname = faker.last_name()
        email = faker.safe_email()
        password = faker.password(length=8)
        phone = faker.phone_number()

        print("firstname: ", firstname)
        print("lastname: ", lastname)
        print("email: ", email)
        print("password: ", password)
        print("phone: ", phone)
        print("fullname: ", fullname)
