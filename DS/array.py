class Array:
    def search(self, arr,n, key):
        for i in range(n):
            if(arr[i]== key):
                return i

        return -1
    def insert_specific_loc(self, arr, value, pos):
        for i in reversed(range(pos)):
            arr[i+1] = arr[i]
        arr[pos] = value


if __name__ == '__main__':
    arr = [12, 45, 32, 6, 89, 2, 34, 54]
    size = len(arr)
    key = 6

    arr_obj = Array()
    result = arr_obj.search(arr, size, key)
    print('searching index')
    print(result)
    #travase the array
    print('before insertion')
    for i in range(size):
        print(arr[i])

    #after insertion
    print('after insertion')
    arr_obj.insert_specific_loc(arr, 100, 3)
    for i in range(len(arr)):
         print(arr[i])

