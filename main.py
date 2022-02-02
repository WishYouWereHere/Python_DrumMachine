import tkinter as tk

window = tk.Tk()

kick_drum_frame = tk.Frame()
snare_drum_frame = tk.Frame()
high_hat_frame = tk.Frame()


kick_drum = tk.Button(
    master = kick_drum_frame,
    text = "Kick drum",
    width = 10,
    height = 5,
    bg = "black",
    fg = "white",
)
snare_drum = tk.Button(
    master = snare_drum_frame,
    text = "Snare drum",
    width = 10,
    height = 5,
    bg = "black",
    fg = "white",
)
high_hat = tk.Button(
    master = high_hat_frame,
    text = "High hat",
    width = 10,
    height = 5,
    bg = "black",
    fg = "white",
)
kick_drum.pack()
snare_drum.pack()
high_hat.pack()

kick_drum_frame.pack()
snare_drum_frame.pack()
high_hat_frame.pack()

window.mainloop()