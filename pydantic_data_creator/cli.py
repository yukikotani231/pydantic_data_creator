import argparse
import subprocess
from pathlib import Path


DIR = Path(__file__).parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "module_path", help="The path to the module that includes the pydantic models"
    )
    parser.add_argument("model_name", help="The name of the pydantic model to use for the form")
    args = parser.parse_args()

    cmd = ["streamlit", "run", str(DIR / "main.py"), args.module_path, args.model_name]

    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        pass
