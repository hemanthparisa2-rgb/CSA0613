# CO5_AT2 - Maximum Cut Problem

## Question 27

Design and implement a Backtracking algorithm to partition a graph into two groups while maximizing the number of cut edges.

## Objective

Find two partitions of the graph such that the number of edges between the partitions is maximum.

## Algorithm

**Backtracking with Recursion and Pruning**

The algorithm assigns each vertex to either Group A or Group B. It recursively explores possible partitions and prunes branches that are not promising.

## Input

Graph represented using an adjacency matrix.

## Output

* Group A
* Group B
* Maximum number of cut edges

## Sample Output

```text
Maximum Cut Problem
Group A: [1, 3]
Group B: [2, 4]
Maximum Cut Edges: 4
```

## Complexity

**Time Complexity:** O(2ⁿ × n²)

**Space Complexity:** O(n)

## Repository Structure

```text
CO5_AT2/
│
├── Question_1/
│   ├── Source_Code/
│   │   └── maximum_cut.py
│   │
│   └── Report/
│       └── Maximum_Cut_Report.docx
│
└── README.md
```

## How to Run

Open a terminal in the `Source_Code` folder and run:

```bash
python maximum_cut.py
```

## Result

The Maximum Cut Problem is successfully solved using Backtracking with recursion and pruning.

