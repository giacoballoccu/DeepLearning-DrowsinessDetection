import os
import csv
from detect_blinks import *

path = "/media/andrea/Dati2/DLA/Dataset"
detect_blinks = "detect_blinks.py"

print("....Video watching!!")

for video in os.listdir(path):
    N_Blinks = 0

    #Only 0 and 10 videos
    if(video.split(".")[0] != '5'):
        if (video.split(".")[0] == '10'):
            label = 1
        else:
            label = 0

        result_file = detect("/media/andrea/Dati2/DLA/Dataset/blink_detection_demo.mp4")

        with open('resultCSV.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([result_file[0], label, result_file[1]]) #NumeroBLinks, label, ear

        #control ear!!!!!!!!!!!!!!!!!!!!!

