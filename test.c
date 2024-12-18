#include <stdio.h>

int main(void)

{

    double minutes, hours, stor1, stor2;
    int time, min, hour;
    time = 32767;
    minutes = time / 60;
    min = (int)minutes;
    stor1 = ((double)minutes - (double)min) * 60;
    hours = min / 60;
    hour = (int)hours;
    stor2 = ((double)hours - (double)hour) * 60;
    printf("%d초는 %d시간 %i분 %i초 입니다.\n", time, hour, (int)stor2, (int)stor1);
    return 0;
}
