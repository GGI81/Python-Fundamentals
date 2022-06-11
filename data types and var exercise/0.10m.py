lost = int(input())
hprice = float(input())
sprice = float(input())
shprice = float(input())
aprice = float(input())
kaski = 0
mechove = 0
shtitowe = 0
broni = 0
s = 0
for i in range(1, lost):
    if i % 2 == 0:
        kaski += 1
    if i % 3 == 0:
        mechove += 1
    if i % 3 == 0 and i % 2 == 0:
        shtitowe += 1
        s += 1
    if s == 2:
        broni += 1
        s = 0

expenses = kaski * hprice + mechove * sprice + shtitowe * shprice + broni * aprice
print(f"Gladiator expenses: {expenses:.2f} aureus")
