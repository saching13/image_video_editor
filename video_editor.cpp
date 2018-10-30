#include "opencv2/opencv.hpp"

using namespace cv;
using namespace std;

int main()
{
    int fourcc = CV_FOURCC('H','2','6','4');

    // Open video file
    VideoCapture in_video("VID_20181019_184605.mp4");

    // getting fps
    double fps = in_video.get(CV_CAP_PROP_FPS);
    VideoWriter  video_writer("conveted_c.mp4", fourcc, 60.0, Size(in_video.get(CV_CAP_PROP_FRAME_WIDTH),
               in_video.get(CV_CAP_PROP_FRAME_HEIGHT)), true);

    cout << "Frames per second using video.get(CV_CAP_PROP_FPS) : " << fps << endl;
    Mat frame;
    if(!in_video.isOpened()){
       cerr << "Error opening file or file not found in the directory"<< endl;
        exit(0);
    }
    while(in_video.read(frame)){

    video_writer.write(frame);

    }
    video_writer.release();

    
    in_video.release();
    return 0;
    
}
