#!/usr/local/miniconda3/bin/python


import pandas as pd
import argparse
import re

def parse_ps_file(ps_file):
  REGEXP_ATLEAST_ONE_SPACE = " +"
  re_one_space_compiled = re.compile(REGEXP_ATLEAST_ONE_SPACE)
  BASH_COMMAND_FIELD_POSITION = 10
  PS_COLUMN_NAMES = ["USER", "PID", "%CPU", "%MEM", "VSZ", "RSS", "TTY", "STAT", "START", "TIME", "COMMAND"]
  df_ps_data = pd.DataFrame(data=[], columns=PS_COLUMN_NAMES)
  
  with open(ps_file, "r") as ps_file_object:
    line = ps_file_object.readline()
    while line:
      line = line.strip()
      split_line = re_one_space_compiled.split(line, maxsplit=BASH_COMMAND_FIELD_POSITION)
      df_line = pd.DataFrame(data=[split_line], columns=PS_COLUMN_NAMES)
      df_ps_data = df_ps_data.append(df_line, ignore_index=True)
      line = ps_file_object.readline()

  for column in ["%CPU", "%MEM", "VSZ", "RSS"]:
    df_ps_data.loc[:, column] = pd.to_numeric(df_ps_data.loc[:, column])
  
  return df_ps_data


def setup_arguments():
  """
  This is the function that sets up the flags and the arguements you can pass to the script.
  :author: Neil A. Patel
  """
  a_parser = argparse.ArgumentParser("Get's the arguments for the comutation_plot tool.")
  a_parser.add_argument('-f', '--file', action='store', dest='file_input_data', required=True,
      help='Please supply a fixed-width file outputed from ps ux.')
  return a_parser.parse_args()


def main():
  args = setup_arguments()

  df_ps_data = parse_ps_file(args.file_input_data)
  # df_ps_data = pd.read_csv(args.file_input_data, sep=REGEXP_ATLEAST_ONE_SPACE, engine="python", header=None)
  cpu_usage_data = df_ps_data.loc[:, "%CPU"]
  virtual_ram_data = df_ps_data.loc[:, "VSZ"]
  reserved_ram_data = df_ps_data.loc[:, "RSS"]

  max_cpu_usage = max(cpu_usage_data)
  max_virtual = max(virtual_ram_data)
  max_reserved = max(reserved_ram_data)

  used_cores = float(max_cpu_usage) / 100.0
  used_virtual = float(max_virtual) / 1000.0**2
  used_reserved = float(max_reserved) / 1000.0**2

  with_buffer_cores = used_cores * 1.2
  with_buffer_virtual = used_virtual * 1.2
  with_buffer_reserved = used_reserved * 1.2

  summary_usage_data = [[max_cpu_usage, max_virtual, max_reserved],
      [used_cores, used_virtual, used_reserved],
      [with_buffer_cores, with_buffer_virtual, with_buffer_reserved]]
  df_summary_usage = pd.DataFrame(summary_usage_data, columns=["CPU", "Virtual RAM", "Reserved RAM"],
      index=["Max", "Cores or GB", "With Buffer"])
  pd.set_option('display.float_format', lambda x: '%.2f' % x)
  print(df_summary_usage.to_string())


if __name__ == '__main__':
  main()

