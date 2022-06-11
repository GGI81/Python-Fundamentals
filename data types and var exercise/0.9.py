n = int(input())
snowball_value = 0
max_value = 0
max_snow = 0
max_time = 0
max_quality = 0

for snowball in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value >= max_value:
        max_quality = snowball_quality
        max_snow = snowball_snow
        max_value = snowball_value
        max_time = snowball_time
print(f"{max_snow} : {max_time} = {max_value:.0f} ({max_quality})")