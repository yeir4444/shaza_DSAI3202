import heapq

class AStarExplorer:
    def __init__(self, maze, visualize=False):
        self.maze = maze
        self.visualize = visualize
        self.start = maze.start_pos
        self.goal = maze.end_pos
        self.moves = []
        self.backtrack_count = 0  # Not applicable in A*, but included for consistency

    def heuristic(self, a, b):
        """Manhattan distance heuristic"""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.maze.width and 0 <= ny < self.maze.height:
                if not self.maze.is_wall((nx, ny)):
                    neighbors.append((nx, ny))
        return neighbors

    def solve(self):
        open_set = []
        heapq.heappush(open_set, (0, self.start))
        came_from = {}
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}
        visited_nodes = 0
        MAX_NODES = 10000

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.goal:
                print(f"✅ Goal reached in {visited_nodes} steps")
                self.reconstruct_path(came_from, current)
                return

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, self.goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

            visited_nodes += 1
            if visited_nodes % 500 == 0:
                print(f"🔍 Explored {visited_nodes} nodes...")

            if visited_nodes > MAX_NODES:
                print("❌ A* failed: too many nodes explored.")
                return

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        self.moves = path
