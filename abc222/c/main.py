#!/usr/bin/env python3

n, m = map(int, input().split())
players_hands = []
players_winnum = {i:0 for i in range(1, 2*n+1)}
for _ in range(2*n):
    players_hands.append(list(input()))



def play(k):
    for i in range(1, 2*n+1):
    players_hands[players_ranking[i]-1][k]
     players_ranking[i+1]]

def sort_player():
    rank_sorted = sorted(players_winnum.items(), key=lambda x:x[1])
    