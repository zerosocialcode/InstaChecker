import requests
import time
import random
import sys
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Dummy:
        RESET = ''
        CYAN = ''
        RED = ''
        YELLOW = ''
    Fore = Style = Dummy()

class UltimateInstagramChecker:
    def __init__(self, proxies=None, max_threads=3, request_delay=2):
        self.session = requests.Session()
        self.proxies = proxies if proxies else [None]
        self.max_threads = max_threads
        self.request_delay = request_delay
        self.retry_limit = 2
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
        ]
        self.running = True
        self.reset_url = "https://www.instagram.com/accounts/password/reset/"
        self.check_url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
        self.base_headers = {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-IG-App-ID": "936619743392459",
            "X-Requested-With": "XMLHttpRequest",
        }

    def _rotate_proxy(self):
        return random.choice(self.proxies)

    def _check_account(self, email_or_username, attempt=0):
        if not self.running:
            return None

        try:
            proxy = self._rotate_proxy()
            user_agent = random.choice(self.user_agents)
            self.session.headers.update({
                **self.base_headers,
                **{"User-Agent": user_agent}
            })

            response = self.session.get(
                self.reset_url,
                headers={"Referer": "https://www.instagram.com/"},
                proxies={"http": proxy, "https": proxy} if proxy else None,
                timeout=10
            )

            if response.status_code != 200:
                if attempt < self.retry_limit:
                    time.sleep(3)
                    return self._check_account(email_or_username, attempt + 1)
                return "error"

            payload = {"email_or_username": email_or_username}
            headers = {
                **self.session.headers,
                **{
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-CSRFToken": self.session.cookies.get("csrftoken", ""),
                    "Referer": self.reset_url,
                }
            }
            response = self.session.post(
                self.check_url,
                data=urlencode(payload),
                headers=headers,
                proxies={"http": proxy, "https": proxy} if proxy else None,
                timeout=10
            )

            if response.status_code == 200:
                try:
                    data = response.json()
                    if "users" in data:
                        return "found"
                    elif data.get("user_exists", False) or data.get("status") == "ok":
                        return "found"
                    else:
                        return "not found"
                except ValueError:
                    return "error"
            elif response.status_code == 400:
                try:
                    data = response.json()
                    return "found"
                except ValueError:
                    return "error"
            elif response.status_code in [429, 403]:
                if attempt < self.retry_limit:
                    time.sleep(5)
                    return self._check_account(email_or_username, attempt + 1)
                return "error"
            else:
                return "error"
        except Exception:
            return "error"

    def bulk_check(self, input_file):
        try:
            with open(input_file, "r") as f:
                targets = [line.strip() for line in f if line.strip()]
            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                futures = {executor.submit(self._check_account, target): target for target in targets}
                for future in as_completed(futures):
                    if not self.running:
                        executor.shutdown(wait=False)
                        break
                    result = future.result()
                    user = futures[future]
                    if result == "found":
                        print(Fore.CYAN + f"{user}: Account found boss")
                    elif result == "not found":
                        print(Fore.CYAN + f"{user}: Account not found")
                    else:
                        print(Fore.CYAN + f"{user}: Error or blocked, try again")
                    time.sleep(self.request_delay)
        except Exception:
            print(Fore.RED + "bulk error")

def print_short_warning():
    print(Fore.CYAN + "WARNING: For educational use only. Do not abuse.\nUsage: 1=single, 2=bulk, proxies.txt optional.\n")

def main():
    print_short_warning()

    try:
        proxies = []
        try:
            with open("proxies.txt", "r") as f:
                proxies = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            pass

        checker = UltimateInstagramChecker(proxies=proxies if proxies else None)

        print(Fore.CYAN + "="*30)
        choice = input(Fore.CYAN + "1. Single check\n2. Bulk check\n> ").strip()

        if choice == "1":
            target = input(Fore.CYAN + "Username/email: ").strip()
            result = checker._check_account(target)
            if result == "found":
                print(Fore.CYAN + "Account found boss")
            elif result == "not found":
                print(Fore.CYAN + "Account not found")
            else:
                print(Fore.CYAN + "Error or blocked, try again")
        elif choice == "2":
            input_file = input(Fore.CYAN + "Input file: ").strip()
            checker.bulk_check(input_file)
        else:
            print(Fore.RED + "Invalid choice.")
    except Exception:
        print(Fore.RED + "Critical error.")
        sys.exit(1)

if __name__ == "__main__":
    main()
