import csv
from datetime import datetime
from pathlib import Path

# 数据目录和文件
DATA_DIR = Path("data2")
RECORD_FILE = DATA_DIR / "borrow_records.csv"


def user_type(role: str) -> str:
    role = (role or "").lower()
    if role.startswith("s"):
        return "student"
    elif role.startswith("e") or role.startswith("st"):
        return "staff"
    else:
        return "other"

def borrow_book(user_id: str, role: str, book_id: str, book_type: str):
    borrow_id = f"B{int(datetime.now().timestamp())}"
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

if __name__ == "__main__":
    borrow_book(
        user_id="U1001",
        role="student",
        book_id="BK001",
        book_type="Physical book"
    )
