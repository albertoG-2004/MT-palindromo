import tkinter as tk
from tkinter import messagebox
from turingMachine import TuringMachine

class PalindromeCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Turing - Verificador de Palíndromos")
        self.root.geometry("400x250")
        self.root.configure(bg="#2c3e50")
        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Máquina de Turing - Palíndromo", 
                               font=("Helvetica", 16, "bold"), fg="#ecf0f1", bg="#2c3e50")
        title_label.pack(pady=20)

        prompt_label = tk.Label(self.root, text="Ingrese una palabra:", 
                                font=("Helvetica", 12), fg="#ecf0f1", bg="#2c3e50")
        prompt_label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Helvetica", 12), width=30, justify="center", fg="#2c3e50", bg="#ecf0f1")
        self.entry.pack(pady=5)

        check_button = tk.Button(self.root, text="Verificar", command=self.check_palindrome, 
                                 font=("Helvetica", 12, "bold"), fg="#ecf0f1", bg="#3498db", 
                                 activebackground="#2980b9", width=15)
        check_button.pack(pady=20)

    def check_palindrome(self):
        word = self.entry.get().strip()
        turing_machine = TuringMachine(word)
        if turing_machine.is_palindrome():
            messagebox.showinfo("Resultado", f"La palabra '{word}' es un palíndromo.")
        else:
            messagebox.showinfo("Resultado", f"La palabra '{word}' no es un palíndromo.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PalindromeCheckerApp(root)
    root.mainloop()