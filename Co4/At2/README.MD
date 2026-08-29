# Q27 – Smart City Waste Collection Routing

## Aim

To find an optimal waste collection route using graph optimization and reduce travel distance, fuel consumption, time, and cost.

## Algorithm

**Dijkstra’s Shortest Path Algorithm**

The road cost is calculated using:

`Cost = Distance × Traffic Factor`

## Technologies

* Python
* Dijkstra Algorithm
* Graph
* Heap Queue

## Features

* Finds the optimal route.
* Considers traffic conditions.
* Estimates fuel consumption.
* Calculates fuel cost.
* Considers vehicle capacity.
* Reduces environmental impact.

## Sample Result

**Optimal Route:** `0 → 1 → 3 → 4 → 5`

**Travel Cost:** 36 units

**Fuel Consumption:** 2.88 litres

**Fuel Cost:** Rs. 288

## Complexity

Dijkstra’s algorithm using a priority queue:

`O((V + E) log V)`

## Repository Structure

```text
Q27_Smart_City_Waste_Collection_Routing/
│
├── Source_Code/
│   └── main.py
│
├── Report/
│   └── Q27_Report.docx
│
├── Supporting_Files/
│   └── sample_input.txt
│
└── README.md
```

## Conclusion

The proposed system uses Dijkstra’s algorithm to find efficient waste collection routes. Optimized routing helps reduce fuel consumption, transportation costs, travel time, and CO₂ emissions.

