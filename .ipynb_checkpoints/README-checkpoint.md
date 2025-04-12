# Maze Explorer Game

A simple maze exploration game built with Pygame where you can either manually navigate through a maze or watch an automated solver find its way to the exit.

## Getting Started

### 1. Connect to Your VM

1. Open **<span style="color:red">Visual Studio Code</span>**
2. Install the "Remote - SSH" extension if you haven't already
3. Connect to your VM using SSH:
   - Press `Ctrl+Shift+P` to open the command palette
   - Type "Remote-SSH: Connect to Host..."
   - Enter your VM's SSH connection details
   - Enter your credentials when prompted

### 2. Project Setup

1. Clone this repository to your VM
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Game

### Basic Usage
Run the game with default settings (30x30 random maze):
```bash
python main.py
```

### Manual Mode (Interactive)
Use arrow keys to navigate through the maze:
```bash
# Run with default random maze
python main.py

# Run with static maze
python main.py --type static

# Run with custom maze dimensions
python main.py --width 40 --height 40
```

### Automated Mode (Explorer)
The explorer will automatically solve the maze and show statistics:

#### Without Visualization (Text-only)
```bash
# Run with default random maze
python main.py --auto

# Run with static maze
python main.py --type static --auto

# Run with custom maze dimensions
python main.py --width 40 --height 40 --auto
```

#### With Visualization (Watch the Explorer in Action)
```bash
# Run with default random maze
python main.py --auto --visualize

# Run with static maze
python main.py --type static --auto --visualize

# Run with custom maze dimensions
python main.py --width 40 --height 40 --auto --visualize
```

Available arguments:
- `--type`: Choose between "random" (default) or "static" maze generation
- `--width`: Set maze width (default: 30, ignored for static mazes)
- `--height`: Set maze height (default: 30, ignored for static mazes)
- `--auto`: Enable automated maze exploration
- `--visualize`: Show real-time visualization of the automated exploration

## Maze Types

### Random Maze (Default)
- Generated using depth-first search algorithm
- Different layout each time you run the program
- Customizable dimensions
- Default type if no type is specified

### Static Maze
- Predefined maze pattern
- Fixed dimensions (50x50)
- Same layout every time
- Width and height arguments are ignored

## How to Play

### Manual Mode
1. Controls:
- Use the arrow keys to move the player (<span style="color:blue">blue circle</span>)
- Start at the <span style="color:green">green square</span>
- Reach the <span style="color:red">red square</span> to win
- Avoid the <span style="color:black">black walls</span>

### Automated Mode
- The explorer uses the right-hand rule algorithm to solve the maze
- Automatically finds the path from start to finish
- Displays detailed statistics at the end:
  - Total time taken
  - Total moves made
  - Number of backtrack operations
  - Average moves per second
- Works with both random and static mazes
- Optional real-time visualization:
  - Shows the explorer's position in <span style="color:blue">blue</span>
  - Updates at 30 frames per second
  - Pauses for 2 seconds at the end to show the final state

## Project Structure

```
maze-runner/
├── src/
│   ├── __init__.py
│   ├── constants.py
│   ├── maze.py
│   ├── player.py
│   ├── game.py
│   └── explorer.py
├── main.py
├── requirements.txt
└── README.md
```

## Code Overview

### Main Files
- `main.py`: Entry point of the game. Handles command-line arguments and initializes the game with specified parameters.
- `requirements.txt`: Lists all Python package dependencies required to run the game.

### Source Files (`src/` directory)
- `__init__.py`: Makes the src directory a Python package.
- `constants.py`: Contains all game constants like colors, screen dimensions, cell sizes, and game settings.
- `maze.py`: Implements maze generation using depth-first search algorithm and handles maze-related operations.
- `player.py`: Manages player movement, collision detection, and rendering of the player character.
- `game.py`: Core game implementation including the main game loop, event handling, and game state management.
- `explorer.py`: Implements automated maze solving using the right-hand rule algorithm and visualization.

## Game Features

- Randomly generated maze using depth-first search algorithm
- Predefined static maze option
- Manual and automated exploration modes
- Real-time visualization of automated exploration
- Smooth player movement
- Collision detection with walls
- Win condition when reaching the exit
- Performance metrics (time and moves) for automated solving

## Development

The project is organized into several modules:
- `constants.py`: Game constants and settings
- `maze.py`: Maze generation and management
- `player.py`: Player movement and rendering
- `game.py`: Game implementation and main loop
- `explorer.py`: Automated maze solving implementation and visualization

## Student Questions

