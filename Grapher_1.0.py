import os.path
import tkinter as tk
import numpy as np
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import matplotlib
import tkinter.scrolledtext
from tkinter import messagebox
from matplotlib.animation import FuncAnimation
#########################
matplotlib.use("TkAgg")
#########################
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
from sklearn import metrics
from matplotlib import style, animation
#########################
style.use("ggplot")
#########################
import warnings
import psutil

# for polyfit warnings
warnings.simplefilter('ignore', np.RankWarning)

#########################################################
# additional information
# padding

pad_x = 2
pad_y = 2

########################################
# information for pyplot for ALL frames.
# Most important data for plotting is here

x_data = []
x_data_name = []
x_data_path = []
y_data = []
y_data_name = []
y_data_path = []
xy_data = []
xy_data_name = []
xy_data_path = []
x_label = []
y_label = []
title_pyplot = []
save_as = []
graph_title_name = []
queue_gridline = []
queue_legend = []
queue_textannotate = []
interpolation_list = []
interpolation_grid = []
weird_delimiter = []
line_type = []
point_type = []
r2_list = []
r2_value = []
subplot_check = []
plot_trigger = []
color_plot = []
color_marker = []
grid_style = []
legend_name = []
annotate_text = []
#########################
# animation specific lists
colors_animation = []

#########################################

def clear_all(event):
    global x_data, x_data_name, x_data_path, y_data, y_data_name, y_data_path, xy_data
    global xy_data_name, xy_data_path, x_label, y_label, title_pyplot, save_as
    global graph_title_name, queue_gridline, queue_legend, queue_textannotate, interpolation_list
    global interpolation_grid, weird_delimiter, line_type, point_type, r2_list, subplot_check
    global plot_trigger, plot_trigger, grid_style, color_plot, legend_name, annotate_text
    global r2_value, color_marker

    x_data = []
    x_data_name = []
    x_data_path = []
    y_data = []
    y_data_name = []
    y_data_path = []
    xy_data = []
    xy_data_name = []
    xy_data_path = []
    x_label = []
    y_label = []
    title_pyplot = []
    save_as = []
    graph_title_name = []
    queue_gridline = []
    queue_legend = []
    queue_textannotate = []
    interpolation_list = []
    interpolation_grid = []
    weird_delimiter = []
    line_type = []
    point_type = []
    r2_list = []
    r2_value = []
    subplot_check = []
    plot_trigger = []
    color_plot = []
    color_marker = []
    grid_style = []
    legend_name = []
    annotate_text = []


def get_data_x(event):
    file = askopenfilename()
    if file is not None:

        # read excel
        data = pd.read_excel(io=file, header=None)

        # create DataFrame of excel
        df_x = pd.DataFrame(data=data, index=None)

        # split file name from path
        file_name = os.path.split(file)[1]
        file_name_head = os.path.splitext(file_name)[0]

        # add temp file to folder (modified file)
        new_name = file_name_head + "_temp"
        new_path = os.path.join(os.path.split(file)[0], new_name + os.path.splitext(file_name)[1])

        # create new temp excel file that stores modifified data
        df_x.to_excel(new_path, sheet_name="sheet1", index=False)

        # show excel file
        os.system(new_path)

        # check whether Excel if running
        if "EXCEL.EXE" in (i.name() for i in psutil.process_iter()):
            pass
        else:

            # append modified path to path and path name
            x_data_path.append(new_path)
            x_data_name.append(new_path)
            text_x.insert(index="end", chars=f"x data read from {new_path}\n")

        # disable xy button
        import_xy_button.config(state="disabled", text="DO NOT USE")
        import_xy_button.unbind(sequence="<ButtonRelease-1>")


def get_data_y(event):
    file = askopenfilename()
    if file is not None:

        # read excel
        data = pd.read_excel(io=file, header=None)

        # create DataFrame of excel
        df_y = pd.DataFrame(data=data, index=None)

        # split file name from path
        file_name = os.path.split(file)[1]
        file_name_head = os.path.splitext(file_name)[0]

        # add temp file to folder (modified file)
        new_name = file_name_head + "_temp"
        new_path = os.path.join(os.path.split(file)[0], new_name + os.path.splitext(file_name)[1])

        # create new temp excel file that stores modifified data
        df_y.to_excel(new_path, sheet_name="sheet1", index=False)

        # show excel file
        os.system(new_path)

        # check whether Excel if running
        if "EXCEL.EXE" in (i.name() for i in psutil.process_iter()):
            pass
        else:
            # append modified path to path and path name
            y_data_path.append(new_path)
            y_data_name.append(new_path)
            text_y.insert(index="end", chars=f"y data read from {new_path}\n")

            # disable xy button
        import_xy_button.config(state="disabled", text="DO NOT USE")
        import_xy_button.unbind(sequence="<ButtonRelease-1>")


def get_data_xy(event):
    file = askopenfilename()
    if file is not None:

        # read excel
        data = pd.read_excel(io=file, header=None)

        # create DataFrame of excel
        df_xy = pd.DataFrame(data=data, index=None)

        # split file name from path
        file_name = os.path.split(file)[1]
        file_name_head = os.path.splitext(file_name)[0]

        # add temp file to folder (modified file)
        new_name = file_name_head + "_temp"
        new_path = os.path.join(os.path.split(file)[0], new_name + os.path.splitext(file_name)[1])

        # create new temp excel file that stores modifified data
        df_xy.to_excel(new_path, sheet_name="sheet1", index=False)

        # show excel file
        os.system(new_path)

        # check whether Excel if running
        if "EXCEL.EXE" in (i.name() for i in psutil.process_iter()):
            pass
        else:
            # append modified path to path and path name
            xy_data_path.append(new_path)
            xy_data_name.append(new_path)
            text_both.insert(index="end", chars=f"xy data read from {new_path}\n")

        import_x_button.config(state="disabled", text="DO NOT USE")
        import_x_button.unbind(sequence="<ButtonRelease-1>")
        import_y_button.config(state="disabled", text="DO NOT USE")
        import_y_button.unbind(sequence="<ButtonRelease-1>")


