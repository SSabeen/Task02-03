#TASK 03, MAIN PROGRAM FILE!

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import threading
import os


# RUN BANDIT FUNCTION
def run_bandit(file_path, output_box):
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "🔍 Scanning for vulnerabilities...\n\n")

    try:
        # Run bandit command
        result = subprocess.run(
            ["bandit", file_path],
            capture_output=True,
            text=True
        )

        output_box.insert(tk.END, result.stdout)

    except Exception as e:
        output_box.insert(tk.END, f"Error: {str(e)}")



# SAVE REPORT FUNCTION
def save_report(output_box):
    report = output_box.get(1.0, tk.END).strip()
    if not report:
        messagebox.showwarning("Empty", "No report to save.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(report)
        messagebox.showinfo("Saved", "Report saved successfully!")



# FILE SELECT FUNCTION
def select_file(output_box):
    file_path = filedialog.askopenfilename(
        title="Select Python File",
        filetypes=[("Python Files", "*.py")]
    )

    if file_path:
        selected_file_label.config(text=f"Selected: {os.path.basename(file_path)}")

        # Run in background thread (prevents GUI freezing)
        thread = threading.Thread(target=run_bandit, args=(file_path, output_box))
        thread.start()



# MAIN GUI WINDOW
window = tk.Tk()
window.title("Bug Bounty Vulnerability Scanner")
window.geometry("800x600")
window.config(bg="#1e1e1e")



# TITLE LABEL
title = tk.Label(window, text="🐞 Bug Bounty Vulnerability Scanner",
                 font=("Arial", 20, "bold"), fg="white", bg="#1e1e1e")
title.pack(pady=10)



# SELECTED FILE LABEL
selected_file_label = tk.Label(window, text="No file selected",
                               font=("Arial", 12), fg="white", bg="#1e1e1e")
selected_file_label.pack()



# BUTTONS
btn_frame = tk.Frame(window, bg="#1e1e1e")
btn_frame.pack(pady=10)

select_btn = tk.Button(btn_frame, text="📁 Select Python File",
                       font=("Arial", 14), width=20,
                       command=lambda: select_file(output_area))
select_btn.grid(row=0, column=0, padx=10)

save_btn = tk.Button(btn_frame, text="💾 Save Report",
                     font=("Arial", 14), width=20,
                     command=lambda: save_report(output_area))
save_btn.grid(row=0, column=1, padx=10)



# OUTPUT AREA
output_area = scrolledtext.ScrolledText(window, width=90, height=25,
                                        font=("Consolas", 11), bg="black", fg="white")
output_area.pack(pady=10)



# START GUI LOOP
window.mainloop()
