from manim import *
from scenes import scene_1

def remove_all_mobjects(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
    return wrapper

class FallingDotScene(Scene):
    def construct(self):

        @remove_all_mobjects
        def section_intro(self):
            scene_1.section_intro(self)

        @remove_all_mobjects
        def section_scene_1(self):
            # Create the number line from 0 to 5 (positive numbers only)
            number_line = NumberLine(
                x_range=[0, 4, 1],
                length=4,
                include_numbers=True,
                include_tip=True
            )
            # number_line.to_edge(DOWN)  # Position it near the bottom of the screen
            number_line.shift(RIGHT)
            number_line.shift(2 * DOWN)
            self.play(Create(number_line))

            # Create a dot above the number line at position 1
            start_pos = number_line.number_to_point(1) + UP

            stick_figure = SVGMobject("person.svg").move_to(start_pos)
            stick_figure.set(height=1)  # Scale appropriately

            self.play(FadeIn(stick_figure))
            self.wait(0.5)

            # Dot jumps to position 0 (above the number line)
            jump_pos = number_line.number_to_point(0) + UP
            self.play(stick_figure.animate.move_to(jump_pos), run_time=0.5)
            self.wait(0.3)

            # Dot "falls" down past the number line
            fall_pos = number_line.number_to_point(0) + 5 * DOWN
            self.play(stick_figure.animate.move_to(fall_pos), run_time=1)
            self.wait(1)

            stick_figure = SVGMobject("person.svg").move_to(start_pos)
            stick_figure.set(height=1)  # Scale appropriately

            self.play(FadeIn(stick_figure))

            # === Label with arrow ===
            label_text = MathTex("p = \\frac{1}{3}")
            arrow = Arrow(start=label_text.get_left(), end=label_text.get_left() + LEFT, buff=0.1)
            label_group = VGroup(label_text, arrow)
            label_group.arrange(LEFT, buff=0.2)
            label_group.next_to(stick_figure, LEFT, buff=0.3)
            self.play(FadeIn(label_text), GrowArrow(arrow))

            # === Label with arrow ===
            label_text = MathTex("q = \\frac{2}{3}")
            arrow = Arrow(start=label_text.get_right(), end=label_text.get_right() + RIGHT, buff=0.1)
            label_group = VGroup(label_text, arrow)
            label_group.arrange(RIGHT, buff=0.2)
            label_group.next_to(stick_figure, RIGHT, buff=0.3)
            self.play(FadeIn(label_text), GrowArrow(arrow))

            self.wait(2)


        section_intro(self)

        self.next_section("Number Line Representation")

        section_scene_1(self)


