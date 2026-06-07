"""Lunch PacMan game."""
import sys
from src.main import run


def main() -> None:
    """Lunch PacMan game."""

    if len(sys.argv) != 2:
        print(f"You need {sys.argv[0]} 'config.json':"
              "but 'config.json' not found")
        sys.exit(1)

    config_path: str = sys.argv[1]
    if not config_path.endswith(".json"):
        print(f"The {sys.argv[1]} need to be a json file")
        sys.exit(1)

    # x = run(config_path)
    # print(x)
    # # run(config_path)
    sys.exit(run(config_path))


if __name__ == "__main__":
    main()
