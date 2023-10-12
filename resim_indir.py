from bing_image_downloader import downloader
import tkinter as tk

def download():
    downloader.download(prompt.get(), limit=int(times.get()),  output_dir=fileName.get(), adult_filter_off=True, force_replace=False, timeout=int(timeout.get()), verbose=True)


app = tk.Tk()
app.geometry('800x600')
app.title('IMG DWN')
app.resizable = True
infoEntry = tk.Label(text=" IMG DWN ", font = "Helvetica 32", fg="light green", bg="gray")
infoEntry.pack()
i1 = tk.Label(text = "PROMPT")
i2 = tk.Label(text="FILE NAME")
i3 = tk.Label(text="LIMIT")
i4 = tk.Label(text="TIMEOUT")
prompt = tk.Entry(width=30, font="Helvetica 16", fg="light green", bg="gray")
fileName = tk.Entry(width=30, font="Helvetica 16", fg="light green", bg="gray")
times = tk.Entry(width=30, font="Helvetica 16", fg="light green", bg="gray")
timeout = tk.Entry(width=30, font="Helvetica 16", fg="light green", bg="gray")
okButton = tk.Button(text="DOWNLOAD", font="Helvetica 16", fg="light green", bg="gray", command=download)

i1.pack()
prompt.pack()
i2.pack()
fileName.pack()
i3.pack()
times.pack()
i4.pack()
timeout.pack()
okButton.pack()

app.mainloop()




