#!/usr/bin/python3

import argparse
import csv
from random import randint
import sys

def fifo_routine(dataframe):
    """
    input: dataframe -- dictionary of process information
    output: total_time
    """
    if len(dataframe) == 0:
        return 0

    clock = 0
    for process in dataframe:
        clock = max(clock, process['start'])
        print("[SCHED] %ds: Executing %s for a duration of %ds" % (
            clock, process['name'], process['duration']
        ))
        clock += process['duration']

    return clock

def random_routine(dataframe):
    """
    input: dataframe -- dictionary of process information
    output: total_time
    """
    if len(dataframe) == 0:
        return 0

    notarrived_pool = dataframe
    waiting_pool = []
    clock = 0
    
    while len(notarrived_pool) != 0 or len(waiting_pool) != 0:
        if len(waiting_pool) == 0:
            clock = max(clock, notarrived_pool[0]['start'])

        while True:
            if len(notarrived_pool) == 0 or notarrived_pool[0]['start'] > clock:
                break
            waiting_pool.append(notarrived_pool.pop(0))

        idx = randint(0, len(waiting_pool) - 1)
        process = waiting_pool.pop(idx)

        print("[SCHED] %ds: Executing %s for a duration of %ds" % (
            clock, process['name'], process['duration']
        ))
        clock += process['duration']

    return clock

def priority_fifo_routine(dataframe):
    """
    input: dataframe -- dictionary of process information
    output: total_time
    """
    if len(dataframe) == 0:
        return 0

    notarrived_pool = dataframe
    waiting_pool = []
    clock = 0

    while len(notarrived_pool) != 0 or len(waiting_pool) != 0:
        if len(waiting_pool) == 0:
            clock = max(clock, notarrived_pool[0]['start'])

        while True:
            if len(notarrived_pool) == 0 or notarrived_pool[0]['start'] > clock:
                break
            waiting_pool.append(notarrived_pool.pop(0))

        waiting_pool.sort(key=lambda x: (x['priority'], x['start']))
        process = waiting_pool.pop(0)

        print("[SCHED] %ds: Executing %s for a duration of %ds" % (
            clock, process['name'], process['duration']
        ))
        clock += process['duration']

    return clock

def round_robin_routine(dataframe):
    """
    input: dataframe -- dictionary of process information
    output: total_time
    """
    if len(dataframe) == 0:
        return 0;

    notarrived_pool = dataframe
    waiting_pool = []
    clock = 0
    quantum = 2
    process = None

    while len(notarrived_pool) != 0 or len(waiting_pool) != 0 or process is not None:
        if len(waiting_pool) == 0:
            clock = max(clock, notarrived_pool[0]['start'])

        while True:
            if len(notarrived_pool) == 0 or notarrived_pool[0]['start'] > clock:
                break
            waiting_pool.append(notarrived_pool.pop(0))

        if process is not None:
            waiting_pool.append(process)

        process = waiting_pool.pop(0)
        current_duration = min(quantum, process['duration'])

        print("[SCHED] %ds: Executing %s for a duration of %ds" % (
            clock, process['name'], current_duration
        ))
        clock += current_duration

        process['duration'] -= current_duration
        if process['duration'] == 0:
            process = None

    return clock

def supra_optimal_routine(dataframe):
    if len(dataframe) == 0:
        return ''

    notarrived_pool = dataframe
    waiting_pool = []
    clock = 0
    quantum = 2
    process = None

    result = ''

    while len(notarrived_pool) != 0 or len(waiting_pool) != 0:
        if len(waiting_pool) == 0:
            while clock < notarrived_pool[0]['start']:
                result += ' '
                clock += 1

        while True:
            if len(notarrived_pool) == 0 or notarrived_pool[0]['start'] > clock:
                break
            waiting_pool.append(notarrived_pool.pop(0))

        waiting_pool.sort(key=lambda x: (x['priority'], x['duration'], x['start']))
        process = waiting_pool.pop(0)
        current_duration = min(quantum, process['duration'])

        for _ in range(current_duration):
            result += process['name']

        clock += current_duration
        process['duration'] -= current_duration
        if process['duration'] == 0:
            process = None
        else:
            waiting_pool.append(process)
            process = None

    return result

# DO NOT MODIFY THE PART BELOW

if __name__ == '__main__':
    NAME_TO_FUNC = {
        "fifo": fifo_routine,
        "random": random_routine,
        "priority": priority_fifo_routine,
        "quantum": round_robin_routine,
    }

    # Command line parsing, execute `./scheduler.py -h` for more information
    AP = argparse.ArgumentParser()
    AP.add_argument('algo', help='algorithm to use',
                    choices=NAME_TO_FUNC.keys())
    AP.add_argument('input', help='input file, in csv format')
    args = AP.parse_args(sys.argv[1::])

    process_list = []

    # Input file parsing
    with open(args.input, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        # Each row is composed of 4 columns:
        # process name, start time, duration time and priority (lower is better)
        for row in reader:
            if row[0][0] == '#':
                continue
            # You can access to the start field of the 2nd item using:
            # process_list[1]['start']
            process_list.append({
                'name': row[0],
                'start': int(row[1]),
                'duration': int(row[2]),
                'priority': int(row[3]),
            })

    # Sort the list by start time
    process_list.sort(key=lambda x: x['start'])

    # Call the scheduling routine
    clock = NAME_TO_FUNC[args.algo](process_list)

    print("Total time for the given execution: %ds" % (clock))