def datasets(event):
    wn_data = tk.Tk()
    wn_data.geometry("985x1000")
    wn_data.title("Available Data")
    wn_data.resizable(False, False)

    frame_data1 = ttk.Frame(master=wn_data, relief=tk.GROOVE)
    frame_data1.grid(row=0, column=0)
    frame_data2 = ttk.Frame(master=wn_data, relief=tk.GROOVE)
    frame_data2.grid(row=0, column=1)
    frame_data3 = ttk.Frame(master=wn_data, relief=tk.GROOVE)
    frame_data3.grid(row=1, column=0, columnspan=2)

    lbl = ttk.Label(master=frame_data1, text="All available data for x, y and z axes is below:")
    lbl.grid(row=0, column=0, sticky=tk.EW)

    textdata_x = tk.scrolledtext.ScrolledText(master=frame_data1, height=20, width=120)
    textdata_x.grid(row=1, column=0, sticky=tk.NSEW)

    textdata_y = tk.scrolledtext.ScrolledText(master=frame_data1, height=20, width=120)
    textdata_y.grid(row=2, column=0, sticky=tk.NSEW)

    textdata_xy = tk.scrolledtext.ScrolledText(master=frame_data1, height=20, width=120)
    textdata_xy.grid(row=3, column=0, sticky=tk.NSEW)

    # everytime you open application it updates list_x
    list_x = []
    for i in x_data_path:
        aux_x = pd.read_excel(i, header=None, names=["x_axis"], index_col=None)
        for index, row in aux_x.iterrows():
            list_x.append(row["x_axis"])

        # delete first row b/c of formatting
        list_x.pop(0)

        x = x_data_path.index(i)
        # insert all data:
        textdata_x.insert(index="end", chars=f"\nx list #{x} ({i}): {list_x}")

    # everytime you open application it updates list_x
    list_y = []
    for i in y_data_path:
        aux_y = pd.read_excel(i, header=None, names=["y_axis"], index_col=None)
        for index, row in aux_y.iterrows():
            list_y.append(row["y_axis"])

        # delete first row b/c of formatting
        list_y.pop(0)

        x = y_data_path.index(i)
        # insert all data:
        textdata_y.insert(index="end", chars=f"\ny list #{x} ({i}): {list_y}")

    # everytime you open application it updates list_x
    list_xy_x = []
    list_xy_y = []
    for i in xy_data_path:
        aux_xy = pd.read_excel(i, header=None, names=["x_axis", "y_axis"], index_col=None)
        for ind in aux_xy.index:
            list_xy_x.append(aux_xy["x_axis"][ind])
        for ind in aux_xy.index:
            list_xy_y.append(aux_xy["y_axis"][ind])

        # delete first row b/c of formatting
        list_xy_x.pop(0)
        list_xy_y.pop(0)

        x = xy_data_path.index(i)
        # insert all data:
        textdata_xy.insert(index="end", chars=f"\nx list #{x} ({i}): {list_xy_x}")
        textdata_xy.insert(index="end", chars=f"\ny list #{x} ({i}): {list_xy_y}")

    wn_data.mainloop()


def progress_x():
    if len(x_data_path) == 1:
        if bar['value'] < 100:
            bar['value'] += 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nAdded x entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def deprogress_x():
    if len(x_data_path) == 0:
        if bar['value'] < 100:
            bar['value'] -= 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nRemoved x entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def progress_y():
    if len(y_data_path) == 1:
        if bar['value'] < 100:
            bar['value'] += 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nAdded y entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def deprogress_y():
    if len(y_data_path) == 0:
        if bar['value'] < 100:
            bar['value'] -= 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nRemoved y entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def progress_xy():
    if len(xy_data_path) == 1:
        if bar['value'] < 100:
            bar['value'] += 100 / 3
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nAdded xy entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")

def deprogress_xy():
    if len(xy_data_path) == 0:
        if bar['value'] < 100:
            bar['value'] -= 100 / 3
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nRemoved xy entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def progress_line():
    if len(line_type) == 1:
        if bar['value'] < 100:
            bar['value'] += 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nAdded line entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def deprogress_line():
    if len(line_type) == 0:
        if bar['value'] < 100:
            bar['value'] -= 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nRemoved line entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def progress_point():
    if len(point_type) == 1:
        if bar['value'] < 100:
            bar['value'] += 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nAdded point entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def deprogress_point():
    if len(point_type) == 1:
        if bar['value'] < 100:
            bar['value'] -= 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nRemoved point entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def progress_color_point():
    if len(color_marker) == 1:
        if bar['value'] < 100:
            bar['value'] += 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nAdded point color entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def deprogress_color_point():
    if len(color_marker) == 0:
        if bar['value'] < 100:
            bar['value'] -= 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nRemoved point color entry")
        else:
           text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def progress_color_line():
    if len(color_plot) == 1:
        if bar['value'] < 100:
            bar['value'] += 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nAdded line color entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


def deprogress_color_line():
    if len(color_plot) == 0:
        if bar['value'] < 100:
            bar['value'] -= 100 / 6
            text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
            text_box.insert(index="end", chars=f"\nRemoved line color entry")
        else:
            text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: No addition to progress")


"""
def progress_plot():
    if bar['value'] < 100:
        bar['value'] += 12.5
        text_box.insert(index="end", chars=f"\nCurrent Progress: {bar['value']}%")
        text_box.insert(index="end", chars=f"\nCreated plot")
    else:
        text_box.insert(index="end", chars=f"\nCurrent Progress: The progress completed!")
"""




