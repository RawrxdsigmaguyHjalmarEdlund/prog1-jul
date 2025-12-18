"""Simple clicker GUI using tkinter."""
import random
import tkinter as tk

def main():
    """Run the clicker application."""
    cookies = 0
    cookies_per_click = 1
    cookies_per_second = 1

    root = tk.Tk()
    root.columnconfigure(0, weight=1, minsize=100)
    root.columnconfigure(1, weight=2, minsize=200)
    root.columnconfigure(2, weight=1, minsize=100)
    root.rowconfigure(0, weight=1, minsize=50)
    root.rowconfigure(1, weight=2, minsize=100)
    root.rowconfigure(2, weight=1, minsize=50)

    img1 = None
    img2 = None
    current_frame = 1
    click_btn = None

    def click_cookie():
        nonlocal cookies, current_frame
        cookies += cookies_per_click
        cookie_label.config(text=f"Haki: {cookies}")
        if img1 is not None and img2 is not None and click_btn is not None:
            if current_frame == 1:
                click_btn.config(image=img2)
                click_btn.image = img2
                current_frame = 2
            else:
                click_btn.config(image=img1)
                click_btn.image = img1
                current_frame = 1

    def start_auto_generation():
        nonlocal cookies
        cookies += cookies_per_second
        cookie_label.config(text=f"Haki: {cookies}")
        try:
            if random.random() < 0.02:
                open_popup()
        except Exception:
            pass
        root.after(1000, start_auto_generation)

    def open_popup():
        nonlocal cookies
        top = tk.Toplevel(root)
        top.title("Pedro")
        try:
            pedro_img = tk.PhotoImage(file="Pedro.png")
        except tk.TclError:
            pedro_img = None

        def on_pedro_click():
            nonlocal cookies
            cookies *= 2
            cookie_label.config(text=f"[Haki]: {cookies}")
            top.destroy()

        if pedro_img is not None:
            pedro_btn = tk.Button(top, image=pedro_img, command=on_pedro_click)
            pedro_btn.image = pedro_img
            pedro_btn.pack(expand=True, fill="both")
        else:
            pedro_btn = tk.Button(top, text="Pedro (double)", command=on_pedro_click)
            pedro_btn.pack(expand=True, fill="both")
    
    cookie_label = tk.Label(
        root,
        text=f"[Haki]: {cookies}"
    )
    cookie_label.grid(column=1, row=1)

    try:
        img1 = tk.PhotoImage(file="luffy katakuri frame 1.png")
    except tk.TclError:
        img1 = None
    try:
        img2 = tk.PhotoImage(file="luffy katakuri frame 2.png")
    except tk.TclError:
        img2 = None

    if img1 is not None:
        click_btn = tk.Button(root, image=img1, command=click_cookie)
        click_btn.image = img1
    else:
        click_btn = tk.Button(root, text="Click me!", command=click_cookie)
    click_btn.grid(column=1, row=0)

    armament_cost = 2

    def buy_armament():
        nonlocal cookies, cookies_per_click, armament_cost
        if cookies >= armament_cost:
            cookies -= armament_cost
            cookies_per_click *= 2
            armament_cost *= 3
            per_click_label.config(text=f"Per click: {cookies_per_click}")
            armament_btn.config(text=f"Armament [Haki] (+1/click) Cost: {armament_cost}")
            cookie_label.config(text=f"[Haki]: {cookies}")

    per_click_label = tk.Label(root, text=f"Per click: {cookies_per_click}")
    per_click_label.grid(column=2, row=2)

    armament_btn = tk.Button(
        root,
        text=f"Armament Haki (+1/click) Cost: {armament_cost}",
        command=buy_armament
    )
    armament_btn.grid(column=2, row=1)

    observation_cost = 3

    def buy_observation():
        nonlocal cookies, cookies_per_second, observation_cost
        if cookies >= observation_cost:
            cookies -= observation_cost
            cookies_per_second *= 2
            observation_cost *= 3
            per_second_label.config(text=f"Per second: {cookies_per_second}")
            observation_btn.config(text=f"Observation Haki (+1/second) Cost: {observation_cost}")
            cookie_label.config(text=f"[Haki]: {cookies}")

    per_second_label = tk.Label(root, text=f"Per second: {cookies_per_second}")
    per_second_label.grid(column=0, row=2)

    observation_btn = tk.Button(
        root, 
        text=f"Observation Haki (+1/second) Cost: {observation_cost}",
        command=buy_observation
    )
    observation_btn.grid(column=0, row=1)
    start_auto_generation()

    root.mainloop()

if __name__ == "__main__":
    main()