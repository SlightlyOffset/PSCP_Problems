"""Saitama"""
def main():
    """main"""

    pushup = int(input())
    situp = int(input())
    squat = int(input())
    run = int(input())
    pushup_pd = int(input())
    situp_pd = int(input())
    run_pd = int(input())
    squat_pd = int(input())

    top = 0
    time_pushup = pushup / pushup_pd
    if time_pushup > top:
        top = time_pushup
    time_situp = situp / situp_pd
    if time_situp > top:
        top = time_situp
    time_squat = squat / squat_pd
    if time_squat > top:
        top = time_squat
    time_run = run / run_pd
    if time_run > top:
        top = time_run

    print(f"{top:.0f}")
if __name__ == "__main__":
    main()
