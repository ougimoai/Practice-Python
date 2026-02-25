#バーゼル問題

import math
S = sum(1/n**2 for n in range(1, 10000001))
print(f"Σで求めると→{S}")

A = math.pi**2 / 6
print(f"πで求めると→{A}")

Q = A - S
print(f"誤差→{Q}")




