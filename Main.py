import tkinter

from PFVisualizerApp import PathFinderVisualizerApp


def start_btn():
    app.run()


def left_move(event):
    if state == "normal":
        app.set_node_blocked_state(event.x, event.y, True)


def right_move(event):
    if state == "normal":
        app.set_node_blocked_state(event.x, event.y, False)


def scale_canvas():
    app.change_grid_size(scale_var.get(), scale_var.get())


def set_point(event):
    global state

    if state == "placing_source_point":
        app.set_source_node(event.x, event.y)
        btn_set_source.config(state="normal")
    elif state == "placing_end_point":
        app.set_end_point(event.x, event.y)
        btn_set_end.config(state="normal")

    canvas.unbind("<Button-1>")
    canvas.unbind("<Motion>")
    app.ui.current_rect_position = -1, -1
    app.ui.clear_hover()
    state = "normal"


def set_source_btn():
    global state
    state = "placing_source_point"
    canvas.bind("<Button-1>", set_point)
    canvas.bind("<Motion>", lambda event: canvas_motion_event(event, "green"))

    btn_set_source.config(state="disabled")


def set_end_btn():
    global state
    state = "placing_end_point"
    canvas.bind("<Button-1>", set_point)
    canvas.bind("<Motion>", lambda event: canvas_motion_event(event, "black"))

    btn_set_end.config(state="disabled")


def canvas_motion_event(event, color):
    app.ui.draw_rect_on_hover(event.x, event.y, color)


def reset(event):
    app.init()


def exit_state(event):
    global state
    if state != "normal":
        canvas.unbind("<Button-1>")
        canvas.unbind("<Motion>")
        btn_set_end.config(state="normal")
        btn_set_source.config(state="normal")
        app.ui.clear_hover()
        state = "normal"


def select_algorithm(event):
    app.set_algorithm(algorithm_var.get().split()[0])


def select_visualization():
    app.visualize = not app.visualize


main = tkinter.Tk()
main.title("Pathfinder Visualizer")
main.geometry("1000x1000")
canvas = tkinter.Canvas(main, width=800, height=800)
canvas.configure(bg="white")
canvas.grid(row=1, column=1, rowspan=1, columnspan=5)

scale_var = tkinter.IntVar()
w1 = tkinter.Scale(main, from_=5, to=60, tickinterval=5, length=600, variable=scale_var)
w1.grid(row=1, column=0, rowspan=4)

buttonFrame = tkinter.Frame(main, height=100)
buttonFrame.grid(row=0, column=1, columnspan=5, sticky="W")

visualize_var = tkinter.IntVar()
visualize_var.set(1)
c1 = tkinter.Checkbutton(buttonFrame, text='Visualize', variable=visualize_var, onvalue=1, offvalue=0,
                         command=select_visualization)
c1.pack(side="left")

btn_scale = tkinter.Button(main, text="Scale", command=scale_canvas)
btn_scale.grid(row=1, column=0, sticky="N", pady=60)

btn_start = tkinter.Button(buttonFrame, text="Start", command=start_btn)
btn_start.pack(side="left", padx=(10, 10))

btn_set_source = tkinter.Button(buttonFrame, text="Set Source Point", command=set_source_btn)
btn_set_source.pack(side="left", padx=(10, 10))

btn_set_end = tkinter.Button(buttonFrame, text="Set End Point", command=set_end_btn)
btn_set_end.pack(side="left", padx=(10, 10))

algorithm_var = tkinter.StringVar(main)
algorithm_var.set("Dijkstra Algorithm")

algorithm_menu = tkinter.OptionMenu(buttonFrame, algorithm_var, "Dijkstra Algorithm", "A* Algorithm",
                                    command=select_algorithm)
algorithm_menu.pack(side="right", padx=(10, 10))

app = PathFinderVisualizerApp(canvas)

state = "normal"
main.update()

canvas.bind("<B1-Motion>", left_move)
canvas.bind("<B3-Motion>", right_move)



main.bind("<Return>", reset)
main.bind("<Button-3>", exit_state)
main.mainloop()
