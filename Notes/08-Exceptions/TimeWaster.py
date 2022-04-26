from decorators import timer


class TimeWaster:
    def __init__(self, max_num) -> None:
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


@timer
class TimeWaster:
    def __init__(self, max_num) -> None:
        self.max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
