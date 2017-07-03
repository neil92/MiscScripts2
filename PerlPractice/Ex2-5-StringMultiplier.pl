#!/usr/bin/env perl

print "Enter in a string: ";
$favString = <STDIN>;
print "Enter in the number of times to multiply: ";
$factor = <STDIN>;

print "OUTPUT: \n";
print $favString x $factor;