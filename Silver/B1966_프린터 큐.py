iteration = int(input())
for i in range(iteration):
    document_num, position = list(map(int, input().split()))
    documents = list(map(int, input().split()))
    found = 0
    i = 0
    current_pos = position
    while found == 0:
        if documents[0] < max(documents) and current_pos == 0:
            documents.append(documents[0])
            documents.pop(0)
            current_pos = len(documents) - 1
        elif documents[0] < max(documents) and current_pos != 0:
            documents.append(documents[0])
            documents.pop(0)
            current_pos = current_pos - 1
        elif documents[0] >= max(documents) and current_pos == 0:
            i += 1
            print(i)
            found = 1
        elif documents[0] >= max(documents) and current_pos != 0:
            documents.pop(0)
            current_pos = current_pos - 1
            i += 1
