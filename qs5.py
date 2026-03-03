# List is mutable
playlist = ["song1", "song2", "song3"]
playlist[0] = "new_song"
print(playlist)

# String is immutable
title = "book"
# title[0] = "B"   # This would give an error because strings cannot be changed by index
title = "Book"     # This creates a new string instead
print(title)