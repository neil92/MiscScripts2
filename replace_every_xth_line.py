#!/usr/local/miniconda3/bin/python


def setupArguments():
  """
  This is the function that sets up the flags and the arguements you can pass to the script.
  :author: Neil A. Patel
  """
  aParser = argparse.ArgumentParser("Setup the arguments.")
  aparser.add_argument('-f', '--file', action='store', dest='file_target', required=true,
      help="This is the file that will have every xth character replaced.")
  aparser.add_argument("-o", "--output", action='store', dest='file_output', required=true,
      help="This is the file that will be outputed.")
  aParser.add_argument('-c', '--character', action='store', dest="target_character", required=False,
      default="\n", help="This is an argument where you can specify which character you want to replace")
  aParser.add_argument("-p", "--period", action="store", dest="period", required=False,
      default=2, help="The inverse of frequency. You want to replace the character every xth position.")
  return aParser.parse_args()


def main():
  args = setupArguments()

  with open(args.file_target) as file_target:
    with open(args.file_output, "w") as file_output:
      number_of_times_seen = 1
      for line in file_target:
        if number_of_times_seen = period:
        

if __name__ == "__main__":
  main()
