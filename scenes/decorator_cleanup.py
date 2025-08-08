from manim import *

def remove_all_mobjects(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
    return wrapper