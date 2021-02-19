from PIL import Image


class Country:
    def __init__(self, name, color=(0,0,0), isVassal = False):
        self.name = name
        self.file_name = ''
        self.color = color
        self.vassals = []
        self.isVassal = isVassal
        self.overlord = None

    def addVassal(self, vassal):
        if vassal is not None:
            self.vassals.append(vassal)
            vassal.overlord = self
            vassal.isVassal = True

    def getFileName(self):
        if self.file_name == '':
            weirdoDict = listWeirdos()
            if self.name in weirdoDict:
                self.file_name = weirdoDict[self.name]
            else:
                self.file_name = self.name

    def findColor(self):
        self.getFileName()
        countryFile = open(createDirectory()+self.file_name+'.txt')
        for n in range(5):
            line = countryFile.readline()
        line = line.split('{'); line = line[1].split('}')
        line = line[0].strip(); line = line.split()
        self.color = (int(line[0]), int(line[1]), int(line[2]))


def collectCountries():
    countryList = []
    overlord = None
    with open('player_country_list.txt', 'r') as countryFile:
        for line in countryFile:
            line = line.strip()
            if '-' not in line:
                newCountry = Country(line)
                overlord = newCountry
                countryList.append(newCountry)
            elif '-' in line:
                name = line[1:]
                newVassal = Country(name)
                overlord.addVassal(newVassal)
                countryList.append(newVassal)
    for country in countryList:
        country.findColor()
    ocean = Country('ocean', (68, 107, 163))
    uncolonized = Country('uncolonized', (150, 150, 150))
    wasteland = Country('wasteland', (94, 94, 94))
    for feature in [ocean, uncolonized, wasteland]:
        countryList.append(feature)
    return countryList


def listWeirdos():
    weirdoDict = {'game_name':'file_name'}
    with open('weird_names.txt', 'r') as weirdoFile:
        for line in weirdoFile:
            equivalency = line.split(' = ')
            equivalency[1] = equivalency[1].strip()
            weirdoDict[equivalency[0]] = equivalency[1]
    return weirdoDict


def createDirectory():
    file = open('eu4_directory.txt','r')
    eu4Directory = file.readline()
    file.close()
    totalDirectory  = eu4Directory+'\common\countries\\'
    return totalDirectory


def imageLocator():
    useImageFile = raw_input('Use image_names.txt? (y/n): ')
    if useImageFile == 'n':
        inputImage = raw_input('Input image file name: ')
        outputImage = raw_input('Output image file name: ')
    elif useImageFile == 'y':
        with open('image_names.txt', 'r') as file:
            inputImage = file.readline().split(' = ')[1].strip()
            outputImage = file.readline().split(' = ')[1].strip()
    return (inputImage,outputImage)


def getColorList(countryList):
    colorDict = {}
    for country in countryList:
        if country.isVassal:
            colorDict[country.color] = country.overlord.color
        else:
            colorDict[country.color] = country.color
    return colorDict


def changeColors(inputImage):
    im = Image.open(inputImage)
    colorDict = getColorList(collectCountries())
    newImData = []
    for color in im.getdata():
        if color in colorDict:
            newImData.append(colorDict[color])
        else:
            newImData.append((150,150,150))
    newIm = Image.new(im.mode,im.size)
    newIm.putdata(newImData)
    return newIm


def main():
    inputImage, outputImage = imageLocator()
    changeColors(inputImage).save(outputImage)


if __name__ == "__main__":
    main()