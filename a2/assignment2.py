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
  f = open('/proc/meminfo', 'r')
  for line in f:
    if line.startswith('MemTotal:'):
      return int(line.split()[1])
  f.close()

  raise RuntimeError("Could not find total memory in /proc/meminfo")

def get_avail_mem() -> int:

  "return total memory that is currently in use"

  # open the meminfo file to accomplish the task!

  f = open('/proc/meminfo', 'r')
  for line in f:
    if line.startswith('MemAvailable:'):
      return int(line.split()[1])

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
    

  # Open the smaps file
  f = open(smaps_path, 'r')
  for line in f:
    if line.startswith('Rss:'):
      # Sum up all Rss values
      total_rss += int(line.split()[1])                  
  f.close()
    
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

  total_mem = get_sys_mem()
  available_mem = get_avail_mem()
  used_mem = total_mem - available_mem
  percent_used = used_mem / total_mem


  if args.human_readable:
    total_mem_hr = bytes_to_human_r(total_mem)
    used_mem_hr = bytes_to_human_r(used_mem)
  else:
    total_mem_hr = f'{total_mem}'
    used_mem_hr = f'{used_mem}'

  if args.program:
    pids = pids_of_prog(args.program)
    if not pids:
      print(f"{args.program} not found.")
    else:
      for pid in pids:
        mem = rss_mem_of_pid(pid)
        percent_pid = mem / total_mem
        if args.human_readable:
          mem_hr = bytes_to_human_r(mem)
        else:
          mem_hr = f'{mem}'
        print(f"{pid: <15} [ {percent_to_graph(percent_pid, args.length)} | {percent_pid*100:3.0f}% ] {mem_hr}/{total_mem_hr}")
      total_program_mem = sum(rss_mem_of_pid(pid) for pid in pids)
      percent_program = total_program_mem / total_mem
      if args.human_readable:
        total_program_mem_hr = bytes_to_human_r(total_program_mem)
      else:
        total_program_mem_hr = f'{total_program_mem}'
      print(f"{args.program: <15} [ {percent_to_graph(percent_program, args.length)} | {percent_program*100:3.0f}% ] {total_program_mem_hr}/{total_mem_hr}")
  else:
    print(f"Memory         [ {percent_to_graph(percent_used, args.length)} | {percent_used*100:3.0f}% ] {used_mem_hr}/{total_mem_hr}")