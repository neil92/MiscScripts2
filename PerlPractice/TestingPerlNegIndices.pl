#!/usr/bin/env perl
#Neil A. Patel
#2016-10-01

@itsArray = qw(6 7 8 9);

print "itsArray\n";
print @itsArray;
print "\n" . '$itsArray[2]:' . "\n";
print $itsArray[2];
print "\n" . '$itsArray[-1]:' . "\n";
print $itsArray[-1];
print "\n" . '$itsArray[-5]:' . "\n";
print $itsArray[-5];
if  ($itsArray[-5] == undef) {
	#Apparently, unallocated RAM is undef
	print "undef";
}

$itsArray[-5] = 11; #This crashes your program. Thank god the interpreter catches
#it otherwise that could be bad if it overwrote unallocated RAM

print "\n";