### Question 1 (10 points)
Explain how the automated maze explorer works. Your answer should include:
1. The algorithm used by the explorer
2. How it handles getting stuck in loops
3. The backtracking strategy it employs
4. The statistics it provides at the end of exploration

To answer this question:
1. Run the explorer both with and without visualization
2. Observe its behavior in different maze types
3. Analyze the statistics it provides
4. Read the source code in `explorer.py` to understand the implementation details

Your answer should demonstrate a clear understanding of:
- The right-hand rule algorithm
- The loop detection mechanism
- The backtracking strategy
- The performance metrics collected


**answer:** 

The explorer uses the right-hand rule algorithm, which is one of the most widely known strategies for solving a maze (Roberts, 2015). Where you place your right hand on the wall and keep it there until you find an exit. In this case, the agent always attempts to turn right first, move straight if possible, or turn left as a last resort. If none of these options are viable, it initiates the backtracking mechanism. 

While this algorithm is very useful, it sometimes fails if there are loops in the maze that surround either the starting position or the goal (Roberts, 2015). Fortunately, this algorithm has a pretty effective method for handling these types of situations, starting with the short history (deque of the last 3 positions) maintained by the explorer. If it notices repeated movement patterns, it interprets that as being stuck and backtracks by storing previous positions in `self.backtrack\_path`, and each backtrack step increases `self.backtrack_count`. 

So, when trapped, the explorer will:
1. Step back to the last junction.
2. Try an alternative unexplored direction.

The process continues until the explorer reaches the goal (marked as a red square in the game). At the end, the system outputs detailed performance statistics:

- Total time taken
- Total number of moves
- Number of backtracks
- Average move speed


As can be seen in the `print_statistics` function below.
```
def print_statistics(self, time_taken: float):
        """Print detailed statistics about the exploration."""
        print("\n=== Maze Exploration Statistics ===")
        print(f"Total time taken: {time_taken:.2f} seconds")
        print(f"Total moves made: {len(self.moves)}")
        print(f"Number of backtrack operations: {self.backtrack_count}")
        print(f"Average moves per second: {len(self.moves)/time_taken:.2f}")
        print("==================================\n")
```
Reference: 
- Roberts, E. (2015). Recursive backtracking. Recursive Backtracking. https://cs.stanford.edu/people/eroberts/courses/cs106b/handouts/16-RecursiveBacktracking.pdf
  
### Question 2 (30 points)
Modify the main program to run multiple maze explorers simultaneously. This is because we want to find the best route out of the maze. Your solution should:
1. Allow running multiple explorers in parallel
2. Collect and compare statistics from all explorers
3. Display a summary of results showing which explorer performed best

*Hints*:
- To get full marks, use Celery and RabbitMQ to distribute the exploration tasks. If you don't use Celery, RabbitMQ and redis, you will still get marks but you will not get the full 30 points.
- Implement a task queue system
- Do not visualize the exploration, just run it in parallel
- Store results for comparison

**To answer this question:** 
1. Study the current explorer implementation
2. Design a parallel execution system
3. Implement task distribution
4. Create a results comparison system

**answer:** 
To run multiple explorers in parallel, we created a task distribution system using Celery, RabbitMQ, and Redis. each explorer was packaged as a Celery task and used for parallel execution.

`tasks.py` was created to define a `run_explorer()` function that initializes a maze and solves it using the right-hand rule as explained in question 1. Then it returns performance statistics. we then launched 4 explorers simultaneously using `parallel_run.py`, each solving a separate instance of the maze without visualization.

Celery workers handled the concurrent task execution, while Redis served as the result backend. After execution, we collected results from all explorers and printed a summary, including total moves, backtracks, and average moves per second. This setup allowed us to compare their performance and identify the best explorer.


=== Explorer Results ===
Explorer 0 ✅ - static Maze
  Moves: 1279
  Backtracks: 0
  Time: 0.01s
  Moves/sec: 127900.0

Explorer 1 ✅ - static Maze
  Moves: 1279
  Backtracks: 0
  Time: 0.01s
  Moves/sec: 127900.0

Explorer 2 ✅ - static Maze
  Moves: 1279
  Backtracks: 0
  Time: 0.01s
  Moves/sec: 127900.0

Explorer 3 ✅ - static Maze
  Moves: 1279
  Backtracks: 0
  Time: 0.01s
  Moves/sec: 127900.0


🏆 Best Explorer: #0 with 1279 moves

### Question 3 (10 points)
Analyze and compare the performance of different maze explorers on the static maze. Your analysis should:

