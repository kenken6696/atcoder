#!/usr/bin/env python3

pages = int(input())
mod = pages % 2

if mod == 1:
    papers = pages // 2 + 1
else:
    papers = pages // 2

print(papers)