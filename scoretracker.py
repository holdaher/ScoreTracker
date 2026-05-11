import tkinter as tk
from tkinter import ttk

iconic_matches = {

    "🦁 Premier League - Manchester City": {
        "score": "Manchester City 3 - 2 Queens Park Rangers",
        "event": "Final Match Day",
        "details": "Sergio Agüero's 94th-minute goal secured City's first title in 44 years."
    },

    "⭐ Champions League - Liverpool": {
        "score": "Liverpool 3 - 3 AC Milan",
        "event": "2005 UEFA Champions League Final",
        "details": "Liverpool won on penalties after being down 3-0 before halftime."
    },

    "👑 La Liga - Real Madrid": {
        "score": "Real Madrid 2 - 1 Barcelona",
        "event": "2012 El Clásico",
        "details": "A huge win that helped Real Madrid win La Liga."
    },

    "🏆 World Cup - Germany": {
        "score": "Germany 7 - 1 Brazil",
        "event": "2014 World Cup Semifinal",
        "details": "One of the most shocking World Cup results ever."
    }
}


def get_match_info(team_choice):
    match = iconic_matches[team_choice]
    
    return match["score"], match["event"], match["details"]


def show_match():
    team_choice = team_var.get()

    score, event, details = get_match_info(team_choice)

    result_label.config(
        text=f"{score}\n\n{event}\n\n{details}"
    )


main = tk.Tk()

main.title("ScoreTracker")
main.geometry("500x380")
main.configure(bg="black")


title_label = tk.Label(
    main,
    text="⚽ ScoreTracker",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg="black"
)

title_label.pack(pady=20)


subtitle_label = tk.Label(
    main,
    text="Pick a team to see an iconic match",
    font=("Segoe UI", 12),
    fg="light gray",
    bg="black"
)

subtitle_label.pack(pady=5)


team_var = tk.StringVar()

team_box = ttk.Combobox(
    main,
    textvariable=team_var,
    width=35,
    font=("Segoe UI", 11)
)

team_box["values"] = list(iconic_matches.keys())

team_box.set("🦁 Premier League - Manchester City")

team_box.pack(pady=15)


show_button = tk.Button(
    main,
    text="Show Match",
    font=("Segoe UI", 12, "bold"),
    bg="blue",
    fg="white",
    activebackground="dark blue",
    activeforeground="white",
    padx=12,
    pady=6,
    borderwidth=0,
    command=show_match
)

show_button.pack(pady=10)


result_label = tk.Label(
    main,
    text="Select a team and click the button.",
    font=("Segoe UI", 13),
    fg="white",
    bg="black",
    wraplength=420,
    justify="center"
)

result_label.pack(pady=25)


main.mainloop()