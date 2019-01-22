# import ctypes
#
# from PIL import ImageTk, Image
# import cv2
# import tkinter as tk
# import music_control
# import speed_detection
# import threading
#
# class MainWindow(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.newMaster = master
#         self.master = master
#         self.pack()
#
#         user32 = ctypes.windll.user32
#         self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#         # back = tk.Frame(width=self.screensize[0], height=self.screensize[1], bg='white')
#
#
#         self.lmain1 = tk.Label(self, text="hi")
#         self.lmain1.grid(row=0, column=0)
#
#         myimage = tk.PhotoImage(file='songo.png')
#         label = tk.Label(self, image=myimage)
#         label.image = myimage  # the reference
#         label.grid(row=1, column=0)
#
#
#
#
#         self.video_stream()
#
#
#     def video_stream(self):
#         _, frame1 = self.cap.read()
#         speed_detection.speed_detection(frame1)
#         cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
#         img1 = Image.fromarray(cv2image1)
#         imgtk1 = ImageTk.PhotoImage(image=img1)
#         self.lmain1.imgtk = imgtk1
#         self.lmain1.configure(image=imgtk1)
#
#         self.flag = self.music_on()
#         if self.flag:
#             self.lmain1.after(1, self.video_stream)
#         else:
#             print("finish")
#             self.cap1 = cv2.VideoCapture('videoplayback.mp4')
#             self.video_stream1()
#
#     def video_stream1(self):
#         print("here")
#         _, frame1 = self.cap1.read()
#         cv2image1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGBA)
#         img1 = Image.fromarray(cv2image1)
#         imgtk1 = ImageTk.PhotoImage(image=img1)
#         self.lmain1.imgtk = imgtk1
#         self.lmain1.configure(image=imgtk1)
#         self.flag = self.continue_movie()
#         if self.flag:
#             self.lmain1.after(1, self.video_stream)
#         else:
#             print("finish")
#             self.cap1.release()
#             # cv2.destroyAllWindows()
#             # self.master = None
#             #conclusion = Conclusion(self.newMaster, speed=[23, 54, 6, 88, 34, 32, 5, 7], volume=[4, 33, 8,2,67,98,46,3])
#
#     def continue_movie(self):
#         if self.counter == 0:
#             return True
#         self.counter -= 1
#
#     def music_on(self):
#         return music_control.get_busy()
#
# def is_one_not_dance(mp_list):
#     pass
#
# def conclusion(list_of_mph):
#     pass
#
#
# def calaulate_volum(avg):
#      print("========vol=================")
#
#      if avg > 500:
#          music_control.set_volume(1)
#          print('1')
#      elif avg <= 500 and avg > 400:
#          print('0.1')
#          music_control.set_volume(0.9)
#      elif avg <= 400 and avg > 320:
#          music_control.set_volume(0.8)
#          print('0.8')
#      elif avg <= 320 and avg > 250:
#          music_control.set_volume(0.7)
#          print('0.7')
#      elif avg <= 250 and avg > 210:
#          music_control.set_volume(0.7)
#          print('0.6')
#      elif avg <= 210 and avg > 170:
#          music_control.set_volume(0.7)
#          print('0.5')
#      elif avg <= 170 and avg > 120:
#          music_control.set_volume(0.4)
#          print('0.4')
#      elif avg <= 120 and avg > 70:
#          music_control.set_volume(0.3)
#          print('0.3')
#      elif avg <= 70 and avg > 30:
#          music_control.set_volume(0.2)
#          print('0.2')
#      elif avg <= 30 and avg > 1:
#          music_control.set_volume(0.1)
#          print('0.1')
#      elif avg <= 1:
#          music_control.set_volume(0)
#          print('0')


import ctypes

from PIL import ImageTk, Image
import cv2
import tkinter as tk
import music_control
import speed_detection
import threading
import last_screen

class ImageWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()


        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

        a = "C:\\Users\\שרה ויסברגר\\Desktop\\EXELLENTIM\\excellenteam-hackathon-ella-songo\\fa.png"
        lf = [a, a, a, a, a, a, a, a, a]
        imgee = last_screen.last_screen(lf)
        img = tk.PhotoImage(imgee)
        panel = tk.Label(self, text="image pro")
        panel.image = img
        panel.grid()





import ctypes
from PIL import ImageTk, Image
import cv2
import tkinter as tk
import music_control
import speed_detection
import threading
import last_screen
import os

class ImageWindow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()


        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        File = os.listdir('images_collection/')
        lf = []
        for i in range(9):
            lf.append('images_collection/' + File[1])
            # img = ImageTk.PhotoImage(Image.open(FileDir))
        # a = "C:\\Users\\שרה ויסברגר\\Desktop\\EXELLENTIM\\excellenteam-hackathon-ella-songo\\fa.png"
        # lf = [a, a, a, a, a, a, a, a, a]

        # print(lf)
        imgee = last_screen.last_screen(lf)
        img = tk.PhotoImage(imgee)
        panel = tk.Label(self, text="image pro")
        panel.image = img
        panel.grid()







