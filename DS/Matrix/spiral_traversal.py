def spiral_traversal(arr):
    ans = []
    length = len(arr)
    if( length  == 0):
        return ans
    m = length
    n = len(arr[0])
    seen = [[0 for i in range(n)] for i in range(m)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    di = 0
    x = 0
    y = 0

    for i in range(m*n):
        ans.append(arr[x][y])
        seen[x][y] = True
        cr = x + dr[di]
        cc = y + dc[di]
        if(0 <= cr and cr<m and 0 <= cc and cc<n and not (seen[cr][cc]) ):
            x = cr
            y = cc
        else:
            di = (di+1) % 4
            x += dr[di]
            y += dc[di]
    return ans



if __name__ == '__main__':
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    ans = spiral_traversal(arr)
    for x in ans:
        print(x, end=" ")
    print()


