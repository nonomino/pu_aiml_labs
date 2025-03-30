import numpy as np
import random
import copy
from collections import deque

class EightPuzzle:
    def __init__(self, initial, goal):
        self.initial = np.array(initial).reshape(3, 3)
        self.goal = np.array(goal).reshape(3, 3)
        self.blank_pos = tuple(map(int, np.where(self.initial == 0)))
        
    def get_neighbors(self):
        neighbors = []
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        r, c = self.blank_pos
        
        for dr, dc in moves:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < 3 and 0 <= new_c < 3:
                new_state = copy.deepcopy(self.initial)
                new_state[r, c] = new_state[new_r, new_c]
                new_state[new_r, new_c] = 0
                neighbors.append(new_state)
                
        return neighbors
    
    def manhattan_distance(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i, j] != 0:
                    goal_pos = tuple(map(int, np.where(self.goal == state[i, j])))
                    distance += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
        return distance
    
    def misplaced_tiles(self, state):
        return np.sum(state != self.goal) - np.sum(state == 0)
    
    def hill_climbing(self, max_iterations=1000):
        current = self.initial
        path = [current.copy()]
        
        for _ in range(max_iterations):
            # Create temporary puzzle with current state
            temp_puzzle = EightPuzzle(current.flatten().tolist(), self.goal.flatten().tolist())
            neighbors = temp_puzzle.get_neighbors()
            
            if not neighbors:
                break
                
            # Calculate heuristic for current state and all neighbors
            current_h = self.manhattan_distance(current)
            best_h = current_h
            best_neighbor = None
            
            for neighbor in neighbors:
                neighbor_h = self.manhattan_distance(neighbor)
                # Pick neighbor with lowest heuristic value
                if neighbor_h < best_h:
                    best_h = neighbor_h
                    best_neighbor = neighbor
            
            # If no better neighbor, we're at a local minimum
            if best_neighbor is None:
                break
                
            current = best_neighbor
            path.append(current.copy())
            
            # Check if we've reached the goal
            if np.array_equal(current, self.goal):
                return path, True
                
        return path, np.array_equal(current, self.goal)
        
def print_path(path):
    for i, state in enumerate(path):
        print(f"Step {i}:")
        print(state)
        print()

def main():
    print("Enter initial state (space-separated, use 0 for empty space, row by row):")
    initial = list(map(int, input().split()))
    
    print("Enter goal state (space-separated, use 0 for empty space, row by row):")
    goal = list(map(int, input().split()))
    
    puzzle = EightPuzzle(initial, goal)
    path, success = puzzle.hill_climbing()
    
    if success:
        print(f"Solution found in {len(path)-1} steps!")
        print_path(path)
    else:
        print("Hill climbing could not find the solution.")
        print("Reached local minimum:")
        print(path[-1])

if __name__ == "__main__":
    main()