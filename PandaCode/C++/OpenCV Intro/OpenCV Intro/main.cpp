//
//  main.cpp
//  OpenCV Intro
//
//  Created by Henry on 9/6/16.
//  Copyright © 2016 HenryOM. All rights reserved.
//

#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;

int main(int argc, const char * argv[]) {
    // insert code here...
    VideoCapture cap;
    cap = VideoCapture(0);
    
    //cvNamedWindow("Original");
    cvNamedWindow("B&W");
    cvNamedWindow("controls");
    
    int hueMin = 0;
    int hueMax = 0;
    int satMin = 0;
    int satMax = 0;
    int viMin = 0;
    int viMax = 0;
    
    cvCreateTrackbar("Hue Min", "controls", &hueMin, 179);
    cvCreateTrackbar("Hue Max", "controls", &hueMax, 179);
    
    cvCreateTrackbar("Saturation Min", "controls", &satMin, 255);
    cvCreateTrackbar("Saturation Max", "controls", &satMax, 255);
    
    cvCreateTrackbar("Vibrance Min", "controls", &viMin, 255);
    cvCreateTrackbar("Vibrance Max", "controls", &viMax, 255);
    
    if (!cap.open(0)){
        return 0;
    }
    
    
    for (;;){
        Mat originalFrame;
        cap >> originalFrame;
        
        Mat hsvFrame;
        cvtColor(originalFrame, hsvFrame, COLOR_BGR2HSV);
        
        Mat bFrame;
        inRange(hsvFrame, Scalar(hueMin, satMin, viMin), Scalar(hueMax, satMax, viMax), bFrame);
        
        
        
        if (originalFrame.empty()){break;}
        //imshow("Original", originalFrame);
        //imshow("B&W", bFrame);
        imshow("window", originalFrame);
        if (waitKey(30) == 27){
            return 0;
        }
    }
    
    
    return 0;
}
