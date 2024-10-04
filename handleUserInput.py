import pygame
import grid


def CheckUserInputAndOpenPressedBlock(blocks: grid.Grid):
    keys = pygame.key.get_pressed()
    # left click
    if pygame.mouse.get_pressed()[0] or keys[pygame.K_g]:
        for row_index in range(blocks.number_of_blocks_in_each_row):
            for column_index in range(blocks.number_of_blocks_in_each_row):
                if blocks.matrix[row_index][column_index].rect.collidepoint(pygame.mouse.get_pos()):
                    # first time click of mine
                    if blocks.matrix[row_index][column_index].is_mine and blocks.number_of_opened_blocks == 0:
                        blocks.ChangeMineIntoNormalBlock(row_index, column_index)
                    blocks.OpenBlockAndUpdateItsImage(row_index, column_index)



    # right click (flag)
    if pygame.mouse.get_pressed()[-1] or keys[pygame.K_f]:
        for row_index in range(blocks.number_of_blocks_in_each_row):
            for column_index in range(blocks.number_of_blocks_in_each_row):
                if blocks.matrix[row_index][column_index].rect.collidepoint(pygame.mouse.get_pos()):
                    blocks.FlagBlock(row_index, column_index)
                    pygame.time.delay(200)
