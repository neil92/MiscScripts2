#!/usr/bin/env perl
#Neil A. Patel

@names = qw (fred betty barney dino wilma pebbles bamm-bamm);


print "Enter in a list of numbers: \n";
@indexOfNames = <STDIN>;

print "List of names: \n";
foreach $iName (@indexOfNames) {
	print $names[$iName-1] . " ";
}

print "\n";