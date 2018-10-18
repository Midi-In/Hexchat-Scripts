# coding=UTF-8
__module_name__ = "Svet"
__module_version__ = "1.0"
__module_description__ = "Midori's svetposting reimplementation for xChat"

import xchat


def stringconvert (inputstr):

	fontdict = [
		{"a": ".XXX.", "b": "XXXX.", "c": ".XXXX", "d": "XXXX.", "e": "XXXXX", "f": "XXXXX", "g": ".XXXX", "h": "X...X", "i": "..X..", "j": "XXXXX", "k": "X...X", "l": "X....", "m": "X...X", "n": "X...X", "o": ".XXX.", "p": "XXXX.", "q": ".XXX.", "r": "XXXX.", "s": ".XXXX", "t": "XXXXX", "u": "X...X", "v": "X...X", "w": "X...X", "x": "X...X", "y": "X...X", "z": "XXXXX", " ": ".....", "~": ".......", "^": "...X..."},
		{"a": "X...X", "b": "X...X", "c": "X....", "d": "X...X", "e": "X....", "f": "X....", "g": "X....", "h": "X...X", "i": "..X..", "j": "....X", "k": "X..X.", "l": "X....", "m": "XX.XX", "n": "XX..X", "o": "X...X", "p": "X...X", "q": "X...X", "r": "X...X", "s": "X....", "t": "..X..", "u": "X...X", "v": "X...X", "w": "X...X", "x": ".X.X.", "y": ".X.X.", "z": "...X.", " ": ".....", "~": ".XX....", "^": "..X.X.."},
		{"a": "XXXXX", "b": "XXXX.", "c": "X....", "d": "X...X", "e": "XXXXX", "f": "XXXXX", "g": "X..XX", "h": "XXXXX", "i": "..X..", "j": "....X", "k": "XXX..", "l": "X....", "m": "X.X.X", "n": "X.X.X", "o": "X...X", "p": "XXXX.", "q": "X.X.X", "r": "XXXX.", "s": ".XXX.", "t": "..X..", "u": "X...X", "v": "X...X", "w": "X.X.X", "x": "..X..", "y": "..X..", "z": "..X..", " ": ".....", "~": "X..X..X", "^": "......."},
		{"a": "X...X", "b": "X...X", "c": "X....", "d": "X...X", "e": "X....", "f": "X....", "g": "X...X", "h": "X...X", "i": "..X..", "j": "X...X", "k": "X..X.", "l": "X....", "m": "X...X", "n": "X..XX", "o": "X...X", "p": "X....", "q": "X..XX", "r": "X..X.", "s": "....X", "t": "..X..", "u": "X...X", "v": ".X.X.", "w": "XX.XX", "x": ".X.X.", "y": "..X..", "z": ".X...", " ": ".....", "~": "....XX.", "^": "......."},
		{"a": "X...X", "b": "XXXX.", "c": ".XXXX", "d": "XXXX.", "e": "XXXXX", "f": "X....", "g": ".XXX.", "h": "X...X", "i": "..X..", "j": ".XXXX", "k": "X...X", "l": "XXXXX", "m": "X...X", "n": "X...X", "o": ".XXX.", "p": "X....", "q": ".XXX.", "r": "X...X", "s": "XXXX.", "t": "..X..", "u": ".XXX.", "v": "..X..", "w": "X...X", "x": "X...X", "y": "..X..", "z": "XXXXX", " ": ".....", "~": ".......", "^": "......."}
		]
	
	convoutput = ["", "", "", "", ""]

	userinput = list(inputstr[1]);
	
	print (userinput);
	
	for x in range(len(userinput)):
			for a in range(len(convoutput)):
				try:
					convoutput[a] += fontdict[a][userinput[x]]
					convoutput[a] += ".";
				except:
					charerr = True
					pass
	
	
	if charerr:
		print ("One or more characters not present in the conversion table")
	else
		pass
		
	return convoutput;
	
	
	
def svetpost (inputstr, colortype):
	
	outtext = stringconvert (inputstr);
	
	if colortype == "1":
		fg = "9,9/"
		bg = "14,14/"
	
	elif colortype == "2":
		fg = "7,7/"
		bg = "1,1/"
	
	elif colortype == "3":
		fg = "2,2/"
		bg = "14,14/"
	
	outtext = [w.replace("X", fg) for w in outtext]
	outtext = [w.replace(".", bg) for w in outtext]
	
	for x in range(len(outtext)):
		xchat.command("say %s" % outtext[x]);
	
	return xchat.EAT_XCHAT;


	
def svetgreen (word, word_eol, userdata):
	svetpost(word_eol, "1");
	return xchat.EAT_XCHAT;

def svetorange (word, word_eol, userdata):
	svetpost(word_eol, "2");
	return xchat.EAT_XCHAT;

def svetblue (word, word_eol, userdata):
	svetpost(word_eol, "3");
	return xchat.EAT_XCHAT;

	
	
xchat.hook_command ("SVET", svetgreen);
xchat.hook_command ("SVETOR", svetorange);
xchat.hook_command ("SVETBL", svetblue);