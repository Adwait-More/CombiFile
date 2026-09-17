"""
CombiFile — Merge multiple text files into one.
"""

import os
from tkinter import filedialog

import customtkinter as ctk


class CombiFileApp(ctk.CTk):
    """Main application window."""

    # ── colour constants ──────────────────────────────────────────────
    BG        = "#111111"
    SURFACE   = "#1a1a1a"
    BORDER    = "#2a2a2a"
    TEXT      = "#e0e0e0"
    TEXT_DIM  = "#777777"
    BTN_BG    = "#222222"
    BTN_HOVER = "#2e2e2e"

    def __init__(self) -> None:
        super().__init__()

        # ── window ────────────────────────────────────────────────────
        self.title("CombiFile")
        self.geometry("480x420")
        self.resizable(False, False)
        self.configure(fg_color=self.BG)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self._selected_files: list[str] = []

        self._build_ui()

    # ── UI construction ───────────────────────────────────────────────
    def _build_ui(self) -> None:
        pad = {"padx": 14, "pady": (8, 0)}

        # — select files button ----------------------------------------
        self.btn_select = ctk.CTkButton(
            self,
            text="Select Files",
            fg_color=self.BTN_BG,
            hover_color=self.BTN_HOVER,
            border_color=self.BORDER,
            border_width=1,
            text_color=self.TEXT,
            font=ctk.CTkFont(size=13),
            height=32,
            corner_radius=4,
            command=self._on_select_files,
        )
        self.btn_select.pack(fill="x", **pad)

        # — file list ---------------------------------------------------
        self.file_list = ctk.CTkTextbox(
            self,
            fg_color=self.SURFACE,
            text_color=self.TEXT_DIM,
            border_color=self.BORDER,
            border_width=1,
            font=ctk.CTkFont(family="Consolas", size=12),
            height=200,
            corner_radius=4,
            state="disabled",
        )
        self.file_list.pack(fill="x", padx=14, pady=(8, 0))

        # — output filename label + entry --------------------------------
        ctk.CTkLabel(
            self,
            text="Output filename",
            text_color=self.TEXT_DIM,
            font=ctk.CTkFont(size=11),
            anchor="w",
        ).pack(fill="x", padx=16, pady=(10, 0))

        self.entry_filename = ctk.CTkEntry(
            self,
            placeholder_text="combined_output.txt",
            fg_color=self.SURFACE,
            text_color=self.TEXT,
            border_color=self.BORDER,
            border_width=1,
            font=ctk.CTkFont(size=13),
            height=32,
            corner_radius=4,
        )
        self.entry_filename.insert(0, "combined_output.txt")
        self.entry_filename.pack(fill="x", padx=14, pady=(2, 0))

        # — merge button ------------------------------------------------
        self.btn_merge = ctk.CTkButton(
            self,
            text="Merge",
            fg_color=self.BTN_BG,
            hover_color=self.BTN_HOVER,
            border_color=self.BORDER,
            border_width=1,
            text_color=self.TEXT,
            font=ctk.CTkFont(size=13),
            height=32,
            corner_radius=4,
        )
        self.btn_merge.pack(fill="x", padx=14, pady=(10, 0))

        # — status label ------------------------------------------------
        self.lbl_status = ctk.CTkLabel(
            self,
            text="Ready",
            text_color=self.TEXT_DIM,
            font=ctk.CTkFont(size=11),
            anchor="w",
        )
        self.lbl_status.pack(fill="x", padx=16, pady=(6, 10))

    # ── file selection ────────────────────────────────────────────────
    def _on_select_files(self) -> None:
        """Open a multi-file dialog and store the paths."""
        paths = filedialog.askopenfilenames(
            title="Select text files",
            filetypes=[("Text files", "*.txt *.md *.log *.csv *.json *.xml *.html *.py *.js *.ts *.css"), ("All files", "*.*")],
        )
        if not paths:
            return

        self._selected_files = list(paths)
        self._refresh_file_list()
        self._set_status(f"{len(self._selected_files)} file(s) selected")

    def _refresh_file_list(self) -> None:
        """Re-render the file list textbox."""
        self.file_list.configure(state="normal")
        self.file_list.delete("1.0", "end")
        for path in self._selected_files:
            self.file_list.insert("end", os.path.basename(path) + "\n")
        self.file_list.configure(state="disabled")

    def _set_status(self, text: str) -> None:
        """Update the status label."""
        self.lbl_status.configure(text=text)


# ── entry point ───────────────────────────────────────────────────────
if __name__ == "__main__":
    app = CombiFileApp()
    app.mainloop()
