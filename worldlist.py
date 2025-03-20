import itertools
import string
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import threading
from queue import Queue

class WordlistGenerator:
    def __init__(self):
        self._stop_event = threading.Event()
        self.progress_queue = Queue()

    def generate(self, chars, min_len, max_len, output_file):
        total = sum(len(chars) ** i for i in range(min_len, max_len + 1))
        processed = 0
        with open(output_file, 'w') as f:
            for length in range(min_len, max_len + 1):
                for word in itertools.product(chars, repeat=length):
                    if self._stop_event.is_set(): return
                    f.write(''.join(word) + '\n')
                    processed += 1
                    if processed % 10000 == 0:
                        self.progress_queue.put((processed / total) * 100)
        self.progress_queue.put("done")

    def stop(self):
        self._stop_event.set()

class WordlistGeneratorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerador de Wordlists")
        self.generator = WordlistGenerator()
        self._setup_ui()

    def _setup_ui(self):
        ttk.Label(self.root, text="Caracteres:").pack()
        self.chars_entry = ttk.Entry(self.root)
        self.chars_entry.insert(0, string.ascii_letters + string.digits)
        self.chars_entry.pack()
        
        ttk.Label(self.root, text="Tamanho Mínimo:").pack()
        self.min_len_entry = ttk.Entry(self.root, width=5)
        self.min_len_entry.insert(0, "1")
        self.min_len_entry.pack()
        
        ttk.Label(self.root, text="Tamanho Máximo:").pack()
        self.max_len_entry = ttk.Entry(self.root, width=5)
        self.max_len_entry.insert(0, "4")
        self.max_len_entry.pack()
        
        self.progress = ttk.Progressbar(self.root, maximum=100)
        self.progress.pack(fill=tk.X, pady=5)
        
        self.start_btn = ttk.Button(self.root, text="Gerar", command=self.start_generation)
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = ttk.Button(self.root, text="Parar", command=self.generator.stop, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT)
        
    def start_generation(self):
        chars = self.chars_entry.get().strip()
        try:
            min_len = int(self.min_len_entry.get())
            max_len = int(self.max_len_entry.get())
            if min_len > max_len or min_len < 1:
                raise ValueError("Valores inválidos")
        except ValueError:
            messagebox.showerror("Erro", "Insira valores válidos.")
            return
        
        output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])
        if not output_file: return
        
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.progress.config(value=0)
        
        threading.Thread(target=self.generator.generate, args=(chars, min_len, max_len, output_file), daemon=True).start()
        self.root.after(100, self.check_progress)

    def check_progress(self):
        try:
            progress = self.generator.progress_queue.get_nowait()
            if progress == "done":
                self.progress.config(value=100)
                messagebox.showinfo("Concluído", "Wordlist gerada com sucesso!")
                self.start_btn.config(state=tk.NORMAL)
                self.stop_btn.config(state=tk.DISABLED)
            else:
                self.progress.config(value=progress)
                self.root.after(100, self.check_progress)
        except:
            self.root.after(100, self.check_progress)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    WordlistGeneratorGUI().run()
