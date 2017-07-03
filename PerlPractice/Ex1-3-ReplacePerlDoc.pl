#!/usr/bin/env perl

#Supposedly, this goes to through the perldoc
#And replaces all the < and > with something

@lines = `perldoc -u -f atan2`;
foreach (@lines) {
	s/\w<([^>]+)>/\U$1/g;
	print;
}

#Ah, it makes everything within <> in uppercase
#That's probably what the \U is for.

#do: perl -u -f atan2 | cat
#to compare the output