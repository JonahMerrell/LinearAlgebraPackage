#include <stdio.h>
#include <omp.h>

int main()
{
     #pragma omp parallel
     {
     printf("Hello World from %d\n", omp_get_thread_num()); 
     }
     return 0;
}