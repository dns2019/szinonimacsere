#!/usr/bin/python3.6
# Keszitette: Lajos Denes, Toth Zalan szinonima-szkriptje alapjan.
import sys
import io 
import os
if sys.version_info[0] == 2:
	from Tkinter import *
else:
	from tkinter import *
	from TkinterDnD2 import *

def readin(filename: str):
    with open(filename) as f:
        content = f.read().splitlines()
    return content

def contains(arr, word):
    for i in range(0, len(arr)):
        spltln = arr[i].split("|")
        for x in spltln:
            if(x.__contains__(word)):
                return (True, i)
    return False

def replace(line, word):
	spltln = line.split("|")
	print(spltln)
	for i in spltln:
		if(i != word and i.isdigit() == False and len(i) > 1):
			return i
	return word

            

def drop(event):
	entry_sv.set(event.data)
	path = entry_sv.get()
	print(entry_sv.get())
	with open(path, 'r', encoding='utf8') as file:
		text = file.read()#.replace('\n', '')
	text_list = text.split(' ')
	lines = readin("data.dat")
	for x in range(0,len(text_list),2):
		if text_list[x]!=' ' and text_list[x] != '.' and text_list[x] != '?' and text_list[x] != '!' and text_list[x] != ',':
			print(text_list[x])
			word = text_list[x]
			cnt = contains(lines,word)
			print(cnt)
			if cnt:
				print(replace(lines[cnt[1]],word))
				text_list[x] = replace(lines[cnt[1]],word)
	new_text_list = " ".join(text_list)
	print(new_text_list)
	#Ha nem kell fajlba kiirna, akkor ezt lehet torolni.
	filename = os.path.dirname(path)
	filename += "/kimenet.txt"
	with io.open(filename,'w',encoding='utf8') as f:
    		f.write(new_text_list)
	print(filename)

root = TkinterDnD.Tk()
root.winfo_toplevel().title("Auto-Szinoníma")
entry_sv = StringVar()
entry_sv.set('Dobd csak ide azt a fájlt: ...')
entry = Entry(root, textvar=entry_sv, width=80)
entry.pack(fill=X, padx=10, pady=10)
entry.drop_target_register(DND_FILES)
entry.dnd_bind('<<Drop>>', drop)
root.mainloop()
