#AdvoOfCode2022 1

import pandas as pd

if __name__ == '__main__':

    data = open('input.txt', 'r')

    map = {}
    values = []
    counter = 0

    lines = data.readlines()
    for n, line in enumerate(lines):
        #print(f'n: {n}, length: {len(line)}')
        if len(line)==1:
            map[counter] = values.copy()
            values.clear()
            counter += 1
            continue
        values.append(int(line))

    # get the last one
    map[counter] = values.copy()

    def getGreediestElfAndValue(map):
        max_value = 0
        greediest_elf = -1
        for elf, food_cals in map.items():
            cals = sum(food_cals)
            if cals > max_value:
                max_value = cals
                greediest_elf = elf
        return greediest_elf, max_value

    first = getGreediestElfAndValue(map)
    greediest_elf, max_value = first
    print(f'Greediest elf is number {greediest_elf} with {max_value} total cals!')
    map.pop(greediest_elf)

    second = getGreediestElfAndValue(map)

    greediest_elf2, max_value2 = second
    print(f'Greediest elf is number {greediest_elf2} with {max_value2} total cals!')
    map.pop(greediest_elf2)

    third = getGreediestElfAndValue(map)

    greediest_elf3, max_value3 = third
    print(f'Greediest elf is number {greediest_elf3} with {max_value3} total cals!')
    
    top_three_sum = max_value + max_value2 + max_value3
    print(f'Top three summed: {top_three_sum}')