arr_a = [3, 5, 7, 9, 5, 9]
for i in arr_a:
    print(i, end=' ')

print('\n' + '-'*80)
print('sets')
set_a = set(arr_a)

for i in set_a:
    print(i, end=' ')
set_b = set_a.copy()
set_b.remove(9)
print(set_b)

list_a = list(set_a)
print(list_a)
print(list_a[2])

list_a.insert(2, 100)
print(list_a)



