def sort_final_output(targets):
    targets = list(map(lambda x: str(x), targets))
    targets = "|".join(targets)
    return targets


def shooting(given_command, targets):
    index = int(given_command[1])
    value = int(given_command[2])
    if 0 <= index < len(targets):
        if targets[index] > value:
            targets[index] -= value
        else:
            targets.pop(index)
    return targets


def adding(given_command, targets):
    index = int(given_command[1])
    value_to_add = int(given_command[2])
    if 0 <= index < len(targets):
        targets.insert(index, value_to_add)
    else:
        print("Invalid placement!")
    return targets


def striking(given_command, targets):
    strike_index = int(given_command[1])
    radius = int(given_command[2])
    left_index = strike_index - radius
    right_index = strike_index + radius
    if 0 <= left_index and right_index < len(targets):
        left_part = targets[:left_index]
        right_part = targets[right_index + 1:]
        together = left_part + right_part
        targets.clear()
        targets.extend(together)
    else:
        print("Strike missed!")
    return targets


sequence_of_targets = list(map(lambda x: int(x), input().split(" ")))
while True:
    command = input().split(" ")
    if "Shoot" in command:
        shooting(command, sequence_of_targets)
    elif "Add" in command:
        adding(command, sequence_of_targets)
    elif "Strike" in command:
        (striking(command, sequence_of_targets))
    elif "End" in command:
        print(sort_final_output(sequence_of_targets))
        break