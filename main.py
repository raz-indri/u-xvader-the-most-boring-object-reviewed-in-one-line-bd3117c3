import os

ENTRY = "Five stars. The rubber band survived eleven years in the drawer, then snapped the instant it finally got a job."

print(ENTRY)
out_dir = os.environ.get("OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
