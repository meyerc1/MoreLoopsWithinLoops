"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Carson Meyer.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    for k in range(n):
        old_x1 = rectangle.corner_1.x
        old_y1 = rectangle.corner_1.y
        old_x2 = rectangle.corner_2.x
        old_y2 = rectangle.corner_2.y

        x1 = old_x1
        y1 = old_y1
        x2 = old_x2
        y2 = old_y2
        w = old_x2 - old_x1
        l = old_y2 - old_y1
        for j in range(n):
            for k in range(j + 1):
                new_rectangle = rg.Rectangle(rg.Point(x1, y1), rg.Point(x2, y2))
                new_rectangle.attach_to(window)
                window.render(0.1)

                x1 = x1 - w
                x2 = x2 - w

            y1 = y1 - l
            y2 = y2 - l
            x1 = old_x1 + ((j + 1) * (w / 2))
            x2 = old_x2 + ((j + 1) * (w / 2))



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
