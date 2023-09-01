#include <iostream>
#include <graphics.h>
using namespace std;

class Circle {
public:
    int centerX, centerY, radius;

    void input() {
        cout << "Enter the center coordinates of the circle: ";
        cin >> centerX >> centerY;
        cout << "Enter the radius of the circle: ";
        cin >> radius;
    }

    void draw() {
        int x = 0, y = radius;
        int d = 3 - 2 * radius;

        initwindow(800, 600, "Circle Drawing");

        while (x <= y) {
            putpixel(centerX + x, centerY + y, WHITE);
            putpixel(centerX + y, centerY + x, WHITE);
            putpixel(centerX - y, centerY + x, WHITE);
            putpixel(centerX - x, centerY + y, WHITE);
            putpixel(centerX - x, centerY - y, WHITE);
            putpixel(centerX - y, centerY - x, WHITE);
            putpixel(centerX + y, centerY - x, WHITE);
            putpixel(centerX + x, centerY - y, WHITE);

            if (d <= 0) {
                d = d + 4 * x + 6;
            } else {
                d = d + 4 * (x - y) + 10;
                y--;
            }
            x++;
        }

        delay(2000);
        closegraph();
    }
};

int main() {
    Circle circle;
    int gd = DETECT, gm;
    initgraph(&gd, &gm, NULL);

    circle.input();
    circle.draw();

    delay(5000);
    return 0;
}


