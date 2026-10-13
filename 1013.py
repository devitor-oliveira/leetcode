A, B, C = map(int, input().split(" "))

maiorAB: int = (A+B+abs(A-B)) / 2
maior:int  = (C + maiorAB + abs(C - maiorAB)) / 2

print(f"{maior:.0f} eh o maior")