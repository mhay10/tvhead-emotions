#!/bin/bash

# List of predefined expressions with left and right eyes
declare -A expressions=(
	["angry"]="angry-left,angry-right",
	["broken"]="broken,broken",
	["happy"]="happy,happy",
	["love"]="love,love",
	["neutral"]="neutral,neutral",
	["sad"]="sad-left,sad-right",
	["skeptical"]="skeptical,skeptical",
	["surprised"]="surprised,surprised",
	["tired"]="tired,tired"
)

# Process each expression
for expression in "${!expressions[@]}"; do
	# Get left and right eyes
	IFS="," read -r left right <<< "${expressions[$expression]}"

	# Create predefined expression
	echo -n "Creating expression: $expression (left: $left, right: $right) ... "
	python3 create_expression.py "$left" "$right" "$expression"
	echo "Done"
done
