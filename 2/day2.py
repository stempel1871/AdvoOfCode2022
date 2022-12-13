#AdvoOfCode2022 2



if __name__ == '__main__':

    data = open('input.txt', 'r')

    lines = data.readlines()

    response_point_map = {'X':1, 'Y':2, 'Z':3}
    rock_response_point_map = {'X':3, 'Y':6, 'Z':0}
    paper_response_point_map = {'X':0, 'Y':3, 'Z':6}
    scissors_response_point_map = {'X':6, 'Y':0, 'Z':3}
    endcond_point_map = {'win':6, 'draw':3, 'lose':0}

    round_point_list = []
    for line in lines:
        call, _, response, _ = line
        resp_points = response_point_map[response]

        if call=='A':
            points = resp_points + rock_response_point_map[response]
        elif call=='B':
            points = resp_points + paper_response_point_map[response]
        elif call=='C':
            points = resp_points + scissors_response_point_map[response]

        round_point_list.append(points)

    total = sum(round_point_list)
    print(f'Total points, part 1: {total}')

    calls = ['A','B','C']
    rpts = [1, 2, 3]
    resp_point_map2 = {calls[n]:rpts[n] for n in range(3)}
    end_cond_point_map = {'X':0, 'Y':3, 'Z':6}
    response_win_map = {'A':'B', 'B':'C', 'C':'A'}
    response_lose_map = {'A':'C', 'B':'A', 'C':'B'}
    response_draw_map = {thing:thing for thing in calls}
    end_cond_map_map = {'X':response_lose_map, 'Y':response_draw_map, 'Z':response_win_map}

    round_point_list.clear()
    for line in lines:
        call, _, end_cond, _ = line
        end_cond_points = end_cond_point_map[end_cond]
        needed_throw = end_cond_map_map[end_cond][call]
        total_points = end_cond_points + resp_point_map2[needed_throw]
        round_point_list.append(total_points)

    total = sum(round_point_list)
    print(f'Total points, part 2: {total}')

    # An inelegant exploration of some brute force mapping, but it works! On to the next.

