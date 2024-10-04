import pygame
import sys
import grid
import Render
import handleUserInput

FPS = 60
NUMBER_OF_BLOCKS_IN_EACH_ROW = 15
SCREEN_WIDTH = NUMBER_OF_BLOCKS_IN_EACH_ROW * 40 + 200
SCREEN_HEIGHT = NUMBER_OF_BLOCKS_IN_EACH_ROW * 40 + 100
BLACK = (0, 0, 0)
NUMBER_OF_MINES = 40
USER_PRESSED_ON_MINE_EVENT = pygame.USEREVENT + 1
BLOCK_DIM = (40, 40)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("MineSweeper")
    clock = pygame.time.Clock()
    camera_group = pygame.sprite.Group()
    blocks = grid.Grid(NUMBER_OF_BLOCKS_IN_EACH_ROW, NUMBER_OF_MINES, camera_group, BLOCK_DIM)
    # empty_blocks = blocks.ReturnBlockWithTheLeastAmountOfMinesSurroundingIt()
    # print(empty_blocks)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or blocks.CheckWhetherThePlayerWon():
                pygame.time.delay(1500)
                pygame.quit()
                sys.exit()

            if event.type == USER_PRESSED_ON_MINE_EVENT:
                blocks.OpenAllMinesImages(screen, camera_group)
                pygame.time.delay(1500)
                pygame.quit()
                sys.exit()

        handleUserInput.CheckUserInputAndOpenPressedBlock(blocks)

        Render.RenderScreen(BLACK, screen, camera_group)


if __name__ == '__main__':
    main()
