from tkinter import *
from PIL import Image, ImageTk

def mainwindow():
    global mainpage
    mainpage = Tk()
    mainpage.geometry("500x550+525+125")
    mainpage.title("Train Yourself")
    mainpage.resizable(FALSE, FALSE)

    background_image = Image.open("C:\\Users\\emin2\\Desktop\\OOP Final Project\\SMC-MRT.jpg")
    background_image = background_image.resize((500, 550), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(background_image)

    background_label = Label(mainpage, image=photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    mainpage_title = Label(mainpage, text="TRAIN TO METROPOLITAN", font=("Compact", 21, "bold"))
    mainpage_title.pack(pady=20)

    Label(mainpage, text="Choose Your Transit Line", font=("Compact", 10, "bold"), bd=0).pack(pady=10)
    Button(mainpage, text="LRT-1", font=("Helvetica", 18, "bold"), width=23, height=3, bd=9, bg="#526D82", fg="white", command=lrt1).pack(pady=4)
    Button(mainpage, text="LRT-2", font=("Helvetica", 18, "bold"), width=23, height=3, bd=9, bg="#526D82", fg="white", command=lrt2).pack(pady=4)
    Button(mainpage, text="MRT", font=("Helvetica", 18, "bold"), width=23, height=3, bd=9, bg="#526D82", fg="white", command=mrt).pack(pady=4)

    mainpage.mainloop()

def lrt1():
    global pagelrt1
    mainpage.withdraw()
    pagelrt1 = Toplevel(mainpage)
    pagelrt1.geometry("710x680+450+50")
    pagelrt1.title("LRT-1 Transit")
    pagelrt1.resizable(FALSE, FALSE)

    image_lrt1map = Image.open("C:\\Users\\emin2\\Desktop\\OOP Final Project\\LRT1.png")
    desired_width = 450
    desired_height = 600
    resized_image = image_lrt1map.resize((desired_width, desired_height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    Label(pagelrt1, image=photo).grid(column=1, row=1, columnspan=5, rowspan=21)

    global lrt1chosenstation1
    lrt1chosenstation1 = IntVar()

    global lrt1chosenstation2
    lrt1chosenstation2 = IntVar()

    global lrt1stations
    lrt1stations = ["Invalid Station", "Baclaran", "EDSA", "Libertad", "Gil Puyat", "Vito Cruz", "Quirino", "Pedro Gil",
                    "United Nation", "Central Terminal", "Carriedo", "Doroteo Jose", "Bambang", "Tayuman",
                    "Blumentritt", "Abad Santos", "R. Papa", "5th Avenue", "Monumento", "Balintawak", "Roosevelt"]

    Label(pagelrt1, text="LRT-1 Transit Line", font=("Century", 18, "bold")).grid(column=3, row=0)
    Label(pagelrt1, text="Station    ", font=("Century", 15,"bold")).grid(column=0, row=0)
    Label(pagelrt1, text="Destination", font=("Century", 15, "bold")).grid(column=6, row=0)

    for i in range(1, 21):
        Radiobutton(pagelrt1, variable=lrt1chosenstation1, text=lrt1stations[i], value=i, font=("Century", 9)).grid(column=0, row=i, sticky='w')

    for i in range(1, 21):
        Radiobutton(pagelrt1, variable=lrt1chosenstation2, text=lrt1stations[i], value=i, font=("Century", 9)).grid(column=6, row=i, sticky='w')

    global showinfo_lrt1
    showinfo_lrt1 = StringVar()
    Entry(pagelrt1, width=40, state="readonly", textvariable=showinfo_lrt1, bd=0, font=("Century", 13, "bold"), fg="red").grid(column=3, row=24)

    Button(pagelrt1, text="Continue", command=calc_lrt1, width=13, height=1, bd=3, bg="lightgreen").grid(column=6, row=24, pady=7)
    Button(pagelrt1, text="Main Page", command=lrt1backtomain, width=13, height=1, bd=3, bg="lightgreen").grid(column=0, row=24, pady=7)

    pagelrt1.mainloop()

def calc_lrt1():
    fare_lrt1 = [0, 15, 15, 15, 15, 15, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30]
    distance_lrt1 = [0, 588, 1010, 730, 1061, 827, 794, 754, 1214, 725, 685, 648, 618, 671, 927, 660, 954, 1087,
                     2250, 1870]

    chosen_stationlrt1 = lrt1chosenstation1.get()
    destinationlrt1 = lrt1chosenstation2.get()

    if chosen_stationlrt1 == 0 and destinationlrt1 == 0 or chosen_stationlrt1 == 0 or destinationlrt1 == 0:
        showinfo_lrt1.set("\t        Invalid Stations")
    elif chosen_stationlrt1 == destinationlrt1:
        showinfo_lrt1.set("        You have Chosen the Same Stations")
    else:
        global resultscreenlrt1
        pagelrt1.withdraw()
        resultscreenlrt1 = Toplevel(mainpage)
        resultscreenlrt1.geometry("580x426+525+125")
        resultscreenlrt1.title("Result Lrt-1")
        resultscreenlrt1.configure(bg="#E6DDC4")
        resultscreenlrt1.resizable(FALSE, FALSE)

        Button(resultscreenlrt1, text="", bg='black', state='disabled', width=11, height=23, bd=0).grid(column=0, row=1)
        Button(resultscreenlrt1, text="", bg='black', state='disabled', width=11, height=23, bd=0).grid(column=6, row=1)

        for i in range(0, 7):
            Button(resultscreenlrt1, text="============", bg='black', state='disabled', width=11, height=2, bd=0).grid(
                column=i, row=0)

        Button(resultscreenlrt1, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(column=0, row=6)
        Button(resultscreenlrt1, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(column=1, row=6)
        Button(resultscreenlrt1, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(column=2, row=6)
        Button(resultscreenlrt1, text="Main Page", command=lrt1resultbacktomain, bg="#E6DDC4", fg="blue", width=11, height=2, bd=0).grid(column=3, row=6)
        Button(resultscreenlrt1, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(column=4, row=6)
        Button(resultscreenlrt1, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(column=5, row=6)
        Button(resultscreenlrt1, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(column=6, row=6)

        calc_lrt1 = abs(chosen_stationlrt1 - destinationlrt1)
        timelrt1 = calc_lrt1 * 3
        calc_lrt1_distance = chosen_stationlrt1 - destinationlrt1
        distance_lrt_one_array = 0

        if calc_lrt1_distance < 0:
            for i in range(chosen_stationlrt1, destinationlrt1):
                distance_lrt_one_array += distance_lrt1[i]
        else:
            for i in range(destinationlrt1, chosen_stationlrt1):
                distance_lrt_one_array += distance_lrt1[i]

        Label(resultscreenlrt1, text="\n\t\t\t\t" + "\n" + lrt1stations[chosen_stationlrt1] + "  >>>  " + lrt1stations[destinationlrt1] +
                    "\n" + "\n" + "P " + str(fare_lrt1[calc_lrt1]) + "\n" + "\n" + str(timelrt1) + " mins" +"\n" + "\n" + str(distance_lrt_one_array)
                    + " meters\n" + "\n\t\t\t\t", font=("Compact", 15, "bold"), bg="#E6DDC4", width=34, height=14, bd=0, fg="#675D50").grid(column=1, row=1, columnspan=5)

        resultscreenlrt1.mainloop()

def lrt2():
    global pagelrt2
    mainpage.withdraw()
    pagelrt2 = Toplevel(mainpage)
    pagelrt2.geometry("840x430+375+160")
    pagelrt2.title("LRT-2 Transit")
    pagelrt2.resizable(FALSE, FALSE)

    image_lrt2map = Image.open("C:\\Users\\emin2\\Desktop\\OOP Final Project\\LRT2.png")
    desired_width = 600
    desired_height = 350
    resized_image = image_lrt2map.resize((desired_width, desired_height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    Label(pagelrt2, image=photo).grid(column=1, row=1, columnspan=5, rowspan=15)

    global lrt2chosenstation1
    lrt2chosenstation1 = IntVar()

    global lrt2chosenstation2
    lrt2chosenstation2 = IntVar()

    global lrt2stations
    lrt2stations = ["Invalid Station", "Recto", "Legarda", "Purez", "V. Mapa", "J. Ruiz", "Gilmore", "Betty Go",
                    "Cubao", "Anonas", "Katipunan", "Santolan", "Marikina", "Antipolo"]

    Label(pagelrt2, text="LRT-2 Transit Line", font=("Century", 18, "bold")).grid(column=3, row=0)
    Label(pagelrt2, text="Station    ", font=("Century", 15, "bold")).grid(column=0, row=0)
    Label(pagelrt2, text="Destination", font=("Century", 15, "bold")).grid(column=6, row=0)

    for i in range(1, 14):
        Radiobutton(pagelrt2, variable=lrt2chosenstation1, text=lrt2stations[i], value=i, font=("Century", 9)).grid(column=0, row=i, sticky='w')

    for i in range(1, 14):
        Radiobutton(pagelrt2, variable=lrt2chosenstation2, text=lrt2stations[i], value=i, font=("Century", 9)).grid(column=6, row=i, sticky='w')

    global showinfo_lrt2
    showinfo_lrt2 = StringVar()
    Entry(pagelrt2, width=50, state="readonly", textvariable=showinfo_lrt2, bd=0, font=("Century", 13, "bold"), fg="red").grid(column=3, row=16)

    Button(pagelrt2, text="Continue", command=calc_lrt2, width=13, height=1, bd=3, bg="lightgreen").grid(column=6, row=16, pady=7)
    Button(pagelrt2, text="Main Page", command=lrt2backtomain, width=13, height=1, bd=3, bg="lightgreen").grid(column=0, row=16, pady=7)

    pagelrt2.mainloop()

def calc_lrt2():
    fare_lrt2 = [0, 15, 15, 15, 20, 20, 20, 20, 25, 25, 25, 30, 30]
    distance_lrt2 = [0, 1050, 1389, 1357, 1234, 928, 1075, 1164, 1438, 955, 1970, 2320, 1670]

    chosen_stationlrt2 = lrt2chosenstation1.get()
    destinationlrt2 = lrt2chosenstation2.get()

    if chosen_stationlrt2 == 0 and destinationlrt2 == 0 or chosen_stationlrt2 == 0 or destinationlrt2 == 0:
        showinfo_lrt2.set("\t\t    Invalid Stations")
    elif chosen_stationlrt2 == destinationlrt2:
        showinfo_lrt2.set("\t    You have Chosen the Same Stations")
    else:
        global resultscreenlrt2
        pagelrt2.withdraw()
        resultscreenlrt2 = Toplevel(mainpage)
        resultscreenlrt2.geometry("580x426+525+125")
        resultscreenlrt2.title("Result Lrt-2")
        resultscreenlrt2.configure(bg="#E6DDC4")
        resultscreenlrt2.resizable(FALSE, FALSE)

        Button(resultscreenlrt2, text="", bg='black', state='disabled', width=11, height=23, bd=0).grid(column=0, row=1)
        Button(resultscreenlrt2, text="", bg='black', state='disabled', width=11, height=23, bd=0).grid(column=6, row=1)

        for i in range(0, 7):
            Button(resultscreenlrt2, text="============", bg='black', state='disabled', width=11, height=2, bd=0).grid(
                column=i, row=0)

        Button(resultscreenlrt2, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=0, row=6)
        Button(resultscreenlrt2, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=1, row=6)
        Button(resultscreenlrt2, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=2, row=6)
        Button(resultscreenlrt2, text="Main Page", command=lrt2resultbacktomain, bg="#E6DDC4", fg="blue", width=11,
               height=2, bd=0).grid(column=3, row=6)
        Button(resultscreenlrt2, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=4, row=6)
        Button(resultscreenlrt2, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=5, row=6)
        Button(resultscreenlrt2, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=6, row=6)

        calc_lrt2 = abs(chosen_stationlrt2 - destinationlrt2)
        timelrt2 = calc_lrt2 * 3
        calc_lrt2_distance = chosen_stationlrt2 - destinationlrt2
        distance_lrt_two_array = 0

        if calc_lrt2_distance < 0:
            for i in range(chosen_stationlrt2, destinationlrt2):
                distance_lrt_two_array += distance_lrt2[i]
        else:
            for i in range(destinationlrt2, chosen_stationlrt2):
                distance_lrt_two_array += distance_lrt2[i]

        Label(resultscreenlrt2,
              text="\n\t\t\t\t" + "\n" + lrt2stations[chosen_stationlrt2] + "  >>>  " + lrt2stations[destinationlrt2] +
                   "\n" + "\n" + "P " + str(fare_lrt2[calc_lrt2]) + "\n" + "\n" + str(
                  timelrt2) + " mins" + "\n" + "\n" + str(distance_lrt_two_array)
                   + " meters\n" + "\n\t\t\t\t", font=("Compact", 15, "bold"), bg="#E6DDC4", width=34, height=14, bd=0,
              fg="#675D50").grid(column=1, row=1, columnspan=5)

        resultscreenlrt2.mainloop()

def mrt():
    global pagemrt
    mainpage.withdraw()
    pagemrt = Toplevel(mainpage)
    pagemrt.geometry("740x715+400+50")
    pagemrt.title("MRT Transit")
    pagemrt.resizable(FALSE, FALSE)

    image_mrtmap = Image.open("C:\\Users\\emin2\\Desktop\\OOP Final Project\\MRT.png")
    desired_width = 425
    desired_height = 635
    resized_image = image_mrtmap.resize((desired_width, desired_height), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    Label(pagemrt, image=photo).grid(column=1, row=1, columnspan=4, rowspan=14)

    global mrtchosenstation1
    mrtchosenstation1 = IntVar()

    global mrtchosenstation2
    mrtchosenstation2 = IntVar()

    global mrtstations
    mrtstations = ["Invalid Station", "Taft", "Magallanes", "Ayala", "Beundia", "Guadalupe", "Boni", "Shaw Blvd",
                   "Ortigas", "Santolan", "Araneta Center-Cubao", "GMA Kamuning", "Q. Ave", "N. Ave"]

    Label(pagemrt, text="MRT Transit Line", font=("Century", 18, "bold")).grid(column=3, row=0)
    Label(pagemrt, text="Station      ", font=("Century", 15, "bold")).grid(column=0, row=0)
    Label(pagemrt, text="Destination", font=("Century", 15, "bold")).grid(column=6, row=0)

    for i in range(1, 14):
        Radiobutton(pagemrt, variable=mrtchosenstation1, text=mrtstations[i], value=i, font=("Century", 9)).grid(column=0, row=i, sticky='w')

    for i in range(1, 14):
        Radiobutton(pagemrt, variable=mrtchosenstation2, text=mrtstations[i], value=i, font=("Century", 9)).grid(column=6, row=i, sticky='w')

    global showinfo_mrt
    showinfo_mrt = StringVar()
    Entry(pagemrt, width=35, state="readonly", textvariable=showinfo_mrt, bd=0, font=("Century", 13, "bold"), fg="red").grid(column=3, row=16)

    Button(pagemrt, text="Continue", command=calc_mrt, width=13, height=1, bd=3, bg="lightgreen").grid(column=6, row=16, pady=7)
    Button(pagemrt, text="Main Page", command=mrtbacktomain, width=13, height=1, bd=3, bg="lightgreen").grid(column=0, row=16, pady=7)

    pagemrt.mainloop()

def calc_mrt():
    fare_mrt = [0, 13, 13, 16, 16, 20, 20, 20, 24, 24, 24, 28, 28]
    distance_mrt = [0, 1630, 1020, 1960, 3480, 660, 840, 670, 1790, 1120, 1615, 800, 1025]

    chosen_stationmrt = mrtchosenstation1.get()
    destinationmrt = mrtchosenstation2.get()

    if chosen_stationmrt == 0 and destinationmrt == 0 or chosen_stationmrt == 0 or destinationmrt == 0:
        showinfo_mrt.set("\t  Invalid Stations")
    elif chosen_stationmrt == destinationmrt:
        showinfo_mrt.set("  You have Chosen the Same Stations")
    else:
        global resultscreenmrt
        pagemrt.withdraw()
        resultscreenmrt = Toplevel(mainpage)
        resultscreenmrt.geometry("580x426+525+125")
        resultscreenmrt.title("Result Lrt-2")
        resultscreenmrt.configure(bg="#E6DDC4")
        resultscreenmrt.resizable(FALSE, FALSE)

        Button(resultscreenmrt, text="", bg='black', state='disabled', width=11, height=23, bd=0).grid(column=0, row=1)
        Button(resultscreenmrt, text="", bg='black', state='disabled', width=11, height=23, bd=0).grid(column=6, row=1)

        for i in range(0, 7):
            Button(resultscreenmrt, text="============", bg='black', state='disabled', width=11, height=2, bd=0).grid(
                column=i, row=0)

        Button(resultscreenmrt, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=0, row=6)
        Button(resultscreenmrt, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=1, row=6)
        Button(resultscreenmrt, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=2, row=6)
        Button(resultscreenmrt, text="Main Page", command=mrtresultbacktomain, bg="#E6DDC4", fg="blue", width=11,
               height=2, bd=0).grid(column=3, row=6)
        Button(resultscreenmrt, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=4, row=6)
        Button(resultscreenmrt, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=5, row=6)
        Button(resultscreenmrt, text="===========", bg='black', state='disabled', width=11, height=2, bd=0).grid(
            column=6, row=6)

        calc_mrt = abs(chosen_stationmrt - destinationmrt)
        timemrt = calc_mrt * 3
        calc_mrt_distance = chosen_stationmrt - destinationmrt
        distance_mrt_array = 0

        if calc_mrt_distance < 0:
            for i in range(chosen_stationmrt, destinationmrt):
                distance_mrt_array += distance_mrt[i]
        else:
            for i in range(destinationmrt, chosen_stationmrt):
                distance_mrt_array += distance_mrt[i]

        Label(resultscreenmrt,
              text="\n\t\t\t\t" + "\n" + mrtstations[chosen_stationmrt] + "  >>>  " + mrtstations[destinationmrt] +
                   "\n" + "\n" + "P " + str(fare_mrt[calc_mrt]) + "\n" + "\n" + str(
                  timemrt) + " mins" + "\n" + "\n" + str(distance_mrt_array)
                   + " meters\n" + "\n\t\t\t\t", font=("Compact", 15, "bold"), bg="#E6DDC4", width=34, height=14, bd=0,
              fg="#675D50").grid(column=1, row=1, columnspan=5)

        resultscreenmrt.mainloop()

def lrt1resultbacktomain():
    resultscreenlrt1.destroy()
    mainpage.deiconify()

def lrt2resultbacktomain():
    resultscreenlrt2.destroy()
    mainpage.deiconify()

def mrtresultbacktomain():
    resultscreenmrt.destroy()
    mainpage.deiconify()

def lrt1backtomain():
    pagelrt1.destroy()
    mainpage.deiconify()

def lrt2backtomain():
    pagelrt2.destroy()
    mainpage.deiconify()

def mrtbacktomain():
    pagemrt.destroy()
    mainpage.deiconify()

mainwindow()
