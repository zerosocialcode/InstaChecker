# Instagram Account Checker

A fast, efficient, and privacy-focused tool for checking if an email or username is linked to an Instagram account. Designed for researchers, cybersecurity professionals, and OSINT enthusiasts, this checker supports both single and bulk queries, with proxy and anti-blocking best practices.

---

## 🚀 Features

- **Single & Bulk Checking:** Instantly verify one or thousands of Instagram handles or emails.
- **Proxy Support:** Easily rotate proxies for maximum reliability and to reduce rate-limiting.
- **Minimal, Clean Output:** No clutter—just the info you need.
- **Colorized Terminal Output:** Read results at a glance with clear, colored messages.
- **Rate Limiting & Retry Logic:** Smart delays and retry on failures.
- **Optional Proxy File:** Plug in your own proxies for added anonymity.
- **Educational & Ethical Use:** Built-in warnings and usage reminders.

---

## ⚡️ Quick Start

1. **Clone the repository:**
   ```sh
   git clone https://github.com/falconthehunter/InstaChecker.git
   cd InstaChecker
   ```

2. **(Optional)** Add a `proxies.txt` file (one proxy per line, e.g., `http://user:pass@ip:port`).

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the script:**
   ```sh
   python main.py
   ```

---

## 🛡️ Usage

- **Single Check:**  
  Enter a username or email when prompted.  
  Output:  
  - `Account found boss` (account exists)  
  - `Account not found` (no linked account)  
  - `Error or blocked, try again` (rate-limited or error)

- **Bulk Check:**  
  Prepare a text file with one username/email per line.  
  Select bulk mode and provide the file path.  
  Each query will display a clear result for that input.

---

## 💡 Advanced Usage & Best Practices

- **Proxy Rotation:**  
  Blocked or rate-limited? Add more proxies in `proxies.txt` to bypass restrictions and improve reliability.
- **Delay Configuration:**  
  Adjust the `request_delay` in the script for high-volume tasks to avoid bans.
- **No Logging:**  
  Script is privacy-friendly and does not store results unless you extend it.

---

## 🌟 Roadmap & Premium Feature Ideas

1. **Instagram Login Session Support:**  
   Reduce blocking by authenticating as a real user.

2. **Auto Proxy Scraper and Validator:**  
   Fetch, test, and rotate fresh proxies on the fly.

3. **CAPTCHA Bypass Integration:**  
   Use third-party services when Instagram triggers extra security.

4. **Export Options:**  
   Save results to CSV, JSON, or Excel for further analysis.

5. **Customizable Output Formats:**  
   Choose between minimal, detailed, or JSON output.

6. **REST API & Web Dashboard:**  
   Expose the checker via an API or a web interface for team use.

7. **Desktop GUI:**  
   User-friendly graphical interface for point-and-click operation.

8. **Notifications & Reporting:**  
   Optional email, Telegram, or Discord alerts for finished checks.

9. **Docker Container:**  
   Run securely and portably with `docker run`.

10. **Error Analytics:**  
    Track and visualize failure trends for proxy or request errors.

11. **Multi-Platform Packaging:**  
    Single-file executables for Windows, macOS, and Linux.

12. **Full OSINT Suite Integration:**  
    Plug-and-play with other reconnaissance tools.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue for discussion before submitting pull requests.

---

## ⚠️ Disclaimer

This tool is for educational, research, and legitimate security testing purposes only.  
**Do not** use it for harassment, unauthorized access, or any illegal activity.  
Use of this tool is at your own risk, and you are responsible for compliance with all local laws and Instagram’s Terms of Service.

---
