# Battery Scheduling Problem

## Problem Statement

The objective is to calculate the minimum total runtime required to execute a sequence of tasks on a battery-powered wearable device.

The battery level must always satisfy the following conditions:

* Battery should never go below 0
* Battery should never exceed maximum capacity
* Tasks must execute in the given order
* Charging is allowed only during idle periods

If a task cannot be executed under the given constraints, return `-1`.

---
## Setup Instructions

### Requirements

* Python 3.8 or above
* Visual Studio Code (recommended)

### Libraries Used

No external libraries are required.

Only Python built-in features are used.

### Environment Setup

1. Install Python
2. Install Visual Studio Code
3. Create a project folder
4. Add the solution.py file
5. Open terminal in VS Code

---
## Approach

My approach processes tasks one by one in the given order.

For every task:

1. Calculate the battery needed

   Required Battery = Duration × Drain Rate

2. Check whether the required battery exceeds battery capacity

   * If yes, execution is impossible
   * Return `-1`

3. Check whether current battery level is sufficient

   * If battery is insufficient:

     * Find the missing battery amount
     * Calculate minimum charging time required

4. Update total runtime with:

   * Charging time (if needed)
   * Task execution time

5. Update battery level after task execution

---

## Assumptions

* Tasks cannot be reordered
* Charging happens only during idle state
* Minimum charging time is preferred
* Battery changes continuously

---

## Design Decisions

* Tasks are processed sequentially because order cannot be changed
* Impossible cases are handled immediately
* Only the minimum charging time is used to reduce total runtime
* Simple and readable implementation is preferred

---

## Time Complexity

O(n)

where n = number of tasks

Reason:
Each task is processed only once.

---

## Space Complexity

O(1)

Reason:
Only a few variables are used regardless of input size.

---

## How to Run

Open terminal and run:

python solution.py

---

## Sample Input

batteryCapacity = 100

initialBattery = 50

tasks = [
[10,5],
[5,8],
[20,2]
]

chargeRate = 4

---

## Sample Output

Minimum Total Runtime = 35.0
