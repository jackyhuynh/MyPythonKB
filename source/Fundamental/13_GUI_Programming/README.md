## Chapter 13: GUI Programming

This chapter introduces the exciting world of **Graphical User Interface (GUI) programming**, allowing you to create
interactive applications with windows, buttons, text boxes, and other visual elements. We'll focus on Python's built-in
`tkinter` library.

### 1. Introduction to GUI Programming

#### Understanding the Basics of GUI Programming

A Graphical User Interface (GUI) is a visual way for users to interact with a computer program, using elements like
windows, icons, menus, and pointers. This contrasts with Command Line Interfaces (CLIs), where interaction happens via
text commands.

**Key concepts in GUI programming:**

* **Widgets (Controls):** Individual graphical components like buttons, labels, text entry fields, scrollbars, etc.
* **Window (Root Window/Top-Level Window):** The main application window that contains all other widgets.
* **Event-Driven Programming:** GUIs operate on an event-driven model. The program waits for user actions (events) like
  mouse clicks, key presses, or window resizing, and then responds accordingly.
* **Layout Management:** How widgets are positioned and resized within a window.

#### Using the `tkinter` Library to Create GUI Applications

`tkinter` is Python's standard GUI library. It's a thin object-oriented layer on top of Tcl/Tk, a widely used GUI
toolkit. While other powerful GUI libraries exist (e.g., PyQt, Kivy), `tkinter` is excellent for getting started due to
its simplicity and built-in availability.

**Basic `tkinter` structure:**

1. **Import `tkinter`:** `import tkinter as tk`
2. **Create the root window:** `root = tk.Tk()`
3. **Set window properties:** `root.title()`, `root.geometry()`
4. **Create widgets:** `tk.Label()`, `tk.Button()`, etc.
5. **Place widgets:** Using layout managers (`pack()`, `grid()`, `place()`).
6. **Start the event loop:** `root.mainloop()` (This keeps the window open and responsive to events).

```python
import tkinter as tk

# 1. Create the root window
root = tk.Tk()
root.title("My First GUI")
root.geometry("400x200") # Width x Height

# 2. Create a Label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20) # Pack the label into the window with some padding

# 3. Create a Button widget
def on_button_click():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me!", command=on_button_click)
button.pack()

# 4. Start the main event loop
root.mainloop()
```

### 2. Creating GUI Components

#### Creating and Using Widgets like Buttons, Labels, and Text Boxes

Let's explore some common `tkinter` widgets:

* **`tk.Label`:** Used to display static text or images.

```python
# text: The text to display
# fg/bg: foreground/background color
# font: font family, size, style
label = tk.Label(root, text="Display Message", fg="blue", font=("Arial", 14))
```

* **`tk.Button`:** A clickable button that triggers an action.

```python
# text: Text on the button
# command: A function to call when the button is clicked
button = tk.Button(root, text="Submit", command=my_function_to_run)
```

* **`tk.Entry`:** A single-line text input field.

```python
# width: Width of the entry field in characters
entry = tk.Entry(root, width=30)
# Getting text: entry.get()
# Setting text: entry.insert(index, string)
```

* **`tk.Text`:** A multi-line text input field.

```python
# width/height: dimensions in characters
text_area = tk.Text(root, height=5, width=40)
# Getting text: text_area.get("1.0", tk.END) (from line 1, character 0 to end)
# Setting text: text_area.insert(tk.END, "Initial text")
```

* **`tk.Checkbutton`:** A checkbox for boolean choices.

```python
var = tk.IntVar() # Variable to store the checkbox state (0 or 1)
checkbutton = tk.Checkbutton(root, text="Agree", variable=var, onvalue=1, offvalue=0)
# To get state: var.get()
```

* **`tk.Radiobutton`:** For selecting one option from a set.

```python
radio_var = tk.StringVar()
radio1 = tk.Radiobutton(root, text="Option A", variable=radio_var, value="A")
radio2 = tk.Radiobutton(root, text="Option B", variable=radio_var, value="B")
# To get selected value: radio_var.get()
```

