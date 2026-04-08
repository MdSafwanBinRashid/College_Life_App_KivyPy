# College Life App

A mobile-style desktop application built with **Kivy** and **Python** to help college students manage their daily academic life.

## Features

- **Dashboard** – View budget overview, to-do list, GPA summary, and current grades
- **Schedule** – Add and manage weekly class schedule with day-wise organization
- **Budgeting** – Track monthly budget, add/delete transactions, edit category estimates
- **Social Hub** – Discover campus and local events with calendar integration
- **Flashcards** – Study with built-in flashcards, create your own, and delete cards
- **Settings** – Customize theme, font size, font family, and account info

## Data Persistence

All user data is saved locally using **JSON files**:
- `user_settings.json` – Theme, font, and account preferences
- `budget_data.json` – Budget, transactions, and category estimates
- `dashboard_data.json` – To-do list tasks
- `flashcards.json` – User-created and default flashcards

## Requirements

- Python 3.10+
- Kivy 2.3+

## Installation

```bash
git clone https://github.com/MdSafwanBinRashid/College_Life_App_KivyPy.git
cd College_Life_App_KivyPy
pip install kivy
python main.py



College_Life_App_KivyPy/
├── main.py                 # Entry point
├── collegelife.kv          # Main UI layout
├── dashboard_controller.py # Dashboard logic
├── dashboard_view.kv       # Dashboard UI
├── schedule_controller.py  # Schedule logic
├── schedule_view.kv        # Schedule UI
├── budget_controller.py    # Budgeting logic
├── budget_view.kv          # Budgeting UI
├── socialhub_controller.py # Social Hub logic
├── socialhub_view.kv       # Social Hub UI
├── flashcard_controller.py # Flashcards logic
├── flashcard_view.kv       # Flashcards UI
├── settings_controller.py  # Settings logic
├── settings_view.kv        # Settings UI
├── settings_manager.py     # Settings persistence
├── images/                 # App images
└── *.json                  # User data files