1. Run multiple explorers (at least 4 ) simultaneously on the static maze
2. Collect and compare the following metrics for each explorer:
   - Total time taken to solve the maze
   - Number of moves made
   - *Optional*:
     - Number of backtrack operations

3. What do you notice regarding the performance of the explorers? Explain the results and the observations you made.

**answer:** 

After running 4 explorers in parallel, as mentioned in question 2. We saved the results in a CSV file as a `results/` directory. and the results are as follows: 


| Explorer ID | Total Moves | Backtracks | Time (s) | Moves/sec   |
|-------------|-------------|------------|----------|-------------|
| 0           | 1279        | 0          | 0.01     | 127900.0    |
| 1           | 1279        | 0          | 0.01     | 127900.0    |
| 2           | 1279        | 0          | 0.01     | 127900.0    |
| 3           | 1279        | 0          | 0.01     | 127900.0    |

**Observations:**

- All explorers followed the exact same path and completed the maze with the same number of moves.
- No backtracks were needed, confirming the static maze has a straightforward solution for the right-hand rule.
- Minor timing variance may be masked by fast computation speed (so we used a floor time of 0.01s to ensure meaningful stats).

While the identical results from all explorers suggest the algorithm behaves deterministically on the static maze, it also raises the possibility of a bug or oversight. Specifically, this could mean that all explorers are solving the exact same maze rather than different instances. This might indicate a limitation in how explorers are initialized or how the maze is cloned per task.

### Question 4 (20 points)
Based on your analysis from Question 3, propose and implement enhancements to the maze explorer to overcome its limitations. Your solution should:

1. Identify and explain the main limitations of the current explorer:

2. Propose specific improvements to the exploration algorithm:

3. Implement at least two of the proposed improvements:

Your answer should include:
1. A detailed explanation of the identified limitations
2. Documentation of your proposed improvements
3. The modified code with clear comments explaining the changes

**answer:**

The explorer we developed in question 4 uses the right-hand rule, which is deterministic and guarantees a solution in simply-connected mazes. However, it has very clear limitations, including:

1. It does not adapt based on path conditions.
2. It produces identical results across all runs on static mazes.
3. There is no variability.
4. Possibly all explorers are solving either the same shared maze object (my error) of a maze where the right-hand rule always performs identically.


This clearly limits our ability to compare performance fairly or to improve solver efficiency. 

To enhance the solution we can:

1. Use Independent Maze Instances per Explorer.

   We can use the `create_maze()` function inside each Celery task to ensure every explorer gets an isolated copy, which helps avoid the shared memory bugs.
   
2. Implement a Smarter Solver: `ImprovedExplorer`.

   By adding a simple greedy direction preference that prioritizes moving towards the goal's direction (based on coordinate difference) and falls back to the right-hand rule if blocked, we can enhance the algorithm.

**results after improvment:**


=== Explorer Results ===
Explorer 0 ✅ - static Maze | Enhanced
  Moves: 1357
  Backtracks: 607
  Time: 0.01s
  Moves/sec: 135700.0

Explorer 1 ✅ - static Maze | Enhanced
  Moves: 1417
  Backtracks: 640
  Time: 0.01s
  Moves/sec: 141700.0

Explorer 2 ✅ - static Maze | Enhanced
  Moves: 1159
  Backtracks: 509
  Time: 0.01s
  Moves/sec: 115900.0

Explorer 3 ✅ - static Maze | Enhanced
  Moves: 2061
  Backtracks: 960
  Time: 0.01s
  Moves/sec: 206100.0


🏆 Best Explorer: #2 with 1159 moves

