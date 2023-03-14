#include <stdio.h>
#include <unistd.h>

int main(int argc, char* argv[]){
  int aStdoutPipe[2];
  int aStdinPipe[2];

  if(pipe(aStdoutPipe) == -1) {
    perror("failed to construct pipe.");
    return -1;
  }
  if(pipe(aStdinPipe) == -1) {
    perror("failed to construct pipe.");
    return -1;
  }
}