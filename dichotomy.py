import math

from support import E

LOCALITY_DELTA = E * 0.1


class Dichotomy:
    __function__ = None
    __exterm_history__: list[float]

    def __init__(self, evaluable_function):
        self.__function__ = eval(evaluable_function)

    def get_result_exterm(self):
        return self.__exterm_history__[-1]

    def calculate_exterm(self, range_x: list[list[float], list[float]]):
        self.__exterm_history__ = []
        xs = list(map(lambda x1, x2: (x1 + x2) / 2, range_x[0], range_x[1]))
        is_max = self.__function__(range_x[1]) \
                 < self.__function__(xs) \
                 > self.__function__(range_x[0])
        while max(map(lambda x1, x2: abs(x1 - x2), range_x[0], range_x[1])) > E:
            xs = list(map(lambda x1, x2: (x1 + x2) / 2, range_x[0], range_x[1]))
            xs1 = list(map(lambda x: x - LOCALITY_DELTA, xs))
            xs2 = list(map(lambda x: x + LOCALITY_DELTA, xs))
            f1 = self.__function__(xs1)
            f2 = self.__function__(xs2)
            if is_max and f1 < f2 or not is_max and f1 > f2:
                range_x[0] = xs
            else:
                range_x[1] = xs
            self.__exterm_history__.append(self.__function__(xs))
