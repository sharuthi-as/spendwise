import customtkinter as ctk
from models.db_manager import DatabaseManager
from ui.theme import *

class AddTransactionFrame(ctk.CTkFrame):
    def __init__(self, parent, refresh_callback):
        super().__init__(parent, fg_color=BG_COLOR, corner_radius=0)
        self.db = DatabaseManager()
        self.refresh_callback = refresh_callback
        self._build_ui()

    def _build_ui(self):
        # Page title
        title = ctk.CTkLabel(
            self, text="Add Transaction",
            font=ctk.CTkFont(family="Helvetica", size=22, weight="bold"),
            text_color=TEXT
        )
        title.pack(anchor="w", padx=30, pady=(30, 5))

        sub = ctk.CTkLabel(
            self, text="Record a new income or expense",
            font=ctk.CTkFont(size=13),
            text_color=TEXT_MUTED
        )
        sub.pack(anchor="w", padx=30, pady=(0, 25))

        # Form card
        form = ctk.CTkFrame(self, fg_color=CARD_COLOR, corner_radius=16, border_width=1, border_color=BORDER)
        form.pack(fill="x", padx=30, pady=5)

        # Type toggle
        type_row = ctk.CTkFrame(form, fg_color="transparent")
        type_row.pack(fill="x", padx=25, pady=(25, 10))

        ctk.CTkLabel(type_row, text="Type", font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=TEXT_MUTED).pack(anchor="w", pady=(0, 8))

        self.type_var = ctk.StringVar(value="Expense")
        btn_frame = ctk.CTkFrame(type_row, fg_color=BG_COLOR, corner_radius=10)
        btn_frame.pack(anchor="w")

        self.income_btn = ctk.CTkButton(
            btn_frame, text="Income", width=130, height=36,
            fg_color=ACCENT_GREEN, hover_color="#00cc6e",
            font=ctk.CTkFont(size=13, weight="bold"), text_color="#000000",
            command=lambda: self._set_type("Income")
        )
        self.income_btn.pack(side="left", padx=4, pady=4)

        self.expense_btn = ctk.CTkButton(
            btn_frame, text="Expense", width=130, height=36,
            fg_color=ACCENT_RED, hover_color="#cc3355",
            font=ctk.CTkFont(size=13, weight="bold"), text_color="#ffffff",
            command=lambda: self._set_type("Expense")
        )
        self.expense_btn.pack(side="left", padx=(0, 4), pady=4)

        self._set_type("Expense")

        # Fields in a 2-column grid
        fields_frame = ctk.CTkFrame(form, fg_color="transparent")
        fields_frame.pack(fill="x", padx=25, pady=10)

        # Amount
        left = ctk.CTkFrame(fields_frame, fg_color="transparent")
        left.pack(side="left", expand=True, fill="both", padx=(0, 10))

        ctk.CTkLabel(left, text="Amount (₹)", font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=TEXT_MUTED).pack(anchor="w", pady=(0, 6))
        self.amount = ctk.CTkEntry(
            left, placeholder_text="0.00", height=42,
            fg_color=BG_COLOR, border_color=BORDER,
            font=ctk.CTkFont(size=14), text_color=TEXT
        )
        self.amount.pack(fill="x")

        # Category
        right = ctk.CTkFrame(fields_frame, fg_color="transparent")
        right.pack(side="left", expand=True, fill="both")

        ctk.CTkLabel(right, text="Category", font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=TEXT_MUTED).pack(anchor="w", pady=(0, 6))
        self.category = ctk.CTkOptionMenu(
            right,
            values=["Food & Dining", "Transport", "Shopping", "Bills", "Health",
                    "Entertainment", "Education", "Salary", "Freelance", "Investment", "Other"],
            height=42, fg_color=BG_COLOR, button_color=ACCENT,
            font=ctk.CTkFont(size=13), text_color=TEXT
        )
        self.category.pack(fill="x")

        # Notes
        notes_row = ctk.CTkFrame(form, fg_color="transparent")
        notes_row.pack(fill="x", padx=25, pady=(10, 0))

        ctk.CTkLabel(notes_row, text="Notes (optional)", font=ctk.CTkFont(size=13, weight="bold"),
                     text_color=TEXT_MUTED).pack(anchor="w", pady=(0, 6))
        self.notes = ctk.CTkEntry(
            notes_row, placeholder_text="Add a description…", height=42,
            fg_color=BG_COLOR, border_color=BORDER,
            font=ctk.CTkFont(size=13), text_color=TEXT
        )
        self.notes.pack(fill="x")

        # Status label
        self.status_label = ctk.CTkLabel(form, text="", font=ctk.CTkFont(size=12), text_color=ACCENT_GREEN)
        self.status_label.pack(pady=(10, 0))

        # Submit button
        ctk.CTkButton(
            form, text="+ Add Transaction", height=44,
            fg_color=ACCENT, hover_color="#00aadd",
            font=ctk.CTkFont(size=14, weight="bold"), text_color="#000000",
            corner_radius=10, command=self.save
        ).pack(padx=25, pady=(10, 25), fill="x")

    def _set_type(self, t_type):
        self.type_var.set(t_type)
        dim = "#1e2e1e" if t_type == "Income" else "#1a1a1a"
        self.income_btn.configure(fg_color=ACCENT_GREEN if t_type == "Income" else "#1e1e1e")
        self.expense_btn.configure(fg_color=ACCENT_RED if t_type == "Expense" else "#1e1e1e")

    def save(self):
        try:
            amt = float(self.amount.get())
            if amt <= 0:
                raise ValueError
        except ValueError:
            self.status_label.configure(text="⚠  Enter a valid amount", text_color=ACCENT_RED)
            return

        self.db.add_transaction(
            amt,
            self.category.get(),
            self.type_var.get(),
            self.notes.get()
        )
        self.amount.delete(0, "end")
        self.notes.delete(0, "end")
        self.status_label.configure(text="✔  Transaction added successfully", text_color=ACCENT_GREEN)
        self.after(2500, lambda: self.status_label.configure(text=""))
        self.refresh_callback()
