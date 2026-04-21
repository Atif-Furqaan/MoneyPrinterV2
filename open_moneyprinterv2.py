from __future__ import annotations

import shutil
import subprocess
import sys
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VENV_PYTHON = ROOT / "venv" / "Scripts" / "python.exe"
CONFIG = ROOT / "config.json"
CONFIG_EXAMPLE = ROOT / "config.example.json"
ENTRYPOINT = ROOT / "src" / "main.py"


def main() -> int:
    if not VENV_PYTHON.exists():
        print("Missing virtual environment.")
        print(f"Expected: {VENV_PYTHON}")
        print("Run dependency installation first.")
        return 1

    if not CONFIG.exists() and CONFIG_EXAMPLE.exists():
        shutil.copyfile(CONFIG_EXAMPLE, CONFIG)
        print("Created config.json from config.example.json")

    if not ENTRYPOINT.exists():
        print(f"Missing entrypoint: {ENTRYPOINT}")
        return 1

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    return subprocess.call([str(VENV_PYTHON), str(ENTRYPOINT)], cwd=str(ROOT), env=env)


if __name__ == "__main__":
    sys.exit(main())
