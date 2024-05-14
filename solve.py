def split_array(ipt: str) -> list:
    ll = []
    exclude = {'[', ']'}
    split = {' ', ','}
    count = 0
    
    for x in exclude:
        if x in ipt:
            ipt = ipt.replace(x, '')
            count+=1

    for x in split:
        if x in ipt:
            ll = [int(num) for num in ipt.split(x) if num.strip()]
    if ll:
        return ll 
    else:
        ll.append(int(ipt))

    
    return ll
def cin(type: str) -> list | int | str:
    x = input()
    if type == 'arr':
        return split_array(x)
    elif type == 'int':
        return int(x)
    elif type == 'str':
        return str(x)
    else:
        print('Type not found.')
        return None

def parr(ll: list):
    for i, ans in enumerate(ll):
        print(f'Case #{i+1}: {ans}')

def output(t:int, type:str):
    output = []
    for i in range(t):
        nums = cin(type)
        output.append(nums)
    return output

if __name__ == "__main__":
    nums = cin('arr')
    print(nums)

