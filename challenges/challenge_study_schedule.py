def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if target_time == '':
        return None

    if not all(
        isinstance(period, tuple) and
        len(period) == 2 and
        all(isinstance(x, int) for x in period)
        for period in permanence_period
    ):
        return None

    count = sum(
        1 for start, end in permanence_period if start <= target_time <= end)

    return count
