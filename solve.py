def split_array(ipt: str) -> list:
    ll = []
    exclude = {'[', ']'}
    split = {' ', ','}
    for x in exclude:
        if x in ipt:
            ipt = ipt.replace(x, '')

    for x in split:
        if x in ipt:
            ll = [int(num) for num in ipt.split(x) if num.strip()]
            return ll

    return ll

def cin(type: str):
    x = input()
    if type == 'arr':
        return split_array(x)
    elif type == 'int':
        return int(x)
    elif type == 'str':
        return str(x)
    else:
        print('Type not found.')

if __name__ == "__main__":
    t = cin('int')
    nums = cin('arr')

