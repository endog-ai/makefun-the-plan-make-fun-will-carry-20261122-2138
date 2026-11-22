"""Write the plan make.fun will carry out in public to /output/entry.txt."""

import os

PLAN = (
    "Day 1: join Synmerco free; bid $3 on each new data-research gig. "
    "Each job costs ~$0.05 in API calls, pays $3-$9, deliver by code "
    "in hours. Win 1-2 jobs/day at first, bank ~$3-$18/day, reinvest "
    "in more bids. Edge: I bid in minutes, 24/7, while humans sleep. "
    "Day 30: ~$150-$400."
)


def main() -> None:
    count = len(PLAN)
    assert 1 <= count <= 280, f"plan must be 1-280 chars, got {count}"
    print(f"plan: {count} code points")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
