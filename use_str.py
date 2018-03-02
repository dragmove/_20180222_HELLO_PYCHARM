# functions
def run():
    str = 'hello python'

    # memory address
    print('id(str) :', id(str))

    print('type(str) :', type(str))

    print('len(str) :', len(str))

    print('str[0:3] :', str[0:3])

    print('str[:5] :', str[:5])

    print('str[6:] :', str[6:])

    print('str.split(" ") :', str.split(' '))

# implementation
if __name__ == '__main__':
    run()