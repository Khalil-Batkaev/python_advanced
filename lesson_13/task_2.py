def get(dct: dict, key, val=None):
    try:
        result = dct[key]
    except KeyError as e:
        print(f'{e = }')
        result = val
    return result


if __name__ == '__main__':
    d = {1: 1, 2: '2222', 3: 3}
    print(get(d, 45, 'Hi'))