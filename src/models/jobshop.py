# src/models/jobshop.py

from typing import List, Tuple, Dict

class Operation:
    """
    Each operation belongs to a job and must be processed on a specific machine
    for a certain duration.
    """
    def __init__(self, job_id: int, machine_id: int, processing_time: int, order: int):
        self.job_id = job_id
        self.machine_id = machine_id
        self.processing_time = processing_time
        self.order = order  # The index of this operation in the job
        self.start_time = None
        self.end_time = None

    def __repr__(self):
        return f"Op(J{self.job_id}, M{self.machine_id}, T{self.processing_time})"


class Job:
    """
    Represents a job which consists of a list of operations.
    Each operation must be executed in a fixed order.
    """
    def __init__(self, job_id: int, operations: List[Tuple[int, int]]):
        self.job_id = job_id
        self.operations = [
            Operation(job_id, machine_id, proc_time, order)
            for order, (machine_id, proc_time) in enumerate(operations)
        ]

    def __len__(self):
        return len(self.operations)

    def __getitem__(self, idx):
        return self.operations[idx]

    def __repr__(self):
        return f"Job{self.job_id}: {self.operations}"


class JobShopInstance:
    """
    Loads and represents a complete Job-Shop problem instance.
    """
    def __init__(self, data: List[List[Tuple[int, int]]]):
        # data: List of jobs, each with a list of (machine_id, processing_time)
        self.jobs: List[Job] = [
            Job(job_id, operations) for job_id, operations in enumerate(data)
        ]
        self.num_jobs = len(self.jobs)
        self.num_machines = self._count_machines()

    def _count_machines(self) -> int:
        """
        Count the total number of unique machines from all operations.
        """
        machine_ids = set()
        for job in self.jobs:
            for op in job.operations:
                machine_ids.add(op.machine_id)
        return len(machine_ids)

    def get_operations(self) -> List[Operation]:
        """
        Returns a flat list of all operations across all jobs.
        """
        return [op for job in self.jobs for op in job.operations]

    def __repr__(self):
        return f"JSSP with {self.num_jobs} jobs and {self.num_machines} machines"
