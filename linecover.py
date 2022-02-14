from PIL import Image, ImageDraw, ImageFont
import sys
import random

words = []

count = 1
while count < len(sys.argv):
	words.append(sys.argv[count].upper())
	count += 1 
	
coords = []
wordsAm = len(sys.argv) - 1

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alph = list(alph)

font_size = 28

minRand = 0
count = 0
while count < wordsAm:
	protoCoords = []
	minRand = random.randint(minRand, 40)
	protoCoords.append(minRand * font_size)
	protoCoords.append(random.randint(0, 72) * int(font_size / 2))
	
	coords.append(protoCoords)
	
	count += 1

word_bool = False
letter = 0
letterAm = 0

redWord = 0
repAlph = []

while redWord < wordsAm:
	repCount = 0

	img = Image.new("RGB", (1080, 1080), "black")
	pixels = img.load()
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("FreeMono.ttf", font_size)

	count = 0
	i = 0
	while i < 1080:
		j = 0
		while j < 1080:
			if (count < wordsAm and i == coords[count][0] and j == coords[count][1]) or word_bool:
				letterAm = len(words[count])
				if letter < letterAm:
					word_bool = True
					if redWord == count:
						draw.text((j, i), words[count][letter], (255, 0, 0), font)
					else:
						draw.text((j, i), words[count][letter], (255, 255, 255), font)
					letter += 1
				else:
					letter = 0
					j -= int(font_size / 2)
					count += 1
					word_bool = False
			else:
				if redWord == 0:
					thisAlph = random.choice(alph)
					draw.text((j, i), thisAlph, (255, 255, 255), font)
					repAlph.append(thisAlph)
				else:
					draw.text((j, i), repAlph[repCount], (255, 255, 255), font)
					repCount += 1
			j += int(font_size / 2)
		i += font_size

	img.save("linecover" + str(redWord + 1) + ".jpg")
	print("Done " + str(redWord + 1))
	redWord += 1
print("Finished")

 

