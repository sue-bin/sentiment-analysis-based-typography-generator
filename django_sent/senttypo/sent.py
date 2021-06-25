import os, random
from PIL import Image
from datetime import datetime 



def sentence_to_image(sentence, emotion, save_directory):
    # input example: "abcd efg", emotion: "anger"," save_directory: "src/save_image/

    sentence_image = Image.new('RGBA',(len(sentence)*80, 80), (250,250,250))

    for i in range(len(sentence)):
        if sentence[i] == " ":
            sentence_image.paste(Image.new('RGBA',(80, 80), (250,250,250)),(i*64,0)) 
        else:
            parent_directory = "font/%s/%s/" %(emotion,sentence[i])
            child_directory = ""
            while child_directory.endswith(".png") == False:
                child_directory = random.choice(os.listdir(parent_directory)) #randomly choose font image for the letter
            directory = parent_directory + child_directory
            letter_image = Image.open(directory)
            sentence_image.paste(letter_image,(i*64,0))    

    padding = 10
    entire_image = Image.new('RGBA',(len(sentence)*64+padding*2, 64+padding*2), (250,250,250))
    entire_image.paste(sentence_image, (padding,padding))

    
    save_directory += "output.png"
    entire_image.save(save_directory,"PNG",quality=95)
    
    
    
    return save_directory
