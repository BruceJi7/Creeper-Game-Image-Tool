from PIL import Image
import os

def resizeForGame(sourceImageList, outputImagePath, targetSize=120):
    
    for count, image in enumerate(sourceImageList):

        print(f'Working on image {image}...')
          
        rawImg = Image.open(image)

        origWidth, origHeight = rawImg.size

        if origWidth > origHeight:
            proportion = origWidth / origHeight
        else:
            proportion = origWidth / origHeight
        
        cutWidth = origWidth - 120

        cutHeight = origHeight - int(120 / proportion)
        heightResizedImg = rawImg.resize((origWidth-cutWidth, origHeight-cutHeight))
        imgNum = str(count).zfill(3)

        outputFolder = outputImagePath
        
        os.makedirs(outputFolder, exist_ok=True)

        outputImageName = os.path.join(outputImagePath, f'flash_{imgNum}.png')

        heightResizedImg.save(outputImageName)


sourceFolders = {
    'CO1' : r'C:\Come On, Everyone 1\contents\flashCard\image\b1',
    'CO2' : r'C:\Come On, Everyone 2\contents\flashCard\image\b2',
    'CO3' : r'C:\Come On, Everyone 3\contents\flashCard\image\b3',
    'CO4' : r'C:\Come On, Everyone 4\contents\flashCard\image\b4'
}

unitsList = [f'u{num}' for num in range(1, 9)]

destinationFolders = {
    'CO1' : r'C:\Come On Python Games\resources\CO1',
    'CO2' : r'C:\Come On Python Games\resources\CO2',
    'CO3' : r'C:\Come On Python Games\resources\CO3',
    'CO4' : r'C:\Come On Python Games\resources\CO4',
}

for sourceFolder in sourceFolders.keys():
    for unit in unitsList:
        # Join path to access correct folder
        sourceFolderPath = os.path.join(sourceFolders[sourceFolder], unit)
        destiPath = os.path.join(destinationFolders[sourceFolder], unit)
        # Extract only PNG files and not that fucking thumbs.db file
        allImagesList = [PNGfile for PNGfile in os.listdir(sourceFolderPath) if os.path.splitext(PNGfile)[1] == '.png']
        onlyPicsImagesList = [flashCard for flashCard in allImagesList if '_02' not in str(flashCard) ]
        sourceImagePaths = [os.path.join(sourceFolderPath, imageFile) for imageFile in onlyPicsImagesList]
        print(f'Working on images in {sourceFolderPath}...')
        resizeForGame(sourceImagePaths, destiPath)