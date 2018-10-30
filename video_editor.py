import cv2


#def fps_modifier():






vid_cap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
success, image = vid_cap.read()
count = 0
fps = vid_cap.get(cv2.cv.CV_CAP_PROP_FPS)
while success:
    success, image = vid_cap.read()
    print('Read a new frame: ', success)
    count += 1





