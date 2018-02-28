# function
def run():
    person_1 = Contact('kim', '010-8888-9999', 'kim@naver.com', 'seoul')
    person_1.print_info()

# implementation
if __name__ == '__main__':
    run()

# Contact Class
class Contact:
    def __init__(self, name, phone_number, email, addr):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.addr = addr

    def print_info(self):
        print('name :', self.name)
        print('phone_number :', self.phone_number)
        print('email :', self.email)
        print('addr :', self.addr)
