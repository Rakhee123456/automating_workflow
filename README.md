# 🤖 Autonomous Daily GitHub Commit & Push System (367 Days)

A fully autonomous system designed to push Python updates and commit code to GitHub every day for 367+ days continuously.

---

## 🌟 Two Automation Options

### 1. ☁️ Cloud Automation via GitHub Actions (Recommended)
- **100% Autonomous**: Runs directly on GitHub's cloud servers.
- **No PC Required**: Your computer does **not** need to stay on or connected to the internet.
- Runs every day at the scheduled time (configured in [`.github/workflows/daily_commit.yml`](file:///.github/workflows/daily_commit.yml)).

### 2. 💻 Local Automation via Windows Task Scheduler
- Runs locally on your Windows machine using [`auto_push.py`](file:///auto_push.py).
- Can be scheduled using [`setup_scheduler.ps1`](file:///setup_scheduler.ps1).

---

## 🚀 Setup Guide (Cloud GitHub Actions)

### Step 1: Initialize Git and Connect your GitHub Repo
In this project folder, run the following commands in terminal:

```bash
git init
git add .
git commit -m "🎉 Initial setup: 367-day autonomous GitHub commit system"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
git push -u origin main
```

---

### Step 2: Enable Workflow Permissions on GitHub (Crucial!)
To allow GitHub Actions to commit and push changes back into your repository:

1. Open your repository on **GitHub.com**.
2. Click **Settings** (top bar).
3. In the left sidebar, click **Actions** -> **General**.
4. Scroll down to **Workflow permissions**.
5. Select **"Read and write permissions"**.
6. Check **"Allow GitHub Actions to create and approve pull requests"**.
7. Click **Save**.

---

### Step 3: Test Workflow Immediately
1. Go to the **Actions** tab on your GitHub repository.
2. Select **"Autonomous Daily Python Push"** in the left list.
3. Click **"Run workflow"** -> **"Run workflow"** (green button).
4. Watch the action run: it will execute `main.py`, generate the daily update, and push the new commit to `main`!

---

## ⏰ Changing the Schedule Time
The schedule is defined in [`.github/workflows/daily_commit.yml`](file:///.github/workflows/daily_commit.yml) using standard cron format:

```yaml
on:
  schedule:
    - cron: '0 0 * * *' # Runs at 00:00 UTC every day
```

### Examples (UTC Timezone):
- `'0 0 * * *'` -> 12:00 AM UTC
- `'0 6 * * *'` -> 6:00 AM UTC
- `'30 14 * * *'` -> 2:30 PM UTC
- `'0 18 * * *'` -> 6:00 PM UTC

*(Note: Convert your local time to UTC when setting the cron).*

---

## 💻 Optional: Local Windows Automation

If you also want your computer to run and push updates locally:

1. Open PowerShell in this folder as Administrator.
2. Run:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\setup_scheduler.ps1 -Time "09:00"
   ```
   *(Replace `"09:00"` with your preferred local time in 24h format).*

---

## 📁 Repository Structure
```
├── .github/
│   └── workflows/
│       └── daily_commit.yml  # GitHub Actions Cloud Cron Workflow
├── main.py                   # Python daily update and snippet generator
├── auto_push.py              # Local autonomous git stage, commit & push script
├── run_daily.bat             # 1-click batch runner for Windows
├── setup_scheduler.ps1       # Windows Task Scheduler registration script
├── activity_log.json         # Structured JSON tracking progress & day streak
├── DAILY_UPDATES.md          # Generated human-readable progress & code log
└── README.md                 # Complete documentation
```
