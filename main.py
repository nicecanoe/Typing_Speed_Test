import tkinter
from tkinter import messagebox
import time

timer_started = False
start_time = None
the_score = 0
the_example_plain = "Sunt aut facere repellat provident occaecati excepturi optio reprehenderit quia et suscipit suscipit recusandae consequuntur expedita et cum reprehenderit molestiae ut ut quas totam nostrum rerum est autem sunt rem eveniet architecto \nQui est esse, est rerum tempore vitae sequi sint nihil reprehenderit dolor beatae ea dolores neque fugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis qui aperiam non debitis possimus qui neque nisi nulla \nEa molestias quasi exercitationem repellat qui ipsa sit aut et iusto sed quo iure voluptatem occaecati omnis eligendi aut ad voluptatem doloribus vel accusantium quis pariatur molestiae porro eius odio et labore et velit aut"


def start_timer(event):
    global timer_started, start_time,the_score
 # 如果计时未开始，则记录当前时间并设置计时开始标志
    if not timer_started:
        start_time = time.time()
        timer_started = True
        # 这里可以更新UI，显示计时开始
    print(time.time() - start_time)
    if time.time() - start_time >= 60:
        messagebox.showinfo("STOP","TIME OVER")
        the_word = the_entry_box.get().split(" ")
        the_example_word = the_example_plain.split(" ")
        i = 0
        for word in the_word:
            if word == the_example_word[i].strip().lower():
                i += 1
                the_score += 1
        messagebox.showinfo("STOP", f"You speed is {the_score}/WPM")




windows = tkinter.Tk()
windows.title("Typing Speed Test")

the_title = tkinter.Label(windows, text="Typing Speed Test",font=("Arial",24,"bold"))
the_title.grid(column=1,row=0)

the_example = tkinter.Label(windows, text="Example Text",font=("Arial",20))
the_example.grid(column=1,row=1)

the_example_text = tkinter.Text(height=15,width=50,font=("Arial",20))
the_example_text.insert(tkinter.END, the_example_plain)
the_example_text.grid(column=1,row=2)

the_entry = tkinter.Label(text="The Entry Box")
the_entry.grid(column=1,row=3)

the_entry_box = tkinter.Text(width=50,height=15,font=("Arial",20))
the_entry_box.bind("<Key>", start_timer)
the_entry_box.grid(column=1,row=4)



windows.config(padx=20,pady=20)
windows.mainloop()