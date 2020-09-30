# gitconfig changer - A cli tool to do bulk git config changes to fix issues with Github Classroom

Github Classroom puts unwanted tokens in front of repository urls and it breaks stuff, these scripts undo that

`clean.py` can be run with `python clean.py` and will update a single config file that must be at `.git/config` relative to where the script is run from.

`clean_v2.py` can be run with `python clean_v2.py <path>` and will update every git config file that it can find in git repos that are contained in the folder designated by `path`.

