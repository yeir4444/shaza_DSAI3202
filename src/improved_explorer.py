from src.explorer import Explorer
import random

class ImprovedExplorer(Explorer):
    def choose_direction(self):
        # Get goal position
        goal_x, goal_y = self.maze.end_pos
        dx = goal_x - self.x
        dy = goal_y - self.y

        # Greedy: try to move closer to the goal first
        if abs(dx) > abs(dy):
            preferred_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)] if dx > 0 else [(-1, 0), (1, 0), (0, 1), (0, -1)]  
            random.shuffle(preferred_dirs)
        else:
            preferred_dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)] if dy > 0 else [(0, -1), (0, 1), (1, 0), (-1, 0)]

        # Only keep directions that lead to open paths
        for dx, dy in preferred_dirs:
            nx, ny = self.x + dx, self.y + dy
            if self.maze.is_wall((nx, ny)) == False and (nx, ny) not in self.visited:
                return dx, dy

        return None  # No valid direction found

    def move(self, direction):
        dx, dy = direction
        new_x, new_y = self.x + dx, self.y + dy
        self.path.append((self.x, self.y))
        self.visited.add((new_x, new_y))
        self.x, self.y = new_x, new_y
        self.moves.append((self.x, self.y))

    def backtrack(self):
        if self.path:
            self.backtrack_count += 1
            self.x, self.y = self.path.pop()
            self.moves.append((self.x, self.y))
    def at_goal(self):
        return (self.x, self.y) == self.maze.end_pos

    def solve(self):
        self.path = []
        self.moves = []  
        self.visited = set()
        self.visited.add((self.x, self.y))


        while not self.at_goal():
            direction = self.choose_direction()
            if direction:
                self.move(direction)
            else:
                self.backtrack()

        print("✅ ImprovedExplorer reached the goal.")
