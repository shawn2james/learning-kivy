# Kivy Tutorials
**Link**: https://buildmedia.readthedocs.org/media/pdf/kivy/latest/kivy.pdf
<br>
<br>
All the code that I write going through the official Kivy Tutorials

## Kivy App Lifecycle
<img src="kivy-basics/kivy-lifecycle.jpg" height=600px>

## Kivy App Architecture
<img src='kivy-basics/kivy-architecture.jpg' width=500px height=300px>
<br>

**Core Provider**:
A piece of code that uses an API to talk to the operating system on one side and to Kivy on the other.<br>
**Input Provider**:
A piece of code that adds support to an input device

### Core Package
  - Clock: schedule timer events
  - Cache: cache something that you use often
  - Gesture Detection: detect various kinds of strokes
  - Kivy Language: efficiently describe user interfaces
  - Properties: link widget code to UI description

### UIX
  - Widgets: user interface elements that offers functionality to your program
  - Layouts: used to arrange widgets

### Input Events (Touches)
Three states of touches:
  - Down: a touch is down only once, at the very moment where it first appears
  - Move: whenever a 2D position of the touch changes
  - Up: a touch goes up at most once, or never.

## Event Handling in Kivy
<img src="kivy-basics/event-handling.jpg" width=800px height=500px>
