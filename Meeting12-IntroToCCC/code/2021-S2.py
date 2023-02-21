M = int(input())
N = int(input())
K = int(input())
 
row = ["B"] * M
col = ["B"] * N
 
for i in range(K):
  stroke = input().split(" ")
  if stroke[0] == "R":
    if row[int(stroke[1]) - 1] == "B":
      row[int(stroke[1]) - 1] = "G"
    else:
      row[int(stroke[1]) - 1] = "B"
  if stroke[0] == "C":
    if col[int(stroke[1]) - 1] == "B":
      col[int(stroke[1]) - 1] = "G"
    else:
      col[int(stroke[1]) - 1] = "B"
 
gold = 0
for i in range(M):
  for j in range(N):
    if row[i] == "B":
      if col[j] == "G":
        gold += 1
    else:
      if col[j] == "B":
        gold += 1
 
print(gold)