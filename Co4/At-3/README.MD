# CO4_AT3

## Q27 – Knapsack Problem vs Container Loading

### Aim

To compare **0/1 Knapsack using Dynamic Programming** with **Greedy Container Loading** and analyze their solution quality and computational efficiency.

### Algorithms

* **0/1 Knapsack:** Dynamic Programming
* **Container Loading:** Greedy Algorithm

### Input

* Item weights
* Item values
* Container capacity

### Comparison

| Method            | Approach            | Complexity |
| ----------------- | ------------------- | ---------- |
| 0/1 Knapsack      | Dynamic Programming | O(n × W)   |
| Container Loading | Greedy              | O(n log n) |

### Key Insight

Dynamic Programming evaluates different combinations and can find the optimal value. Greedy is faster but can fail for discrete optimization because it makes decisions based only on the current best choice.

### Applications

* Cargo loading
* Warehouse management
* Truck packing
* Resource allocation
* Logistics optimization

### Repository Structure

```text
CO4_AT3/
│
├── Question_1/
│   ├── Source_Code/
│   │   └── main.py
│   │
│   ├── Report/
│   │   └── Q27_Report.docx
│   │
│   └── Supporting_Files/
│       └── sample_input.txt
│
└── README.md
```

### Conclusion

The **DP approach** is preferred when an optimal solution is required, while the **Greedy approach** is useful when faster computation and simple implementation are more important.

