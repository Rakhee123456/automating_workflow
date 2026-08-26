"""
Local Autonomous Git Commit & Push Utility
Runs main.py, stages changes, commits, and pushes to GitHub.
"""

import subprocess
import sys
import io
from datetime import datetime, timezone

# Ensure UTF-8 output encoding across Windows terminals
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
if sys.stderr.encoding != 'utf-8':
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def run_cmd(cmd, check=True):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True, encoding='utf-8', errors='replace')
    if check and result.returncode != 0:
        print(f"[ERROR] Command failed: {cmd}\n{result.stderr.strip()}", file=sys.stderr)
    return result

def main():
    print("=" * 60)
    print("[INFO] Starting Autonomous Daily Update & Push Process")
    print("=" * 60)
    
    # 1. Run main.py
    print("[1/4] Running main.py generator...")
    res = run_cmd(f'"{sys.executable}" main.py')
    if res.returncode != 0:
        print("[FAIL] Execution of main.py failed.")
        sys.exit(1)
    print(res.stdout.strip())
    
    # 2. Stage changes
    print("\n[2/4] Staging changes with git add...")
    run_cmd("git add -A")
    
    # Check if there are changes to commit
    diff_check = run_cmd("git status --porcelain", check=False)
    if not diff_check.stdout.strip():
        print("[INFO] Working tree is clean. No new changes to commit.")
        sys.exit(0)
        
    # 3. Create commit
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    commit_msg = f"Auto update: Python daily commit - {now_str}"
    print(f"\n[3/4] Committing changes: '{commit_msg}'...")
    res_commit = run_cmd(f'git commit -m "{commit_msg}"')
    print(res_commit.stdout.strip())
    
    # 4. Push to remote
    print("\n[4/4] Checking remote and pushing to origin main...")
    remotes = run_cmd("git remote", check=False)
    if "origin" not in remotes.stdout:
        print("[WARNING] No remote 'origin' configured yet!")
        print("To push to GitHub, add your remote repository URL first:")
        print("  git remote add origin https://github.com/<USERNAME>/<REPO>.git")
        print("  git push -u origin main")
        return

    push_res = run_cmd("git push origin main", check=False)
    if push_res.returncode == 0:
        print("[SUCCESS] Successfully pushed daily commit to GitHub!")
    else:
        print(f"[ERROR] Git push failed. Details:\n{push_res.stderr.strip()}")
        print("Tip: Make sure you have authentication credentials configured or use GitHub Actions.")

if __name__ == "__main__":
    main()
