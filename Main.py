import tkinter
import PathFindingGrid

def start_btn():
    grid.run()


def left_move(event):
    if state == "normal":
        grid.set_blocked_state(event.x, event.y, True)


def right_move(event):
    if canvas.winfo_x() <= event.x <= canvas.winfo_x() + int(canvas['width']):
        if canvas.winfo_y() <= event.y <= canvas.winfo_y() + int(canvas['height']):
            grid.set_blocked_state(event.x, event.y, False)


def scale_canvas():
    grid.change_grid_size(scale_var.get(), scale_var.get())


def set_point(event):
    global state

    if state == "placing_source_point":
        grid.set_source(event.x, event.y)
    elif state == "placing_end_point":
        grid.set_end_point(event.x, event.y)

    canvas.unbind("<Button-1>")
    canvas.unbind("<Motion>")
    grid.ui.current_rect_position = -1, -1
    state = "normal"


def set_source_btn():
    global state
    state = "placing_source_point"
    canvas.bind("<Button-1>", set_point)
    canvas.bind("<Motion>", lambda event: canvas_motion_event(event, "green"))


def set_end_btn():
    global state
    state = "placing_end_point"
    canvas.bind("<Button-1>", set_point)
    canvas.bind("<Motion>", lambda event: canvas_motion_event(event, "black"))


def canvas_motion_event(event, color):
    grid.ui.draw_rect_on_hover(event.x, event.y, color)

def reset(event):
    grid.init()

def exit_state(event):
    global state
    if state != "normal":
        canvas.unbind("<Button-1>")
        canvas.unbind("<Motion>")
        grid.ui.clear_by_tag("hover")
        state = "normal"

main = tkinter.Tk()
main.title("Pathfinder Visualizer")
main.geometry("1000x1000")

canvas = tkinter.Canvas(main, width=800, height=800)
canvas.configure(bg="white")
canvas.grid(row=1, column=1, rowspan=2, columnspan=4)

scale_var = tkinter.IntVar()
w1 = tkinter.Scale(main, from_=5, to=60, tickinterval=5, length=600, variable=scale_var)
w1.grid(row=1, column=0)

buttonFrame = tkinter.Frame(main, bg="grey", height=100)
buttonFrame.grid(row=0, column=0, columnspan=5, sticky="E")

btn = tkinter.Button(main, text="OK", command=scale_canvas)
btn.grid(row=2, column=0, sticky="N")

btn_start = tkinter.Button(buttonFrame, text="Start", command=start_btn)
btn_start.pack(side="left")

btn_set_source = tkinter.Button(buttonFrame, text="Set Source Point", command=set_source_btn)
btn_set_source.pack(side="left")

btn_set_end = tkinter.Button(buttonFrame, text="Set End Point", command=set_end_btn)
btn_set_end.pack(side="left")

grid = PathFindingGrid.PathFinderGrid(canvas)

state = "normal"
main.update()

canvas.bind("<B1-Motion>", left_move)
canvas.bind("<B3-Motion>", right_move)

main.bind("<Return>", reset)
main.bind("<Button-3>", exit_state)
main.mainloop()
