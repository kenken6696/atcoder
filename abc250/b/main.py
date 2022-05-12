#!/usr/bin/env python3

n, a, b = map(int, input().split())
x = ['' for _ in range(n)]
def make_i_tiles(start_color, a, b, n):
    w_tile = '.'*b
    b_tile = '#'*b
    color = start_color
    tile_c = ''
    for i in range(n):
        if color == 'w':
            tile_c += w_tile
            color = 'b'
        else:
            tile_c += b_tile
            color = 'w'
    i_tiles = [tile_c for _ in range(a)]
    return i_tiles

start_color = 'w'
for i in range(n):
        x[i] = make_i_tiles(start_color, a, b, n)
        if start_color == 'w':
            start_color = 'b'
        else:
            start_color = 'w'

for i in range(n):
    for xi in x[i]:
        print(xi)