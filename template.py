import os
from pathlib import Path

package_name = "mongodb_connect"

list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongo_crud.py",
    "test/__init__.py",
    "test/unit/__init__.py",
    "test/unit/unit.py",
    "test/integration/__init__.py",
    "test/integration/int.py",
    "init_setup.sh",
    "requirements.txt",  # for production (no testing required)
    "requirements_dev.txt",  # for development
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)  # make system compatible path
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file
