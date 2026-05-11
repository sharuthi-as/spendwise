import customtkinter as ctk
from ui.dashboard import DashboardFrame
from ui.add_transaction import AddTransactionFrame
from ui.history import HistoryFrame
from ui.theme import *

class SpendWiseApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SpendWise")
        self.geometry("1100x720")
        self.minsize(900, 600)
        self.configure(fg_color=BG_COLOR)

        self._active_page = None
        self._nav_buttons = {}

        self._build_navbar()
        self._build_content()

        # Show dashboard by default
        self.show_page("dashboard")

    # ──────────────────────────────────────────────
    # NAV BAR (fixed height, packed BEFORE content)
    # ──────────────────────────────────────────────
    def _build_navbar(self):
        self.navbar = ctk.CTkFrame(
            self, fg_color=NAV_COLOR, corner_radius=0,
            height=NAV_HEIGHT, border_width=0
        )
        # Pack at top — this reserves the space so content never overlaps
        self.navbar.pack(side="top", fill="x")
        self.navbar.pack_propagate(False)   # keep fixed height

        # ── Logo / Brand ──
        brand = ctk.CTkFrame(self.navbar, fg_color="transparent")
        brand.pack(side="left", padx=24)

        ctk.CTkLabel(
            brand, text="◈",
            font=ctk.CTkFont(size=20),
            text_color=ACCENT
        ).pack(side="left", padx=(0, 6))

        ctk.CTkLabel(
            brand,
            text="SpendWise",
            font=ctk.CTkFont(family="Helvetica", size=18, weight="bold"),
            text_color=TEXT
        ).pack(side="left")

        # ── Nav links ──
        nav_links = ctk.CTkFrame(self.navbar, fg_color="transparent")
        nav_links.pack(side="left", padx=30)

        pages = [
            ("dashboard",        "Dashboard"),
            ("add_transaction",  "Add Transaction"),
            ("history",          "History"),
        ]

        for page_key, label in pages:
            btn = ctk.CTkButton(
                nav_links, text=label,
                width=130, height=34,
                fg_color="transparent",
                hover_color="#1e1e2e",
                font=ctk.CTkFont(size=13),
                text_color=TEXT_MUTED,
                corner_radius=8,
                command=lambda k=page_key: self.show_page(k)
            )
            btn.pack(side="left", padx=4)
            self._nav_buttons[page_key] = btn

        # ── Right side badge ──
        badge = ctk.CTkLabel(
            self.navbar, text="v1.0",
            font=ctk.CTkFont(size=11),
            text_color=TEXT_MUTED
        )
        badge.pack(side="right", padx=24)

        # Thin accent line at the bottom of nav
        separator = ctk.CTkFrame(self.navbar, fg_color=BORDER, height=1)
        separator.pack(side="bottom", fill="x")

    # ──────────────────────────────────────────────
    # CONTENT AREA (fills remainder, no overlap)
    # ──────────────────────────────────────────────
    def _build_content(self):
        self.content = ctk.CTkFrame(self, fg_color=BG_COLOR, corner_radius=0)
        # Pack below the navbar — fill remaining space
        self.content.pack(side="top", fill="both", expand=True)

        # Build all pages inside content
        self.pages = {
            "dashboard":       DashboardFrame(self.content),
            "add_transaction": AddTransactionFrame(self.content, self._refresh_all),
            "history":         HistoryFrame(self.content),
        }

        # Place all frames in the same grid cell; only one visible at a time
        for page in self.pages.values():
            page.place(relx=0, rely=0, relwidth=1, relheight=1)

    # ──────────────────────────────────────────────
    # PAGE SWITCHING
    # ──────────────────────────────────────────────
    def show_page(self, page_key: str):
        if self._active_page == page_key:
            return

        self._active_page = page_key

        # Update button styles
        for key, btn in self._nav_buttons.items():
            if key == page_key:
                btn.configure(
                    fg_color=ACCENT,
                    text_color="#000000",
                    font=ctk.CTkFont(size=13, weight="bold")
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=TEXT_MUTED,
                    font=ctk.CTkFont(size=13)
                )

        # Raise the selected page on top
        self.pages[page_key].lift()

    # ──────────────────────────────────────────────
    # REFRESH
    # ──────────────────────────────────────────────
    def _refresh_all(self):
        self.pages["dashboard"].refresh()
        self.pages["history"].load_data()


if __name__ == "__main__":
    app = SpendWiseApp()
    app.mainloop()
