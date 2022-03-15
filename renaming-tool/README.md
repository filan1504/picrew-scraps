# renaming tool!

renames *all* .png files in its own and its subdirectories ascendingly fom "00001", so that uploading images to picrew can be made easier ^^

## usage

run `python3 renamer.py` in the terminal/shell/cmd to see all filenames, and teh changes that will be made. quit with ctrl + c anytime, but the changes already made will be saved
 
to not see the agreement prompts and just rename all files recursively run `python3 renamer.py y`

the assumption is that your repository looks something like this: 

```
main-folder/
├─ renamer.py
├─ body-shapes/
│  ├─ variant1/
│  │  ├─ basic body.png
│  │  ├─ round body.png
│  │  ├─ lanky body.png
│  ├─ variant2/
│  │  ├─ round body two.png
│  │  ├─ lank body2.png
│  ├─ shapes-reference.png
│  ├─ inspo-collage.png
├─ hair/
│  ├─ black/
│  │  ├─ bangs1.png
│  │  ├─ curly.png
│  ├─ brown/
│  │  ├─ brownbangs.png
│  │  ├─ curly.png
│  ├─ blonde/
│  │  ├─ bangs blonde 1.png
│  ├─ hair ideas.txt
│  ├─ all hair.psd

```
 after navigating to the main-folder and running `python3 renamer.py y` the filenames will have changed to

```

```

as you can see the tool renamed all .png files (even the ones that the user would not necessarily want renamed like "inspo-collage.png and shapes.reference.png")
in the body-shapes/variant1 folder "round body.png" go changed inti "0003.png" which makes sense - alphabethically it is the third in order. but the file with the same name in the folder variant2 got the name "0002.png", becaue there were only two items in that directory. so to have properly corresponding files for layers or for color alternatives to upload, i'd recommend having an empty transparent .png as to not bring the files out of order/aligment :)
