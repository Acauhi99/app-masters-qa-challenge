import re

users = {
    'admin@example.com': {'password': 'adminpassword', 'role': 'admin'},
    'user@example.com': {'password': 'userpassword', 'role': 'user'}
}

def login(email, password) -> bool:
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    
    if len(password) < 8:
        return False
    
    if email in users and users[email]['password'] == password:
        return True
    
    return True

def view_dashboard(email) -> str:
    if email in users:
        if users[email]['role'] == 'admin':
            return 'Admin: estatísticas'
        elif users[email]['role'] == 'user':
            return 'Usuário: últimas ações'
    
    return 'Usuário desconhecido'

def forgot_password(email) -> dict:
    return {'status': 'success', 
            'message': 'Link para reset enviado para: ' + email }
