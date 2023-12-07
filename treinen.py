import json


    

class Train:

    def __init__(self, index, times):
        self.index = index
        self.times = times
        self.sequence = None
    
    @property
    def start(self):
        return self.times[0]
    
    @property
    def end(self):
        return self.times[1]
    
    @property
    def length(self):
        return self.end - self.start
    
    def __str__(self) -> str:
        return f'[{self.index}]({self.start} -> {self.end})'
    
    def get_sequence(self, all_trains):
        if self.sequence is not None:
            return self.sequence
        sequence = self._calculate_sequence(all_trains)
        self.sequence = sequence
        return sequence
    
    def _calculate_sequence(self, all_trains):
        next_index_train = all_trains[self.index + 1] if self.index < len(all_trains) - 1 else None
        if next_index_train is None or next_index_train.start < self.end:
            return [self]
        return [self] + next_index_train.get_sequence(all_trains)



with open('input.json') as inputJson:
    input = json.load(inputJson)
    all_trains = [Train(index, times) for index, times in enumerate(input)]
    highest_length = 0
    best_sequence = None
    for train in all_trains:
        seq = train.get_sequence(all_trains)
        length = sum([seq_train.length for seq_train in seq])
        if length > highest_length:
            highest_length = length
            best_sequence = seq
    print('highest length', highest_length)
    print('best sequence')
    for seq_train in best_sequence:
        print('   ' + str(seq_train))