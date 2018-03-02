# functions
def run():
    dic = {};

    print('type(dic) :', type(dic))

    dic['name'] = 'python'
    dic['version'] = '3'
    dic['desc'] = 'python language'

    for k, v in dic.items():
        print('%s: value is %s' % (k, v))

    print('dic :', dic)

    print('dic["name"] :', dic['name'])

    del dic['name']
    print('dic :', dic)

    print('dic.keys() :', dic.keys())

    print('dic.values() :', dic.values())

    print('version' in dic.keys())

# implementation
if __name__ == '__main__':
    run()