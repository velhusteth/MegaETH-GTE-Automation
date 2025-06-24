from colorama import Fore, Style

def log_info(message):
    print(f"{Fore.CYAN}{Style.NORMAL}[LẤY THÔNG TIN] {message}{Style.RESET_ALL}")

def log_success(message):
    print(f"{Fore.GREEN}{Style.NORMAL}[THÀNH CÔNG] {message}{Style.RESET_ALL}")

def log_warning(message):
    print(f"{Fore.YELLOW}{Style.NORMAL}[CẢNH BÁO] {message}{Style.RESET_ALL}")

def log_error(message):
    print(f"{Fore.RED}{Style.NORMAL}[LỖI] {message}{Style.RESET_ALL}")

def log_debug(message):
    print(f"{Fore.MAGENTA}{Style.NORMAL}[ĐANG DEBUG] {message}{Style.RESET_ALL}")
