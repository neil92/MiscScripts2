#!/usr/bin/env perl

$radius = <STDIN>;
$circumference = $radius * 2 * 3.141592654;

if ($circumference <= 0) {
	print "The circumference of the circle you entered was 0\n";
} else {
	print "The circumference of the circle you entered was $circumference\n";
}
