import csv
from datetime import datetime
from pathlib import Path

import pandas as pd
from flask import Flask, render_template

# =========================
# Flask app（关键在这里）
# =========================
app = Flask(__name__)

# =========================
# 数据路径
# =========================
DATA_DIR = Path("data2")
RECORD_FILE = DATA_DIR / "borrow_records.csv"

# =========================
# 原有业务逻辑（保留）
# =========================
def user_type(role: str) -> str:
    role = (role or "").lower()
    if role.startswith("s"):
        return "student"
    elif role.startswith("e") or role.startswith("st"):
        return "staff"
    else:
        return "other"

def borrow_book(user_id: str, role: str, book_id: str, book_type: str):
    borrow_id = f"B{int(datetime.now().timestamp() * 1000)}"  # 用毫秒，避免重复
    utype = user_type(role)
    borrow_date = datetime.now().strftime("%Y-%m-%d")

    with open(RECORD_FILE, "a", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow([
            borrow_id,
            user_id,
            utype,
            book_id,
            book_type,
            borrow_date,
            "",
            ""
        ])

    print("✅ Borrow recorded:", borrow_id)

# =========================
# Analytics 页面（核心）
# =========================
@app.route("/analytics")
def analytics():
    df = pd.read_csv(RECORD_FILE)

    borrow_by_user_type = df.groupby("user_type").size().to_dict()
    top_books = df["book_id"].value_counts().to_dict()
    book_type_dist = df["book_type"].value_counts().to_dict()

    return render_template(
        "analytics.html",
        borrow_by_user_type=borrow_by_user_type,
        top_books=top_books,
        book_type_dist=book_type_dist
    )

# =========================
# 程序入口（只做一件事）
# =========================
if __name__ == "__main__":
    app.run(debug=True)
