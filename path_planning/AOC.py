import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
from numpy.random import choice as np_choice


class AntColony:
    def __init__(self, distances, n_ants, pheromone_decay=0.1, alpha=1, beta=1):
        """
        Args:
            distances (2D numpy.array): Square matrix of distances. Diagonal is assumed to be np.inf.
            n_ants (int): Number of ants running per iteration
            pheromone_decay (float): Rate it which pheromone decays. The pheromone value is multiplied by this number,
                                    so 0.95 will lead to decay, 1.0 will lead to no decay.
            alpha (int or float): exponenet on pheromone, higher alpha gives pheromone more weight.
            beta (int or float): exponent on distance, higher beta give distance more weight
        """
        self.distances  = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.pheromone_decay = pheromone_decay
        self.alpha = alpha
        self.beta = beta
        self.n_ants = n_ants

    def run(self, num_iterations):
        """
        Args:
            num_iterations (int): number of iterations for which the ant colony will be run
        """
        for i in range(num_iterations):
            all_inds = []
            for i in range(self.n_ants):
                all_inds.append(self.gen_all_paths())
            self.spread_pheronome(all_inds, self.pheromone_decay)

    def spread_pheronome(self, all_inds, decay):
        """
        Args:
            all_inds (list): list of all paths selected by the ants
            decay (float): pheromone decay parameter
        """
        self.pheromone *=(1-decay)
        for path in all_inds:
            for move in path:
                self.pheromone[move] += 1.0 / self.distances[move]

    def gen_all_paths(self):
        """
        Returns:
            all_paths: list of lists, where each list is a path
        """
        all_paths = []
        for i in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append(path)
        return all_paths

    def gen_path_dist(self, start):
        """
        Args:
            start: starting location of the ant
        Returns:
            path: list of indices of the path
        """
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append((prev, move))
            prev = move
            visited.add(move)
        path.append((prev, start)) # going back to where we started    
        return path

    def pick_move(self, pheromone, dist, visited):
        """
        Args:
            pheromone (1D numpy.array): pheromone of the edges
            dist (1D numpy.array): distance matrix of the edges
            visited (1D numpy.array): array of visited nodes
        Returns:
            int: the index of the next node to visit
        """
        row = pheromone ** self.alpha * (( 1.0 / dist) ** self.beta)

        row[list(visited)] = 0

        norm_row = row / row.sum()
        move = np_choice(self.all_inds, 1, p=norm_row)[0]
        return move

    def visualize(self):
        fig, ax = plt.subplots()

        def update(frame):
            ax.clear()
            ax.set_title(f'Iteration {frame + 1}')
            self.run(1)
            paths = self.gen_all_paths()
            self.plot_paths(ax, paths)

        ani = FuncAnimation(fig, update, frames=range(10), repeat=False)
        plt.show()

    def plot_paths(self, ax, paths):
        for path in paths:
            line = Line2D(*zip(*path), marker='o', markersize=8, linestyle='-', linewidth=2)
            ax.add_line(line)
        ax.set_xlim(-1, len(self.distances))
        ax.set_ylim(-1, len(self.distances))
        plt.pause(0.1)

# 거리 행렬 생성 (예시)
distances = np.array([[0, 2, 3, 4],
                      [2, 0, 5, 6],
                      [3, 5, 0, 7],
                      [4, 6, 7, 0]])

# ACO 알고리즘 생성
aco = AntColony(distances, n_ants=5)

# 시각화 실행
aco.visualize()
