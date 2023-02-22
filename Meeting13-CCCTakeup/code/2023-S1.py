# CCC '23 J4/S1 - Aritro Saha
c = int(input())

# Gathering input, True represents a black triangle and False represents a white triangle
row1 = [bool(int(triangle)) for triangle in input().split()]
row2 = [bool(int(triangle)) for triangle in input().split()]

# The maximum tape that we need is the number of black triangles * the edges per triangle (3)
tape = (row1.count(True) + row2.count(True)) * 3

# Checking for left-right adjacency in both rows
for i in range(c - 1):
  if row1[i] and row1[i + 1]:
    tape -= 2  # Subtract 2 because one edge on both adjacent triangles aren't needed

  if row2[i] and row2[i + 1]:
    tape -= 2

# Checking for top-bottom adjacency
for i in range(c):
  # If the triangles are pointing into each other, they don't share an edge
  # Referring to the diagram, this only happens on even triangle columns (starting at 0)
  if row1[i] and row2[i] and i % 2 == 0:
    tape -= 2

print(tape)