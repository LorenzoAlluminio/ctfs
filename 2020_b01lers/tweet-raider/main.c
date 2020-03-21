#include <stdio.h>
#include <stdlib.h>

int main(){

	  uint *puVar1;
	  char *__s;
	  long in_FS_OFFSET;
	  char local_138 [296];
	  long local_10;

  
  //getchar();
  //setvbuf(stdin,(char *)0x0,2,0);
  //setvbuf(stdout,(char *)0x0,2,0);
  puVar1 = (uint *)malloc(4);
  *puVar1 = 0x0;
  printf("%p\n",puVar1);
  puts("Welcome to Mlon Eusk\'s Tweet Rater!\nInput your tweet, and we will give you a rating.\n");
  printf("Tweet: ");
  fgets(local_138,0x118,stdin);
  puts("Your tweet:");
  printf(local_138);
  printf("Your score: %d\n",(ulong)*puVar1);
  if (9000 < (int)*puVar1) {
    puts("Your score is over 9000!");
  }
  return 0;
}