def create_window(event):
    global color_box, legend_entry
    # stupid, but too far into project to do classes
    global pack_fit, line_fit, line_validate, line_delete, point_fit, \
        point_validate, point_delete, pack_fit_validate, pack_fit_delete, diagnostic_box, frame_additional2, \
        grid_background_combobox, text_entry_width, text_entry_height, button_text, text_annotate, color_box_marker
    global selection_pack

    wn_additional = tk.Toplevel()
    wn_additional.geometry("940x465")
    wn_additional.title("Additional settings")
    wn_additional.resizable(False, False)
    frame_additional1 = ttk.Frame(master=wn_additional, relief=tk.GROOVE, width=460)
    frame_additional1.pack(side=tk.LEFT, fill=tk.BOTH)
    frame_additional2 = ttk.Frame(master=wn_additional, relief=tk.GROOVE)
    frame_additional2.pack(side=tk.LEFT, fill=tk.BOTH)

    ####################################################################
    # create window widgets

    # Styles
    style = ttk.Style()
    style.configure("A.TButton", background="green")
    style.configure("Disable.TButton", text="DO NOT USE", font="red", background="green")
    style.map("TCheckbutton", foreground=[("selected", "red")])
    style.configure("TLabel", font="bold")

    # label for window
    lbl = ttk.Label(master=frame_additional1, text=f"Plot customization:")
    lbl.grid(column=0, row=0, columnspan=1, rowspan=1, sticky=tk.W)

    # choose line style
    styles_line = ['-', '--', '-.', ':', '']
    line_fit = ttk.Combobox(master=frame_additional1, values=styles_line, width=15)
    line_fit.set("Line:")
    line_fit.grid(column=0, row=1, columnspan=1, rowspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

    # line button - validate
    line_validate = ttk.Button(master=frame_additional1, text="Validate", width=4, command=progress_line, style="A.TButton")
    line_validate.grid(column=1, row=1, columnspan=1, rowspan=1, sticky=tk.EW, ipadx=0, ipady=0)
    line_validate.bind(sequence="<ButtonRelease-1>", func=validate_line)

    # line button - delete
    line_delete = ttk.Button(master=frame_additional1, text="Reset", width=4, command=deprogress_line, style="A.TButton")
    line_delete.grid(column=2, row=1, columnspan=1, rowspan=1, sticky=tk.EW, ipadx=0, ipady=0)
    line_delete.bind(sequence="<ButtonRelease-1>", func=delete_line)

    # choose point style
    styles_point = ['.', ',', 'o', "v", "^", "<", ">", "*"]
    point_fit = ttk.Combobox(master=frame_additional1, values=styles_point, width=15)
    point_fit.set("Point:")
    point_fit.grid(column=0, row=2, columnspan=1, rowspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

    # point button - validate
    point_validate = ttk.Button(master=frame_additional1, text="Validate", width=4, command=progress_point, style="A.TButton")
    point_validate.grid(column=1, row=2, columnspan=1, rowspan=1, sticky=tk.EW, ipadx=0, ipady=0)
    point_validate.bind(sequence="<ButtonRelease-1>", func=validate_point)

    # point button - delete
    point_delete = ttk.Button(master=frame_additional1, text="Reset", width=4, command=deprogress_point, style="A.TButton")
    point_delete.grid(column=2, row=2, columnspan=1, rowspan=1, sticky=tk.EW, ipadx=0, ipady=0)
    point_delete.bind(sequence="<ButtonRelease-1>", func=delete_point)

    # add selection for interpolation
    selection_pack = []
    a = []
    for x in range(1, 5):
        for y in range(1, 5):
            selection_pack.append(f"{x, y}")
    pack_fit = ttk.Combobox(master=frame_additional1, values=selection_pack, width=15)
    pack_fit.set("Subplot grid:")
    pack_fit.grid(column=0, row=3, columnspan=1, rowspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

    # pack_fit validate
    pack_fit_validate = ttk.Button(master=frame_additional1, text="Validate", width=4, style="A.TButton")
    pack_fit_validate.grid(column=1, row=3, columnspan=1, rowspan=1, ipadx=0, ipady=0, sticky=tk.EW)
    pack_fit_validate.bind(sequence="<ButtonRelease-1>", func=validate_pack_fit)

    # pack_fit delete
    pack_fit_delete = ttk.Button(master=frame_additional1, text="Reset", width=4, style="A.TButton")
    pack_fit_delete.grid(column=2, row=3, columnspan=1, rowspan=1, ipadx=0, ipady=0, sticky=tk.EW)
    pack_fit_delete.bind(sequence="<ButtonRelease-1>", func=delete_pack_fit)

    # label for text annotation
    lbl_txt = ttk.Label(master=frame_additional1, text="Input text:")
    lbl_txt.grid(column=0, row=4, columnspan=1, rowspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

    # submit text
    button_txt = ttk.Button(master=frame_additional1, text="Submit text", style="A.TButton")
    button_txt.grid(column=0, row=4, columnspan=1, rowspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
    button_txt.bind(sequence="<ButtonRelease-1>", func=get_text)

    # relative choices for width and height of text annotation
    relative_fractions = ["0.0", "0.1", "0.2", "0.3", "0.4", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0"]

    # text location width
    text_entry_width = ttk.Combobox(master=frame_additional1, values=relative_fractions)
    text_entry_width.set("Rel. width")
    text_entry_width.grid(column=1, row=4, columnspan=1, rowspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

    # text location height
    text_entry_height = ttk.Combobox(master=frame_additional1, values=relative_fractions)
    text_entry_height.set("Rel. height")
    text_entry_height.grid(column=2, row=4, columnspan=1, rowspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

    # text box - annotation
    text_annotate = tk.Text(master=frame_additional1, height=9)
    text_annotate.grid(column=0, row=5, columnspan=3, rowspan=9, padx=pad_x, pady=pad_y, sticky=tk.NSEW)
    text_annotate.insert(index="end", chars="Input text for short plot description ...")

    # draw color
    # available colors for line
    colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon",
              "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
    color_box_marker = ttk.Combobox(frame_additional1, values=colors)
    color_box_marker.set("Draw colors point:")
    color_box_marker.grid(column=0, row=14, padx=pad_x, pady=pad_y, sticky=tk.W)

    # validate colors
    validate_color_marker = ttk.Button(master=frame_additional1, text="Validate", command=progress_color_point, style="A.TButton")
    validate_color_marker.grid(column=1, row=14, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
    validate_color_marker.bind(sequence="<ButtonRelease-1>", func=color_validate_marker)

    # reset colors
    reset_color_marker = ttk.Button(master=frame_additional1, text="Reset", command=deprogress_color_point, style="A.TButton")
    reset_color_marker.grid(column=2, row=14, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
    reset_color_marker.bind(sequence="<ButtonRelease-1>", func=color_delete_marker)

    # available colors for line
    colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon",
              "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
    color_box = ttk.Combobox(frame_additional1, values=colors)
    color_box.set("Draw colors line:")
    color_box.grid(column=0, row=15, padx=pad_x, pady=pad_y, sticky=tk.W)

    # validate colors
    validate_color = ttk.Button(master=frame_additional1, text="Validate", command=progress_color_line, style="A.TButton")
    validate_color.grid(column=1, row=15, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
    validate_color.bind(sequence="<ButtonRelease-1>", func=color_validate)

    # reset colors
    reset_color = ttk.Button(master=frame_additional1, text="Reset", command=deprogress_color_line, style="A.TButton")
    reset_color.grid(column=2, row=15, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
    reset_color.bind(sequence="<ButtonRelease-1>", func=color_delete)

    # legend label
    legend_label = ttk.Label(master=frame_additional1, text="Legend:")
    legend_label.grid(column=0, row=16, columnspan=1, padx=0, pady=0, sticky=tk.W)

    # legend entry
    legend_entry = ttk.Entry(master=frame_additional1, width=12)
    legend_entry.grid(column=0, row=16, columnspan=1, padx=0, pady=0, sticky=tk.E)

    # validate legend
    validate_color = ttk.Button(master=frame_additional1, text="Validate", style="A.TButton")
    validate_color.grid(column=1, row=16, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
    validate_color.bind(sequence="<ButtonRelease-1>", func=legend_validate)

    # reset legend
    reset_color = ttk.Button(master=frame_additional1, text="Reset", style="A.TButton")
    reset_color.grid(column=2, row=16, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
    reset_color.bind(sequence="<ButtonRelease-1>", func=legend_delete)

    # grid_type_combobox
    grids = ['-', '--', '-.', ':', '']
    grid_background_combobox = ttk.Combobox(master=frame_additional1, values=grids)
    grid_background_combobox.set("Grid type:")
    grid_background_combobox.grid(column=0, row=17, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

    # grid validate
    grid_validate = ttk.Button(master=frame_additional1, text="Validate", width=4, style="A.TButton")
    grid_validate.grid(column=1, row=17, columnspan=1, rowspan=1, ipadx=0, ipady=0, sticky=tk.EW)
    grid_validate.bind(sequence="<ButtonRelease-1>", func=validate_grid)

    # grid delete
    grid_validate_delete = ttk.Button(master=frame_additional1, text="Reset", width=4, style="A.TButton")
    grid_validate_delete.grid(column=2, row=17, columnspan=1, rowspan=1, ipadx=0, ipady=0, sticky=tk.EW)
    grid_validate_delete.bind(sequence="<ButtonRelease-1>", func=delete_grid)

    # Preview
    Preview_button = ttk.Button(master=frame_additional1, text="Preview", width=4, style="A.TButton")
    Preview_button.grid(column=0, row=18, columnspan=3, rowspan=1, ipadx=0, ipady=0, sticky=tk.EW)
    Preview_button.bind(sequence="<ButtonRelease-1>", func=preview)

    # scrollbar for text box - annotation
    scrollbar_annotate = ttk.Scrollbar(master=text_annotate, command=text_annotate.yview, orient="vertical")
    text_annotate.config(yscrollcommand=scrollbar_annotate.set)
    scrollbar_annotate.pack(side=tk.RIGHT, fill=tk.BOTH)

    # text box on bottom
    diagnostic_box = tk.scrolledtext.ScrolledText(master=frame_additional1, height=9, width=5)
    diagnostic_box.grid(column=0, columnspan=3, row=19, rowspan=5, sticky=tk.EW)
    diagnostic_box.insert(index="end", chars="Diagnostic box:")



    # end of Toplevel mainloop
    wn_additional.mainloop()


#####################################################################


def validate_x(event):
    x_label.append(label_x_entry.get())
    if len(x_label) > 0 and x_label != [""]:
        if x_label[-1].isprintable():
            text_box.insert(index="end", chars=f"\nEntered valid x label: {x_label[-1]}.\n"
                                               f"List of x labels: {x_label}")
            x_label_counter["text"] = f"Count number of instances: {len(x_label)}."
        else:
            text_box.insert(index="end", chars=f"\nEntered invalid x label: {x_label[-1]}.")
            x_label.pop(-1)
    else:
        text_box.insert(index="end", chars=f"\nEntered None x label. You may choose to not"
                                           f" enter a label.")


def validate_y(event):
    y_label.append(label_y_entry.get())
    if len(y_label) > 0 and y_label != [""]:
        if y_label[-1].isprintable():
            text_box.insert(index="end", chars=f"\nEntered valid y label: {y_label[-1]}.\n"
                                               f"List of y labels: {y_label}")
            y_label_counter["text"] = f"Count number of instances: {len(y_label)}."
        else:
            text_box.insert(index="end", chars=f"\nEntered invalid y label: {y_label[-1]}.")
            y_label.pop(-1)
    else:
        text_box.insert(index="end", chars=f"\nEntered None y label. You may choose to not"
                                           f" enter a label.")


def validate_title(event):
    title_pyplot.append(title.get())
    if len(title_pyplot) > 0 and title_pyplot != [""]:
        if title_pyplot[-1].isprintable():
            text_box.insert(index="end", chars=f"\nEntered valid title: {title_pyplot[-1]}.\n"
                                               f"List of titles: {title_pyplot}")
            title_counter["text"] = f"Count number of instances: {len(title_pyplot)}"
        else:
            text_box.insert(index="end", chars=f"\nEntered invalid title label: {title_pyplot[-1]}.")
            title_pyplot.pop(-1)
    else:
        text_box.insert(index="end", chars=f"\nEntered None title label. You may choose to not"
                                           f" enter a label.")


def validate_name(event):
    graph_title_name.append(entry_graph.get())
    if len(graph_title_name) > 0 and graph_title_name != [""]:
        if graph_title_name[-1].isprintable():
            text_box.insert(index="end", chars=f"\nEntered valid name: {graph_title_name[-1]}.\n"
                                               f"List of titles: {graph_title_name}")
            name_counter["text"] = f"Count number of instances: {len(graph_title_name)}"
        else:
            text_box.insert(index="end", chars=f"\nEntered invalid name label: {graph_title_name[-1]}.")
            graph_title_name.pop(-1)
    else:
        text_box.insert(index="end", chars=f"\nEntered None name label. You may choose to not"
                                           f" enter a label.")


def color_validate(event):
    color_plot.append(color_box.get())
    if len(color_plot) > 0 and color_plot != ["Draw colors:"]:
        if color_plot[-1].isprintable():
            diagnostic_box.insert(index="end", chars=f"\nEntered valid color: {color_plot[-1]}.\n"
                                                     f"List of colors: {color_plot}")
        else:
            diagnostic_box.insert(index="end", chars=f"\nEntered invalid color label: {color_plot[-1]}.")
            color_plot.pop(-1)
    else:
        diagnostic_box.insert(index="end", chars=f"\nEntered None color label. You may choose to not"
                                                 f" enter a label.")


def color_validate_marker(event):
    color_marker.append(color_box_marker.get())
    if len(color_marker) > 0 and color_marker != ["Draw colors:"]:
        if color_marker[-1].isprintable():
            diagnostic_box.insert(index="end", chars=f"\nEntered valid color: {color_marker[-1]}.\n"
                                                     f"List of colors: {color_marker}")
        else:
            diagnostic_box.insert(index="end", chars=f"\nEntered invalid color label: {color_marker[-1]}.")
            color_marker.pop(-1)
    else:
        diagnostic_box.insert(index="end", chars=f"\nEntered None color label. You may choose to not"
                                                 f" enter a label.")


def legend_validate(event):
    legend_name.append(legend_entry.get())
    if len(legend_name) > 0 and legend_name != [""]:
        if legend_name[-1].isprintable():
            diagnostic_box.insert(index="end", chars=f"\nEntered valid legend name: {legend_name[-1]}.\n"
                                                     f"List of colors: {legend_name}")
        else:
            diagnostic_box.insert(index="end", chars=f"\nEntered invalid legend label: {legend_name[-1]}.")
            legend_name.pop(-1)
    else:
        diagnostic_box.insert(index="end", chars=f"\nEntered None legend label. You may choose to not"
                                                 f" enter a label.")


def delete_last_x(event):
    if len(x_label) > 0:
        text_box.insert(index="end", chars=f"\nRemoved {x_label[-1]} from x labels.")
        x_label.pop(-1)
        text_box.insert(index="insert", chars=f" New list is:{x_label}.")
        x_label_counter["text"] = f"Count: {len(x_label)}."

    else:
        text_box.insert(index="end", chars=f"\nEmpty x labels list.")


def delete_last_y(event):
    if len(y_label) > 0:
        text_box.insert(index="end", chars=f"\nRemoved {y_label[-1]} from y labels.")
        y_label.pop(-1)
        text_box.insert(index="insert", chars=f" New list is:{y_label}.")
        y_label_counter["text"] = f"Count: {len(y_label)}."

    else:
        text_box.insert(index="end", chars=f"\nEmpty y labels list.")


def color_delete(event):
    if len(color_plot) > 0:
        diagnostic_box.insert(index="end", chars=f"\nRemoved {color_plot[-1]} from colors.")
        color_plot.pop(-1)
        diagnostic_box.insert(index="insert", chars=f" New list is:{color_plot}.")

    else:
        diagnostic_box.insert(index="end", chars=f"\nEmpty color list.")


def color_delete_marker(event):
    if len(color_marker) > 0:
        diagnostic_box.insert(index="end", chars=f"\nRemoved {color_marker[-1]} from colors.")
        color_marker.pop(-1)
        diagnostic_box.insert(index="insert", chars=f" New list is:{color_marker}.")

    else:
        diagnostic_box.insert(index="end", chars=f"\nEmpty color list.")


def legend_delete(event):
    if len(legend_name) > 0:
        diagnostic_box.insert(index="end", chars=f"\nRemoved {legend_name[-1]} from legend.")
        legend_name.pop(-1)
        diagnostic_box.insert(index="insert", chars=f" New list is:{legend_name}.")

    else:
        diagnostic_box.insert(index="end", chars=f"\nEmpty legend name list.")


def delete_import_x(event):
    if len(x_data_path) > 0:
        text_x.insert(index="end", chars=f"\nRemoved {x_data_path[-1]} from x list.")
        x_data_path.pop(-1)
        text_x.insert(index="insert", chars=f" New list is:{x_data_path}.")

    else:
        text_x.insert(index="end", chars=f"\nEmpty x list.")


def delete_import_y(event):
    if len(y_data_path) > 0:
        text_y.insert(index="end", chars=f"\nRemoved {y_data_path[-1]} from y list.")
        y_data_path.pop(-1)
        text_y.insert(index="insert", chars=f" New list is:{y_data_path}.")

    else:
        text_y.insert(index="end", chars=f"\nEmpty x list.")


def delete_import_xy(event):
    if len(xy_data_path) > 0:
        text_both.insert(index="end", chars=f"\nRemoved {xy_data_path[-1]} from xy list.")
        xy_data_path.pop(-1)
        text_both.insert(index="insert", chars=f" New list is:{xy_data_path}.")

    else:
        text_both.insert(index="end", chars=f"\nEmpty xy list.")


def delete_last_title(event):
    if len(title_pyplot) > 0:
        text_box.insert(index="end", chars=f"\nRemoved {title_pyplot[-1]} from title labels.")
        title_pyplot.pop(-1)
        text_box.insert(index="insert", chars=f" New list is:{title_pyplot}.")
        title_counter["text"] = f"Count: {len(title_pyplot)}"
    else:
        text_box.insert(index="end", chars=f"\nEmpty title labels list.")


def delete_last_name(event):
    if len(graph_title_name) > 0:
        text_box.insert(index="end", chars=f"\nRemoved {graph_title_name[-1]} from title labels.")
        graph_title_name.pop(-1)
        text_box.insert(index="insert", chars=f" New list is:{graph_title_name}.")
        name_counter["text"] = f"Count: {len(graph_title_name)}"
    else:
        text_box.insert(index="end", chars=f"\nEmpty name labels list.")


def validate_point(event):
    point_type.append(point_fit.get())
    if len(point_type) == 1 and point_type != ["Point:"]:
        if point_type[-1].isprintable():
            diagnostic_box.insert(index="end", chars=f"\nEntered point type: {point_type[-1]}.")
        else:
            diagnostic_box.insert(index="end", chars=f"\nEntered invalid point type: {point_type[-1]}.")
            point_type.pop(-1)
    else:
        diagnostic_box.insert(index="end", chars=f"\nNon valid point type / only 1 allowed."
                                                 f"\nChoice for point type has been reset.")
        point_type.clear()


def validate_line(event):
    line_type.append(line_fit.get())
    if len(line_type) == 1 and line_type != ["Line:"]:
        if line_type[-1].isprintable():
            diagnostic_box.insert(index="end", chars=f"\nEntered line type: {line_type[-1]}.")
        else:
            diagnostic_box.insert(index="end", chars=f"\nEntered invalid line type: {line_type[-1]}.")
            line_type.pop(-1)
    else:
        diagnostic_box.insert(index="end", chars=f"\nNon valid line type / only 1 allowed."
                                                 f"\nChoice for line type has been reset.")
        line_type.clear()


def validate_pack_fit(event):
    interpolation_grid.append(pack_fit.get())
    if len(interpolation_grid) == 1 and interpolation_grid != ["Subplot grid:"]:
        if interpolation_grid[-1].isprintable():
            diagnostic_box.insert(index="end", chars=f"\nEntered grid type: {interpolation_grid[-1]}.")
        else:
            diagnostic_box.insert(index="end", chars=f"\nEntered invalid grid type: {interpolation_grid[-1]}.")
            interpolation_grid.pop(-1)
    else:
        diagnostic_box.insert(index="end", chars=f"\nNon valid grid type / only 1 allowed."
                                                 f"\nChoice for grid type has been reset.")
        interpolation_grid.clear()


def validate_grid(event):
    grid_style.append(grid_background_combobox.get())
    if len(grid_style) == 1 and grid_style != ["Grid type:"]:
        if grid_style[-1].isprintable():
            diagnostic_box.insert(index="end", chars=f"\nEntered grid style: {grid_style[-1]}.")
        else:
            diagnostic_box.insert(index="end", chars=f"\nEntered invalid grid style: {grid_style[-1]}.")
            grid_style.pop(-1)
    else:
        diagnostic_box.insert(index="end", chars=f"\nNon valid grid style / only 1 allowed."
                                                 f"\nChoice for grid style has been reset.")
        grid_style.clear()


def delete_point(event):
    point_type.clear()
    diagnostic_box.insert(index="end", chars=f"\nCleared point selection.")


def delete_line(event):
    line_type.clear()
    diagnostic_box.insert(index="end", chars=f"\nCleared line selection.")


def delete_pack_fit(event):
    interpolation_grid.clear()
    diagnostic_box.insert(index="end", chars=f"\nCleared grid selection.")


def graph_title(event):
    graph_title_name.append(entry_graph.get())


def delete_grid(event):
    grid_style.clear()
    diagnostic_box.insert(index="end", chars=f"\nCleared grid style.")


def pyplot_grid(event):
    queue_gridline.append("trigger_grid")
    if len(queue_gridline) == 1:
        text_box.insert(index="end", chars="\nAdded grid option")

    if len(queue_gridline) > 1:
        queue_gridline.clear()
        text_box.insert(index="end", chars="\nReset grid option")


def pyplot_legend(event):
    queue_legend.append("trigger_legend")
    if len(queue_legend) == 1:
        text_box.insert(index="end", chars="\nAdded legend option")
        #pack_fit_validate.configure(state=tk.ACTIVE)
        #pack_fit_validate.bind(sequence="<ButtonRelease-1>", func=validate_pack_fit)
        #pack_fit_validate.update()

    if len(queue_legend) > 1:
        queue_legend.clear()
        text_box.insert(index="end", chars="\nReset legend option")
        #pack_fit_validate.configure(state=tk.DISABLED)
        #pack_fit_validate.unbind(sequence="<ButtonRelease-1>")
        #pack_fit_validate.update()


def interpolate_plot(event):
    interpolation_grid.append(pack_fit.get())


def add_r2(event):
    r2_selection_entry.config(state=tk.ACTIVE)
    r2_selection_entry_confirm.config(state=tk.ACTIVE)
    r2_selection_entry_confirm.bind(sequence="<ButtonRelease-1>", func=get_r2)
    r2_list.append("trigger r2")
    if len(r2_list) == 0:
        text_box.insert(index="end", chars="\nAdded r^2 option")

    if len(r2_list) > 1:
        r2_list.clear()
        r2_selection_entry.config(state=tk.DISABLED)
        r2_selection_entry_confirm.config(state=tk.DISABLED)
        r2_selection_entry_confirm.unbind("<ButtonRelease-1>")
        text_box.insert(index="end", chars="\nReset r^2 option")


def get_r2(event):
    if len(r2_list) == 1:
        # convert string to float
        r2_value.append(float(r2_selection_entry.get()))
        text_box.insert(index="end", chars="\nAdded r^2 value to calc.")
    else:
        text_box.insert(index="end", chars="\nNo r^2 option")


def pyplot_subplot(event):
    subplot_check.append("trigger subplot")
    if len(subplot_check) == 1:
        text_box.insert(index="end", chars="\nAdded subplot option")
        text_box.insert(index="end", chars="\nDisabled animation option")
        # modify aniamtion buttons
        animate.unbind("<ButtonRelease-1>")
        animate.configure(state=tk.DISABLED)
        animate.configure(text="Only available without subplots")
        animate_preview.unbind("<ButtonRelease-1>")
        animate_preview.configure(state=tk.DISABLED)
        animate_preview.configure(text="Only available without subplots")

    if len(subplot_check) > 1:
        subplot_check.clear()
        text_box.insert(index="end", chars="\nReset subplot option")
        text_box.insert(index="end", chars="\nAdded animation option")
        # modify aniamtion buttons
        animate.bind("<ButtonRelease-1>", func=animate_plot)
        animate.configure(text="Create Animation")
        animate.configure(state=tk.ACTIVE)
        animate_preview.bind("<ButtonRelease-1>", func=animate_preview_plot)
        animate_preview.configure(state=tk.ACTIVE)
        animate_preview.configure(text="Animation Preview")


def get_text(event):
    annotate_text.append(text_annotate.get(index1="1.0", index2="end"))


def preview(event):
    coord = []
    if subplot_check:
        for x in interpolation_grid:
            for y in x:
                if y.isdigit():
                    coord.append(int(y))
        # tuple from string grid
        tuple_grid = tuple(coord)
        # product of entries for iteration
        product = np.prod(tuple_grid)

        # blit frame to canvas
        figure = plt.Figure(figsize=(5, 5), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, master=frame_additional2)

        for i in range(product):
            # for i in range(4):
            axes = figure.add_subplot(tuple_grid[0], tuple_grid[1], i + 1, xlabel="x", ylabel="y")
            # axes = figure.add_subplot(2, 2, i + 1, xlabel="x", ylabel="y")
            axes.scatter([1, 2], [1, 3], c=color_marker[-1], marker=point_type[-1], label="string1")
            axes.plot([1, 3], [1, 3], c=color_plot[-1], linestyle=line_type[-1], label="string2")
            if len(queue_gridline) > 0:
                axes.grid(linestyle=grid_style[-1])
            axes.set(xlabel=f"x axis")
            axes.set(ylabel=f"y axis")
            axes.set(title=f"Title")

            if len(queue_legend) > 0:
                if len(legend_name) > 0:
                    figure.legend(title=legend_name[-1])

            if len(annotate_text) > 0:
                axes.annotate(text=annotate_text[-1], textcoords="axes fraction",
                              xycoords="axes fraction", xy=(float(text_entry_width.get()),
                                                            float(text_entry_height.get())))

        NavigationToolbar2Tk(figure_canvas, frame_additional2)
        figure_canvas.get_tk_widget().pack(fill=tk.BOTH)

    if not subplot_check:

        # blit canvas to screen / frame
        figure = plt.Figure(figsize=(5, 4.5), dpi=100)
        figure_canvas = FigureCanvasTkAgg(figure, master=frame_additional2)

        axes = figure.add_subplot(1, 1, 1, xlabel="x", ylabel="y")
        axes.scatter([1, 2], [1, 3], c=color_marker[-1], marker=point_type[-1], label="string1")
        axes.plot([1, 2], [1, 3], c=color_plot[-1], linestyle=line_type[-1], label="string2")
        if len(queue_gridline) > 0:
            axes.grid(linestyle=grid_style[-1])
        axes.set(xlabel=f"x axis")
        axes.set(ylabel=f"y axis")
        axes.set(title=f"Title")
        if len(queue_legend) > 0:
            if len(legend_name) > 0:
                figure.legend(title=legend_name[-1])

        if len(annotate_text) > 0:
            axes.annotate(text=annotate_text[-1], textcoords="axes fraction",
                          xycoords="axes fraction", xy=(float(text_entry_width.get()),
                                                        float(text_entry_height.get())))

        NavigationToolbar2Tk(figure_canvas, frame_additional2)
        figure_canvas.get_tk_widget().pack(fill=tk.BOTH)


def create_plot(event):

    global r2_criteria

    if len(x_label) == len(y_label) == len(title_pyplot) == len(graph_title_name):
        if bar["value"] > 95:
            if len(x_data_path) != 0 and len(xy_data_path) == 0:
                if len(y_data_path) != 0:
                    figure = plt.Figure(figsize=(9, 9), dpi=100)
                    figure_canvas = FigureCanvasTkAgg(figure, frame2)

                    # if user does not choose subplot
                    if not subplot_check:
                        axes = figure.add_subplot(111, xlabel="x", ylabel="y")
                        if len(queue_gridline) > 0:
                            axes.grid(linestyle=f"{grid_style[-1]}")
                        if len(x_label) >= 1:
                            # take the last one, more are for subplots
                            axes.set(xlabel=f"{x_label[-1]}")
                        if len(y_label) >= 1:
                            # take the last one, more are for subplots
                            axes.set(ylabel=f"{y_label[-1]}")
                        if len(title_pyplot) >= 1:
                            # take the last one, more are for subplots
                            axes.set(title=f"{title_pyplot[-1]}")

                        for i in range(len(x_data_path)):

                            list_x = []
                            list_y = []

                            aux_x = pd.read_excel(x_data_path[i], header=None, names=["x_axis"], index_col=None)
                            aux_y = pd.read_excel(y_data_path[i], header=None, names=["y_axis"], index_col=None)
                            for index, row in aux_x.iterrows():
                                list_x.append(row["x_axis"])
                            for index, row in aux_y.iterrows():
                                list_y.append(row["y_axis"])

                            if len(r2_list) > 0:
                                def r2_criteria():
                                    global check
                                    j = 0
                                    while True:
                                        # test_fit is a test function that takes x values for arguments
                                        test_fit = np.poly1d(np.polyfit(list_x, list_y, deg=j))
                                        # check whether r2 score of data (list_y) and curve fit is above threshold:
                                        check = metrics.r2_score(list_y, test_fit(list_x))
                                        if check >= r2_value[-1]:
                                            print(j)
                                            return j
                                        else:
                                            j = j + 1
                                            continue

                                g = np.polyfit(list_x, list_y, deg=int(r2_criteria()))
                                f = np.poly1d(g)

                                fit_name = np.polynomial.polynomial.Polynomial([round(k, 2) for k in g])
                                r2_rounded = round(check, 3)

                                # if r2 present add curve fit
                                axes.plot(list_x, f(list_x), c=color_plot[-1], linestyle=line_type[-1],
                                          label=f"curve fit: {fit_name}, R\u00B2 = {r2_rounded}")

                                # add plots to figure
                                axes.scatter(list_x, list_y, c=color_marker[-1], marker=point_type[-1], label=f"{graph_title_name[i]}")

                            if len(r2_list) == 0:
                                # add plots to figure
                                axes.scatter(list_x, list_y, c=color_marker[-1], marker=point_type[-1],
                                             label=f"{graph_title_name[i]}")

                        if len(queue_legend) > 0:
                            figure.legend(title=f"{legend_name[-1]}")

                        NavigationToolbar2Tk(figure_canvas, frame2)
                        figure_canvas.get_tk_widget().pack(fill=tk.BOTH)

                    # if user chooses subplot
                    if subplot_check:
                        coord = []
                        for x in interpolation_grid:
                            for y in x:
                                if y.isdigit():
                                    coord.append(int(y))
                        # tuple from string grid
                        tuple_grid = tuple(coord)
                        # product of entries for iteration
                        product = np.prod(tuple_grid)

                        for i in range(len(x_data_path)):

                            list_x = []
                            list_y = []

                            aux_x = pd.read_excel(x_data_path[i], header=None, names=["x_axis"], index_col=None)
                            aux_y = pd.read_excel(y_data_path[i], header=None, names=["y_axis"], index_col=None)
                            for index, row in aux_x.iterrows():
                                list_x.append(row["x_axis"])
                            for index, row in aux_y.iterrows():
                                list_y.append(row["y_axis"])

                            if len(r2_list) > 0:
                                def r2_criteria():
                                    global check
                                    j = 0
                                    while True:
                                        # test_fit is a test function that takes x values for arguments
                                        test_fit = np.poly1d(np.polyfit(list_x, list_y, deg=j))
                                        # check whether r2 score of data (list_y) and curve fit is above threshold:
                                        check = metrics.r2_score(list_y, test_fit(list_x))
                                        if check >= r2_value[-1]:
                                            print(j)
                                            return j
                                        else:
                                            j = j + 1
                                            continue

                                # interpolation part:
                                g = np.polyfit(list_x, list_y, deg=int(r2_criteria()))
                                f = np.poly1d(g)

                                r2_rounded = round(check, 3)
                                fit_name = np.polynomial.polynomial.Polynomial([round(k, 2) for k in g])

                                axes = figure.add_subplot(tuple_grid[0], tuple_grid[1], i + 1, xlabel="x", ylabel="y")
                                axes.plot(list_x, f(list_x), c=color_plot[-1],
                                          label=f"curve fit: {fit_name}, R\u00B2 = {r2_rounded}")
                                axes.scatter(list_x, list_y, c=color_marker[-1], label=f"{graph_title_name[i]}")

                            if len(r2_list) == 0:

                                axes = figure.add_subplot(tuple_grid[0], tuple_grid[1], i + 1, xlabel="x", ylabel="y")
                                axes.scatter(list_x, list_y, c=color_marker[-1], label=f"{graph_title_name[i]}")

                            if len(queue_gridline) > 0:
                                axes.grid(linestyle=f"{grid_style[-1]}")
                            if len(x_label) >= 1:
                                # take the last one, more are for subplots
                                axes.set(xlabel=f"{x_label[i]}")
                            if len(y_label) >= 1:
                                # take the last one, more are for subplots
                                axes.set(ylabel=f"{y_label[i]}")
                            if len(title_pyplot) >= 1:
                                # take the last one, more are for subplots
                                axes.set(title=f"{title_pyplot[i]}")

                        if len(queue_legend) > 0:
                            figure.legend(title=f"{legend_name[-1]}")

                        NavigationToolbar2Tk(figure_canvas, frame2)
                        figure_canvas.get_tk_widget().pack(fill=tk.BOTH)
        else:
            text_box.insert(index="end", chars="\nMissing Data!")
    else:
        messagebox.showerror("Counts", "Check counts for all labels and plot names")
        text_box.insert(index="end", chars="\nERROR: Counts not matching!")


def animate_plot(event):
    pass


def animate_preview_plot(event):
    pass
    #wn_animation = tk.Tk()
    #wn_animation.title("Animation Preview")
    #wn_animation.geometry("800x500")

    #frame_animation =



#########################################################
# creating window

wn = tk.Tk()
wn.geometry("1650x965+0+0")
wn.title("Grapher GUI by MathiasTensor")
wn.resizable(True, True)

# creating notebook

notebook = ttk.Notebook(master=wn, width=1650, height=965, padding=(5, 5, 5, 5))

# creating frame1 & frame2

frame = ttk.Frame(master=notebook)
frame.pack(fill=tk.BOTH)

frame1 = ttk.Frame(master=frame, relief=tk.GROOVE)
frame1.pack(fill=tk.BOTH, side=tk.LEFT)

frame2 = ttk.Frame(master=frame, relief=tk.GROOVE)
frame2.pack(fill=tk.BOTH, side=tk.RIGHT)

frame3 = ttk.Frame(master=notebook)
frame3.pack(fill=tk.BOTH, side=tk.RIGHT)

# adding frames to notebook !!! not to wn

notebook.add(child=frame, text="Plot 2D")
notebook.add(child=frame3, text="Plot 3D w\+ choices")

################################################################################
# adding grid widgets to frame 1

# Styles
style = ttk.Style()
style.configure("A.TButton", background="green")
style.configure("Disable.TButton", text="DO NOT USE", font="red", background="green")
style.map("TCheckbutton", foreground=[("selected", "red")])
style.configure("TLabel", font="bold")


# import x
import_x = ttk.Label(frame1, text="Import x-axis:")
import_x.grid(column=0, row=0, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# delete x button
delete_x_button = ttk.Button(frame1, text="Delete last x", command=deprogress_x, style="A.TButton")
delete_x_button.bind(sequence="<ButtonRelease-1>", func=delete_import_x)
delete_x_button.grid(column=0, row=0, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# import x button
import_x_button = ttk.Button(frame1, text="Import x", command=progress_x, style="A.TButton")
import_x_button.bind(sequence="<ButtonRelease-1>", func=get_data_x)
import_x_button.grid(column=0, row=1, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)

# text box x
text_x = tk.scrolledtext.ScrolledText(master=frame1, height=3, width=7)
text_x.grid(column=1, row=0, columnspan=1, rowspan=2, padx=pad_x, pady=pad_y, sticky=tk.NSEW)

# import y
import_y = ttk.Label(frame1, text="Import y-axis:")
import_y.grid(column=0, row=2, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# delete y button
delete_y_button = ttk.Button(frame1, text="Delete last y", command=deprogress_y, style="A.TButton")
delete_y_button.bind(sequence="<ButtonRelease-1>", func=delete_import_y)
delete_y_button.grid(column=0, row=2, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# import y button
import_y_button = ttk.Button(frame1, text="Import y", command=progress_y, style="A.TButton")
import_y_button.bind(sequence="<ButtonRelease-1>", func=get_data_y)
import_y_button.grid(column=0, row=3, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)

# text box y
text_y = tk.scrolledtext.ScrolledText(master=frame1, height=3, width=7)
text_y.grid(column=1, row=2, columnspan=1, rowspan=2, padx=pad_x, pady=pad_y, sticky=tk.NSEW)


# import both
import_xy = ttk.Label(frame1, text="Import x,y:")
import_xy.grid(column=0, row=4, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# import both button
import_xy_button = ttk.Button(frame1, text="Import x,y", command=progress_xy, style="A.TButton")
import_xy_button.bind(sequence="<ButtonRelease-1>", func=get_data_xy)
import_xy_button.grid(column=0, row=5, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)

# text box both
text_both = tk.scrolledtext.ScrolledText(master=frame1, height=3, width=7)
text_both.grid(column=1, row=4, columnspan=1, rowspan=2, padx=pad_x, pady=pad_y, sticky=tk.NSEW)

# delete both button
delete_xy_button = ttk.Button(frame1, text="Delete last x,y", command=deprogress_xy, style="A.TButton")
delete_xy_button.bind(sequence="<ButtonRelease-1>", func=delete_import_xy)
delete_xy_button.grid(column=0, row=4, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# Data sets:
data_button = ttk.Button(master=frame1, text="Data List", style="A.TButton")
data_button.grid(column=0, row=6, columnspan=1, rowspan=1, sticky=tk.W, padx=15)
data_button.bind(sequence="<ButtonRelease-1>", func=datasets)

# add r2 score
r2_score_button = ttk.Checkbutton(master=frame1, text=f"Add R\u00B2 score")
r2_score_button.grid(column=0, row=6, columnspan=1, rowspan=1, sticky=tk.E)
r2_score_button.bind(sequence="<ButtonRelease-1>", func=add_r2)

# add r2_selection_label
r2_selection_label = ttk.Label(frame1, text="R\u00B2 score threshold:")
r2_selection_label.grid(column=1, row=6, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add r2_selection_entry
r2_selection_entry = ttk.Entry(frame1, width=30, state=tk.DISABLED)
r2_selection_entry.grid(column=1, row=6, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# confirm add r2_selection_entry
r2_selection_entry_confirm = ttk.Button(frame1, text="Confirm", style="A.TButton", state=tk.DISABLED)
r2_selection_entry_confirm.grid(column=1, row=7, columnspan=1, padx=0, pady=0, sticky=tk.EW)

# add grid
add_grid = ttk.Checkbutton(frame1, text="Add Grid")
add_grid.bind(sequence="<ButtonRelease-1>", func=pyplot_grid)
add_grid.grid(column=0, row=13, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# add x label - header
label_x = ttk.Label(frame1, text="x-label / input below:")
label_x.grid(column=0, row=7, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add x label
label_x_entry = ttk.Entry(frame1, justify="left", width=30)
label_x_entry.grid(column=0, row=8, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add x label delete button
x_label_delete = ttk.Button(master=frame1, text="Delete last\nlabel input", style="A.TButton")
x_label_delete.bind(sequence="<ButtonRelease-1>", func=delete_last_x)
x_label_delete.grid(column=0, row=8, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# add x label button
x_label_checkmark = ttk.Button(master=frame1, text="Validate input\n(not optional)", style="A.TButton")
x_label_checkmark.bind(sequence="<ButtonRelease-1>", func=validate_x)
x_label_checkmark.grid(column=1, row=8, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add x label counter
x_label_counter = ttk.Label(master=frame1, text=f"Count number of instances: {0}\n"
                                                f"If > 0 then all counts must match")
x_label_counter.grid(column=1, row=8, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# add y label - header
label_y = ttk.Label(frame1, text="y-label / input below:")
label_y.grid(column=0, row=9, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add y label
label_y_entry = ttk.Entry(master=frame1, justify="left", width=30)
label_y_entry.grid(column=0, row=10, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add y label delete button
y_label_delete = ttk.Button(master=frame1, text="Delete last\nlabel input", style="A.TButton")
y_label_delete.bind(sequence="<ButtonRelease-1>", func=delete_last_y)
y_label_delete.grid(column=0, row=10, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# add y label button
y_label_checkmark = ttk.Button(master=frame1, text="Validate input\n(not optional)", style="A.TButton")
y_label_checkmark.bind(sequence="<ButtonRelease-1>", func=validate_y)
y_label_checkmark.grid(column=1, row=10, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add y label counter
y_label_counter = ttk.Label(master=frame1, text=f"Count number of instances: {0}\n"
                                                f"If > 0 then all counts must match")
y_label_counter.grid(column=1, row=10, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# add title - header
title = ttk.Label(frame1, text="Title / input below:")
title.grid(column=0, row=11, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add title - entry
title = ttk.Entry(frame1, justify="left", width=30)
title.grid(column=0, row=12, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add title label delete button
title_delete = ttk.Button(master=frame1, text="Delete last\nlabel input", style="A.TButton")
title_delete.bind(sequence="<ButtonRelease-1>", func=delete_last_title)
title_delete.grid(column=0, row=12, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# add title label checkmark
title_checkmark = ttk.Button(master=frame1, text=f"Validate input\n(not optional)", style="A.TButton")
title_checkmark.bind(sequence="<ButtonRelease-1>", func=validate_title)
title_checkmark.grid(column=1, row=12, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add title counter
title_counter = ttk.Label(master=frame1, text=f"Count number of instances: {0}\n"
                                                f"If > 0 then all counts must match")
title_counter.grid(column=1, row=12, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# legend
legend = ttk.Checkbutton(master=frame1, text="Check for legend")
legend.bind(sequence="<ButtonRelease-1>", func=pyplot_legend)
legend.grid(column=0, row=13, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# Add subplot
subplot = ttk.Checkbutton(master=frame1, text="Check for subplot\n(Configure in Advanced options)")
subplot.bind(sequence="<ButtonRelease-1>", func=pyplot_subplot)
subplot.grid(column=1, row=13, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)

# Additional
additional = ttk.Button(master=frame1, text="Advanced options", style="A.TButton")
additional.grid(column=1, row=17, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.NSEW)
additional.bind(sequence="<ButtonRelease-1>", func=create_window)

# Create plot
plot = ttk.Button(master=frame1, text="Create Plot", style="A.TButton")
plot.grid(column=0, row=17, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
plot.bind(sequence="<ButtonRelease-1>", func=create_plot)

# Progressbar
bar = ttk.Progressbar(master=frame1, orient="horizontal", length=290, mode="determinate")
bar.grid(column=0, row=19, rowspan=1, columnspan=2, padx=0, pady=5, sticky=tk.NSEW)

# Animation button
animate = ttk.Button(master=frame1, text="Create Animation", style="A.TButton")
animate.grid(column=0, row=18, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
animate.bind(sequence="<ButtonRelease-1>", func=animate_plot)

# Animation button
animate_preview = ttk.Button(master=frame1, text="Animation Preview", style="A.TButton")
animate_preview.grid(column=1, row=18, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.EW)
animate_preview.bind(sequence="<ButtonRelease-1>", func=animate_preview_plot)



# Animation settings / Preview



# text box for diagnostic information

text_box = tk.scrolledtext.ScrolledText(master=frame1, height=19)
text_box.insert(index="end", chars=f"INFORMATION: All relevant "
                                   "information will be printed here! For x and y data please use"
                                   ".csv files or .xlsx files. If you use .txt files with"
                                   "an unusual delimiter, provide that information "
                                   "in Advanced options.\n"
                                   "------------------------------------------"
                                   "-----------------------------------------\n"
                                   "Plots don't need axes or titles and names. But for"
                                   " consistency provide equal number of x and y labels."
                                   " Valid input data is .xlsx, .xls or .csv files (.txt supported,"
                                   " but a delimiter must be provided and first number in a line "
                                   " must be a row number in accordance with DataFrame rules.)\n"
                                   "------------------------------------------"
                                   "-----------------------------------------\n"
                                   "For now only .xlsx is accepted. Please use only 1"
                                   " column for data for import x and import y. For import xy"
                                   " don't use because it's not properly implemented\n"
                                   "------------------------------------------"
                                   "-----------------------------------------     LOG:\n")


text_box.grid(column=0, row=20, rowspan=1, columnspan=2, padx=0, pady=5, sticky=tk.NSEW)

# name of graph
name_graph = ttk.Label(master=frame1, text="Input graph name/(s):")
name_graph.grid(column=0, row=14, columnspan=1, padx=pad_x, pady=pad_y)

# graph name entry
entry_graph = ttk.Entry(master=frame1, width=30)
entry_graph.grid(column=0, row=15, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add title label delete button
graph_name_delete = ttk.Button(master=frame1, text="Delete last\nname input", style="A.TButton")
graph_name_delete.bind(sequence="<ButtonRelease-1>", func=delete_last_name)
graph_name_delete.grid(column=0, row=15, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)

# add title label checkmark
title_checkmark = ttk.Button(master=frame1, text=f"Validate input\n(not optional)", style="A.TButton")
title_checkmark.bind(sequence="<ButtonRelease-1>", func=validate_name)
title_checkmark.grid(column=1, row=15, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.W)

# add name counter
name_counter = ttk.Label(master=frame1, text=f"Count number of instances: {0}\n"
                                                f"If > 0 then all counts must match")
name_counter.grid(column=1, row=15, columnspan=1, padx=pad_x, pady=pad_y, sticky=tk.E)
########################################################################
# ending
notebook.pack()
wn.mainloop()