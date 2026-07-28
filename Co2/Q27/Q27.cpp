#include <iostream>
#include <cmath>
using namespace std;

struct Station {
    string name;
    double x, y;
};

int main() {

    Station stations[] = {
        {"A", 2, 3},
        {"B", 5, 7},
        {"C", 1, 8},
        {"D", 6, 2},
        {"E", 8, 5}
    };

    int n = 5;

    double minDistance = 1e9;
    string s1, s2;

    cout << "Distances Between All Station Pairs\n\n";

    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {

            double distance = sqrt(pow(stations[i].x - stations[j].x,2) +
                                   pow(stations[i].y - stations[j].y,2));

            cout << stations[i].name << " - "
                 << stations[j].name
                 << " = " << distance << endl;

            if(distance < minDistance) {
                minDistance = distance;
                s1 = stations[i].name;
                s2 = stations[j].name;
            }
        }
    }

    cout << "\nNearest Stations: "
         << s1 << " and " << s2 << endl;

    cout << "Minimum Distance = "
         << minDistance << endl;

    return 0;
}