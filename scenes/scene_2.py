from manim import *
from .decorator_cleanup import remove_all_mobjects

@remove_all_mobjects
def section(self):
    # Create the number line from 0 to 5 (positive numbers only)
    number_line = NumberLine(
        x_range=[0, 4, 1],
        length=4,
        include_numbers=True,
        include_tip=True
    )
    # number_line.to_edge(DOWN)  # Position it near the bottom of the screen
    number_line.shift(RIGHT)
    number_line.shift(2.5 * DOWN)
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
    fall_pos = number_line.number_to_point(0) + 3 * DOWN
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


    for mobject in self.mobjects:
        self.play(mobject.animate.shift(0.75*DOWN), run_time=0.2)

    text_p = MathTex("P_n")
    text_p_next = MathTex("P_n = \\text{P(reaching 0 from n)}")
    text_q = MathTex("1-P_1?")
    text_q.next_to(text_p_next, DOWN, buff=0.5)

    self.play(FadeIn(text_p))
    self.wait(2)
    self.play(ReplacementTransform(text_p,text_p_next))
    self.wait(2)
    self.play(FadeIn(text_q))

    self.wait(2)

    self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob not in [text_q]],
            text_q.animate.shift(LEFT * 2)
        )
    
    self.wait(2)

    text_p1 = MathTex("P_1 = ")
    text_p1.move_to(text_q.get_left())
    text_p1_a1 = MathTex("p \\times 1")
    text_p1_a2 = MathTex("+ \\text{ } q \\times P_2")

    text_p1_a1.next_to(text_p1, RIGHT, buff=0.2)
    text_p1_a2.next_to(text_p1_a1, RIGHT, buff=0.2)

    self.play(ReplacementTransform(text_q, text_p1))
    self.play(FadeIn(text_p1_a1))
    self.play(FadeIn(text_p1_a2))

    text_p1_group = VGroup(text_p1_a1, text_p1_a2)

    self.wait(2)

    text_p2 = MathTex("P_2 = P_{2 \\rightarrow 1} \\times P_{1 \\rightarrow 0}")
    text_p2.next_to(text_p1.get_left() + DOWN, aligned_edge= LEFT)

    self.play(FadeIn(text_p2))
    self.wait(2)

    text_p2_side = MathTex("P_{2 \\rightarrow 1} = P_{1 \\rightarrow 0}")
    text_p2_side.next_to(text_p2.get_left() + DOWN, aligned_edge= LEFT)

    self.play(FadeIn(text_p2_side))
    self.wait(2)

    text_p2_side_transition = MathTex("P_{2 \\rightarrow 1} = P_{1}")
    text_p2_side_transition.next_to(text_p2_side.get_left(), aligned_edge= LEFT)

    self.play(ReplacementTransform(text_p2_side, text_p2_side_transition))
    self.wait(2)

    text_p2_transition = MathTex("P_2 = P_1^2")
    text_p2_transition.next_to(text_p2.get_left(), aligned_edge= LEFT)

    self.play(ReplacementTransform(text_p2, text_p2_transition),
              FadeOut(text_p2_side_transition))
    self.wait(2)

    text_p1_transition = MathTex("p \\times 1 + q \\times P_1^2")
    text_p1_transition.next_to(text_p1, RIGHT, buff=0.2)

    self.play(
        Transform(text_p1_group,text_p1_transition, replace_mobject_with_target_in_scene=True),
        FadeOut(text_p2_transition)
        )
    self.wait(2)

    text_sidenote = MathTex("p + q = 1")
    text_sidenote.next_to(text_p1.get_left() + UP)

    self.play(FadeIn(text_sidenote))
    self.wait(2)
    self.play(FadeOut(text_sidenote))
    self.wait(2)

    text_ans = MathTex("\\dfrac{p}{q}, 1")
    text_ans.next_to(text_p1, RIGHT, buff=0.2)

    self.play(Transform(text_p1_transition, text_ans, replace_mobject_with_target_in_scene=True))   
    self.wait(2)

    text_ans_2 = MathTex("\\dfrac{p}{q}")
    text_ans_2.next_to(text_p1, RIGHT, buff=0.2)

    self.play(Transform(text_ans, text_ans_2, replace_mobject_with_target_in_scene=True))
    self.wait(2)

    text_ans_3 = MathTex("\\dfrac{1/3}{2/3} = \\dfrac{1}{2}")
    text_ans_3.next_to(text_p1, RIGHT, buff=0.2)

    self.play(Transform(text_ans_2, text_ans_3, replace_mobject_with_target_in_scene=True))
    self.wait(2)

    text_ans_4 = MathTex("50\\%")
    text_ans_4.next_to(text_p1, RIGHT, buff=0.2)

    self.play(Transform(text_ans_3, text_ans_4, replace_mobject_with_target_in_scene=True))
    self.wait(2)

    text_ans_5 = MathTex("1-P_1 = 50\\%")

    self.play(
        FadeOut(text_p1),
        Transform(text_ans_4, text_ans_5, replace_mobject_with_target_in_scene=True)
        )
    self.wait(2)


    self.wait(5)


    """
    Starting at P1, there a p chance he falls off the cliff and a q chance that he reaches position 2. At Position 2, the probability of falling off the cliff is P2, and that gives us the formula that P1 = p*1+q*P2. Next, notice that each step the man takes is independent of one another. That tells us that the probability of the man going from position 2 to 0 is the probability of the man going from position 2 to 1 times the probability of the man going from position 1 to 0. Also note that probabililty of the man net moving from position 2 to 1 is the same as moving from position 1 to 0 given the memoryless nature of the situation. That tells us that P2 is P1 squared. We can plug that into our original formula for P1, and solve it using the quadratic equation. Then we apply algebra, which I'll skim over because you guys probably know how to solve the quadratic equation. Though note that p+q =1 so p= 1-q. At the end, we get that P1 = p/q or 1. We keep the p/q, and plugging in our values for p and q, we find that P1 is 1/2. Therefore, the probability the man survives is 50 percent.
    """

