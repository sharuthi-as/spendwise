# SpendWise 💰

A sleek, dark-themed personal finance tracker built with Python and CustomTkinter.

---

## Features

- **Dark minimalist UI** with a clean top navigation bar
- **Income & Expense tracking** with category tagging
- **Live Dashboard** showing income, expenses, and net balance
- **Transaction History** with delete support
- **SQLite database** — no setup required
- Fully modular codebase

---

## Project Structure

```
spendwise/
├── main.py                  ← App entry point
├── requirements.txt
├── README.md
├── database/
│   └── expenses.db          ← Auto-created on first run
├── models/
│   ├── __init__.py
│   └── db_manager.py
└── ui/
    ├── __init__.py
    ├── theme.py
    ├── dashboard.py
    ├── add_transaction.py
    └── history.py
```

---

## ▶ Run in VS Code — Step by Step

### Step 1 — Install Python
- Download Python 3.10+ from https://python.org/downloads
- During install, check **"Add Python to PATH"**
- Verify: open Terminal in VS Code → `python --version`

### Step 2 — Open the Project in VS Code
1. Launch **VS Code**
2. Click **File → Open Folder**
3. Select the `spendwise/` folder
4. VS Code will show the file tree on the left

### Step 3 — Open the Terminal
- Press **Ctrl + `` ` ``** (backtick) or go to **Terminal → New Terminal**

### Step 4 — Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

Activate it:
- **Windows:**  `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

You'll see `(venv)` in your terminal prompt.

### Step 5 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 6 — Run the App
```bash
python main.py
```

The SpendWise window will open. The `database/expenses.db` file is created automatically.

---

## 🐙 Push to GitHub — Step by Step

### Step 1 — Install Git
- Download from https://git-scm.com/downloads
- Verify: `git --version`

### Step 2 — Configure Git (first time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Step 3 — Create a Repo on GitHub
1. Go to https://github.com → click **New** (green button)
2. Name it `spendwise`
3. Leave it **Public** or **Private**
4. Do **NOT** check "Initialize with README" (we already have one)
5. Click **Create repository**
6. Copy the repo URL (e.g. `https://github.com/yourusername/spendwise.git`)

### Step 4 — Create a .gitignore
In your project folder, create a file named `.gitignore`:
```
venv/
database/expenses.db
__pycache__/
*.pyc
.DS_Store
```

### Step 5 — Initialize and Push
Run these commands in your VS Code terminal (inside the `spendwise/` folder):

```bash
git init
git add .
git commit -m "Initial commit - SpendWise App"
git branch -M main
git remote add origin https://github.com/yourusername/spendwise.git
git push -u origin main
```

Replace `yourusername` with your actual GitHub username.

### Step 6 — Future Updates
After making changes, run:
```bash
git add .
git commit -m "Describe your changes here"
git push
```

---

## Planned Upgrades

- [ ] Budget alerts
- [ ] Charts & visual analytics (matplotlib)
- [ ] CSV / PDF export
- [ ] Monthly summaries
- [ ] AI spending insights
