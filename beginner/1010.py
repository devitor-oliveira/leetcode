p1_code, p1_qt, p1_unitPrice, = input().split(" ")
p2_code, p2_qt, p2_unitPrice, = input().split(" ")

p1_bill:float = float(p1_unitPrice) * int(p1_qt)
p2_bill:float = float(p2_unitPrice) * int(p2_qt)

total_bill: float = p1_bill + p2_bill

print(f"VALOR A PAGAR: R$ {total_bill:.2f}")