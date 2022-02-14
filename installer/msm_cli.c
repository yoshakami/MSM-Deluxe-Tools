#include <stdlib.h>
#define _WIN32_WINNT 0x0500
#include <windows.h>

int main(int argc, char *argv[])
{
    char args[500] = {"msm_cli.py exe "};
    int len = 15;
    int i=1;
    int j;
    for (; i<argc; i++)
    {
        j = 0;
        for (;argv[i][j] != '\0';j++)
        {
            args[len] = argv[i][j];
            len++;
        }
        args[len] = ' ';
        len++;
    }
    args[len-1] = '\0';
    system(args);
    return 0;
}