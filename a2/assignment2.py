#!/usr/bin/env python3

import argparse

import os, sys

def parse_command_args() -> object:

  "Set up argparse here. Call this function inside main."

  parser = argparse.ArgumentParser(description="Memory Visualiser -- See Memory Usage Report with bar charts",epilog="Copyright 2024")

  parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")

  # Make this entry for human-readable. Check the docs to make it a True/False option.

  parser.add_argument("program", type=str, nargs='?', help="if a program is specified, show memory use of all associated processes. Show only total use if not.")

  # Makes a human readable format.
  parser.add_argument("-H", "--human-readable", action="store_true", help="Print sizes in human readable format")

  args = parser.parse_args()

  return args

def percent_to_graph(percent: float, length: int=20) -> str:

  "turns a percent 0.0 - 1.0 into a bar graph"
  if percent < 0.0 or percent > 1.0:
    raise ValueError("Percent must be between 0.0 and 1.0")

  # To determine how many # as an equivalent of the percentage 
  filled_length = int(length * percent)

  # To make it graphical, we will print the percentage of used and percentage of unused.
  # '' graph equivalent of the unused.
  return '#' * filled_length + ' ' * (length - filled_length)

def get_sys_mem() -> int:

  "return total system memory (used or available) in kB"

  # open the meminfo file to accomplish the task!
  try:
    f = open('/proc/meminfo', 'r')
    for line in f:
      if line.startswith('MemTotal:'):
        return int(line.split()[1])
  except FileNotFoundError:
    print("File /proc/meminfo not found.", file=sys.stderr)
  except Exception as e:
    print(f"Error reading total memory: {e}", file=sys.stderr)
  finally:
    f.close()

  raise RuntimeError("Could not find total memory in /proc/meminfo")

def get_avail_mem() -> int:

  "return total memory that is currently in use"

  # open the meminfo file to accomplish the task!

  try:
    with open('/proc/meminfo', 'r') as f:
      for line in f:
        if line.startswith('MemAvailable:'):
          return int(line.split()[1])
  except FileNotFoundError:
        print("File /proc/meminfo not found.", file=sys.stderr)
  except Exception as e:
        print(f"Error reading available memory: {e}", file=sys.stderr)
    
  raise RuntimeError("Could not find available memory in /proc/meminfo")

def pids_of_prog(app_name: str) -> list:

  "given an app name, return all pids associated with app"

  # please use os.popen('pidof <app>') to accomplish the task!

  try:
    pids = os.popen('pidof ' + str(app_name)).read().strip()
    return [pid for pid in pids.split() if pid.isdigit()]
  except Exception as e:
    print("Error getting pids for " + str(app_name) + ": " + str(e), file=sys.stderr)
    return []

def rss_mem_of_pid(proc_id: str) -> int:

  "given a process id, return the Resident memory used"

  # for a process, open the smaps file and return the total of each
  total_rss = 0
  smaps_path = f'/proc/{proc_id}/smaps'
    
  try:
    # Open the smaps file
    with open(smaps_path, 'r') as f:
      for line in f:
        if line.startswith('Rss:'):
          # Sum up all Rss values
          total_rss += int(line.split()[1])
                    
  except FileNotFoundError:
    print(f"Error: The file {smaps_path} does not exist. The process may not be running or accessible.", file=sys.stderr)
  except PermissionError:
    print(f"Error: Permission denied when accessing {smaps_path}.", file=sys.stderr)
  except ValueError as e:
    print(f"Error parsing RSS memory for pid {proc_id}: {e}", file=sys.stderr)
  except Exception as e:
    print(f"Unexpected error reading memory for pid {proc_id}: {e}", file=sys.stderr)
  
  return total_rss if total_rss > 0 else 0

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:

  "turn 1,024 into 1 MiB, for example"

  suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB'] # iB indicates 1024

  suf_count = 0

  result = kibibytes 

  while result > 1024 and suf_count < len(suffixes):

    result /= 1024

    suf_count += 1

  str_result = f'{result:.{decimal_places}f} '

  str_result += suffixes[suf_count]

  return str_result

if __name__ == "__main__":

  args = parse_command_args()

  if not args.program: # not program name is specified.

    pass

  else:

    pass