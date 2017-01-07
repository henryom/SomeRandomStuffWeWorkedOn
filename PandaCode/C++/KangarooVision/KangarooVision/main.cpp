//
//  main.cpp
//  KangarooVision
//
//  Created by Henry on 9/10/16.
//  Copyright © 2016 HenryOM. All rights reserved.
//

#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main(int argc, const char * argv[]) {
    
    VideoCapture cap;
    
    int hueMin = 40;
    int hueMax = 90;
    int satMin = 0;
    int satMax = 20;
    int viMin = 240;
    int viMax = 260;
    
    
    namedWindow("controls");
    
    cvCreateTrackbar("Hue Min", "controls", &hueMin, 179);
    cvCreateTrackbar("Hue Max", "controls", &hueMax, 179);
    
    cvCreateTrackbar("Saturation Min", "controls", &satMin, 255);
    cvCreateTrackbar("Saturation Max", "controls", &satMax, 255);
    
    cvCreateTrackbar("Vibrance Min", "controls", &viMin, 255);
    cvCreateTrackbar("Vibrance Max", "controls", &viMax, 255);
    
    if (!cap.open(1)){
        return 0;
    }
    
    for (;;){
        Mat originalFrame;
        Mat hsvFrame;
        Mat bFrame;
        Mat bFrameDilate;
        
        //Set original frame to camera output
        cap >> originalFrame;
        
        //Set hsv frame to the original frame but in the HSV colorspace
        cvtColor(originalFrame, hsvFrame, COLOR_BGR2HSV);
        
        //Filter colors and put them into a bianary frame bFrame
        inRange(hsvFrame, Scalar(hueMin, satMin, viMin), Scalar(hueMax, satMax, viMax), bFrame);
        
        vector<vector<Point>> contours;
        
        Mat unmodifiedFrame = originalFrame;
        findContours(bFrame, contours, CV_RETR_TREE, CV_CHAIN_APPROX_SIMPLE);
        drawContours(unmodifiedFrame, contours, -1, Scalar(20,50,80));
        contours.clear();
        
        

        //remove contours with a wrong width to hight ratio
        for (int i = 0; i < contours.size(); i++){
            double perimeter = cvContourPerimeter(&contours[i]);
            double area = cvContourArea(&contours[i]);
            
        }
        
        
        
        drawContours(originalFrame, contours, -1, Scalar(20,50,80));
        
        
        
        if (originalFrame.empty()){break;}
        imshow("Original", originalFrame);
        imshow("Unfixed Orig", unmodifiedFrame);
        
        
        if (waitKey(30) == 27){
            return 0;
        }
    }
    
    
    return 0;

}
