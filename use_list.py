# functions
def run():
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print('list[0] :', list[0])

    print('list[1] :', list[1])

    print('list[3:]', list[3:])

    print('list[:2]', list[:2])

    print('list[1:4]', list[1:4])

    list.append('h')
    print('list :', list)

    for val in list:
        print('this is %s' % val)

    del list[-2:]
    print('list :', list)

# implementation
if __name__ == '__main__':
    run()