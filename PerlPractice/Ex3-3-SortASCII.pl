#!/usr/bin/env perl
#Neil A. Patel

print "Enter in a list of Strings: \n";
@lStrings = <STDIN>;

@lStrings = sort(@lStrings);

print "-------------------------------\n";
print "Strings in alphabetical order: \n";
print @lStrings;