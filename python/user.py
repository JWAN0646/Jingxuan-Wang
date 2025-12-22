from abc import ABC, abstractmethod
import csv
import datetime
import re
table_borrowing_policies = {
    'student': {'Physical book': 10, 'Online': 'Unlimited', 'Quota':4},
    'staff': {'Physical book': 14, 'Online': 'Unlimited', 'Quota':6},
    'other': {'Physical book': 7, 'Online': 'Unlimited', 'Quota':2},
}

def user_type(self):
    if self.role.lower().startswith('s'):
        return 'student'
    elif self.role.lower().startswith('e'):
        return 'staff'
    else:
        return 'other'


class User(ABC):
    def __init__(self, user_id, password, name, role, department):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.role = role
        self.department = department
        self.table_borrowing_policies = table_borrowing_policies

    def __str__(self):
        return (f'user_id: {self.user_id},password: {self.password},name: {self.name}, role: {self.role}, department: {self.department}')

def load_users(users_file: str) -> dict:
    users = {}
    with open (users_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = row['user_id']
            users[user_id] = {
               
                'password': row['password'],
                'name': row['name'],
                'role': row['role'],
                'department': row['department'],
                'user_id':user_id
            }
            
    return users
        
    
    