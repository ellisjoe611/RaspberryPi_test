#ifndef COORDINATE_H
#define COORDINATE_H

float distance(int tx, float rssi);
float getK(float left_dist, float right_dist, float mid_dist);
float getX(float left, float right, float k);
float getY(float mid, float k);

#endif