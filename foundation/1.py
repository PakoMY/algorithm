import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout
    # Edit and remove this code as you like.
    n = len(lines)
    maxl = 0
    start = 0
    for i in range(n):
        print('i  ', i)
        if i - maxl >= 1 and lines[i-maxl-1: i+1] == lines[i-maxl-1: i+1][::-1]:
            print("lines[i-maxl-1: i+1]:", lines[i-maxl-1: i+1])
            start = i - maxl - 1
            maxl += 2
            print("start: " , start, "maxl: ", maxl)
            continue
        if i - maxl >= 0 and lines[i-maxl: i+1] == lines[i-maxl: i+1][::-1]:
            print("lines[i-maxl: i+1]:", lines[i-maxl: i+1])
            start = i - maxl
            maxl += 1
            print("start: " , start, "maxl: ", maxl)
    print(lines[start: start + maxl])

main('43343321')
