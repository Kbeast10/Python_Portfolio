from collections import Counter

def calc_total_area(rectangles):
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, 1, y1, y2))
        events.append((x2, -1, y1, y2))
    #Sorts by lowest x then prioritizes events that need to be removed vs not
    events.sort(key=lambda event: (event[0], -event[1]))

    active_intervals = Counter()


    total_area = 0
    previous_x = events[0][0]

    def get_union_length(intervals):
        if not intervals:
            return 0
        intervals.sort()
        union_length = 0
        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                union_length += current_end - current_start
                current_start, current_end = start, end
        union_length += current_end - current_start
        return union_length
    for x, event_type, y1, y2 in events:
        delta_x = x - previous_x
        if delta_x > 0:
            current_intervals = [interval for interval, count in active_intervals.items() for _ in range(count)]

            covered_y_length = get_union_length(current_intervals)

            total_area += covered_y_length * delta_x
            previous_x = x
        active_intervals[(y1, y2)] += event_type
        if active_intervals[(y1, y2)] == 0:
            del active_intervals[(y1, y2)]
    return total_area

def main():
    areas = []
    while True:

        #number of rectangles in one case
        n = int(input())
        if n != 0:
            rectangles = []
            for x in range(n):
                #coordinates of one rectangle
                x1, y1, x2, y2 = input().split()
                rect_coords = [int(x1), int(y1), int(x2), int(y2)]
                rectangles.append(rect_coords)
            areas.append(calc_total_area(rectangles))
        else:
            break
    #call functions
    for x in areas:
        print(x)
  # prints the union area
main()
