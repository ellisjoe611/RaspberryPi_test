#include "coordinate.h"
#include <math.h>

float distance(int tx, float rssi) {
	if (rssi == 0) {
		return -1.0;
	}

	double ratio = rssi / (double)tx;

	if (ratio < 1.0) {
		return (float) pow(ratio, 10.0);
	}
	else {
		return (float) ((0.89976)*pow(ratio, 7.7095) + 0.111);
	}
}

float getK(float left, float right, float middle) {
	return (float) sqrt(left*left + right * right - 2.0 * middle*middle);
}

float getX(float left, float right, float k) {
	return (left*left - right * right) / (4.0 * k);
}

float getY(float mid, float k) {
	return (float) sqrt(mid*mid - k * k);
}