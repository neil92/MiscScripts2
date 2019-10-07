#!/usr/local/miniconda3/bin/python


import argparse


def parse_file(irregular_file, output_file, delimiter, number_of_fields):
  total_lines = 0
  removed_lines = 0

  with open(irregular_file, "r") as irregular_file_object, open(output_file, "w") as output_file_object:
    line = irregular_file_object.readline()
    while line:
      total_lines = total_lines + 1
      line = line.strip()
      split_line = line.split(sep=delimiter)
      
      if (total_lines == 3):
        print("Number of fields: {}".format(len(split_line)))

      if (len(split_line) == number_of_fields):
        output_file_object.write(line)
      else:
        removed_lines = removed_lines + 1
      line = irregular_file_object.readline()

  return (total_lines, removed_lines)


def setup_arguments():
  """
  This is the function that sets up the flags and the arguements you can pass to the script.
  :author: Neil A. Patel
  """
  a_parser = argparse.ArgumentParser("Get's the arguments for the parse irregular file tool.")
  a_parser.add_argument("-f", "--file", action="store", dest="file_input_data", required=True,
      help="Please supply a file that has an irregular number of fields per line that you want to filter.")
  a_parser.add_argument("-n", "--number_fields", action="store", dest="number_fields", required=False, default=1,
      type=int, help="The number of fields per line (i.e. number of delimiters + 1).")
  a_parser.add_argument("-o", "--output_file", action="store", dest="output_file", required=False, 
      default="output_file.txt", help="The output file that the filtered file goes into.")
  a_parser.add_argument("-d", "--delimiter", action="store", dest="delimiter", required=False, default="\t",
      help="The character used to seperate the fields in the line.")
  return a_parser.parse_args()


def main():
  args = setup_arguments()
  total_lines, removed_lines = parse_file(args.file_input_data, args.output_file, args.delimiter, args.number_fields)
  print("The total number of lines processed: {}".format(total_lines))
  print("The total number removed lines: {}".format(removed_lines))


if __name__ == "__main__":
  main()
