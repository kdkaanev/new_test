def average_treasure_gain(item_list):
    tresure_sum = 0.0
    condition = ''
    for item in item_list:
        tresure_sum += len(item)
    if len(item_list) > 0:
        average = tresure_sum / len(item_list)
        condition = f"Average treasure gain: {average:.2f} pirate credits."
    else:
        condition = "Failed treasure hunt."
    return condition


def treasure(item_list):
    command = input()
    while command != "Yohoho!":
        data = command.split(' ')
        order = data[0]
        if order == 'Loot':
            for i in range(1, len(data)):
                if data[i] not in item_list:
                    item_list.insert(0, data[i])

        elif order == 'Drop':
            index = int(data[1])
            if index < len(item_list):
                x = item_list.pop(index)
                item_list.append(x)
        elif order == 'Steal':
            y = []
            count = int(data[1])
            if count < len(item_list):
                for i in range(count):
                    x = item_list.pop()
                    y.append(x)

                y.reverse()
                print(', '.join(y))
            else:
                print(', '.join(item_list))
                item_list.clear()

        command = input()
    print(average_treasure_gain(item_list))


treasure_chest = input()
treasure(treasure_chest.split('|'))
