def read(name):
    with open(name, 'r') as file:
        return [line.rstrip() for line in file]


def delete(name_file, erase):
    arr = read(name_file)
    erase = erase.strip()
    with open(name_file, 'w') as file:
        for line in arr:
            if erase != line:
                file.write(line + '\n')


def add(name_file, line_add, *files):
    for file in files:
        if line_add in read(file):
            return False
    line_add = line_add.strip()
    with open(name_file, 'a') as file:
        file.write(line_add + '\n')
    return True


def done(name_file_from, line_done, name_file_to):
    delete(name_file_from, line_done)
    add(name_file_to, line_done)


if __name__ == '__main__':
    # print(read('data'))
    done('done', '323969', 'done')

"""
asd
zxc
cxv
fgs
ffgfg
sample
"""
