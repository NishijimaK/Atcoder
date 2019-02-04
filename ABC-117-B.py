"""
https://atcoder.jp/contests/abc117/tasks/abc117_b
"""
N = input() #N角形
sides_length = input().split()
sides_length = [int(i) for i in sides_length]
sides_total = 0
#定理:一番長い辺が他のN-1辺の長さの合計よりも真に短い場合に限り、条件を満たすN角形が描ける。
for i in range(int(N)):
    sides_total += int(sides_length[i])
sides_max = max(sides_length)
total_Nomax = int(sides_total) - int(sides_max)

if int(sides_max) < int(total_Nomax):
    print("Yes")
else:
    print("No")