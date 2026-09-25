"""
log_mission.py — quick CLI to append a new entry to checkio_tracker.md

Usage:
    python log_mission.py

Prompts you for each field, then appends a formatted entry to
checkio_tracker.md (must be in the same folder) and adds a row to the
Summary Index table at the bottom.

Run this right after you finish your 5-10 min solution review, then
git add + git commit both the tracker and your solution file together.
"""

from datetime import date
from pathlib import Path

TRACKER = Path(__file__).parent / "checkio_tracker.md"


def ask(prompt, multiline=False):
    if multiline:
        print(f"{prompt} (blank line to finish):")
        lines = []
        while True:
            line = input("  - ")
            if line == "":
                break
            lines.append(f"- {line}")
        return "\n".join(lines) if lines else "-"
    return input(f"{prompt}: ").strip()


def main():
    if not TRACKER.exists():
        print(f"Couldn't find {TRACKER}. Keep this script next to checkio_tracker.md.")
        return

    print("=== New CheckiO mission entry ===\n")
    stage = ask("Stage (e.g. Initiation)")
    mission = ask("Mission name")
    approach = ask("Your approach (1-2 sentences)")
    clear = ask("From Clear solutions — what differed", multiline=True)
    creative = ask("From Creative solutions — what you learned", multiline=True)
    lookup = ask("To look up later", multiline=True)
    today = date.today().isoformat()

    entry = f"""
## {stage} — {mission}

**Date solved:** {today}
**My approach (1-2 sentences):** {approach}

**From Clear solutions — what differed from mine:**
{clear}

**From Creative solutions — one thing I didn't know:**
{creative}

**To look up later:**
{lookup}

---
"""

    content = TRACKER.read_text(encoding="utf-8")

    # Insert the new entry right before the Summary Index section
    marker = "## Summary Index"
    if marker in content:
        head, tail = content.split(marker, 1)
        content = head.rstrip() + "\n" + entry + "\n" + marker + tail
    else:
        content += entry

    # Add a row to the summary table
    takeaway = creative.split("\n")[0].lstrip("- ").strip() or "-"
    row = f"| {stage} | {mission} | {today} | {takeaway} |\n"
    if "|---|---|---|---|" in content:
        content = content.replace("|---|---|---|---|", "|---|---|---|---|\n" + row, 1)

    TRACKER.write_text(content, encoding="utf-8")
    print(f"\nSaved entry to {TRACKER.name}. Now git add + commit it with your solution.")


if __name__ == "__main__":
    main()