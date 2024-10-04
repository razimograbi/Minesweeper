import pygame


class ImageConverter:
    def __init__(self):
        self.__from_surrounding_number_of_blocks_to_image = {
            0: 'venv/images/EMPTYMINE.png',
            1: 'venv/images/ONE.png',
            2: 'venv/images/TWO.png',
            3: 'venv/images/THREE.png',
            4: 'venv/images/FOUR.png',
            5: 'venv/images/FIVE.png',
            6: 'venv/images/SIX.png',
            7: 'venv/images/SEVEN.png',
            8: 'venv/images/EIGHT.png'
        }
        self.__mine_image_location = 'venv/images/MINE.png'
        self.__flag_image_location = 'venv/images/FLAG.png'

    def GetPygameImageFromNumberOfSurroundingBlocks(self, number_of_surrounding_blocks: int):
        if number_of_surrounding_blocks in self.__from_surrounding_number_of_blocks_to_image:
            return pygame.image.load(self.__from_surrounding_number_of_blocks_to_image[
                                         number_of_surrounding_blocks]).convert()

        else:
            return pygame.image.load('venv/images/Monster.png').convert()

    def GetMinePygameImage(self):
        return pygame.image.load(self.__mine_image_location).convert()

    def GetFlagPygameImage(self):
        return pygame.image.load(self.__flag_image_location).convert()
