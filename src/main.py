# src/main.py

import os
import time
import argparse

# Import our loader and ACO classes
from src.data.jssp_data_loader import load_jssp_from_file
from src.algorithm.ant_colony import AntColony


def main():
    # ----------------------------------------
    # 1. Parse command-line arguments
    # ----------------------------------------
    parser = argparse.ArgumentParser(
        description="Run Ant Colony Optimization on a Job-Shop Scheduling Problem"
    )
    parser.add_argument(
        "--data",
        type=str,
        default=os.path.join("data", "jssp_data.txt"),
        help="Path to the JSSP data file"
    )
    parser.add_argument(
        "--ants",
        type=int,
        default=20,
        help="Number of ants in the colony"
    )
    parser.add_argument(
        "--iters",
        type=int,
        default=100,
        help="Number of ACO iterations"
    )
    parser.add_argument(
        "--alpha",
        type=float,
        default=1.0,
        help="Pheromone importance (alpha)"
    )
    parser.add_argument(
        "--beta",
        type=float,
        default=2.0,
        help="Heuristic importance (beta)"
    )
    parser.add_argument(
        "--rho",
        type=float,
        default=0.5,
        help="Pheromone evaporation rate (rho)"
    )
    args = parser.parse_args()

    # ----------------------------------------
    # 2. Load the Job-Shop instance
    # ----------------------------------------
    print(f"Loading JSSP instance from {args.data}...")
    jobshop = load_jssp_from_file(args.data)
    print(f"Loaded: {jobshop}\n")

    # ----------------------------------------
    # 3. Initialize and run ACO
    # ----------------------------------------
    print("Initializing Ant Colony...")
    colony = AntColony(
        jobshop,
        num_ants=args.ants,
        iterations=args.iters,
        alpha=args.alpha,
        beta=args.beta,
        rho=args.rho
    )

    print("Running ACO...")
    start_time = time.time()
    best_schedule, best_makespan = colony.run()
    elapsed = time.time() - start_time

    print("\n=== RESULTS ===")
    print(f"Best Makespan: {best_makespan}")
    print(f"Time Taken: {elapsed:.2f} seconds")
    print("================\n")

    # ----------------------------------------
    # 4. Save output to file
    # ----------------------------------------
    os.makedirs("results", exist_ok=True)
    output_path = os.path.join("results", "solution_output.txt")
    with open(output_path, "w") as f:
        f.write(f"Best Makespan: {best_makespan}\n")
        f.write(f"Time Taken: {elapsed:.2f} seconds\n\n")
        f.write("Schedule:\n")
        f.write("Job\tOp#\tMachine\tStart\tEnd\n")
        for op in best_schedule:
            f.write(
                f"{op.job_id}\t{op.order}\t{op.machine_id}\t"
                f"{op.start_time}\t{op.end_time}\n"
            )
    print(f"Solution saved to {output_path}")


if __name__ == "__main__":
    main()
