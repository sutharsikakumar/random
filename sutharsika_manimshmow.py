# -*- coding: utf-8 -*-
"""Sutharsika_ManimShmow

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1icQkp3R9v8ufY8UFBsKQCmjJSFXMLJ71
"""

!sudo apt update
!sudo apt install libcairo2-dev ffmpeg \
    texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science \
    tipa libpango1.0-dev
!pip install manim==0.16.0
!pip install IPython --upgrade

from manim import *

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm PolygonOnAxes
# from manim import *
# 
# class PolygonOnAxes(Scene):
#     def get_rectangle_corners(self, bottom_left, top_right):
#         return [
#             (top_right[0], top_right[1]),
#             (bottom_left[0], top_right[1]),
#             (bottom_left[0], bottom_left[1]),
#             (top_right[0], bottom_left[1]),
#         ]
# 
#     def construct(self):
#         ax = Axes(
#             x_range=[0, 10],
#             y_range=[0, 10],
#             x_length=6,
#             y_length=6,
#             axis_config={"include_tip": False},
#         )
# 
#         t = ValueTracker(5)
#         k = 25
# 
#         graph = ax.plot(
#             lambda x: k / x,
#             color=YELLOW_D,
#             x_range=[k / 5, 10.0, 0.01],
#             use_smoothing=False,
#         )
# 
#         def get_rectangle():
#             polygon = Polygon(
#                 *[
#                     ax.c2p(*i)
#                     for i in self.get_rectangle_corners(
#                         (5, 0), (t.get_value(), k / t.get_value())
#                     )
#                 ]
#             )
#             polygon.stroke_width = 1
#             polygon.set_fill(BLUE, opacity=0.5)
#             polygon.set_stroke(YELLOW_B)
#             return polygon
# 
#         polygon = always_redraw(get_rectangle)
# 
#         dot = Dot()
#         dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), k / t.get_value())))
#         dot.set_z_index(5)
# 
#         self.add(ax, graph, dot)
#         self.play(Create(polygon))
#         self.play(t.animate.set_value(10))
#         self.play(t.animate.set_value(k / 5))
#         self.play(t.animate.set_value(5))

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm SineCurveUnitCircle
# class SineCurveUnitCircle(Scene):
#     # contributed by heejin_park, https://infograph.tistory.com/230
#     def construct(self):
#         self.show_axis()
#         self.show_circle()
#         self.move_dot_and_draw_curve()
#         self.wait()
# 
#     def show_axis(self):
#         x_start = np.array([-6,0,0])
#         x_end = np.array([6,0,0])
# 
#         y_start = np.array([-4,-2,0])
#         y_end = np.array([-4,2,0])
# 
#         x_axis = Line(x_start, x_end)
#         y_axis = Line(y_start, y_end)
# 
#         self.add(x_axis, y_axis)
#         self.add_x_labels()
# 
#         self.origin_point = np.array([-4,0,0])
#         self.curve_start = np.array([-3,0,0])
# 
#     def add_x_labels(self):
#         x_labels = [
#             MathTex("\pi"), MathTex("2 \pi"),
#             MathTex("3 \pi"), MathTex("4 \pi"),
#         ]
# 
#         for i in range(len(x_labels)):
#             x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
#             self.add(x_labels[i])
# 
#     def show_circle(self):
#         circle = Circle(radius=1)
#         circle.move_to(self.origin_point)
#         self.add(circle)
#         self.circle = circle
# 
#     def move_dot_and_draw_curve(self):
#         orbit = self.circle
#         origin_point = self.origin_point
# 
#         dot = Dot(radius=0.08, color=YELLOW)
#         dot.move_to(orbit.point_from_proportion(0))
#         self.t_offset = 0
#         rate = 0.25
# 
#         def go_around_circle(mob, dt):
#             self.t_offset += (dt * rate)
#             # print(self.t_offset)
#             mob.move_to(orbit.point_from_proportion(self.t_offset % 1))
# 
#         def get_line_to_circle():
#             return Line(origin_point, dot.get_center(), color=BLUE)
# 
#         def get_line_to_curve():
#             x = self.curve_start[0] + self.t_offset * 4
#             y = dot.get_center()[1]
#             return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )
# 
# 
#         self.curve = VGroup()
#         self.curve.add(Line(self.curve_start,self.curve_start))
#         def get_curve():
#             last_line = self.curve[-1]
#             x = self.curve_start[0] + self.t_offset * 4
#             y = dot.get_center()[1]
#             new_line = Line(last_line.get_end(),np.array([x,y,0]), color=YELLOW_D)
#             self.curve.add(new_line)
# 
#             return self.curve
# 
#         dot.add_updater(go_around_circle)
# 
#         origin_to_circle_line = always_redraw(get_line_to_circle)
#         dot_to_curve_line = always_redraw(get_line_to_curve)
#         sine_curve_line = always_redraw(get_curve)
# 
#         self.add(dot)
#         self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
#         self.wait(8.5)
# 
#         dot.remove_updater(go_around_circle)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm SineCurveUnitCircle
# class SineCurveUnitCircle(Scene):
#   def construct(self):
#         envelope = Text("Tracing Shapes", font="times")
#         name = Text("Sutharsika Kumar", font_size="20")
#         sceneone = Text("Everything Together", font_size="40")
#         self.play(Write(envelope))
#         self.play(envelope.animate().to_edge(UP))
#         self.play(Write(name))
#         self.play(name.animate().to_edge(UP*2.75))
#         self.play(Unwrite(name))
#         self.play(Unwrite(envelope))
#         self.play(sceneone.animate().to_edge(UP))
#         self.wait(2)
# 
#

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm ExampleTransform
# from manim import *
#

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm TracedPathExample
# from manim import *
# 
# class TracedPathExample(Scene):
#     def construct(self):
# 
#         rect = RoundedRectangle(color=RED).shift(4*LEFT)
#         dot = Dot(color=RED).move_to(rect.get_start())
#         rolling_circle = VGroup(rect, dot)
#         trace = TracedPath(rect.get_start)
#         rolling_circle.add_updater(lambda m: m.rotate(-0.3))
#         self.add(trace, rolling_circle)
#         self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=linear)
# 
#         rect = Rectangle(color=GREEN).shift(4*LEFT)
#         dot = Dot(color=RED).move_to(rect.get_start())
#         rolling_circle = VGroup(rect, dot)
#         trace = TracedPath(rect.get_start)
#         rolling_circle.add_updater(lambda m: m.rotate(-0.3))
#         self.add(trace, rolling_circle)
#         self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=exponential_decay)
# 
# 
#         rect2 = Triangle(color=BLUE).shift(4*LEFT)
#         dot = Dot(color=RED).move_to(rect2.get_start())
#         rolling_circle = VGroup(rect2, dot)
#         trace = TracedPath(rect2.get_start)
#         rolling_circle.add_updater(lambda m: m.rotate(-0.3))
#         self.add(trace, rolling_circle)
#         self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=exponential_decay)
# 
#

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm TracedPathExample
# from manim import *
# 
# class TracedPathExample(Scene):
#     def construct(self):
# 
#         rect2 = Triangle(color=BLUE).shift(4*LEFT)
#         dot = Dot(color=RED).move_to(rect2.get_start())
#         rolling_circle = VGroup(rect2, dot)
#         trace = TracedPath(rect2.get_start)
#         rolling_circle.add_updater(lambda m: m.rotate(-0.3))
#         self.add(trace, rolling_circle)
#         self.play(rolling_circle.animate.shift(8*RIGHT), run_time=4, rate_func=exponential_decay)

# Commented out IPython magic to ensure Python compatibility.
# %%manim -qm PangoRender
# class PangoRender(Scene):
#   def construct(self):
#         envelope = Text("Thank you for watching.", font="times")
#         self.play(Write(envelope))
#         self.wait(2)
#         self.play(Uncreate(envelope))