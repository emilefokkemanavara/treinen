import json

def calculate(trains):
    if len(trains) == 0:
        return (0, [])
    best_length = 0
    best_trains = []
    for train in trains:
        (length, trains) = train.determine_best_next_trains(trains)
        candidate_length = best_length

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
        return f'{self.start} -> {self.end}'
    
    def determine_best_next_trains(self, all_trains):
        if self.best_next_trains is not None:
            return self.best_next_trains
        print('calculating best next trains for train', self.index)
        # next_trains = [next for next in all_trains if next.start >= self.end]
        # if len(next_trains) == 0:
        #     return
        # best_next_length = 0
        # best_next_trains = []
        # for next_train in next_trains:



with open('input.json') as inputJson:
    input = json.load(inputJson)[0:3]
    all_trains = [Train(index, times) for index, times in enumerate(input)]
    all_trains[0].determine_best_next_trains(all_trains)
    