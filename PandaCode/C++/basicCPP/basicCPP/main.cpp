//
//  main.cpp
//  basicCPP
//
//  Created by Henry on 7/30/16.
//  Copyright © 2016 HenryOM. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

class cell{
    public:
    int x;
    int y;
    cell(int cx, int cy){
        x = cx;
        y = cy;
    }
};

vector<cell> cells;

int numOfSrndCells(cell tCell){
    int num = 0;
    
    vector<cell> possCells;
    
    possCells.push_back(cell(tCell.x - 1, tCell.y));
    possCells.push_back(cell(tCell.x - 1, tCell.y - 1));
    possCells.push_back(cell(tCell.x, tCell.y - 1));
    possCells.push_back(cell(tCell.x + 1, tCell.y - 1));
    possCells.push_back(cell(tCell.x + 1, tCell.y));
    possCells.push_back(cell(tCell.x + 1, tCell.y + 1));
    possCells.push_back(cell(tCell.x, tCell.y + 1));
    possCells.push_back(cell(tCell.x - 1, tCell.y + 1));
    
    for (unsigned i = 0; i < possCells.size(); i++){
        for (unsigned ai = 0; ai < possCells.size(); ai++){
            if (possCells[i].x == cells[ai].x) {
                if (possCells[i].y == cells[ai].y) {
                    num++;
                }
            }
        }
    }

    return num;
}

void killCellAtIndex(int i){
    
}

void update(){
    for (unsigned i = 0; i < cells.size(); i++){
        
        int neihghbors = numOfSrndCells(cells[i]);
        
        if (neihghbors <= 1) {
            killCellAtIndex(i);
            return;
        }
        
        if (neihghbors >= 4){
            killCellAtIndex(i);
            return;
        }
    }
}

void draw(){
    cout << "--------------------------------------------------";
    
    for (unsigned i = 0; i < cells.size(); i++){
        
    }
    
    cout << "--------------------------------------------------";
}

int main(int argc, const char * argv[]) {
    // insert code here...
//    ball myBall = ball();
//    
//    myBall.bounce();
//    
//    std::vector<ball> balls;
//    
//    char name[50];
//    
//    cout << "please state your name:" << endl;
//    cin >> name;
//    cout << name << endl;
    char useless;
    for (;;){
        draw();
        update();
        cout << "cycle";
        cin >> useless;
    }

    
    return 0;
}

