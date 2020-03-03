import cv2
import numpy as np
import os
import sys
from moviepy.editor import *


if len(sys.argv) > 1:
    param = sys.argv[1]

    #audio_output = sys.argv[3]

    if (param == "--getframes"):
        video = sys.argv[2]
        cap = cv2.VideoCapture(video)

        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except (OSError):
            print("Error: Can't create directory")

        currentFrame = 0
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Saves image of the current frame in jpg file (Change here if you want other format)
            name = './data/' + str(currentFrame) + '.jpg'
            print('Creating...' + name)

            # Stop taking frames when its over
            if ret == False:
                break

            # Create image in the directory
            cv2.imwrite(name, frame)
            currentFrame += 1

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()

    elif (param == "--getaudio"):
        video = sys.argv[2]
        try:
            def get_audio(video_file):
                video = VideoFileClip(video_file)  # 2.
                audio = video.audio  # 3.
                audio.write_audiofile('stripped_audio.mp3')  # 4.
            get_audio(video)
        except (AttributeError):
            print("It only works with .mp4 files, try to convert it first")
        except (OSError):
            print("File not found, Try again")

    elif (param == "--frame2video"):
        path = sys.argv[2] + "/"
        param_sec = sys.argv[3]
        fps = sys.argv[4]

        if (param_sec == "--fps" and fps != None):
            # choose codec according to format needed
            frames = float(fps)
            image_shape = cv2.imread(path + "0"+".jpg")
            w, h, c = image_shape.shape
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            video = cv2.VideoWriter('JoinedVideo.mp4', fourcc, frames, (h, w))
            i = 0
            try:
                while(True):
                    img = cv2.imread(path + str(i)+".jpg")
                    flag = img.shape  # When there isn't more images to join to the video it will originate and error and will end th program
                    print("Joining frame"+str(i)+" to video")
                    video.write(img)
                    i += 1
            except AttributeError:
                print("No more frames to join")

            cv2.destroyAllWindows()
            video.release()

    elif (param == "--video+audio"):
        video_path = input("Put the path of the video:")
        audio_path = input("Put the path of the audio:")
        output = input(
            "Put the name of the file that you pretend after merging:")

        def concatenate_video_audio(video, audio, output_filename):
            videoclip = VideoFileClip(video)
            audioclip = AudioFileClip(audio)
            finalclip = videoclip.set_audio(audioclip)
            finalclip.write_videofile(output_filename, codec='libx264')

        concatenate_video_audio(video_path, audio_path, output)

    elif(param == "--help"):
        print("--getframes To get video frames")
        print("--getaudio To get the audio of a video")
        print("--frame2video To join the frames and make a video")
        print("--video+audio to join a video and an audio")

    elif(param == "--examples"):
        print("python3 Video_Tools.py --getframes teste.mp4")
        print("python3 Video_Tools.py --getaudio teste.mp4")
        print("python3 Video_Tools.py --frame2video data --fps [any number]")
        print("teste.mp4 being te any video, and data de folder containing de frames")
