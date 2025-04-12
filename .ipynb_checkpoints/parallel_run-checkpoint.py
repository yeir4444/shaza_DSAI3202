from tasks import run_explorer
from celery.result import ResultSet
import csv
import os

# === Configuration ===
NUM_EXPLORERS = 4
MAZE_TYPE = "static"  # or "random"
MAZE_WIDTH = 50
MAZE_HEIGHT = 50
USE_ENHANCED_EXPLORER = True  # Set to False to test the original explorer

print("🚀 Submitting explorers...\n")

# Submit Celery tasks
task_set = [
    run_explorer.delay(
        i,
        maze_type=MAZE_TYPE,
        width=MAZE_WIDTH,
        height=MAZE_HEIGHT,
        enhanced=USE_ENHANCED_EXPLORER
    ) for i in range(NUM_EXPLORERS)
]

print("⏳ Waiting for explorers to finish...\n")

# Wait for all tasks to complete
results = ResultSet(task_set)

try:
    explorer_stats = results.join(timeout=60)
except Exception as e:
    print(f"\n⚠️ Timeout or join error: {e}")
    explorer_stats = []

# === Results Processing ===
print("\n=== Explorer Results ===")
valid_results = []

for i, r in enumerate(explorer_stats):
    if r:
        print(f"Explorer {r['task_id']} ✅ - {r['maze_type']} Maze | {'Enhanced' if r.get('enhanced') else 'Original'}")
        print(f"  Moves: {r['total_moves']}")
        print(f"  Backtracks: {r['backtracks']}")
        print(f"  Time: {r['time_taken']}s")
        print(f"  Moves/sec: {r['avg_moves_per_sec']}\n")
        valid_results.append(r)
    else:
        print(f"Explorer {i} ❌ - No result or task failed")

# === Find Best Explorer ===
if valid_results:
    best = min(valid_results, key=lambda x: x["total_moves"])
    print(f"\n🏆 Best Explorer: #{best['task_id']} with {best['total_moves']} moves")
else:
    print("\n❌ No valid explorers completed successfully.")

# === Save to CSV ===
os.makedirs("results", exist_ok=True)
csv_path = "results/explorers_results.csv"

with open(csv_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=[
        "task_id", "maze_type", "enhanced", "total_moves", "backtracks", "time_taken", "avg_moves_per_sec"
    ])
    writer.writeheader()
    for r in valid_results:
        writer.writerow(r)

print(f"\n📁 Results saved to: {csv_path}")
