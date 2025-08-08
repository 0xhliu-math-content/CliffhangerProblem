from manim import *
from scenes import scene_1, scene_2

class FallingDotScene(Scene):
    def construct(self):

        scene_1.section(self)

        self.next_section("Number Line Representation")

        scene_2.section(self)

