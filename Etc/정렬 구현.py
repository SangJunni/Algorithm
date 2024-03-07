def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i+1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    print(array)


def insert_sort(data):
    for i in range(len(data)):
        for j in range(i, 0 , -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
            else:
                break
    print(array)


def quick_sort(data):
    if len(data) <=1:
        return data
    pivot = data[0]
    tail = data[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def coefficient_sort(data):
    sort_array = [0] * (max(data)+1)

    for i in range(len(data)):
        sort_array[data[i]]+=1

    #출력
    for i in range(len(sort_array)):
        for j in range(sort_array[i]):
            print(i, end=' ')


array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
selection_sort(array)
insert_sort(array)
coefficient_sort(array)
print()
print(quick_sort(array))