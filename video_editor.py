import cv2
import argparse


def fps_modifier(filename, speed):
    vid_cap = cv2.VideoCapture(filename)
    success, image = vid_cap.read()
    if not vid_cap.isOpened():
        print("Error opening file or file not found in the directory")
        exit(10)
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    size = image.shape[1], image.shape[0]
    is_color = True
    vid = cv2.VideoWriter("converted.mp4", fourcc, speed * fps, size, is_color)

    while success:
        vid.write(image)
        success, image = vid_cap.read()
    vid.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="enter \"crop\" to crop or \"fps\" to modify video")
    parser.add_argument("speed", help="speed to should be (0.5, 1, 1.5, 2, 3, etc...", type=float)
    parser.add_argument("filename", help="Keep the input file in the same path as of the program file ")
    parser.add_argument("--size", help="size should be of the format (height x width) or empty to make it default")

    args = parser.parse_args()
    print(args.action)
    print(args.speed)
    print(args.size)

    fps_modifier(args.filename,int(args.speed))



