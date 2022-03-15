import os
import sys

skipConfirmation = False
		
def changenames(sortedfiles, dirpath):
	newnames = []	#names to be changed
	changes = "" #preview for user
	
	#name generation		
	for f in sortedfiles:
		prefix = ""
		if (sortedfiles.index(f) + 1) < 10:
			prefix = "000"
		elif (sortedfiles.index(f) + 1) < 100:
			prefix = "00"
		elif (sortedfiles.index(f) + 1) < 1000:
			prefix = "0"
		
		newname = os.path.join(dirpath, prefix + str(sortedfiles.index(f) + 1) + ".png")
		newnames.append(newname)
		changes = changes + "{} --> {}\n".format(f, newname)

	print(changes)

	if not skipConfirmation:
		test = input("Press enter to continue, or Ctrl + C to quit")

	for i in range(len(sortedfiles)):
		os.rename(sortedfiles[i], newnames[i])

	print("done! (hopefully)")

def main():
	test = input("Welcome to the renaming tool! Press Ctrl + C to quit anytime and cancel changing the filenames (doesn't revert the changed names)\nIt searches the current and its sub-directories recursively and renames all .png files to xxxx.png (ex. 0012). The initial file order is assumed to be alphabetical descending :D\n\nPress Enter to continue...")
	global skipConfirmation
	if len(sys.argv) > 1 and (sys.argv[1] == "y" or sys.argv[1] == "Y" or sys.argv[1] == "yes"):
		skipConfirmation = True

	for root, dirs, files in os.walk(os.curdir):
		for dir in dirs:
			dirpath = (os.path.join(root, dir))
			files = os.listdir(dirpath)

			sortedfiles = []
			#prep
			for file in sorted(files):
				if file.endswith(".png"):
					sortedfiles.append(os.path.join(dirpath, file))
				
			if len(sortedfiles) > 0:		
				print("Found {} .pngs in {}".format(str(len(sortedfiles)), dirpath))
				changenames(sortedfiles, dirpath)
			
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
       	 print('Quitting!')
