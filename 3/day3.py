## Advent of Code 2022 day 3: decoding shipping lists

if __name__ == '__main__':

    data = open('input.txt', 'r')
    lines = data.readlines()

    # let's use unicode for points.. a is 97, b is 98, etc, but what's uppercase?
    # well let's just use chr(n) for unicode character from its #, and ord('chr') for reverse
    lower_character_map = {chr(ord('a')+n):n+1 for n in range(26)}
    upper_character_map = {chr(ord('A')+n):n+27 for n in range(26)}
    # it appears to work, let's put them all in one
    character_map = {**lower_character_map, **upper_character_map}
    
    value_accumulator = 0
    
    for line in lines:
        item_count, container_size = len(line), len(line)//2
        # let's do some simple string slicing
        left_string = line[0 : container_size]
        right_string = line[container_size : item_count-1] # minus-1 to skip newline
        left_values = []
        right_values = []
        for char in left_string:
            value = character_map[char]
            left_values.append(value)
        for char in right_string:
            value = character_map[char]
            right_values.append(value)
        # seems like a job for set operations. should only be one value if the prompt isn't lying
        value = list(set(left_values).intersection(set(right_values)))[0]
        value_accumulator += value
    print(f'Accumulated values: {value_accumulator}')

    # part 2: grouping lines into 3s and also matching stuff.
    
    group_count = len(lines)//3
    value_accumulator = 0

    pack_groups = [[lines[n], lines[n+1], lines[n+2]] for n,_ in enumerate(lines) if n%3==0]
    for packs in pack_groups:
        group_values = []
        for pack in packs:
            pack_values = []
            for char in pack[0:len(pack)-1]:
                pack_values.append(character_map[char])
            group_values.append(pack_values)
        # since there's only three, no need to get too fancy
        first_two_match_set = set(group_values[0]).intersection(set(group_values[1]))
        badge_value = list(set(group_values[2]).intersection(first_two_match_set))[0]
        value_accumulator += badge_value

    print(f'Accumulated values: {value_accumulator}')

# This one was a little more elegant than day 2. I continue to find a good amount of utility from set manipulation,
# despite the clunkiness of switching back and forth with lists. I almost used some dreaded regular expressions, but
# the particular setup for this problem's answer (assigning integer values to the characters) forced me to create an
# character-to-integer key from the getgo which allowed me to avoid muddling through regex stuff... this time!