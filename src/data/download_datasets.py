# src/data/download_datasets.py

"""
Generate benchmark JSSP dataset files for the ACO‑JSSP project.
Currently supports the FT06 instance by Fisher & Thompson (1963).
"""

import os

# FT06 dataset: 6 jobs × 6 operations (machine_id, processing_time)
FT06 = [
    [(1, 1),  (2, 3),  (3, 6),  (4, 7),  (5, 3),  (0, 6)],
    [(3, 8),  (2, 5),  (0, 10), (1, 10), (5, 4),  (4, 1)],
    [(2, 5),  (3, 4),  (4, 8),  (0, 9),  (1, 1),  (5, 7)],
    [(1, 5),  (0, 5),  (2, 5),  (3, 3),  (4, 8),  (5, 9)],
    [(2, 9),  (3, 3),  (4, 5),  (0, 4),  (1, 3),  (5, 1)],
    [(1, 3),  (3, 3),  (0, 9),  (5, 10), (2, 4),  (4, 1)],
]


def generate_ft06(output_path: str = "data/FT06.txt"):
    """
    Write the FT06 dataset to a text file.
    Each line corresponds to one job; pairs are: machine_id processing_time.
    """
    # Ensure the data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        for job in FT06:
            # join each (machine, time) pair by a space
            line = " ".join(f"{machine} {time}" for machine, time in job)
            f.write(line + "\n")

    print(f"[✓] FT06 instance generated at `{output_path}`")


if __name__ == "__main__":
    # When run as a script, generate FT06
    generate_ft06()
