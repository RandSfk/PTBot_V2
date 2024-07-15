import json
import datetime

def load_user_credentials(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"account": []}

def save_user_credentials(credentials, filename):
    with open(filename, 'w') as f:
        json.dump(credentials, f, indent=4)

active_sessions = {}
user_credentials = load_user_credentials('users.json')

def get_user_role(username):
    for account in user_credentials['account']:
        if account['username'] == username:
            return account['role']
    return 'guest'

def get_user_password(username):
    for account in user_credentials['account']:
        if account['username'] == username:
            return account['password']
    return None

def login(username, password):
    user_password = get_user_password(username)
    if user_password and user_password == password:
        active_sessions[username] = True
        return True
    else:
        return False

def logout(username):
    if username in active_sessions:
        del active_sessions[username]
        return True
    else:
        return False

def is_logged_in(username):
    return username in active_sessions

def register(username, password):
    if get_user_password(username):
        return False 
    else:
        user_credentials['account'].append({
            'role': 'user',
            'username': username,
            'password': password
        })
        save_user_credentials(user_credentials, 'users.json')
        return True

def format_output(output):
    max_length = 70
    lines = []
    while len(output) > max_length:
        if '\n' in output[:max_length]:
            split_index = output[:max_length].rindex('\n') + 1
            lines.append(output[:split_index])
            output = output[split_index:].lstrip()
        else:
            lines.append(output[:max_length])
            output = output[max_length:].lstrip()
    lines.append(output)
    return '\n'.join(lines)

def cek_waktu():
    current_time = datetime.datetime.now().time()
    if current_time.hour >= 18:
        return "🌅 Selamat sore"
    elif current_time.hour >= 12:
        return "🏜 Selamat siang"
    elif current_time.hour >= 6:
        return "🌄 Selamat pagi"
    else:
        return "🌕 Selamat malam"

def list_menu(username, roles):
    role = get_user_role(username)
    available_commands = []
    command_number = 0
    if role in roles:
        for command in roles[role]:
            command_number += 1
            available_commands.append(f"{command_number}. {command}")
    return '\n'.join(available_commands)

def command(username, args, whisp=False):
    waktu = cek_waktu()
    role = get_user_role(username)
    role_emojis = {
        'guest': '🐴',
        'user': '🦄',
        'admin': '🐲',
        'owner': '👾'
    }

    # Add emoji to username based on role
    emoji = role_emojis.get(role, '')
    decorated_username = f"{username}({emoji})"

    if args.startswith('login '):
        login_info = args[len('login '):].strip()
        if ':' in login_info:
            login_username, password = login_info.split(':', 1)
            if not whisp:
                return "Silakan gunakan whisper untuk melakukan login."
            if login_username != username:
                return "Anda hanya dapat login ke akun Anda sendiri."
            if login(login_username, password):
                return f"Login berhasil sebagai {login_username}."
            else:
                return "Gagal login. Coba lagi."
        else:
            return "Format login tidak valid. Gunakan !login username:password."

    if args.startswith('register '):
        password = args[len('register '):].strip()
        if not whisp:
            return "Silakan gunakan whisper untuk melakukan registrasi."
        if register(username, password):
            return f"Registrasi berhasil sebagai {username}. Silakan login kembali"
        else:
            return "Gagal registrasi. Username sudah terdaftar."

    if args == 'logout':
        if logout(username):
            return f"Logout berhasil untuk {username}."
        else:
            return "Anda belum login."
    
    if args == 'forgot_password':
        return "Silahkan hubungi owner saya ^_^"

    roles = {
        'guest': {
            'login': f"Format login tidak valid. Gunakan !login username:password.",
            'register': f"Format register tidak valid. Gunakan !register password."
        },
        'user': {
            'about|help': "About information for users"
        },
        'admin': {
            'about': "About information for admins"
        },
        'owner': {
            'up <langkah>': "moveUp(<langkah>)",
            'down <langkah>': "moveDown(<langkah>)",
            'kanan <langkah>': "moveRight(<langkah>)",
            'kiri <langkah>': "moveLeft(<langkah>)",
            'forgot_password': "Silahkan hubungi owner saya ^_^"
            # tambahkan perintah-perintah lain yang relevan untuk peran owner di sini
        }
    }

    if role == 'owner':
        for command_text in roles['owner']:
            if args.startswith(command_text):
                try:
                    langkah = int(args.split()[1])
                except (IndexError, ValueError):
                    return "Format perintah tidak valid. Gunakan format yang benar."


                return format_output(f"Menggerakkan {command_text}...")

    if args in ['menu', 'help', 'menus']:
        if is_logged_in(username) or role == "guest":
            available_menu = list_menu(username, roles)
            return format_output(f"{waktu} kak {decorated_username}\nMenu yang tersedia:\n{available_menu}")
        else:
            return "Anda belum login. Gunakan !login untuk login."
    
    return "Perintah tidak dikenali."
