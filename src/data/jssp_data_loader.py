# src/data/jssp_data_loader.py

from typing import List, Tuple
from src.models.jobshop import JobShopInstance


def load_jssp_from_file(filepath: str) -> JobShopInstance:
    """
    Load a Job-Shop Scheduling Problem instance from a text file.

    The file format is expected to be:
    - Each line represents a job.
    - Each job has pairs of integers: (machine_id processing_time)
    
    Example line:
    1 3 2 6 3 7
    means:
    Job with 3 operations:
    Op1 on Machine 1 for 3 units
    Op2 on Machine 2 for 6 units
    Op3 on Machine 3 for 7 units
    """
    jobs_data: List[List[Tuple[int, int]]] = []

    with open(filepath, 'r') as f:
        for line in f:
            parts = list(map(int, line.strip().split()))
            job_operations = [(parts[i], parts[i + 1]) for i in range(0, len(parts), 2)]
            jobs_data.append(job_operations)

    return JobShopInstance(jobs_data)
