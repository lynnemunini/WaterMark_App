# import tkinter as tk, threading
# import imageio
# from PIL import Image, ImageTk

# video_name = "WatermarkApp.mp4" #This is your video file path
# video = imageio.get_reader(video_name)

# def stream(label):

#     for image in video.iter_data():
#         frame_image = ImageTk.PhotoImage(Image.fromarray(image))
#         label.config(image=frame_image)
#         label.image = frame_image

# if __name__ == "__main__":

#     root = tk.Tk()
#     my_label = tk.Label(root)
#     my_label.pack()
#     thread = threading.Thread(target=stream, args=(my_label,))
#     thread.daemon = 1
#     thread.start()
#     root.mainloop()

# A = [5, 2, 7, 9]
# sorted = sorted(A)
# print(sorted)

# def string (S):
#     lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#     # upper_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#     string_list = list(S)

#     n = -1
#     for i in reversed(lower_list):
#         if i in string_list:
#             if i.upper() in string_list:
#                 return i.upper()
#     else:
#         return "NO"
        

# print(string("coffee"))

# import random

# def solution(N):
#     # write your code in Python 3.6
#     integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     count = 0
#     integers_list = []

#     if N % 2 == 0:
#         for i in range (0, (N//2)):
#             val = random.choice(integers)
#             if val not in integers_list:
#                 integers_list.append(val)
#                 integers_list.append(-(val))
#     elif N % 2 != 0:
#         for i in range (0, (N//2)):
#             val = random.choice(integers)
#             if val not in integers_list:
#                 integers_list.append(val)
#                 integers_list.append(-(val))
#         integers_list.append(0)
#     return integers_list

# print(solution(5))

# import random
# import re

# def solution(A, B, C):
#     # write your code in Python 3.6
#     a_list = []
#     b_list = []
#     c_list = []

#     regex = "\\b([a-z])\\1\\1+\\b"

#     compiled = re.compile(regex)

#     if A != 0:
#         for i in range(A):
#             a_list.append("a")
#     if B != 0:
#         for i in range(B):
#             a_list.append("b")
#     if C != 0:
#         for i in range(C):
#             a_list.append("c")


#     a_list = random.shuffle(a_list)
#     b_list = random.shuffle(b_list)
#     c_list = random.shuffle(c_list)

#     abc_list = a_list + b_list + c_list
#     abc_string = "".join(abc_list)

#     while re.search(compiled, abc_str):
#         string = list(abc_str)
#         shuffled = random.shuffle(string)
#         my_string = "".join(shuffled)
#         return my_string
#     else:
#         return ""
# print(solution(5, 1, 4))

x = 0
y = 4
m = 0.4
pixel_array = []

while (x < 10):
    pixel = []
    x = x + 1
    y = y + m

    pixel.append(x)
    pixel.append(round(y))
    pixel_array.append(pixel)

print(pixel_array)
