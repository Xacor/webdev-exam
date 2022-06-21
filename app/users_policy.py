from flask_login import current_user

class UsersPolicy:
    def __init__(self, record=None):
        self.record = record
        
    #Book Section
    def create_book(self):
        return current_user.is_admin

    def update_book(self):
        return current_user.is_admin or current_user.is_moder

    def delete_book(self):
        return current_user.is_admin

    #Review Section  
    def create_review(self):
        return True

    def update_review(self):
        return current_user.is_admin or current_user.is_moder