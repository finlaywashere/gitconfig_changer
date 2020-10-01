# Importing the regex module to search strings
import re

# Importing the os module to handle file io
import os

# Importing the sys module to get cli arguments
import sys

# Check if the user passed a path to the directory where the git repos have been downloaded to
if len(sys.argv) != 2:
	# Tell the user what to enter
	print("Expected path to directory containing git repos but found none!")
	# Exit because theres nothing we can do right now
	exit(1)

# The path to the folder where all the git repos can be found
folderPath = sys.argv[1]

# The regex to search for in the git config file
pattern = "url ="

# The list of git repos
repoDirs = os.listdir(folderPath)

for repo in repoDirs:
	
	# The full path to where the git repo can be found
	repoPath = os.path.join(folderPath,repo)
	
	# Check if it is a file, if it is then its not a git repo
	if os.path.isfile(repoPath):
		# Its not a folder so skip to the next one
		continue
	
	# The path to the git config file
	path = os.path.join(repoPath,".git/config")
	
	# Check if the git config file exists
	if not os.path.exists(path):
		# The config file doesn't exist so it must be some other folder
		# Tell the user what has/hasn't been found
		print("Found non git folder at "+repoPath)
		# Skip to the next item because this one is not a git repo
		continue
	
	# Tell the user what was found
	print("Found git repo at "+repoPath)

	# A string to store the new file's contents
	fileContents = ""

	# Open the git config file for reading
	file = open(path, "r")
	# Iterate over every line
	for line in file:
		# Check if the line matches the regex for the url entry
		if re.search(pattern,line):
			# Line located
			# Get the first occurence of https:// then add 8 to its index because its length is 8 and we want the end
			start = line.find("https://")+8
			# If something is wrong and we can't find https:// in the line, then continue to the next line
			if start == -1:
				# Skip to the next line because this one isn't it
				continue
			# Find where the github.com string is so we know where to actually start keeping text
			end = line.find("github.com")
			# If something is wrong and we can't find github.com in the line then go to the next line
			if end == -1:
				# Go to the next line and check again
				continue
			# Now make the new string which is everything up to the https:// and everything after github.com including github.com
			newLine = line[:start]+line[end:]
			# Add the new line to the files new contents string
			fileContents += newLine
		else:
			# Add the old line to the files new contents string
			fileContents += line

	# Close the file, delete it, and reopen it for writing
	file.close()
	
	# Open the git config again for writing
	# Note that using file.write will overwrite the contents so we don't have to delete it
	file = open(path,"w")

	# Write the new contents to the file, overwriting the old file
	file.write(fileContents);

	# Close the file so its saved
	file.close()

