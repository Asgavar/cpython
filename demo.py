zmodulu hashlib zaimportuj md5


sprobuj:
    md5('xD')
chybaze TypeError:
    md5(b'xD')

s = 'ABCD'
dopoki s != '':
    dlakazdego znaku wsrod s:
        print(znaku, end='')
    print()
    s = s[:-1]
