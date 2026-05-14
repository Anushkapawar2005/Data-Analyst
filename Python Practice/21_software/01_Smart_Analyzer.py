# ==========================================================
# CORPORATE DATA ANALYZER SOFTWARE
# GUI Data Analytics Tool (CSV / Excel)
# Author: Python Data Analyst Version
# ==========================================================

import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ==========================
# MAIN APPLICATION CLASS
# ==========================
class DataAnalyzerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Corporate Data Analyzer")
        self.root.geometry("1100x750")

        # Data containers
        self.file_path = None
        self.df = None
        self.report_df = None
        self.chart_figure = None

        self.create_gui()

    # ==========================
    # GUI DESIGN
    # ==========================
    def create_gui(self):

        top_frame = ttk.LabelFrame(self.root, text="File Selection")
        top_frame.pack(fill="x", padx=10, pady=5)

        ttk.Button(top_frame, text="Browse File",
                   command=self.browse_file).pack(side="left", padx=5, pady=5)

        ttk.Button(top_frame, text="Read File",
                   command=self.read_file).pack(side="left", padx=5)

        self.file_label = ttk.Label(top_frame, text="No file selected")
        self.file_label.pack(side="left", padx=10)

        # Dataset Info
        info_frame = ttk.LabelFrame(self.root, text="Dataset Information")
        info_frame.pack(fill="x", padx=10, pady=5)

        self.info_text = tk.Text(info_frame, height=4)
        self.info_text.pack(fill="x")

        # ======================
        # REPORT BUILDER
        # ======================
        report_frame = ttk.LabelFrame(self.root, text="Report Builder")
        report_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(report_frame, text="Group By").grid(row=0, column=0)
        ttk.Label(report_frame, text="Aggregation").grid(row=0, column=1)
        ttk.Label(report_frame, text="Value Column").grid(row=0, column=2)

        self.group_col = ttk.Combobox(report_frame, state="readonly")
        self.group_col.grid(row=1, column=0, padx=5)

        self.agg_method = ttk.Combobox(
            report_frame,
            values=["sum", "mean", "max", "min", "count", "median"],
            state="readonly"
        )
        self.agg_method.grid(row=1, column=1, padx=5)

        self.value_col = ttk.Combobox(report_frame, state="readonly")
        self.value_col.grid(row=1, column=2, padx=5)

        ttk.Button(report_frame, text="Preview Report",
                   command=self.generate_report).grid(row=1, column=3, padx=10)

        ttk.Button(report_frame, text="Export Report",
                   command=self.export_report).grid(row=1, column=4)

        # Report Table
        table_frame = ttk.LabelFrame(self.root, text="Report Output")
        table_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(table_frame)
        self.tree.pack(fill="both", expand=True)

        # ======================
        # CHART BUILDER
        # ======================
        chart_frame = ttk.LabelFrame(self.root, text="Chart Builder")
        chart_frame.pack(fill="x", padx=10, pady=5)

        self.chart_type = ttk.Combobox(
            chart_frame,
            values=["Bar Chart", "Column Chart",
                    "Line Chart", "Pie Chart"],
            state="readonly"
        )
        self.chart_type.pack(side="left", padx=10)

        ttk.Button(chart_frame, text="Preview Chart",
                   command=self.preview_chart).pack(side="left")

        ttk.Button(chart_frame, text="Export Chart",
                   command=self.export_chart).pack(side="left", padx=10)

        self.chart_canvas_frame = ttk.Frame(self.root)
        self.chart_canvas_frame.pack(fill="both", expand=True)

    # ==========================
    # FILE SELECTION
    # ==========================
    def browse_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("Data Files", "*.csv *.xlsx *.xls")]
        )

        if self.file_path:
            self.file_label.config(text=self.file_path)

    # ==========================
    # READ DATASET
    # ==========================
    def read_file(self):

        if not self.file_path:
            messagebox.showerror("Error", "Please select a file.")
            return

        try:
            if self.file_path.endswith(".csv"):
                self.df = pd.read_csv(self.file_path)
            else:
                self.df = pd.read_excel(self.file_path)

            self.show_dataset_info()
            self.detect_columns()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ==========================
    # SHOW DATASET INFO
    # ==========================
    def show_dataset_info(self):

        self.info_text.delete("1.0", tk.END)

        rows, cols = self.df.shape
        columns = ", ".join(self.df.columns)

        info = f"""
Total Rows : {rows}
Total Columns : {cols}
Columns :
{columns}
"""

        self.info_text.insert(tk.END, info)

    # ==========================
    # COLUMN DETECTION
    # ==========================
    def detect_columns(self):

        text_cols = self.df.select_dtypes(include="object").columns.tolist()
        numeric_cols = self.df.select_dtypes(
            include=["int64", "float64"]).columns.tolist()

        self.group_col["values"] = text_cols
        self.value_col["values"] = numeric_cols

    # ==========================
    # GENERATE REPORT
    # ==========================
    def generate_report(self):

        if self.df is None:
            messagebox.showerror("Error", "Read file first.")
            return

        if not all([self.group_col.get(),
                    self.agg_method.get(),
                    self.value_col.get()]):
            messagebox.showerror(
                "Error", "Please select all dropdown options.")
            return

        try:
            self.report_df = (
                self.df
                .groupby(self.group_col.get())[self.value_col.get()]
                .agg(self.agg_method.get())
                .sort_values(ascending=False)
                .reset_index()
            )

            self.display_table()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ==========================
    # DISPLAY REPORT TABLE
    # ==========================
    def display_table(self):

        self.tree.delete(*self.tree.get_children())

        self.tree["columns"] = list(self.report_df.columns)
        self.tree["show"] = "headings"

        for col in self.report_df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        for _, row in self.report_df.iterrows():
            self.tree.insert("", "end", values=list(row))

    # ==========================
    # EXPORT REPORT
    # ==========================
    def export_report(self):

        if self.report_df is None:
            messagebox.showerror("Error", "Generate report first.")
            return

        folder = os.path.dirname(self.file_path)

        save_path = filedialog.asksaveasfilename(
            initialdir=folder,
            defaultextension=".xlsx",
            filetypes=[("Excel", "*.xlsx"), ("CSV", "*.csv")]
        )

        if not save_path:
            return

        if save_path.endswith(".csv"):
            self.report_df.to_csv(save_path, index=False)
        else:
            self.report_df.to_excel(save_path, index=False)

        messagebox.showinfo("Success", "Report exported successfully.")

    # ==========================
    # CHART PREVIEW
    # ==========================
    def preview_chart(self):

        if self.report_df is None:
            messagebox.showerror("Error", "Generate report first.")
            return

        if not self.chart_type.get():
            messagebox.showerror("Error", "Select chart type.")
            return

        for widget in self.chart_canvas_frame.winfo_children():
            widget.destroy()

        x = self.report_df.iloc[:, 0]
        y = self.report_df.iloc[:, 1]

        fig, ax = plt.subplots()

        chart = self.chart_type.get()

        if chart == "Bar Chart":
            ax.bar(x, y)

        elif chart == "Column Chart":
            ax.barh(x, y)

        elif chart == "Line Chart":
            ax.plot(x, y)

        elif chart == "Pie Chart":
            ax.pie(y, labels=x, autopct="%1.1f%%")

        ax.set_title("Report Visualization")
        plt.xticks(rotation=45)

        self.chart_figure = fig

        canvas = FigureCanvasTkAgg(fig, master=self.chart_canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    # ==========================
    # EXPORT CHART
    # ==========================
    def export_chart(self):

        if self.chart_figure is None:
            messagebox.showerror("Error", "Preview chart first.")
            return

        folder = os.path.dirname(self.file_path)
        save_path = os.path.join(folder, "report_chart.png")

        self.chart_figure.savefig(save_path)
        messagebox.showinfo("Success", f"Chart saved:\n{save_path}")


# ==========================
# RUN APPLICATION
# ==========================
if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalyzerApp(root)
    root.mainloop()