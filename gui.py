import tkinter as tk
from tkinter import filedialog
from index import reconcile

class CSVReconcilerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("CSV Reconciliation Tool")

        self.source_label = tk.Label(master, text="Source CSV:")
        self.source_label.grid(row=0, column=0)

        self.source_entry = tk.Entry(master, width=50)
        self.source_entry.grid(row=0, column=1)

        self.source_button = tk.Button(master, text="Browse", command=self.browse_source)
        self.source_button.grid(row=0, column=2)

        self.target_label = tk.Label(master, text="Target CSV:")
        self.target_label.grid(row=1, column=0)

        self.target_entry = tk.Entry(master, width=50)
        self.target_entry.grid(row=1, column=1)

        self.target_button = tk.Button(master, text="Browse", command=self.browse_target)
        self.target_button.grid(row=1, column=2)

        self.output_label = tk.Label(master, text="Output Report:")
        self.output_label.grid(row=2, column=0)

        self.output_entry = tk.Entry(master, width=50)
        self.output_entry.grid(row=2, column=1)

        self.output_button = tk.Button(master, text="Browse", command=self.browse_output)
        self.output_button.grid(row=2, column=2)

        self.run_button = tk.Button(master, text="Run Reconciliation", command=self.run_reconciliation)
        self.run_button.grid(row=3, columnspan=3, pady=10)

    def browse_source(self):
        """
        Open file dialog to select source CSV file.
        """
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(0, file_path)

    def browse_target(self):
        """
        Open file dialog to select target CSV file.
        """
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.target_entry.delete(0, tk.END)
        self.target_entry.insert(0, file_path)

    def browse_output(self):
        """
        Open file dialog to select output report file.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".csv")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, file_path)

    def run_reconciliation(self):
        """
        Run reconciliation process and display results in a pop-up window.
        """
        source_file = self.source_entry.get()
        target_file = self.target_entry.get()
        output_file = self.output_entry.get()

        # Run reconciliation
        missing_in_target, missing_in_source, discrepancies = reconcile(source_file, target_file, output_file)

        # Display results
        result_text = f"Reconciliation completed:\n- Records missing in target: {missing_in_target}\n- Records missing in source: {missing_in_source}\n- Records with field discrepancies: {discrepancies}\nReport saved to: {output_file}"
        result_window = tk.Toplevel(self.master)
        result_label = tk.Label(result_window, text=result_text)
        result_label.pack()

def main():
    root = tk.Tk()
    CSVReconcilerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
