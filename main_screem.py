import time
from datetime import datetime
import tkinter as tk
from PIL import ImageTk, Image
import cv2
import tkinter as tk
import music_control
import speed_detection
from tracker import Tracker
import numpy as np


class MainWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.newMaster = master
        self.master = master
        self.grid()

        myimage = tk.PhotoImage(file='dance.gif')
        label1 = tk.Label(image=myimage)
        label1.image = myimage  # the reference
        label1.grid(row = 0, column = 1)

        self.lmain1 = tk.Label(self, text="hi")
        self.lmain1.grid(row = 0, column = 0)



        music_control.play_music('mysong.mp3')
        # todo setvolume 0.1]\4/
        music_control.set_volume_start(0)

        self.flag = False
        self.counter = 150
        self.cap = cv2.VideoCapture(0)
        self.video_stream()



    def video_stream(self):
        _, frame1 = self.cap.read()
        speed_detection.speed_detection(frame1)
        cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        img1 = Image.fromarray(cv2image1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        self.lmain1.imgtk = imgtk1
        self.lmain1.configure(image=imgtk1)

        self.flag = self.music_on()
        if self.flag:
            self.lmain1.after(1, self.video_stream)
        else:
            print("finish")
            self.cap1 = cv2.VideoCapture('videoplayback.mp4')
            self.video_stream1()

    def video_stream1(self):
        print("here")
        _, frame1 = self.cap1.read()
        cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
        img1 = Image.fromarray(cv2image1)
        imgtk1 = ImageTk.PhotoImage(image=img1)
        self.lmain1.imgtk = imgtk1
        self.lmain1.configure(image=imgtk1)
        self.flag = self.continue_movie()
        if self.flag:
            self.lmain1.after(1, self.video_stream)
        else:
            print("finish")
            self.cap1.release()
            # cv2.destroyAllWindows()
            # self.master = None
            #conclusion = Conclusion(self.newMaster, speed=[23, 54, 6, 88, 34, 32, 5, 7], volume=[4, 33, 8,2,67,98,46,3])

    def continue_movie(self):
        if self.counter == 0:
            return True
        self.counter -= 1

    def music_on(self):
        return music_control.get_busy()

    # def detect_speed(self):
    #     print("detect speed")
    #     FPS = 30
    #     '''
    #         Distance to line in road: ~0.025 miles
    #     '''
    #     ROAD_DIST_MILES = 0.0025
    #
    #     '''
    #         Speed limit of urban freeways in California (50-65 MPH)
    #     '''
    #     # ToDo small the param
    #     HIGHWAY_SPEED_LIMIT = 40
    #
    #     # Initial background subtractor and text font
    #     fgbg = cv2.createBackgroundSubtractorMOG2()
    #     font = cv2.FONT_HERSHEY_PLAIN
    #
    #     centers = []
    #     # y-cooridinate for speed detection line
    #     Y_THRESH = 242
    #
    #     blob_min_width_far = 6
    #     blob_min_height_far = 6
    #
    #     blob_min_width_near = 18
    #     blob_min_height_near = 18
    #
    #     frame_start_time = None
    #
    #     # Create object tracker
    #     tracker = Tracker(80, 3, 2, 1)
    #
    #     # Capture livestream
    #
    #
    #     # todo playMusic
    #     music_control.play_music('mysong.mp3')
    #     # todo setvolume 0.1]\4/
    #     music_control.set_volume_start(0)
    #     All_mph_list = []
    #
    #     while True:
    #         if not music_control.get_busy():
    #             print(All_mph_list)
    #             # conclusion(All_mph_list)
    #             break
    #
    #         centers = []
    #         frame_start_time = datetime.utcnow()
    #         ret, frame = self.cap.read()
    #
    #
    #         #  Draw line used for speed detection
    #         cv2.line(frame, (0, Y_THRESH), (640, Y_THRESH), (255, 0, 0), 2)
    #
    #         # Convert frame to grayscale and perform background subtraction
    #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #         fgmask = fgbg.apply(gray)
    #
    #         # Perform some Morphological operations to remove noise
    #         kernel = np.ones((4, 4), np.uint8)
    #         kernel_dilate = np.ones((5, 5), np.uint8)
    #         opening = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    #         dilation = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel_dilate)
    #
    #         # todo
    #         _, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #         if len(contours) < 2:
    #             music_control.set_volume(0)
    #         else:
    #             # Find centers of all detected objects
    #             for cnt in contours:
    #                 x, y, w, h = cv2.boundingRect(cnt)
    #
    #                 if y > Y_THRESH:
    #                     if w >= blob_min_width_near and h >= blob_min_height_near:
    #                         center = np.array([[x + w / 2], [y + h / 2]])
    #                         centers.append(np.round(center))
    #
    #                         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #                 else:
    #                     if w >= blob_min_width_far and h >= blob_min_height_far:
    #                         center = np.array([[x + w / 2], [y + h / 2]])
    #                         centers.append(np.round(center))
    #
    #                         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #
    #             if centers:
    #                 tracker.update(centers)
    #
    #                 mph = 0
    #                 counter = 0
    #                 mph_list = []
    #
    #                 for vehicle in tracker.tracks:
    #                     print(len(vehicle.trace))
    #                     if len(vehicle.trace) > 1:
    #                         for j in range(len(vehicle.trace) - 1):
    #                             # Draw trace line
    #                             x1 = vehicle.trace[j][0][0]
    #                             y1 = vehicle.trace[j][1][0]
    #                             x2 = vehicle.trace[j + 1][0][0]
    #                             y2 = vehicle.trace[j + 1][1][0]
    #
    #                             cv2.line(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 255), 2)
    #
    #                         try:
    #                             '''
    #                                 TODO: account for load lag
    #                             '''
    #
    #                             trace_i = len(vehicle.trace) - 1
    #
    #                             trace_x = vehicle.trace[trace_i][0][0]
    #                             trace_y = vehicle.trace[trace_i][1][0]
    #
    #                             # Check if tracked object has reached the speed detection line
    #                             # if trace_y <= Y_THRESH + 25 and trace_y >= Y_THRESH - 25:
    #                             if True:
    #                                 # cv2.putText(frame, 'I PASSED!', (int(trace_x), int(trace_y)), font, 1, (0, 255, 255), 1,
    #                                 #             cv2.LINE_AA)
    #                                 # vehicle.passed = True
    #
    #                                 load_lag = (datetime.utcnow() - frame_start_time).total_seconds()
    #
    #                                 time_dur = (datetime.utcnow() - vehicle.start_time).total_seconds() - load_lag
    #                                 time_dur /= 60
    #                                 time_dur /= 60
    #
    #                                 vehicle.mph = ROAD_DIST_MILES / time_dur
    #                                 print("===mph==========")
    #                                 print(vehicle.mph)
    #
    #                                 mph_list.append(vehicle.mph)
    #
    #                                 # If calculated speed exceeds speed limit, save an image of speeding car
    #                             if vehicle.mph > HIGHWAY_SPEED_LIMIT:
    #                                 mph += int(vehicle.mph)
    #                             counter += 1
    #
    #                             # if vehicle.passed:
    #                             #     mph += int(vehicle.mph)
    #                             #     counter += 1
    #
    #                         except:
    #                             pass
    #
    #                 # todo setvolume
    #                 if counter == 0 or is_one_not_dance(mph_list) or mph / counter < 50:
    #
    #                     music_control.set_volume(0)
    #                     avg = 0
    #                 else:
    #                     avg = mph / counter
    #                     print("==========avg==============")
    #                     print(avg)
    #                     calaulate_volum(avg)
    #
    #                 All_mph_list.append((avg, music_control.get_volume()))
    #
    #                 # music_control.set_volume(avg/100)
    #                 # print(avg)
    #
    #         # Display all images
    #
    #         cv2image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    #         img1 = Image.fromarray(cv2image1)
    #         imgtk1 = ImageTk.PhotoImage(image=img1)
    #         self.lmain1.imgtk = imgtk1
    #         self.lmain1.configure(image=imgtk1)
    #
    #         # cv2.imshow('original', frame)
    #         # cv2.imshow('opening/dilation', dilation)
    #         # cv2.imshow('background subtraction', fgmask)
    #
    #         # Quit when escape key pressed
    #         if cv2.waitKey(5) == 27:
    #             break
    #
    #         # Sleep to keep video speed consistent
    #         time.sleep(1.0 / FPS)

def is_one_not_dance(mp_list):
    pass

def conclusion(list_of_mph):
    pass


def calaulate_volum(avg):
     print("========vol=================")

     if avg > 500:
         music_control.set_volume(1)
         print('1')
     elif avg <= 500 and avg > 400:
         print('0.1')
         music_control.set_volume(0.9)
     elif avg <= 400 and avg > 320:
         music_control.set_volume(0.8)
         print('0.8')
     elif avg <= 320 and avg > 250:
         music_control.set_volume(0.7)
         print('0.7')
     elif avg <= 250 and avg > 210:
         music_control.set_volume(0.7)
         print('0.6')
     elif avg <= 210 and avg > 170:
         music_control.set_volume(0.7)
         print('0.5')
     elif avg <= 170 and avg > 120:
         music_control.set_volume(0.4)
         print('0.4')
     elif avg <= 120 and avg > 70:
         music_control.set_volume(0.3)
         print('0.3')
     elif avg <= 70 and avg > 30:
         music_control.set_volume(0.2)
         print('0.2')
     elif avg <= 30 and avg > 1:
         music_control.set_volume(0.1)
         print('0.1')
     elif avg <= 1:
         music_control.set_volume(0)
         print('0')