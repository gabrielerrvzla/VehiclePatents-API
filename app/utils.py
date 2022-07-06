from itertools import product


class Utils:
    def _generate_secuence(self):
        """
        Generates a sequence
        """
        letters = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']*4
        numbers = ['0123456789']*3

        for i in product(*letters):
            for j in product(*numbers):
                yield "".join(i + j)
