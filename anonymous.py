#When called anonymously called a function, then it's called lambada function
#Labmada has no name
#define labmada with lamada and no def keywrod used

#example-1
mul = lambda x:x*100
print(mul(5))

#used in filter
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li)
new_list = list(filter(lambda x: (x%2==1),li))
print(new_list)
#used in mapping
new_list = list(map(lambda x:x*3,li))
print(new_list)