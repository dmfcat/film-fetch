# Tape file for generating demo video using VHS
# Run `vhs demo/demo.tape` from root to generate new file

# Config
Output demo/demo.gif
Set Shell "fish"
Set Theme "Catppuccin Frappe"
Set FontSize 14
Set Width 960
Set Height 720

# Run command
Type "uv run film-fetch"
Sleep 1s
Enter
Sleep 1.5s

# Search cast/crew
Type "kurosawa"
Sleep 0.5s
Enter
Sleep 1s

# Confirm selection
Down
Sleep 0.5s
Up
Sleep 0.5s
Enter
Sleep 1s

# Select genres
Space
Sleep 0.5s
Down
Sleep 0.5s
Space
Sleep 0.5s
Enter
Sleep 1s

# Enter year
Enter
Sleep 1s

# Select sort order
Down 4
Sleep 0.5s
Enter

# Output
Sleep 5s
