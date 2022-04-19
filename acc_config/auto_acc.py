import sys
import pyautogui


if 'toggle' == sys.argv[0]:
    s = sys.argv[1]
    now_num = 0
    next_num = 0
    for i in s:
        if i == 'b': next_num = 1
        elif i == 'c': next_num = 2
        elif i == 'd': next_num = 3
        elif i == 'e': next_num = 4
        elif i == 'f': next_num = 5
        elif i == 'g': next_num = 5

        for _ in range(next_num-now_num):
            pyautogui.press('down')
        pyautogui.press('space')
        now_num = next_num
    pyautogui.press('enter')