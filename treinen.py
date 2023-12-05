import json

def choose_train(number, train, all_trains):
    print(number)
    length = 0
    chosen_trains = []
    next_trains = []
    if train is None:
        length = 0
        chosen_trains = []
        next_trains = all_trains
    else:
        length = train[1] - train[0]
        chosen_trains = [train]
        next_trains = [next_train for next_train in all_trains if next_train[0] >= train[1]]
    next_trains_length = 0
    next_chosen_trains = []
    for next_train in next_trains:
        (candidate_length, candidate_chosen_trains) = choose_train(number + 1, next_train, all_trains)
        if candidate_length >= next_trains_length:
            next_trains_length = candidate_length
            next_chosen_trains = candidate_chosen_trains
        #else:
            #print(f'skipping candidate for train {number + 1}')
    return (length + next_trains_length, chosen_trains + next_chosen_trains)

with open('input.json') as inputJson:
    input = json.load(inputJson)
    all_trains = input
    print('total number of trains:', len(all_trains))
    (length, chosen_trains) = choose_train(0, None, all_trains)
    print('max length:', length)
    print(f'using {len(chosen_trains)} trains', chosen_trains)