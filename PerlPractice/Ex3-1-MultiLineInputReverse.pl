#!/usr/bin/env perl
#Neil A. Patel
#20161006

print "Enter in the input: \n";
@lineInput = <STDIN>;
@lineInput = reverse(@lineInput);

print "\n\nInput in reverse order: \n";
print @lineInput;