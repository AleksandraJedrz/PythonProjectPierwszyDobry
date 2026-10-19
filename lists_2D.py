points = [[1, 2, 5],
          [4, 5, 4],
          [7, 8, 8]]

print(points)
el_5 = points[1][1]
print(el_5)
print(type(points))
print(type(points[2]))

# for r in points:
#     print(r)
#     for c in r:
#         print(c)
print('\n' + '-'*80)

def sum_rows(my_list):
    result = []
    for r in my_list:
        row_sum = 0
        for c in r:
            row_sum += c
        result.append(row_sum)
    return result
print(sum_rows(points))

print('\n' + '-'*80)
def sum_cols(my_list):
    if not my_list:
        return []
    num_rows = len(my_list)
    num_cols = len(my_list[0])
    result = []
    for col in range(num_cols):
        col_sum = 0
        for row in range(num_rows):
            col_sum += my_list[row][col]
        result.append(col_sum)
    return result
print(sum_cols(points))

print('\n' + '-'*80)
def sum_lists(my_list):

print(sum_lists(points))

