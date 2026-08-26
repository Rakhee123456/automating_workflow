"""
Autonomous Daily Activity Generator
Tracks 367 days of continuous automated updates and Python code generation.
"""

import os
import json
import random
from datetime import datetime, timezone

TOTAL_DAYS_TARGET = 367
DATA_FILE = "activity_log.json"
MARKDOWN_LOG = "DAILY_UPDATES.md"

PYTHON_SNIPPETS = [
    ("Fibonacci Generator", "def fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        yield a\n        a, b = b, a + b"),
    ("Prime Sieve", "def sieve_of_eratosthenes(limit):\n    primes = [True] * (limit + 1)\n    p = 2\n    while (p * p <= limit):\n        if primes[p]:\n            for i in range(p * p, limit + 1, p):\n                primes[i] = False\n        p += 1\n    return [p for p in range(2, limit + 1) if primes[p]]"),
    ("Palindrome Checker", "def is_palindrome(s: str) -> bool:\n    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())\n    return cleaned == cleaned[::-1]"),
    ("Binary Search", "def binary_search(arr, target):\n    low, high = 0, len(arr) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            low = mid + 1\n        else:\n            high = mid - 1\n    return -1"),
    ("Quick Sort", "def quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)"),
    ("Factorial Memoization", "memo = {}\ndef factorial(n):\n    if n in (0, 1):\n        return 1\n    if n not in memo:\n        memo[n] = n * factorial(n - 1)\n    return memo[n]"),
    ("Matrix Transpose", "def transpose(matrix):\n    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]"),
    ("Two Sum Lookup", "def two_sum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n    return []")
]

def load_activity():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "start_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "total_target_days": TOTAL_DAYS_TARGET,
        "total_commits": 0,
        "history": []
    }

def save_activity(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def update_markdown(data, latest_entry):
    current_day = data["total_commits"]
    progress_pct = min(100.0, round((current_day / TOTAL_DAYS_TARGET) * 100, 2))
    
    lines = [
        "# 🚀 Autonomous 367-Day GitHub Automation",
        "",
        f"**Progress**: Day `{current_day}` of `{TOTAL_DAYS_TARGET}` ({progress_pct}%)",
        f"**Last Updated**: `{latest_entry['timestamp_utc']}`",
        f"**Status**: Active & Automating Daily",
        "",
        "## 📊 Summary Stats",
        f"- **Total Automated Commits**: {data['total_commits']}",
        f"- **Started On**: {data['start_date']}",
        f"- **Target Days**: {data['total_target_days']}",
        "",
        "## 📝 Latest Daily Update",
        f"**Day {latest_entry['day']}** (`{latest_entry['date']}`):",
        f"- **Feature/Algorithm**: {latest_entry['snippet_title']}",
        "```python",
        latest_entry["snippet_code"],
        "```",
        "",
        "---",
        "## 📜 Recent Activity History (Last 10 entries)",
        "| Day | Date (UTC) | Time (UTC) | Feature / Snippet |",
        "|---|---|---|---|"
    ]

    for item in reversed(data["history"][-10:]):
        lines.append(f"| Day {item['day']} | {item['date']} | {item['timestamp_utc'].split(' ')[1]} | {item['snippet_title']} |")

    lines.append("")
    lines.append("_Generated automatically by autonomous GitHub Action & Python workflow._\n")

    with open(MARKDOWN_LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def main():
    now_utc = datetime.now(timezone.utc)
    data = load_activity()
    
    current_day = data["total_commits"] + 1
    data["total_commits"] = current_day
    
    title, code = random.choice(PYTHON_SNIPPETS)
    
    entry = {
        "day": current_day,
        "date": now_utc.strftime("%Y-%m-%d"),
        "timestamp_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "snippet_title": title,
        "snippet_code": code
    }
    
    data["history"].append(entry)
    save_activity(data)
    update_markdown(data, entry)
    
    print(f"[SUCCESS] Day {current_day}/{TOTAL_DAYS_TARGET} update recorded at {entry['timestamp_utc']}")
    print(f"Snippet chosen: {title}")

if __name__ == "__main__":
    main()
