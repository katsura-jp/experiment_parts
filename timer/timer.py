import time

class Timer(object):
    def __init__(self):
        self.start = time.time()

    def reset(self):
        self.start = time.time()

    def stamp(self) -> str:
        sec = time.time() - self.start
        return self._sec_convert(sec)
    
    def _sec_convert(self, sec : float) -> str:
        sec = int(sec)
        min_ = sec // 60
        sec = sec % 60
        hour = min_ // 60
        min_ = min_ % 60
        return f'{hour:>03d}:{min_:>02d}:{sec:>02d}'


class TimerManager(object):
    def __init__(self):
        self.timers = dict()

    def set_timer(self, name: str):
        self.timers[name] = Timer()

    def stamp(self, name: str) -> str:
        return self.timers[name].stamp()

    def reset(self, name: str):
        self.timers[name].reset()
    

if __name__ == '__main__':
    import time
    timer = Timer()
    
    for _ in range(5):
        time.sleep(1.0)
        print('\r{}'.format(timer.stamp()), end='')
    print()
    print('-- reset --')
    timer.reset()
    for _ in range(3):
        time.sleep(1.0)
        print('\r{}'.format(timer.stamp()), end='')
    print()
    
