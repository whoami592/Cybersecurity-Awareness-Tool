import tkinter as tk
from tkinter import messagebox
import re

class CyberSecTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Cybersecurity Awareness Tool")
        self.root.geometry("600x400")

        # GUI Elements
        tk.Label(root, text="Cybersecurity Awareness Tool", font=("Arial", 16)).pack(pady=10)
        
        tk.Label(root, text="Enter a Password to Check Strength:").pack()
        self.password_entry = tk.Entry(root, width=30, show="*")
        self.password_entry.pack(pady=5)
        
        tk.Button(root, text="Check Password Strength", command=self.check_password).pack(pady=10)
        
        tk.Label(root, text="Enter URL to Simulate Vulnerability Scan:").pack()
        self.url_entry = tk.Entry(root, width=30)
        self.url_entry.pack(pady=5)
        
        tk.Button(root, text="Scan for Vulnerabilities", command=self.simulate_scan).pack(pady=10)
        
        self.result_label = tk.Label(root, text="", wraplength=500)
        self.result_label.pack(pady=10)

    def check_password(self):
        password = self.password_entry.get()
        if len(password) < 8:
            messagebox.showwarning("Weak Password", "Password is too short! Use at least 8 characters.")
        elif not re.search(r"[A-Z]", password) or not re.search(r"[0-9]", password):
            messagebox.showwarning("Weak Password", "Password should include uppercase letters and numbers!")
        else:
            messagebox.showinfo("Strong Password", "Password is strong! Good job!")

    def simulate_scan(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL!")
            return
        # Simulate a vulnerability scan (educational purposes only)
        self.result_label.config(text=f"Scanning {url}...\n"
                                    "Checking for outdated software: [Simulated] Found outdated CMS.\n"
                                    "Checking for SQL injection: [Simulated] No issues found.\n"
                                    "Recommendation: Update software and use parameterized queries.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberSecTool(root)
    root.mainloop()