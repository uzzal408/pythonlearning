from datetime import datetime
MAX = 1000
arr = [0 for i in range(MAX) for i in range(MAX)]
def rowMajor():
    global arr
    for i in range(MAX):
        for j in range(MAX):
            a = [i,j]
def colMajor():
    global arr
    for i in range(MAX):
        for j in range(MAX):
            a = [i, j]


if __name__ == '__main__':
    t = datetime.now()
    print(t)
    rowMajor()
    t = datetime.now() - t
    t = t.total_seconds()
    print('Row Major Access Time: ', t)

    t = datetime.now()
    colMajor()
    t = datetime.now()-t
    t = t.total_seconds()
    print('Col  Major Access Time: ', t)