### 3. Event-Driven Programming

#### Understanding Event-Driven Programming and Handling Events in a GUI Application

GUI applications are inherently **event-driven**. This means they don't follow a linear flow like script. Instead, they
constantly wait for events to occur (e.g., a mouse click, a key press, a window resize, a timer expiring). When an event
occurs, the program triggers a specific piece of code (an **event handler** or **callback function**) that is associated
with that event.

**How `tkinter` handles events:**

* **Widget-specific events:** Many widgets have a `command` option, which directly links the widget's primary action (
  like a button click) to a function.
* **`bind()` method:** For more general events (e.g., specific key presses, mouse movements, window events), you use the
  `bind()` method. It takes an event sequence string (e.g., `<Button-1>` for left-click, `<Key>` for any key press) and
  a callback function.

**Example with `bind()`:**

```python
import tkinter as tk

def on_key_press(event):
    print(f"Key pressed: {event.char}") # event.char gives the character

def on_mouse_click(event):
    print(f"Mouse clicked at ({event.x}, {event.y})") # event.x, event.y give coordinates

root = tk.Tk()
root.title("Event Handling")

# Bind a function to any key press on the root window
root.bind("<Key>", on_key_press)

# Bind a function to a left mouse button click on the root window
root.bind("<Button-1>", on_mouse_click)

label = tk.Label(root, text="Click or Type anywhere in the window")
label.pack(pady=50)

root.mainloop()
```

### 4. GUI Layout Managers

#### Using Layout Managers like `pack()`, `grid()`, and `place()` to Organize GUI Components

Placing widgets effectively within a window is crucial for a well-designed GUI. `tkinter` provides three geometry
managers:

* **`pack()`:** The simplest and most intuitive for basic layouts. It arranges widgets in blocks before placing them in
  the parent widget. You can specify side (`top`, `bottom`, `left`, `right`), `fill` (expand to fill available space),
  and `expand` (widget takes up extra space).

```python
# Widgets packed top to bottom by default
tk.Button(root, text="Top").pack(side=tk.TOP, pady=5)
tk.Button(root, text="Left").pack(side=tk.LEFT, padx=5)
tk.Button(root, text="Right").pack(side=tk.RIGHT, padx=5)
```

* **`grid()`:** Organizes widgets in a table-like structure of rows and columns. This is excellent for more complex,
  structured layouts.

```python
# Entry for username
tk.Label(root, text="Username:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Entry for password
tk.Label(root, text="Password:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Login button spanning two columns
tk.Button(root, text="Login").grid(row=2, column=0, columnspan=2, pady=10)
```

    * `row`, `column`: Specifies the cell where the widget is placed.
    * `rowspan`, `columnspan`: Makes a widget span multiple rows/columns.
    * `padx`, `pady`: External padding (space around the widget).
    * `ipadx`, `ipady`: Internal padding (space inside the widget).
    * `sticky`: Determines how the widget "sticks" within its grid cell (e.g., `tk.N`, `tk.S`, `tk.E`, `tk.W` for north, south, east, west, or combinations like `tk.NSEW` to fill).

* **`place()`:** Allows you to position widgets at exact coordinates (`x`, `y`) or relative to the parent's size (
  `relx`, `rely`, `relwidth`, `relheight`). While offering precise control, it's generally less flexible and harder to
  maintain for responsive designs compared to `pack()` or `grid()`.

```python
label = tk.Label(root, text="Absolute Positioned")
label.place(x=50, y=50) # Place at absolute coordinates

button = tk.Button(root, text="Relative Positioned")
button.place(relx=0.5, rely=0.8, anchor=tk.CENTER) # Place center of button at 50% width, 80% height
```

For most applications, `grid()` offers the best balance of flexibility and maintainability. `pack()` is great for
simpler layouts, and `place()` is used sparingly for very specific positioning needs.

---