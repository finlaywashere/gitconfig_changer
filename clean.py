# Importing the regex library
import re

# The regex to search for in the git config file
pattern = "url ="

# The path to the git config file
path = ".git/config"

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
		end = line.find("github.com")
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
