from manim import *
from .decorator_cleanup import remove_all_mobjects

@remove_all_mobjects
def section(self):
        # Introduction Text
        intro_text = Text("The Cliffhanger Problem", font_size=42)
        self.play(FadeIn(intro_text))

        self.wait(3)

        # Create the number line from 0 to 5 (positive numbers only)
        # === Create a Box ===
        box_width = 8
        box_height = 3
        box = Rectangle(width=box_width, height=box_height)
        box.set_stroke(color=WHITE, width=2)
        box.set_fill(color=WHITE, opacity=0.5)
        box.shift(4 * DOWN)
        box.shift(RIGHT * box_width*0.4)
        self.play(Create(box))

        start_pos = box.get_corner(UP + LEFT) + UP*0.75 + RIGHT*0.5

        stick_figure = SVGMobject("person.svg").move_to(start_pos)
        stick_figure.set(height=1)  # Scale appropriately

        self.play(FadeIn(stick_figure))
        self.wait(3)

        # Dot jumps to position 0 (above the number line)
        jump_pos = start_pos + LEFT
        self.play(stick_figure.animate.move_to(jump_pos), run_time=0.5)
        self.wait(0.3)

        # Dot "falls" down past the number line
        fall_pos = jump_pos + 3 * DOWN
        self.play(stick_figure.animate.move_to(fall_pos), run_time=1)
        self.wait(1)

        # stick_figure = SVGMobject("person.svg").move_to(start_pos)
        # stick_figure.set(height=1)  # Scale appropriately

        # self.play(FadeIn(stick_figure))
        stick_figure.move_to(start_pos)
        self.play(FadeIn(stick_figure))

        # === Label with arrow ===
        label_text = MathTex("\\frac{1}{3}")
        arrow = Arrow(start=label_text.get_left(), end=label_text.get_left() + LEFT, buff=0.1)
        label_group = VGroup(label_text, arrow)
        label_group.arrange(LEFT, buff=0.2)
        label_group.next_to(stick_figure, LEFT, buff=0.3)
        self.play(FadeIn(label_text), GrowArrow(arrow))

                # === Label with arrow ===
        label_text = MathTex("\\frac{2}{3}")
        arrow = Arrow(start=label_text.get_right(), end=label_text.get_right() + RIGHT, buff=0.1)
        label_group = VGroup(label_text, arrow)
        label_group.arrange(RIGHT, buff=0.2)
        label_group.next_to(stick_figure, RIGHT, buff=0.3)
        self.play(FadeIn(label_text), GrowArrow(arrow))

        self.wait(2)

        question_text = Text("What is the probability he doesn't fall the cliff?", font_size=24)
        question_text.shift(DOWN*0.75)
        self.play(FadeIn(question_text))
        self.wait(3)
