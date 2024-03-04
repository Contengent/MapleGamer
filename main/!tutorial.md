# The Benninigning
#### A little guide to help in the usage of the 'Maple Gamer' bot.

## First thing's first:
- Make sure the routine is a '.csv' file. Python won't read it properly if it's not a csv file.
- Make sure you have all the requirements from `requirements.txt`. Basically just opencv, numpy, and pyautogui.
- Don't add spaces. I haven't yet implemented a way for the bot to read both files using and not using spaces, so just don't use them right now.
- Don't use incorrect types. I haven't implemented an error checker for the user's mistakes yet bro, please don't hack my brain irl. :<
- Fill every space. There also isn't any default options for any function, so you should fill all their variables in.
- Weary of caps. I haven't yet double checked if using capitals will break anything, however you should be fine.
- Getting the right cordinates. There is a menu option to get cordinates. You can copy paste them on like a note, maybe with a label for yourself.
- Don't hold 'down', 'left', or 'right' down before moving. It's untested, but it will most likely break things. Also you have no reason to so just don't. :3

## Keyboard Functions:
`press,'key','presses'` - Self explanitory, it presses a key however many times.
`hold,'key','duration'` - Self explanitory, it holds a key for however long.
`down,'key'` - Starts to hold a key down.
`up,'key'` - Releases a key that is held down. (I think this will crash the program if the key isn't already held down, so... don't do that?)

## Mouse Functions:
`Maybe some day lol`

## Miscellaneous:
`wait,'seconds'` - Pauses the routine for the amount of seconds inputted. (Note: Haven't checked if doubles work)
`move,'x','y'` - Will move the player to given cordinates by using the minimap. (Note: Use this to FINE TUNE your positioning, not to get there :s)
