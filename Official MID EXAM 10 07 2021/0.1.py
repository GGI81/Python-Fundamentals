quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
weight = float(input())

q_f_grams = quantity_food * 1000
q_hay_gram = quantity_hay * 1000
q_cover_grams = quantity_cover * 1000
weight_in_grams = weight * 1000


for i in range(1, 31):
    if q_cover_grams <= 0 or q_f_grams <= 0 or q_hay_gram <= 0:
        break
    q_f_grams -= 300
    if i % 2 == 0:
        q_hay_gram -= q_f_grams * 0.05
    if i % 3 == 0:
        q_cover_grams -= weight_in_grams / 3


if q_cover_grams > 0 and q_f_grams > 0 and q_hay_gram > 0:
    print(f"Everything is fine! Puppy is happy! Food: {q_f_grams / 1000:.2f}, Hay: {q_hay_gram / 1000:.2f}, Cover: {q_cover_grams / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")