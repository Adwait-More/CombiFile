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
        self.geometry("480x450")
        self.resizable(False, False)
        self.configure(fg_color=self.BG)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self._selected_files: list[str] = []

        self._build_ui()

    # ── UI construction ───────────────────────────────────────────────
    def _build_ui(self) -> None:
        pad = {"padx": 14, "pady": (8, 0)}

        # — button row (Select Files + Clear List) ———————————————————
        btn_row = ctk.CTkFrame(self, fg_color="transparent")
        btn_row.pack(fill="x", **pad)

        self.btn_select = ctk.CTkButton(
            btn_row,
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
        self.btn_select.pack(side="left", fill="x", expand=True, padx=(0, 4))

        self.btn_clear = ctk.CTkButton(
            btn_row,
            text="Clear List",
            fg_color=self.BTN_BG,
            hover_color=self.BTN_HOVER,
            border_color=self.BORDER,
            border_width=1,
            text_color=self.TEXT_DIM,
            font=ctk.CTkFont(size=13),
            height=32,
            corner_radius=4,
            command=self._on_clear_list,
        )
        self.btn_clear.pack(side="left", fill="x", expand=True, padx=(4, 0))

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
            command=self._on_merge,
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

    def _set_status(self, text: str, auto_reset: bool = False) -> None:
        """Update the status label. Optionally reset to 'Ready' after 3 s."""
        self.lbl_status.configure(text=text)
        if auto_reset:
            self.after(3000, lambda: self.lbl_status.configure(text="Ready"))

    def _on_clear_list(self) -> None:
        """Remove all queued files."""
        self._selected_files.clear()
        self._refresh_file_list()
        self._set_status("Ready")

    # ── merge logic ───────────────────────────────────────────────────
    def _on_merge(self) -> None:
        """Validate, ask for output folder, and merge all files."""
        # guard: no files selected
        if not self._selected_files:
            self._set_status("Error: no files selected")
            return

        # get output filename
        filename = self.entry_filename.get().strip()
        if not filename:
            filename = "combined_output.txt"

        # ask for output directory
        out_dir = filedialog.askdirectory(title="Choose output folder")
        if not out_dir:
            return

        out_path = os.path.join(out_dir, filename)

        self._set_status("Merging...")
        self.update_idletasks()  # force UI redraw

        try:
            with open(out_path, "w", encoding="utf-8") as out_f:
                for i, filepath in enumerate(self._selected_files):
                    name = os.path.basename(filepath)
                    header = f"\n\n--- [{name}] ---\n\n"
                    # skip leading blank lines for the very first file
                    if i == 0:
                        header = header.lstrip("\n")
                    out_f.write(header)
                    try:
                        with open(filepath, "r", encoding="utf-8") as in_f:
                            out_f.write(in_f.read())
                    except PermissionError:
                        out_f.write(f"[Error: could not read — file is locked]")
                    except UnicodeDecodeError:
                        out_f.write(f"[Error: file is not valid UTF-8 text]")
                    except OSError as exc:
                        out_f.write(f"[Error: {exc}]")
        except OSError as exc:
            self._set_status(f"Error: {exc}")
            return

        self._set_status(f"Success! \u2192 {filename}", auto_reset=True)


# ── entry point ───────────────────────────────────────────────────────
if __name__ == "__main__":
    app = CombiFileApp()
    app.mainloop()
