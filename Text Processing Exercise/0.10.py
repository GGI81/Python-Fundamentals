tickets = input().split(", ")

for ticket in tickets:
    if len(ticket) != 20:
        print("Invalid ticket")
        continue

    left_half = ticket[:10]
