def validate_periods(permanence_period):
    for entry in permanence_period:
        if not isinstance(entry, tuple):
            return False
        if entry[0] < 0 or entry[1] < 0 or entry[0] >= entry[1]:
            return False
    return True


def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if not permanence_period:
        return 0

    if not validate_periods(permanence_period):
        return None

    count = sum(1 for entry in permanence_period
                if entry[0] <= target_time <= entry[1])
    return count
