import imageio
import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

path = 'C:/Users/LiuSeeker/Desktop/5o-semestre/TermoSol/APS5-TransCal/img/' # on Mac: right click on a folder, hold down option, and click "copy as pathname"

image_folder = os.fsencode(path)

filenames = []

for file in os.listdir(image_folder):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpeg', '.png') ):
        filenames.append(filename)

filenames.sort(key=natural_keys) # this iteration technique has no built in order, so sort the frames

images = list(map(lambda filename: imageio.imread(filename), filenames))
#print(filenames)
os.remove("movie2.gif")
imageio.mimsave(os.path.join('movie2.gif'), images, duration = 0.000001) # modify duration as needed
arqs = os.listdir("C:/Users/LiuSeeker/Desktop/5o-semestre/TermoSol/APS5-TransCal/img/")
for arq in arqs:
	if arq.endswith(".png"):
		os.remove(os.path.join("C:/Users/LiuSeeker/Desktop/5o-semestre/TermoSol/APS5-TransCal/img/", arq))