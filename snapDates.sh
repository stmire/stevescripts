#!/bin/bash
# Run this in the hidden .zfs/snapshot directory to see which snapshots correspond to which dates

# Clear the terminal
clear

# Set color code
BLUE=$'\e[1;34m'
END=$'\e[0m'

# Ensure that you are working in the correct directory (WIP)
#pwd=$(pwd)
#if [ $pwd != *".zfs/snapshot"* ]; then
#	echo "You need to be in the hidden snapshot directory!"
#	exit
#fi

# Store all directories (ls) into an array
directories=($(ls))

# Step through the array and list out the epoch and converted date
for i in "${directories[@]}"
do
	date=$(date -d @$i)
	echo "$i --> $date"
done

# Print end message
printf "\n${BLUE}All done!${END}\n"
