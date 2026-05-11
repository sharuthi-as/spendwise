import customtkinter as ctk
from models.db_manager import DatabaseManager
from ui.theme import *

class HistoryFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=BG_COLOR, corner_radius=0)
        self.db = DatabaseManager()
        self._build_ui()
        self.load_data()

    def _build_ui(self):
        # Page title
        title = ctk.CTkLabel(
            self, text="Transaction History",
            font=ctk.CTkFont(family="Helvetica", size=22, weight="bold"),
            text_color=TEXT
        )
        title.pack(anchor="w", padx=30, pady=(30, 5))

        sub = ctk.CTkLabel(
            self, text="All your recorded transactions",
            font=ctk.CTkFont(size=13),
            text_color=TEXT_MUTED
        )
        sub.pack(anchor="w", padx=30, pady=(0, 20))

        # Header row
        header = ctk.CTkFrame(self, fg_color=CARD_COLOR, corner_radius=10)
        header.pack(fill="x", padx=30, pady=(0, 5))

        cols = [("Date", 120), ("Type", 100), ("Category", 150), ("Amount", 120), ("Notes", 200), ("ID", 60)]
        for col, w in cols:
            ctk.CTkLabel(
                header, text=col, width=w,
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color=TEXT_MUTED
            ).pack(side="left", padx=10, pady=10)

        # Scrollable list area
        self.scroll = ctk.CTkScrollableFrame(
            self, fg_color="transparent", corner_radius=0
        )
        self.scroll.pack(fill="both", expand=True, padx=30, pady=(0, 20))

    def load_data(self):
        # Clear existing rows
        for widget in self.scroll.winfo_children():
            widget.destroy()

        rows = self.db.fetch_transactions()
        if not rows:
            ctk.CTkLabel(
                self.scroll, text="No transactions yet. Add one to get started!",
                font=ctk.CTkFont(size=14), text_color=TEXT_MUTED
            ).pack(pady=40)
            return

        for row in rows:
            row_id, date, amount, category, t_type, notes = row
            color = ACCENT_GREEN if t_type == "Income" else ACCENT_RED
            sign = "+" if t_type == "Income" else "-"

            frame = ctk.CTkFrame(
                self.scroll, fg_color=CARD_COLOR, corner_radius=10,
                border_width=1, border_color=BORDER
            )
            frame.pack(fill="x", pady=3)

            data = [
                (date, 120, TEXT),
                (t_type, 100, color),
                (category, 150, TEXT),
                (f"{sign}₹{amount:,.2f}", 120, color),
                (notes or "—", 200, TEXT_MUTED),
                (str(row_id), 60, TEXT_MUTED),
            ]

            for val, w, c in data:
                ctk.CTkLabel(
                    frame, text=val, width=w,
                    font=ctk.CTkFont(size=12), text_color=c,
                    anchor="w"
                ).pack(side="left", padx=10, pady=10)

            # Delete button
            del_btn = ctk.CTkButton(
                frame, text="✕", width=32, height=28,
                fg_color="#2a1a1a", hover_color=ACCENT_RED,
                text_color=ACCENT_RED, font=ctk.CTkFont(size=12),
                corner_radius=6,
                command=lambda rid=row_id: self._delete(rid)
            )
            del_btn.pack(side="right", padx=10)

    def _delete(self, row_id):
        self.db.delete_transaction(row_id)
        self.load_data()
