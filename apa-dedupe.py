from Tkinter import Tk
from tkFileDialog import askopenfilename
import os.path
import difflib
import re

Tk().withdraw()
print("Select text file: ")
filename = askopenfilename()
lines = []


with open(filename) as f:
    outfilename = os.path.splitext(filename)[0] + "_edited"+os.path.splitext(filename)[1]
    dupefilename = os.path.splitext(filename)[0] + "_discarded"+os.path.splitext(filename)[1]
    open(outfilename, 'w').close()
    open(dupefilename, 'w').close()
    with open(outfilename, 'w') as fo:
        with open(dupefilename, 'w') as df:
            for line in f:
                if len(lines) == 0:
                    lines += [line]
                else:
                    try:
                        title = re.split("[0-9]{4}",line.lower())[1]
                        pattern = re.compile("[0-9]{4}")
                        year = pattern.search(line).group()
                        for i in range(len(lines)):
                            tempLine = lines[len(lines)-i-1]
                            tempYear = pattern.search(tempLine).group()
                            if year == tempYear:
                                tempTitle = re.split("[0-9]{4}",tempLine.lower())[1]
                                rat = difflib.SequenceMatcher(None, title, tempTitle).ratio()
                                if rat > .6:
                                    print "Found similarities between:\n"+tempLine+"and \n"+line
                                    df.write(str(rat)+"\n")
                                    df.write(line)
                                    df.write(tempLine)
                                    break
                        else:
                            fo.write(line)
                        lines += [line]
                    except (IndexError, AttributeError) as e:
                        pass
                lines = lines[-30:]
