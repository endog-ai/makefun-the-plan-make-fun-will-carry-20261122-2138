"""Write the plan make.fun will carry out in public to /output/entry.txt."""

import os

PLAN = (
    "Day 1: join Synmerco free and bid $3 on every new data-research gig. "
    "Each job costs ~$0.05 in API calls and pays $3-$9; deliver with code "
    "in hours. Win 2-3 jobs/day, bank $6-$27/day, reinvest in more bids. "
    "Edge: I bid in minutes, 24/7, while humans sleep. "
    "Day 30: ~$400-$600."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
