# Job‑Shop Scheduling Problem with Ant Colony Optimization (ACO)

## Authors
- **Felix Luca Krebs (2470475)**
- **MD KAMRUZZAMAN RUSSEL (2470478)**
- **Justus Izuchukwu Onuh (2470477)**

## Title
**Job‑Shop Scheduling Using Ant Colony Optimization (ACO)**

## Aim
Implement the **Job‑Shop Scheduling Problem (JSSP)** and solve it with **Ant Colony Optimization**, minimizing the makespan (total completion time).

## Problem Overview
The JSSP assigns a set of jobs (each a sequence of operations) to machines. Each operation has a fixed machine requirement and processing time. We seek a schedule that respects operation order and machine capacity, minimizing the overall makespan.

## Why Use ACO?
ACO mimics real ants laying and following pheromone trails to find shortest routes. It excels at NP‑hard problems like JSSP by balancing exploration (randomness) and exploitation (pheromone strength) and adapting over iterations.

## Methodology
1. **Representation**: Each job is a list of operations (machine_id, processing_time).
2. **Ant Colony**: Multiple "ants" build schedules probabilistically using pheromone (learned) + heuristic (1/processing_time).
3. **Pheromone Update**: After each iteration, reinforce edges used in shorter makespans and evaporate old pheromone.

## Repository Layout
```
ACO-JSSP/
│
├── src/
│   ├── algorithm/
│   │   └── ant_colony.py    ← core ACO implementation
│   ├── data/
│   │   ├── download_datasets.py    ← fetch benchmark instances
│   │   └── jssp_data_loader.py    ← loads .txt problem files
│   ├── models/
│   │   └── jobshop.py    ← JSSP data structures
│   └── main.py    ← program entry point
│
├── data/    ← stores dataset files (*.txt)
├── results/    ← contains solution_output.txt
├── Advanced_Algorithm___Ant_Colony_Algorithms_and_Applications__Group_3.pdf
├── requirements.txt
└── README.md
```

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/izunwaonu/ACO-JSSP.git
   cd ACO-JSSP
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download benchmark datasets**
   ```bash
   python src/data/download_datasets.py
   ```
   This will fetch standard JSSP instances (e.g., `FT06.txt`) into `data/`.

4. **Run the ACO algorithm**
  ```bash
python -m src.main --data data/FT06.txt --ants 20 --iters 100 --alpha 1.0 --beta 2.0 --rho 0.5
```
   * `--data` : path to the dataset file
   * `--ants` : number of ants
   * `--iters`: number of iterations
   * `--alpha`: pheromone importance
   * `--beta` : heuristic importance
   * `--rho` : pheromone evaporation rate

5. **View Results**
   * **Console**: Prints best makespan and schedule.
   * **File**: Check `results/solution_output.txt` for detailed output (`Job`, `Op#`, `Machine`, `Start`, `End`).

## Report
The full written report (following the lecturer's guideline) is provided here: `Advanced_Algorithm___Ant_Colony_Algorithms_and_Applications__Group_3.pdf`

## Requirements
```
numpy>=1.26.0
```

