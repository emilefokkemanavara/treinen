import json

def calculate(trains):
    if len(trains) == 0:
        return (0, [])
    best_length = 0
    best_trains = []
    for train in trains:
        (length, trains) = train.determine_best_next_trains(trains)
        if length >= best_length:
            best_length = length
            best_trains = trains
        
    return (best_length, best_trains)
    

class Train:

    def __init__(self, index, times):
        self.index = index
        self.times = times
        self.best_next_trains = None
    
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
    
    def determine_best_next_trains(self, all_trains):
        if self.best_next_trains is not None:
            return self.best_next_trains
        print('calculating best next trains for train', self.index)
        next_trains = [next for next in all_trains if next.start >= self.end]
        (next_length, best_next_trains) = calculate(next_trains)
        result = (self.length + next_length, [self] + best_next_trains)
        self.best_next_trains = result
        print('done calculating best next trains for train', self.index)
        return result



with open('input.json') as inputJson:
    input = json.load(inputJson)
    all_trains = [Train(index, times) for index, times in enumerate(input)]
    (length, trains) = calculate(all_trains)
    print('final length ', length)
    for train in trains:
        print(str(train))
    