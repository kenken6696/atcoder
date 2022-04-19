# 未完
h, w = map(int, input().split())
table = [ [9]* w for _ in range(h)]
for i in range(h):
    l = input()
    for j in range(w):
        if l[j] == '#':
            table[i][j] = 0
        elif l[j] == '.':
            table[i][j] = 1

max_length = [0] * h
for i in range(h):
    l = table[i]
    temp_cl = []
    temp_l = []
    temp_c = 0
    s, e = 0, 0
    for j in range(w):
        if table[i][j] == 0:
            if temp_c > 0:
                temp_cl.append(temp_c)
                temp_l.append([s, e])
            temp_c = 0
            s, e = j+1, j+1
        else:
            temp_c += 1
            e = j
        if j == w-1 and temp_c > 0:
            temp_cl.append(temp_c)
            temp_l.append([s, e])
    m_i = temp_cl.index(max(temp_cl))
    max_length[i] = [temp_cl[m_i]] + temp_l[m_i]

area_l = []
def search_area(i):
    global area_l
    next_i = -1
    temp_wl = max_length[i]
    t_h, t_w = 1, temp_wl[0]
    for ii in range(i+1,h):
        ii_wl = max_length[ii]
        if temp_wl[1] >= ii_wl[1] or temp_wl[2] <= ii_wl[2]:
            if next_i == -1: # 初回のみ更新
                next_i = ii
        if temp_wl[1] >= ii_wl[1] and temp_wl[2] <= ii_wl[2]:
            # 採れる面積が前回より広いか同じ時
            t_h += 1
            continue
        elif temp_wl[1] > ii_wl[2] or temp_wl[2] < ii_wl[1]:
            # 採れる面積が全くかぶらない時
            area_l.append(t_h*t_w)
            return next_i

        else: # 採れる面積が前回未満の時
            area_l.append(t_h*t_w)
            t_w = min(temp_wl[2], ii_wl[2]) - max(temp_wl[1], ii_wl[1]) + 1 # 横を狭めて最後までいく
            t_h += 1

        if ii == h-1:
            area_l.append(t_h*t_w)

    return next_i

search_i = 0
while search_i >= 0:
    search_i = search_area(search_i)
print(max(area_l))