We can see we have different results across explorers, variations in moves and backtracks, and a clear best performer (explorer #2).

### Question 5 (20 points)

Compare the performance of your enhanced explorer with the original:
   - Run both versions on the static maze
   - Collect and compare all relevant metrics
   - Create visualizations showing the improvements
   - Document the trade-offs of your enhancements
Your answer should include:
1. Performance comparison results and analysis
2. Discussion of any trade-offs or new limitations introduced


**answer:**
To compare the performance of the original explorer algorithm (right-hand rule) with the enhanced explorer algorithm (greedy + randomized direction), both solving the same static maze in parallel. The comparison is based on:

- Total moves made
- Number of backtracks
- Time taken (fixed floor of 0.01s due to very fast execution)
- Average moves per second

We executed four explorers using each algorithm. Both sets were run in parallel using Celery with RabbitMQ and Redis for distributed execution. The explorers solved a **50x50 static maze**, and results were logged to a CSV file shown below:

#### **Original Explorer Results (Right-Hand Rule)**

| Explorer ID | Total Moves | Backtracks | Time (s) | Moves/sec |
|-------------|-------------|------------|----------|-----------|
| 0           | 1279        | 0          | 0.01     | 127900.0  |
| 1           | 1279        | 0          | 0.01     | 127900.0  |
| 2           | 1279        | 0          | 0.01     | 127900.0  |
| 3           | 1279        | 0          | 0.01     | 127900.0  |

#### **Improved Explorer Results (Greedy + Random Shuffle)**

| Explorer ID | Total Moves | Backtracks | Time (s) | Moves/sec |
|-------------|-------------|------------|----------|-----------|
| 0           | 1357        | 607        | 0.01     | 135700.0  |
| 1           | 1417        | 640        | 0.01     | 141700.0  |
| 2           | 1159        | 509        | 0.01     | 115900.0  |
| 3           | 2061        | 960        | 0.01     | 206100.0  |

**Observations:**

- The original explorer produced identical results across all runs. This is expected due to the deterministic nature of the right-hand rule algorithm on a fixed maze layout.

- The improved explorer, although operating on the same static maze, produced diverse results due to the randomized direction selection strategy.
  
- Backtracking was introduced in the improved explorer, which allows it to recover from poor path choices but also increases path variability.
- Explorer #2 with the improved method found the most efficient path with just 1159 moves, outperforming the original’s fixed 1279 moves.
- This shows that intelligent and randomized decision-making can lead to better paths, even if other runs perform worse due to randomness.

The improved explorer algorithm introduces necessary variability and adaptability by combining goal-oriented movement with random direction shuffling. While this leads to some explorers performing worse, it also enables at least one to outperform the original fixed-path logic. This kind of adaptive behavior is crucial in dynamic or more complex maze environments.

The experiment validates that the enhancement adds performance diversity, enabling optimization opportunities, and providing a more realistic comparison of pathfinding strategies.


Note: ChatGPT was utilized to debug the code, but I ended up liking the emojis, so I kept the print statements. 

### Final points 6 (10 points)
1. Solve the static maze in 150 moves or less to get 10 points.
2. Solve the static maze in 135 moves or less to get 15 points.
3. Solve the static maze in 130 moves or less to get 100% in your assignment.

**answer:** 
To reach the shortest possible solution, we implemented an A* algorithm for path finding as it guarantees the shortest path.  A* is known for its efficiency and accuracy in grid-based search problems (Foead et al., 2021). It uses a heuristic (Manhattan distance) to estimate distance to the goal, tracks cost for each step taken, and has a priority queue to explore the most promising paths first (GeeksforGeeks, 2024).

The results were as follows:

=== Explorer Results ===
Explorer 0 ✅ - static Maze | Enhanced
  Moves: 128
  Backtracks: 0
  Time: 0.01s
  Moves/sec: 12800.0

Explorer 1 ✅ - static Maze | Enhanced
  Moves: 128
  Backtracks: 0
  Time: 0.01s
  Moves/sec: 12800.0

Explorer 2 ✅ - static Maze | Enhanced
  Moves: 128
  Backtracks: 0
  Time: 0.01s
  Moves/sec: 12800.0

Explorer 3 ✅ - static Maze | Enhanced
  Moves: 128
  Backtracks: 0
  Time: 0.01s
  Moves/sec: 12800.0


🏆 Best Explorer: #0 with 128 moves

Which, as you can see, is under 130 moves. The results are identical for all explorers because all 4 explorers are running A* on the exact same static maze, and A* is designed to always find the optimal (shortest) path. 
meaning, No randomness = all follow the same optimal path = same stats

128 moves is the shortest path from start to end in that static maze, so every run will report exactly that. And as shown in the results, we can observe that there are no backtracks in this algorithm because A* always moves forward toward the optimal path. Identical results confirm that A* produces a deterministic and consistent solution in static environments (Foead et al., 2021), which not only validates the implementation but also proves its optimality.  

With A*, we achieved a reliable shortest-path solution that satisfies the most stringent criteria of this assignment. 

Reference: 
- GeeksforGeeks. (2024, July 30). A* search algorithm. GeeksforGeeks. https://www.geeksforgeeks.org/a-search-algorithm/
- Foead, D., Ghifari, A., Kusuma, M. B., Hanafiah, N., & Gunawan, E. (2021). A Systematic Literature review of A* pathfinding. Procedia Computer Science, 179, 507–514. https://doi.org/10.1016/j.procs.2021.01.034

### Bonus points
1. Fastest solver to get top  10% routes (number of moves)
2. Finding a solution with no backtrack operations --> this has been achieved using A* as mentioned above.
3. Least number of moves.