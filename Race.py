import graphics
from Dice import Dice

WIN_WIDTH = 700
WIN_HEIGHT = 350
START_X = 50
FINISH_OFFSET = 50
FINISH_X = WIN_WIDTH - FINISH_OFFSET
FPS = 30

IMAGE_HORSE_1 = "horse.gif"
IMAGE_HORSE_2 = "horse2.gif"

class Horse:
    def __init__(self, speed: int, y: int, image: graphics.Image, window: graphics.GraphWin):
        self.x = START_X
        self.y = y
        self.image = image
        self.window = window
        self.dice = Dice(speed)

    def move(self) -> None:
        self.x += self.dice.roll()

    def draw(self) -> None:
        self.image.draw_at_pos(self.window, self.x, self.y)

    def crossed_finish_line(self, x: int) -> bool:
        return self.x >= x

def load_image_or_placeholder(filename: str) -> graphics.Image:
    try:
        return graphics.Image(graphics.Point(0, 0), filename)
    except Exception:
        return graphics.Image(graphics.Point(0, 0), 40, 40)

def main() -> None:
    win = graphics.GraphWin("Horse Race", WIN_WIDTH, WIN_HEIGHT, autoflush=False)
    win.setBackground("white")

    img1 = load_image_or_placeholder(IMAGE_HORSE_1)
    img2 = load_image_or_placeholder(IMAGE_HORSE_2)

    horse1 = Horse(speed=12, y=100, image=img1, window=win)
    horse2 = Horse(speed=10, y=250, image=img2, window=win)

    finish_line = graphics.Line(graphics.Point(FINISH_X, 0), graphics.Point(FINISH_X, WIN_HEIGHT))
    finish_line.setWidth(3)

    title = graphics.Text(graphics.Point(WIN_WIDTH / 2, 20), "Click to start the race!")
    title.draw(win)
    horse1.draw()
    horse2.draw()
    finish_line.draw(win)

    win.getMouse()

    race_over = False
    h1_done = h2_done = False

    while not race_over:
        horse1.move()
        horse2.move()

        win.clear_win()
        finish_line.draw(win)
        horse1.draw()
        horse2.draw()

        h1_done = horse1.crossed_finish_line(FINISH_X)
        h2_done = horse2.crossed_finish_line(FINISH_X)
        race_over = h1_done or h2_done

        graphics.update(FPS)

    if h1_done and h2_done:
        outcome = "Tie"
    elif h1_done:
        outcome = "Horse 1 is the winner"
    else:
        outcome = "Horse 2 is the winner"

    result = graphics.Text(
        graphics.Point(WIN_WIDTH / 2, 20), f"{outcome}! Click anywhere to close."
    )
    result.setSize(14)
    result.setStyle("bold")
    result.draw(win)
    graphics.update()

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()

