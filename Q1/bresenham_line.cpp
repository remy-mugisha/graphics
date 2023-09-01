
#include <iostream>
#include <graphics.h>
#include <math.h>
using namespace std;

//void drawBresenhamLine(int, int, int, int, int);
void drawBresenhamLine(int x1, int y1, int x2, int y2, int color) {
    int x, y, dx, dy, dx1, dy1, px, py, xe, ye, i;

    dx = x2 - x1;
    dy = y2 - y1;
    dx1 = fabs(dx);
    dy1 = fabs(dy);
    px = 2 * dy1 - dx1;
    py = 2 * dx1 - dy1;

    initwindow(800, 600, "Bresenham Line Drawing");

    if (dy1 <= dx1) {
        if (dx >= 0) {
            x = x1;
            y = y1;
            xe = x2;
        } else {
            x = x2;
            y = y2;
            xe = x1;
        }

        putpixel(x, y, color);
        for (i = 0; x < xe; i++) {
            x = x + 1;
            if (px < 0) {
                px = px + 2 * dy1;
            } else {
                if ((dx < 0 && dy < 0) || (dx > 0 && dy > 0)) {
                    y = y + 1;
                } else {
                    y = y - 1;
                }
                px = px + 2 * (dy1 - dx1);
            }
            delay(0);
            putpixel(x, y, color);
        }
    } else {
        if (dy >= 0) {
            x = x1;
            y = y1;
            ye = y2;
        } else {
            x = x2;
            y = y2;
            ye = y1;
        }

        putpixel(x, y, color);
        for (i = 0; y < ye; i++) {
            y = y + 1;
            if (py <= 0) {
                py = py + 2 * dx1;
            } else {
                if ((dx < 0 && dy < 0) || (dx > 0 && dy > 0)) {
                    x = x + 1;
                } else {
                    x = x - 1;
                }
                py = py + 2 * (dx1 - dy1);
            }
            delay(0);
            putpixel(x, y, color);
        }
    }

    delay(10000);
    closegraph();
}

int main() {
    int x1, x2, y1, y2;
    initwindow(800, 600, "Bresenham Line Drawing");

    cout << "plz enter the coordinates x1 and y1 as initial point: ";
    cin >> x1 >> y1;
    cout << "Enter the coordinates x2 and y2 as ending point: ";
    cin >> x2 >> y2;
    drawBresenhamLine(x1, y1, x2, y2, WHITE);

    getch();
    closegraph();
    return 0;
}

