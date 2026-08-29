# CO5_AT1 – Q27: Sudoku Variation with Diagonal Constraints

## Question

Solve a Sudoku puzzle where both diagonals must also contain unique numbers. Clearly define additional diagonal constraints. Analyze how constraints interact with standard Sudoku rules. Develop a backtracking-based solution. Apply constraint propagation and pruning. Justify correctness and discuss increased complexity.

## Objective

To develop a backtracking-based solver for a variation of Sudoku in which both diagonals must contain unique numbers in addition to the standard Sudoku constraints.

## Additional Constraints

The program follows the standard Sudoku rules:

* Every row must contain numbers 1–9 without repetition.
* Every column must contain numbers 1–9 without repetition.
* Every 3×3 sub-grid must contain numbers 1–9 without repetition.

Two additional diagonal constraints are applied:

* The main diagonal must contain numbers 1–9 without repetition.
* The secondary diagonal must contain numbers 1–9 without repetition.

## Algorithm

1. Find an empty cell.
2. Try numbers from 1 to 9.
3. Check whether the number is valid in the row, column, and 3×3 sub-grid.
4. If the cell belongs to a diagonal, also check the corresponding diagonal.
5. Place the number if all constraints are satisfied.
6. Recursively solve the remaining puzzle.
7. If a contradiction occurs, remove the number and try another candidate.
8. Continue until all cells are filled.

## Constraint Propagation and Pruning

Constraint checking is performed before placing every number. Invalid candidates are immediately rejected.

This reduces unnecessary recursive calls because numbers that violate row, column, sub-grid, or diagonal constraints are not explored further.

## Correctness

The solution is correct because every number is placed only after satisfying all Sudoku and diagonal constraints. Backtracking ensures that incorrect choices are removed and alternative candidates are explored.

When the algorithm reaches a state with no empty cells, every constraint has been satisfied, so the resulting grid is a valid diagonal Sudoku solution.

## Complexity Analysis

For a 9×9 Sudoku, there are up to 81 cells and at most 9 candidates per empty cell.

In the worst case, the backtracking search can be exponential, approximately:

O(9^81)

The additional diagonal checks increase the amount of constraint checking for cells lying on the diagonals. However, these extra constraints also provide stronger pruning and can reduce the number of possible search branches for suitable puzzles.

Space complexity is approximately O(81) for the recursion depth and Sudoku grid.

## Real-World Applications

The backtracking and constraint-solving approach used here can be applied to:

* Scheduling problems
* Resource allocation
* Timetabling
* Puzzle solving
* Configuration problems
* Constraint satisfaction problems

## Conclusion

A diagonal Sudoku is more restrictive than standard Sudoku because both diagonals must also contain unique numbers. Backtracking provides a systematic method for exploring possible solutions, while constraint propagation and pruning eliminate invalid choices early. The additional diagonal constraints increase checking requirements but can also reduce the search space by restricting possible values.

## Repository Structure

```text
CO5_AT1/
│
├── Question_27/
│   ├── Source_Code/
│   │   └── diagonal_sudoku.cpp
│   │
│   └── Report/
│       └── Q27_Report.docx
│
└── README.md
```

