Tetravex Solver

Overview

Tetravex is a tile-based puzzle game where the objective is to arrange square tiles in a grid so that adjacent edges match in value. This Python script provides a solver for the Tetravex puzzle using a backtracking algorithm.

Features

Solves Tetravex puzzles of any given size.

Uses a backtracking approach to find a valid solution.

Implements a retry mechanism if a solution is not found within a limited number of attempts.

Outputs a color-coded visual representation of the puzzle using ANSI escape codes.

Installation

To use this solver, ensure you have Python installed on your system. No additional libraries are required.

Clone Repository

git clone https://github.com/yourusername/tetravex-solver.git
cd tetravex-solver

Usage

Run the script using:

python tetravex_solver.py

You will be prompted to enter the puzzle size, and the solver will attempt to generate and solve a random Tetravex puzzle.

Example Input:

Puzzle Size (nxn)
3

Example Output:

A visual representation of the puzzle solution with colored numbers representing tile edges.

Algorithm

Generates a random set of tiles with edge values between 0-9.

Attempts to place tiles recursively using backtracking.

If a valid solution is found, it prints the completed puzzle.

If no solution is found after multiple attempts, it regenerates tiles and retries.

Customization

Modify the size variable to specify a fixed puzzle size.

Define a custom set of tiles instead of generating random ones.

Adjust the maximum number of attempts before regenerating tiles.
