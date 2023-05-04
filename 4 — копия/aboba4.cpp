#include <iostream>
#include <math.h>

using namespace std;
extern "C" float SumR(int a, float b);
int factorial(int x) {
    if (x == 0 || x == 1) {
        return 1;
    }
    return (x * factorial(x - 1));
}


int main()
{
    int n;
    float x;
    std::cout << "Input n: ";
    std::cin >> n;
    std::cout << "Input x: ";
    std::cin >> x;
    double R = 0.0;
    R = SumR(n, x);
    std::cout << "\nResult: " << R << std::endl;
    return 0;
}

extern "C" float fun_el(int i, float z) {
    float f;

    f = powf(z, (-1) * i) / (factorial(i) * cos(z));
    return f;
}
