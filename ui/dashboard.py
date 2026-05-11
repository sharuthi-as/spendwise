import customtkinter as ctk
from models.db_manager import DatabaseManager
from ui.theme import *

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=BG_COLOR, corner_radius=0)
        self.db = DatabaseManager()
        self._build_ui()
        self.refresh()

    def _build_ui(self):
        # Page title
        title = ctk.CTkLabel(
            self, text="Overview",
            font=ctk.CTkFont(family="Helvetica", size=22, weight="bold"),
            text_color=TEXT
        )
        title.pack(anchor="w", padx=30, pady=(30, 5))

        sub = ctk.CTkLabel(
            self, text="Your financial snapshot",
            font=ctk.CTkFont(size=13),
            text_color=TEXT_MUTED
        )
        sub.pack(anchor="w", padx=30, pady=(0, 25))

        # Cards row
        cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        cards_frame.pack(fill="x", padx=30, pady=5)

        # Income card
        self.income_card = self._make_card(cards_frame, "Total Income", "₹0.00", ACCENT_GREEN, "↑")
        self.income_card.pack(side="left", expand=True, fill="both", padx=(0, 10))

        # Expense card
        self.expense_card = self._make_card(cards_frame, "Total Expenses", "₹0.00", ACCENT_RED, "↓")
        self.expense_card.pack(side="left", expand=True, fill="both", padx=(0, 10))

        # Balance card
        self.balance_card = self._make_card(cards_frame, "Net Balance", "₹0.00", ACCENT, "◈")
        self.balance_card.pack(side="left", expand=True, fill="both")

    def _make_card(self, parent, title, value, color, icon):
        card = ctk.CTkFrame(parent, fg_color=CARD_COLOR, corner_radius=16, border_width=1, border_color=BORDER)

        icon_label = ctk.CTkLabel(card, text=icon, font=ctk.CTkFont(size=22), text_color=color)
        icon_label.pack(anchor="w", padx=20, pady=(20, 2))

        title_label = ctk.CTkLabel(
            card, text=title,
            font=ctk.CTkFont(size=12),
            text_color=TEXT_MUTED
        )
        title_label.pack(anchor="w", padx=20, pady=(0, 4))

        val_label = ctk.CTkLabel(
            card, text=value,
            font=ctk.CTkFont(family="Helvetica", size=26, weight="bold"),
            text_color=color
        )
        val_label.pack(anchor="w", padx=20, pady=(0, 20))

        # Store reference to value label
        card._val_label = val_label
        return card

    def refresh(self):
        income, expense, balance = self.db.get_summary()
        self.income_card._val_label.configure(text=f"₹{income:,.2f}")
        self.expense_card._val_label.configure(text=f"₹{expense:,.2f}")
        bal_color = ACCENT_GREEN if balance >= 0 else ACCENT_RED
        self.balance_card._val_label.configure(text=f"₹{balance:,.2f}", text_color=bal_color)
