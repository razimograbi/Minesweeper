import random

class Pair:
    def __init__(self, first: int, second: int):
        self.x = first
        self.y = second

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return 2 * hash(self.x) + 3 * hash(self.y)

    @staticmethod
    def random_pair_list_generator(number_of_blocks_in_one_row, number_of_mines):
        # generates a list of random mine positions
        random_list = []
        while len(random_list) < number_of_mines:
            item_found_in_list_flag = False
            pair_coordinates = Pair(0, 0)
            pair_coordinates.x = random.randint(0, number_of_blocks_in_one_row - 1)
            pair_coordinates.y = random.randint(0, number_of_blocks_in_one_row - 1)
            for item in random_list:
                if item == pair_coordinates:
                    item_found_in_list_flag = True
                    break
            if not item_found_in_list_flag:
                random_list.append(pair_coordinates)
        return random_list
