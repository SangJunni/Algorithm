# TODO : 산타 전체 관리하는 리스트 만들기
# N : 맵크기, M: 게임턴수
# 필드내 루돌프 번호: -1, 산타는 자기 번호로 진행
N, M, P, C, D = map(int, input().split())
Rudolph = [x-1 for x in list(map(int, input().split()))]
Santas = []
Santa_score = [0]*P
field = [[0]*N for _ in range(N)]
field[Rudolph[0]][Rudolph[1]] = -1
for _ in range(P):
    s_num, s_x, s_y = list(map(int, input().split()))
    # 산타번호, 위치정보(x, y), 상태(-1: 탈락, 0: 정상 1: 기절)
    Santas.append([s_num, s_x-1, s_y-1, 0])
    field[s_x-1][s_y-1] = s_num
Santas.sort(key= lambda x : x[0])
# 산타의 이동 방향 정의: 상우하좌 우선순위에 맞춰 정의
s_move = [(-1,0),(0,1),(1,0),(0,-1)]
while M*P != 0: # 턴이 끝나거나 활동 가능한 산타가 없을 경우 종료
    # 루돌프 턴 구현
    target_santa = []
    for idx, santa_info in enumerate(Santas):
        s_num, s_x, s_y, s_status = santa_info
        # 활동 불가 상태이면 생략
        if s_status < 0:
            continue
        distance = (Rudolph[0] - s_x)**2 + (Rudolph[1] - s_y)**2
        target_santa.append((distance, s_x, s_y, s_num))
    # 우선 순위 조건 대로 정렬(거리, r이 큰 경우, c가 큰 경우
    target_santa.sort(key = lambda x : (x[0], -x[1], -x[2]))
    _, t_x, t_y, t_num = target_santa[0]
    m_x, m_y = 0,0
    if Rudolph[0] < t_x:
        m_x = 1
    elif Rudolph[0] > t_x:
        m_x = -1
    if Rudolph[1] < t_y:
        m_y = 1
    elif Rudolph[1] > t_y:
        m_y = -1
    field[Rudolph[0]][Rudolph[1]] = 0
    Rudolph = [Rudolph[0]+m_x, Rudolph[1]+m_y]
    # 충돌 발생 -> 이동한 자리에 산타가 있음
    # 루돌프가 달려들 경우 : C점을 얻고 C칸 밀려남
    if field[Rudolph[0]][Rudolph[1]] != 0:
        att_num, att_x, att_y, att_status = Santas[field[Rudolph[0]][Rudolph[1]]-1]
        Santa_score[att_num-1] += C
        att_x += m_x * C
        att_y += m_y * C
        # 밀리는 경우
        if att_x < 0 or att_x >= N or att_y < 0 or att_y >= N:
            Santas[att_num - 1] = [att_num, att_x, att_y, -1]
            P -= 1
        else:
            Santas[att_num-1] = [att_num, att_x, att_y, 2]
            while att_num != 0:
                next_att_num = field[att_x][att_y]
                field[att_x][att_y] = att_num
                att_x += m_x
                att_y += m_y
                att_num = next_att_num
                # 범위 벗어난 경우
                if att_num == 0:
                    break
                if att_x < 0 or att_x >= N or att_y < 0 or att_y >= N:
                    Santas[att_num-1] = [att_num, att_x, att_y, -1]
                    P -= 1
                    break
                else:
                    Santas[att_num-1] = [att_num, att_x, att_y, 0]
    field[Rudolph[0]][Rudolph[1]] = -1
    # 산타턴 구현
    for idx, santa_info in enumerate(Santas):
        s_num, s_x, s_y, s_status = santa_info
        current_dist = (Rudolph[0] - s_x)**2 + (Rudolph[1] - s_y)**2
        move_dir = -1
        if s_status != 0:
            continue
        for way in range(4):
            nx = s_x + s_move[way][0]
            ny = s_y + s_move[way][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or field[nx][ny] > 0:
                continue
            dist = (Rudolph[0] - nx)**2 + (Rudolph[1] - ny)**2
            if dist < current_dist:
                current_dist = dist
                move_dir = way
        #이동이 가능한 경우
        if move_dir != -1:
            nx = s_x + s_move[move_dir][0]
            ny = s_y + s_move[move_dir][1]
            # 루돌프와 충돌한 경우
            if field[nx][ny] == -1:
                Santa_score[idx] += D
                bounce_x = nx + (-s_move[move_dir][0])*D
                bounce_y = ny + (-s_move[move_dir][1])*D
                field[s_x][s_y] = 0
                if bounce_x < 0 or bounce_x >= N or bounce_y < 0 or bounce_y >= N:
                    Santas[idx] = [idx + 1, bounce_x, bounce_y, -1]
                    P -=1
                else:
                    Santas[idx] = [idx+1, bounce_x, bounce_y, 2]
                    current_santa = idx+1
                    while current_santa != 0:
                        next_santa = field[bounce_x][bounce_y]
                        field[bounce_x][bounce_y] = current_santa
                        bounce_x -= s_move[move_dir][0]
                        bounce_y -= s_move[move_dir][1]
                        current_santa = next_santa
                        if current_santa == 0:
                            break
                        if bounce_x < 0 or bounce_x >= N or bounce_y < 0 or bounce_y >= N:
                            Santas[current_santa-1] = [current_santa, bounce_x, bounce_y, -1]
                            P -= 1
                            break
                        else:
                            Santas[current_santa-1] = [current_santa, bounce_x, bounce_y, Santas[current_santa-1][-1]]
            else:
                Santas[idx] = [idx+1, nx, ny, 0]
                field[nx][ny] = idx + 1
                field[s_x][s_y] = 0
    # 기절 상태 상태 및 생존 점수 추가
    for idx, santa in enumerate(Santas):
        if santa[-1] > 0:
            santa[-1] -= 1
        if santa[-1] >= 0:
            Santa_score[idx] += 1
    M -= 1
print(*Santa_score)