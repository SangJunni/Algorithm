words = input()
result = [''] * len(words)
def dfs(words, idx):
    global result
    if len(words) == 0:
        return
    small = min(words)
    small_idx = words.index(small)
    result[idx + small_idx] = small
    print(''.join(result))
    dfs(words[small_idx+1:], idx + small_idx + 1)
    dfs(words[:small_idx], idx)

dfs(words,0)
