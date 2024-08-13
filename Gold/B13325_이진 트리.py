def calculate_minimum_weight_sum(k, weights):
    dfs(0)
    return sum(weights) + weight_increase


def dfs(node):
    global weight_increase
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    # 리프 노드에 도달한 경우
    if left_child >= len(weights) and right_child >= len(weights):
        return 0
    left_sum = 0
    right_sum = 0
    # 왼쪽과 오른쪽 자식의 최대 거리 계산
    if left_child < len(weights):
        left_sum = dfs(left_child) + weights[left_child]

    # 오른쪽 자식 노드가 있는 경우에만 값 계산
    if right_child < len(weights):
        right_sum = dfs(right_child) + weights[right_child]

    # 현재 노드에서 양쪽 자식이 같은 거리를 가지도록 조정
    weight_increase += abs(left_sum - right_sum)

    # 자식 중 더 큰 거리를 반환하여 부모 노드로 합산
    return max(left_sum, right_sum)


# 입력 처리
k = int(input())
weights = [0] + list(map(int, input().split()))

# 결과 계산 및 출력
weight_increase = 0  # 증가된 가중치를 저장하기 위한 리스트
result = calculate_minimum_weight_sum(k, weights)
print(result)
