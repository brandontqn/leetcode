import functools

def removeCoveredIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    
    """
    intervals[0] = (4, 8) => (4, 0, START), (8, 0, END)
    
    (1, 5), (2, 6)
    """
    def compare(event1, event2):
        time1, _, event_type1, complement_time1 = event1
        time2, _, event_type2, complement_time2 = event2
        
        if event_type1 == event_type2 and time1 == time2:
            return 1 if complement_time1 < complement_time2 else -1
                        
        return -1 if time1 < time2 else 1
    
    START = 0
    END = 1
    
    events = []
    
    for event_id, (start_time, end_time) in enumerate(intervals):
        events.append((start_time, event_id, START, end_time))
        events.append((end_time, event_id, END, start_time))
        
    sorted_events = sorted(events, key=functools.cmp_to_key(compare))
    
    res = len(intervals)
    
    active_events = {}
    for time, event_id, event_type, _ in sorted_events:
        if event_type == START:
            active_events[event_id] = time
        if event_type == END:
            curr_start_time = active_events[event_id]
            for event in active_events:
                if event != event_id and curr_start_time >= active_events[event]:
                    res -= 1
                    break
            del active_events[event_id]
    
    return res