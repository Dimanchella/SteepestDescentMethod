import copy

from support import E
from dichotomy import Dichotomy

GRAD_STEP = E * 0.1


class SteepestDecent:
    __dich__: Dichotomy
    __function__ = None
    __xs_history__: list[list[float]]
    __values_history__: list[float]
    __approx_history__: list[float]
    __grad_history__: list[list[float]]
    __alpha_history__: list[float]

    def __init__(self, evaluable_function, start_x: list[float]):
        self.__function__ = eval(evaluable_function)
        self.__xs_history__ = [copy.copy(start_x)]
        self.__dich__ = Dichotomy(evaluable_function)

    def get_xs_history(self):
        return copy.deepcopy(self.__xs_history__)

    def get_values_history(self):
        return copy.copy(self.__values_history__)

    def get_approx_history(self):
        return copy.copy(self.__approx_history__)

    def get_grad_history(self):
        return copy.deepcopy(self.__grad_history__)

    def get_alpha_history(self):
        return copy.copy(self.__alpha_history__)

    def __calculate_grad__(self):
        grad = []
        xs = copy.copy(self.__xs_history__[-1])
        for i in range(len(xs)):
            xs[i] += GRAD_STEP
            grad.append((self.__function__(xs) - self.__values_history__[-1]) / GRAD_STEP)
            xs[i] -= GRAD_STEP
        self.__grad_history__.append(grad)

    def __calculate_alpha__(self):
        self.__dich__.calculate_exterm([
            self.__xs_history__[-1],
            list(map(lambda x, gr: x - gr, self.__xs_history__[-1], self.__grad_history__[-1]))
        ])
        # TODO
        self.__alpha_history__.append(0.01)

    def __calculate_next_xs(self):
        self.__xs_history__.append(list(map(
            lambda x, gr: x - self.__alpha_history__[-1] * gr,
            self.__xs_history__[-1], self.__grad_history__[-1]
        )))

    def __calculate_max_norm__(self):
        self.__approx_history__.append(
            max(map(abs, self.__xs_history__[-1])) - max(map(abs, self.__xs_history__[-2]))
        )

    def calculate_minimize(self):
        self.__xs_history__ = [self.__xs_history__[0]]
        self.__values_history__ = [self.__function__(self.__xs_history__[0])]
        self.__grad_history__ = []
        self.__alpha_history__ = []
        self.__approx_history__ = []
        while True:
            self.__calculate_grad__()
            self.__calculate_alpha__()
            self.__calculate_next_xs()
            self.__values_history__.append(self.__function__(self.__xs_history__[-1]))
            self.__calculate_max_norm__()
            if self.__approx_history__[-1] <= E:
                break
