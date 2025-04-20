# src/algorithm/ant_colony.py

import random
from typing import List
from src.models.jobshop import JobShopInstance, Operation
import copy


class Ant:
    """
    Represents an ant that constructs a solution (a schedule).
    """
    def __init__(self, jobshop: JobShopInstance):
        self.jobshop = jobshop
        self.schedule = []
        self.makespan = None

    def construct_solution(self, pheromone, heuristic, alpha, beta):
        """
        Builds a schedule using pheromone and heuristic matrices.
        """
        operations = [copy.deepcopy(job.operations) for job in self.jobshop.jobs]
        schedule = []
        machine_time = [0] * self.jobshop.num_machines
        job_time = [0] * self.jobshop.num_jobs

        while any(operations):
            eligible_ops = []
            for job_id, ops in enumerate(operations):
                if ops:
                    eligible_ops.append(ops[0])

            probabilities = []
            total = 0
            for op in eligible_ops:
                tau = pheromone[op.job_id][op.order]
                eta = heuristic[op.job_id][op.order]
                prob = (tau ** alpha) * (eta ** beta)
                probabilities.append(prob)
                total += prob

            if total == 0:
                selected = random.choice(eligible_ops)
            else:
                r = random.uniform(0, total)
                cumulative = 0
                for i, op in enumerate(eligible_ops):
                    cumulative += probabilities[i]
                    if r <= cumulative:
                        selected = op
                        break

            start = max(machine_time[selected.machine_id], job_time[selected.job_id])
            end = start + selected.processing_time
            selected.start_time = start
            selected.end_time = end

            machine_time[selected.machine_id] = end
            job_time[selected.job_id] = end
            schedule.append(selected)

            # Remove the operation from its job queue
            operations[selected.job_id].pop(0)

        self.schedule = schedule
        self.makespan = max(op.end_time for op in schedule)
        return schedule


class AntColony:
    """
    The ACO algorithm class. Manages pheromone matrix, ants, and iterations.
    """
    def __init__(self, jobshop: JobShopInstance, num_ants: int = 10, iterations: int = 100,
                 alpha: float = 1.0, beta: float = 2.0, rho: float = 0.5):
        self.jobshop = jobshop
        self.num_ants = num_ants
        self.iterations = iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho

        self.pheromone = [
            [1.0 for _ in range(len(job))] for job in self.jobshop.jobs
        ]
        self.heuristic = [
            [1.0 / op.processing_time for op in job.operations] for job in self.jobshop.jobs
        ]

    def run(self):
        """
        Main loop to run the ACO optimization.
        """
        best_schedule = None
        best_makespan = float('inf')

        for iteration in range(self.iterations):
            ants = [Ant(self.jobshop) for _ in range(self.num_ants)]
            all_schedules = []

            for ant in ants:
                ant.construct_solution(self.pheromone, self.heuristic, self.alpha, self.beta)
                if ant.makespan < best_makespan:
                    best_makespan = ant.makespan
                    best_schedule = ant.schedule
                all_schedules.append(ant)

            self._update_pheromones(all_schedules)
            print(f"[Iteration {iteration + 1}] Best Makespan so far: {best_makespan}")

        return best_schedule, best_makespan

    def _update_pheromones(self, ants: List[Ant]):
        """
        Updates pheromone matrix based on all ants' schedules.
        """
        for i in range(len(self.pheromone)):
            for j in range(len(self.pheromone[i])):
                self.pheromone[i][j] *= (1 - self.rho)

        for ant in ants:
            for op in ant.schedule:
                self.pheromone[op.job_id][op.order] += 1.0 / ant.makespan
