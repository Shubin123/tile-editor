from game import Game
import asyncio


async def main():
    count = 3
    game = Game()
    while True:
        await asyncio.sleep(0)
        game.clock.tick(60)
        game.handle_events()
        game.ui.draw_brush_display()
        game.update()
        # game.draw_adjecent_face(overlap="next", face="left", x=32, y=32)


# NON-BLOCK DONT GO PAST HERE
if __name__ == '__main__':
    asyncio.run(main())