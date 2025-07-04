# 🧮 Sum Mate — Calculator Bot  
[![Telegram Bot](https://img.shields.io/badge/Launch%20Bot-@SumMateBot-2CA5E0?logo=telegram&style=for-the-badge)](https://t.me/SumMateBot)

> **Clean. Instant. Smart.**  
> Sum Mate is your reliable calculator in Telegram — just type a math problem, and get instant results. From simple sums to complex expressions, it handles it all effortlessly.

---

## ✨ Key Features

- **Freeform Math Parsing** — No commands needed! Just type `5+4`, `6×9`, or `25÷5`  
- **Smart Replies** — Understands messages, even in replies or groups  
- **/start** — Friendly welcome message with action buttons  
- **/help** — Usage guide for quick assistance  
- **Health Check Server** — Ready for production deployment  
- **Colorful Logs** — Terminal output with rich, categorized colors  

---

## 🧠 Use Case

Whether you’re a student, group admin, or math hobbyist, Sum Mate is the easiest way to solve calculations right inside Telegram.

> No more switching apps. Just send the math and get the answer.

---

## 📜 Commands Overview

| Command     | Description                                  |
|-------------|----------------------------------------------|
| `/start`    | Sends welcome message with action buttons    |
| `/help`     | Explains how to use the bot effectively      |
| *(Default)* | Type any expression like `2+2`, `3×4` etc.   |

---

## ⚙️ Tech Stack

- **Language:** Python  
- **Framework:** [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)  
- **Parsing Engine:** `simpleeval`  
- **Deployment:** Render / Railway / Replit compatible  
- **Logs:** ANSI color-coded with rich debug info  

---

## 🚀 Getting Started

1. Go to [@SumMateBot](https://t.me/SumMateBot)  
2. Press `/start`  
3. Try messages like:
   - `7+3`
   - `15÷5`
   - `8×4-2`
4. Watch the magic happen!

---

## 📦 Environment Variables

| Variable        | Description                                  |
|-----------------|----------------------------------------------|
| `BOT_TOKEN`     | Your Telegram Bot Token                      |
| `CHANNEL_LINK`  | Link to your updates channel (for button)    |
| `GROUP_LINK`    | Link to your support group (for button)      |
| `ADD_ME_LINK`   | Bot invite link (used in “Add me” button)    |
| `PORT`          | Optional — for HTTP health check (default 8000) |

---

## 🧪 Example Inputs

| Input           | Output          |
|-----------------|-----------------|
| `4+4`           | `4+4 = 8`       |
| `12×2`          | `12×2 = 24`     |
| `30 ÷ 5`        | `30÷5 = 6`      |
| `25% of 200`    | Interprets `%` as `*0.01` internally |

---

## 🧰 Extra Features

- **Auto typing indicators** — Adds human-like feedback before replies  
- **Inline buttons** — Links to support, updates, or add-to-group  
- **Async-safe** — Semaphore to control message flood  
- **Threaded HTTP server** — For uptime checks via health probe  

---

## 👨‍💻 Developed By

**Asadul Islam (Asad)**  
Telegram: [@asad_ofc](https://t.me/asad_ofc)

---

### 💌 Connect with Me

<p align="center">
  <a href="https://t.me/asad_ofc"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" /></a>
  <a href="mailto:mr.asadul.islam00@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://youtube.com/@asad_ofc"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" /></a>
  <a href="https://instagram.com/aasad_ofc"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
  <a href="https://tiktok.com/@asad_ofc"><img src="https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=tiktok&logoColor=white" /></a>
  <a href="https://x.com/asad_ofc"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=twitter&logoColor=white" /></a>
  <a href="https://facebook.com/aasad.ofc"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" /></a>
  <a href="https://www.threads.net/@aasad_ofc"><img src="https://img.shields.io/badge/Threads-000000?style=for-the-badge&logo=threads&logoColor=white" /></a>
  <a href="https://discord.com/users/1067999831416635473"><img src="https://img.shields.io/badge/Discord-asad__ofc-5865F2?style=for-the-badge&logo=discord&logoColor=white" /></a>
</p>

---

## 📄 License

Open source, flexible, and built for the community.  
Feel free to fork, modify, and deploy — just keep the credits alive! ❤️

---

> **Sum Mate** — *Even bots can do quick math faster than humans.*