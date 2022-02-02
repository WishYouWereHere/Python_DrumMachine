import tkinter as tk

window = tk.Tk()
frame = tk.Frame(master=window, width=1000, height=300)
frame.pack()

kick_drum = tk.Button(
    master = frame,
    text = "Kick drum",
    width = 12,
    height = 5,
    bg = "black",
    fg = "white",
)
kick_drum.place(x=25, y=25)

snare_drum = tk.Button(
    master = frame,
    text = "Snare drum",
    width = 12,
    height = 5,
    bg = "black",
    fg = "white",
)
snare_drum.place(x=125, y=25)

closed_high_hat = tk.Button(
    master = frame,
    text = "Closed High hat",
    width = 12,
    height = 5,
    bg = "black",
    fg = "white",
)
closed_high_hat.place(x=225, y=25)

open_high_hat = tk.Button(
    master = frame,
    text = "Open High hat",
    width = 12,
    height = 5,
    bg = "black",
    fg = "white",
)
open_high_hat.place(x=325, y=25)

window.mainloop()