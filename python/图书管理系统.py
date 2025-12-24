import user
import book
import csv
import datetime
import typing
import sys







#Load borrowing records.
def load_loans(loans_file: str):
    loans = []
    with open (loans_file, "r") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            loans.append({'borrow_date': row['borrow_date'],
                          'user_id': row['user_id'],
                          'book_id': row['book_id'],
                          'due_date': row['due_date'],
                          'return_date': row['return_date']})
    return loans
    

#Main menu.
def main(user_file: str, book_file:str, loan_file:str) -> None:
    """
    This is the entry of your program. Please DO NOT modify this function signature, i.e. function name, parameters
    Parameteres:
    - user_file (str): path the `users.csv` which stores user information
    - book_file (str): path the `books.csv` which stores book information
    - loan_file (str): path the `loans.csv` which stores loan information
    """
    users = user.load_users(user_file)
    books_list = book.load_books(book_file) 
    books = {b['book_id']: b for b in books_list}
    loans = load_loans(loan_file)
    

    while True:
        print("Welcome to Library")
        attempts = 3
        login_bool = False

        while attempts > 0:
            user_id = input("Login as: ")
            if user_id == 'quit':
                print("Goodbye!")
                return 
            password = input("Password: ")
            if password == 'quit':
                print("Goodbye!")
                return

            if user_id not in users:
                attempts -= 1
                if attempts > 0:
                    print(f"Invalid credentials. {attempts} attempt(s) remaining.")
                
                continue
            if users[user_id]['password'] != password:
                attempts -= 1
                if attempts > 0:
                    print(f"Invalid credentials. {attempts} attempt(s) remaining.")
                
                continue
            if password == users[user_id]['password']:
                login_bool = True
                user_info = users[user_id]
                role = user_info['role'].capitalize() if user_info['role'].lower() != 'other' else 'Others'
                print(f"Logged in as {user_info['name']} ({role})")
                main_menu(user_info, users, books, loans)
                break

        if not login_bool:
            print("Sorry you're out of attempts. Please contact your librarian for assistance.")
            print("Welcome to Library")
            print("Login as: Goodbye!")
            break



#Show different menus depend on the role of the users.
def different_main_menu(name, role, department):
    role = (role or '').strip().lower()
    department = (department or '').strip().lower()
    options = {
            0: "Quit",
            1: "Log out",
            2: "View account policies",
            3: "View my loans"
        } 
    if role == 'staff' and 'library' in department:
        options[4] = "Library Report"
    
    return options
#Show menu interface.
def first_menu(options):
    print("==================================")
    print("My Library Account")
    for key in sorted(options.keys()):
        print(f"{key}. {options[key]}")
    print("==================================")



#Main menu.
def main_menu(user_info, users, books, loans):
    
    options = different_main_menu(user_info['name'], user_info['role'], user_info['department'])
    
    first_menu(options)
    while True:
        choice = input("Enter your choice: ")
        num = choice.isdigit()
        if num:
            choice_num = int(choice)
        else:
            choice_num = None
        if choice_num not in options:
            continue
        
        
        if choice_num == 0:
            print("Goodbye!")
            sys.exit(0)
        elif choice_num == 1:
            break
        elif choice_num == 2:
            view_policy(user_info, loans, books)
        elif choice_num == 3:
            view_no_policy(user_info, loans, books)
        elif choice_num == 4 and user_info['role'].lower() == 'staff' and 'library' in user_info['department'].lower():
            library_report(users, loans, books)
        print("==================================")
        print("My Library Account")
        for key in sorted(options.keys()):
            print(f"{key}. {options[key]}")
        print("==================================")
        
#View the users' borrowing policies.
def view_policy(user_info:dict, loans:list, books:dict):
    
    role = user_info['role'].lower()
    policy = user.table_borrowing_policies.get(role, user.table_borrowing_policies['other'])

    
    prefix = user_info['role'].capitalize() if role != 'other' else 'Others'
    user_name = user_info['name']
    
    
    user_loans = [loan for loan in loans if loan['user_id'] == user_info['user_id'] and not loan['return_date']] 
    physical = sum(1 for loan in user_loans if books[loan['book_id']]['type'].lower() == 'physical')
    online = sum(1 for loan in user_loans if books[loan['book_id']]['type'].lower() == 'online')

    print(f"{prefix} {user_name}. "
          f"Policies: maximum of {policy['Physical book']} days, {policy['Quota']} items. "
          f"Current loans: {len(user_loans)} ({physical} physical / {online} online).")
#View current borrowed books.
def view_no_policy(user_info:dict, loans:list, books:dict):
    active_loans = [
        loan for loan in loans
        if loan['user_id'] == user_info['user_id'] and not loan['return_date']]

    active_loans.sort(key = lambda x: datetime.datetime.strptime(x['due_date'], '%d/%m/%Y'))
    print(f"You are currently have {len(active_loans)} loan(s).")
    for i, loan in enumerate(active_loans, start=1):
        b = books.get(loan['book_id'])
        if b:
            print(f"{i}. {loan['book_id']} '{b['title']}' by {b['author']} ({b['year']}). Due date: {loan['due_date']}.")


#Library report.
def library_report(users:dict, loans:list, books:dict):
    print("Library report")
    students = len([u for u in users.values() if u['role'].lower() == 'student'])
    staff = len([u for u in users.values() if u['role'].lower() == 'staff'])
    others = len([u for u in users.values() if u['role'].lower() == 'other'])
    total_users = students + staff + others
    print(f"- {total_users} users, including {students} student(s), {staff} staff, and {others} others.")

    
    physical_books = [b for b in books.values() if b['type'].lower() == 'physical']
    
    online_books = [b for b in books.values() if b['type'].lower() == 'online']
    avali_physical = 0
    for b in physical_books:
        
        loaned = sum(1 for loan in loans if loan['book_id'] == b['book_id'] and not loan['return_date'])
        if b['copies'] - loaned > 0:
            avali_physical += 1
    total_physical = len(physical_books)
    total_online = len(online_books)
    
        
    print(f"- {total_physical + total_online} books, including {total_physical} physical book(s) ({avali_physical} currently available) and {total_online} online book(s).")

   

if __name__ == "__main__":
    main('data/users.csv', 'data/books.csv', 'data/loans.csv')