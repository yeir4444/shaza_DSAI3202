from celery import Celery
# from src.explorer import Explorer
#from src.improved_explorer import ImprovedExplorer as Explorer
from src.astar_explorer import AStarExplorer as Explorer
from src.maze import create_maze 
import time

app = Celery('tasks',
             broker='pyamqp://guest@localhost//',
             backend='redis://localhost:6379/0')

@app.task(bind=True)
def run_explorer(self, task_id, maze_type="static", width=30, height=30, enhanced=False):
    try:
        from src.maze import create_maze
        maze = create_maze(width, height, maze_type)

        # Use A* if enhanced is True and "astar" mode is selected
        if enhanced == "astar":
            from src.astar_explorer import AStarExplorer as Explorer
        elif enhanced:
            from src.improved_explorer import ImprovedExplorer as Explorer
        else:
            from src.explorer import Explorer

        explorer = Explorer(maze, visualize=False)

        import time
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
            "total_moves": len(explorer.moves),
            "backtracks": getattr(explorer, "backtrack_count", 0),
            "time_taken": round(duration, 3),
            "avg_moves_per_sec": round(len(explorer.moves) / duration, 2)
        }

        print(f"✅ Task {task_id} done: {stats}")
        return stats

    except Exception as e:
        print(f"❌ Task {task_id} failed: {e}")
        return None
