INNER_BULL = 0.2
OUTER_BULL = 1.05
TOTAL_BULL = 1.25
TRIP_RING = 8.02
DOUBLE_RING = 12.93
INNER_RING = 46.4
OUTER_RING = 72
TOTAL_AREA = 140.6   # TOTAL_BULL + TRIP_RING + DOUBLE_RING + INNER_RING + OUTER_RING

INNER_BULL_POINTS = 50
OUTER_BULL_POINTS = 25

MISS_PROB = 0.05

def throw_expected_val():
    slice_vals = list(range(1, 21))

    inner_bull_prob = INNER_BULL / TOTAL_AREA
    outer_bull_prob = OUTER_BULL / TOTAL_AREA
    trip_ring_prob = TRIP_RING / TOTAL_AREA
    trip_segment_prob = trip_ring_prob / 20
    double_ring_prob = DOUBLE_RING / TOTAL_AREA
    double_segment_prob = double_ring_prob / 20
    inner_ring_prob = INNER_RING / TOTAL_AREA
    inner_segment_prob = inner_ring_prob / 20
    outer_ring_prob = OUTER_RING / TOTAL_AREA
    outer_segment_prob = outer_ring_prob / 20

    throw_expected_value = 0
    for slice_val in slice_vals:
        slice_expected_value = slice_val * inner_segment_prob
        slice_expected_value += slice_val * outer_segment_prob
        slice_expected_value += slice_val * trip_segment_prob * 3
        slice_expected_value += slice_val * double_segment_prob * 2
        throw_expected_value += slice_expected_value

    throw_expected_value += inner_bull_prob * INNER_BULL_POINTS
    throw_expected_value += outer_bull_prob * OUTER_BULL_POINTS
    throw_expected_value *= (1-MISS_PROB)

    return throw_expected_value

if __name__ == '__main__':
    num_throws = int(input("How many throws were made? "))
    print(round(throw_expected_val() * num_throws, 3))