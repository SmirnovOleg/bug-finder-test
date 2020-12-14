"""
Unfortunately, our approach can produce a false positives too. In this example,
`enumerate()` pattern exchange is unacceptable because of logic of the script.

But you can always suppress unnecessary warnings!
"""


# noinspection BugFinder
def merge_intervals(intervals):
    new_intervals = []
    last_interval = None

    intervals = sorted(intervals)
    for i in range(len(intervals)):
        if not last_interval:
            new_intervals.append(intervals[i])
            last_interval = intervals[i]
            continue

        last_start, last_end = last_interval
        start, end = intervals[i]

        if last_end >= start:
            last_interval[1] = max(last_end, end)
        else:
            new_intervals.append(intervals[i])
            last_interval = intervals[i]

    return new_intervals
