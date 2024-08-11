#!/usr/bin/env python3

'''
OPS445 Assignment 2 - Summer 2024
Program: assignment2.py 
The python code in this file is original work written by
Raymond Domingo. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Raymond Domingo
Description: A script that shows the memory usage with a simple bar graph.
'''

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
  return 0

def get_avail_mem() -> int:

  "return total memory that is currently in use"

  # open the meminfo file to accomplish the task!

  f = open('/proc/meminfo', 'r')
  for line in f:
    if line.startswith('MemAvailable:'):
      return int(line.split()[1])
  f.close()

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

  "given a process id, return the Resident memory use "
 
  total_rss = 0
  smaps_path = f'/proc/{proc_id}/smaps'
    
  # for a process, open the smaps file and return the total of each
  f = open(smaps_path, 'r')
  for line in f:
    if line.startswith('Rss'):
      # Sum up all Rss values
      total_rss += int(line.split()[1])                  
  f.close()
  
  if total_rss > 0:
    return total_rss
  else:
    return 0

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

  # if user puts in -H or not
  if args.human_readable:
    total_mem_hr = bytes_to_human_r(total_mem)
    used_mem_hr = bytes_to_human_r(used_mem)
  else:
    total_mem_hr = f'{total_mem}'
    used_mem_hr = f'{used_mem}'

  #if user specifys a program or not
  if args.program:
    pids = pids_of_prog(args.program)
    # One to identify if the program is running is the presence of processes
    # Once tested, we can go either way
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
    '''
    Direct output of the memory usage of the host or a specific program
    the use of :3.0f is a format specifier of the percentage. minimum width of the number is 3. and 0 is the number of 
    decimals. and f is for floating point. THIS MAKES THE PIPES ALLIGN VERTICALLY.
    and % sign at the end for the units.
    a similar format is reused in the earlier part.
    '''
    print(f"Memory         [ {percent_to_graph(percent_used, args.length)} | {percent_used*100:3.0f}% ] {used_mem_hr}/{total_mem_hr}")