from celery import Celery
# from src.explorer import Explorer
from src.improved_explorer import ImprovedExplorer as Explorer
from src.maze import create_maze 
import time

app = Celery('tasks',
             broker='pyamqp://guest@localhost//',
             backend='redis://localhost:6379/0')

@app.task(bind=True)
def run_explorer(self, task_id, maze_type="random", width=30, height=30, enhanced=False):
    try:
        from src.maze import create_maze
        maze = create_maze(width, height, maze_type)

        if enhanced:
            from src.improved_explorer import ImprovedExplorer as Explorer
        else:
            from src.explorer import Explorer

        explorer = Explorer(maze, visualize=False)

        start_time = time.perf_counter()
        explorer.solve()
        end_time = time.perf_counter()

        duration = end_time - start_time
        if duration < 0.01:
            duration = 0.01

        stats = {
            "task_id": task_id,
            "maze_type": maze_type,
            "enhanced": enhanced,
            "time_taken": round(duration, 3),
            "total_moves": len(explorer.moves),
            "backtracks": explorer.backtrack_count,
            "avg_moves_per_sec": round(len(explorer.moves) / duration, 2)
        }

        print(f"✅ Task {task_id} done: {stats}")
        return stats

    except Exception as e:
        print(f"❌ Task {task_id} failed: {e}")
        return None
