from manimlib import *

class SortScene(Scene):
    def construct(self) -> None:
        rect = Rectangle(height=FRAME_HEIDGT,width=1)
        rect.set_fill(opacity=1)
        rect.set_stroke(opacity=0)
        self.add(rect)