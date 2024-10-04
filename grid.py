import pygame
import pair
from block import Block
import imageConverter
import Render

BLACK = (0, 0, 0)
USER_PRESSED_ON_MINE_EVENT = pygame.USEREVENT + 1

class Grid:
    def __init__(self, number_of_blocks_in_each_row: int, number_of_mines: int, group, block_dim: tuple):
        if number_of_mines <= 2 or number_of_blocks_in_each_row <= 2:
            print("Illegal values of number_of_mines or number_of_blocks")
            raise ValueError
        self.__image_converter = imageConverter.ImageConverter()
        self.number_of_opened_blocks = 0
        self.number_of_mines = number_of_mines
        self.number_of_blocks_in_each_row = number_of_blocks_in_each_row
        self.total_number_of_blocks = self.number_of_blocks_in_each_row ** 2
        # self.from_block_position_to_surrounding_number_of_mines_dic: dict[pair.Pair: int] = dict()
        random_mine_position_list = pair.Pair.random_pair_list_generator(number_of_blocks_in_each_row, number_of_mines)

        # building the matrix
        self.matrix = [[Block((0, 0), group, False, block_dim) for _ in range(number_of_blocks_in_each_row)] for _ in
                       range(number_of_blocks_in_each_row)]

        original_row_starting_pos = block_dim[0] * 2
        current_block_position = pair.Pair(original_row_starting_pos, block_dim[1]//2)
        column_space_difference = block_dim[0] + 1
        row_space_difference = block_dim[1] + 1

        for i in range(number_of_blocks_in_each_row):
            for j in range(number_of_blocks_in_each_row):
                self.matrix[i][j].rect.x = current_block_position.x
                self.matrix[i][j].rect.y = current_block_position.y
                block_position = pair.Pair(i, j)
                for p in random_mine_position_list:
                    if block_position == p:
                        self.matrix[i][j].is_mine = True
                        print(str(i) + " " + str(j))
                current_block_position.x = current_block_position.x + column_space_difference
            current_block_position.y = current_block_position.y + row_space_difference
            current_block_position.x = original_row_starting_pos

    def IsInBoundary(self, row_index: int, column_index: int):
        return 0 <= row_index < self.number_of_blocks_in_each_row and 0 <= column_index < self.number_of_blocks_in_each_row

    def __CountSurroundingMines(self, row_index: int, column_index: int):
        mine_count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.IsInBoundary(row_index + i, column_index + j) and \
                        self.matrix[row_index + i][column_index + j].is_mine:
                    mine_count += 1
        return mine_count

    def __UpdateBlockImage(self, row_index: int, column_index: int, is_mine: bool, is_flagged: bool):
        if not self.IsInBoundary(row_index, column_index):
            return

        if is_mine:
            self.matrix[row_index][column_index].image = self.__image_converter.GetMinePygameImage()
            self.matrix[row_index][column_index].image = pygame.transform.scale(
                self.matrix[row_index][column_index].image, (40, 40))
            return

        if is_flagged:
            self.matrix[row_index][column_index].image = self.__image_converter.GetFlagPygameImage()
            self.matrix[row_index][column_index].image = pygame.transform.scale(
                self.matrix[row_index][column_index].image, (40, 40))
            return

        self.matrix[row_index][column_index].number_of_surrounding_mines = self.__CountSurroundingMines(
            row_index, column_index)

        self.matrix[row_index][column_index].image = self.__image_converter.GetPygameImageFromNumberOfSurroundingBlocks(
            self.matrix[row_index][column_index].number_of_surrounding_mines)

        self.matrix[row_index][column_index].image = pygame.transform.scale(
            self.matrix[row_index][column_index].image, (40, 40))

    def __OpenSurroundingBlocksAroundBlock(self, block_row_index: int, block_column_index: int, seen: set):
        if not self.IsInBoundary(block_row_index, block_column_index):
            return
        block = self.matrix[block_row_index][block_column_index]

        if block in seen or block.is_mine or block.is_open or block.is_flagged:
            return
        block.is_open = True
        self.number_of_opened_blocks += 1
        self.__UpdateBlockImage(block_row_index, block_column_index, False, False)
        seen.add(block)
        if not block.number_of_surrounding_mines:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.__OpenSurroundingBlocksAroundBlock(block_row_index + i, block_column_index + j, seen)

    def OpenBlockAndUpdateItsImage(self, block_row_index: int, block_column_index: int):
        if self.matrix[block_row_index][block_column_index].is_open:
            return

        self.matrix[block_row_index][block_column_index].is_open = True

        if self.matrix[block_row_index][block_column_index].is_mine:
            self.__UpdateBlockImage(block_row_index, block_column_index, True, False)
            # set an event
            pygame.event.post(pygame.event.Event(USER_PRESSED_ON_MINE_EVENT))
            return

        self.number_of_opened_blocks += 1
        self.__UpdateBlockImage(block_row_index, block_column_index, is_mine=False, is_flagged=False)
        if self.matrix[block_row_index][block_column_index].number_of_surrounding_mines < 2:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    self.__OpenSurroundingBlocksAroundBlock(block_row_index + i, block_column_index + j, set())

    def FlagBlock(self, row_index, column_index):
        if self.matrix[row_index][column_index].is_open:
            return
        if self.matrix[row_index][column_index].is_flagged:
            block = self.matrix[row_index][column_index]
            block.image = pygame.image.load('venv/images/BLOCKMINESWeeper.png').convert()
            block.image = pygame.transform.scale(block.image, (40, 40))
            block.is_flagged = False
            return

        self.matrix[row_index][column_index].is_flagged = True
        self.__UpdateBlockImage(row_index, column_index, is_mine=False, is_flagged=True)

    def __FindFirstNoneMinePosition(self):
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[0])):
                if not self.matrix[row][column].is_mine:
                    return row, column
        return None, None

    def ChangeMineIntoNormalBlock(self, mine_row_index: int, mine_column_index: int):
        if not self.matrix[mine_row_index][mine_column_index].is_mine:
            return
        block = self.matrix[mine_row_index][mine_column_index]
        block.is_mine = False
        old_normal_row_index, old_normal_column_index = self.__FindFirstNoneMinePosition()
        if old_normal_row_index is not None and old_normal_column_index is not None:
            self.matrix[old_normal_row_index][old_normal_column_index].is_mine = True
            print("new Mine location " + str(old_normal_column_index) + " " + str(old_normal_column_index))

    def OpenAllMinesImages(self, screen, group):
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[0])):
                if self.matrix[row][column].is_mine:
                    self.OpenBlockAndUpdateItsImage(row, column)
                    Render.RenderScreen(BLACK, screen, group, delay_time_in_millie=100)

    def CheckWhetherThePlayerWon(self):
        return self.number_of_opened_blocks == self.total_number_of_blocks - self.number_of_mines


    def ReturnBlockWithTheLeastAmountOfMinesSurroundingIt(self):
        min_amount_of_mines = 500
        target_block = None
        empty_block_array = []
        for row in range(len(self.matrix)):
            for column in range(len(self.matrix[0])):
                if not self.matrix[row][column].is_mine:
                    mine_count = self.__CountSurroundingMines(row, column)
                    if mine_count <= min_amount_of_mines:
                        min_amount_of_mines = mine_count
                        target_block = row, column
                        empty_block_array.append(target_block)

        if len(empty_block_array) == 0:
            return target_block
        return empty_block_array

