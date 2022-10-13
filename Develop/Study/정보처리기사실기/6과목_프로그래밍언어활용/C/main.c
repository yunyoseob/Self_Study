#include <stdio.h>

struct Soojebi{
  char name[20];
  int os,db,hab1,hab2;
/*
name [0,0,0 ..., 0]
os : 0
db : 0
hab1 : 0
hab2 : 0
*/
};

void main() {
  struct Soojebi s[3]={{"데이터1",95,88},{"데이터2",84,91},{"데이터3",86,75}};
  /*
  s[0] : "데이터1",95,88
  // name : "데이터1", os : 95, db :88, hab1 : 0, hab2 :0

  s[1] : "데이터2",84,91
  // name : "데이터2", os : 84, db :91, hab1 : 0, hab2 :0

  s[2] : "데이터3",86,75
  // name : "데이터3", os : 86, db :75, hab1 : 0, hab2 :0
*/

  struct Soojebi *p;

  p=&s[0];
  (p+1)->hab1 = (p+1)->os+(p+2)->db;
  // 84+75=159
  // (p+1)->hab1 : 159 
  printf("%d\n",(p+1)->hab1);
  (p+1)->hab2 = (p+1)->hab1 + p-> os + p-> db;
// 159 + 95 + 88
  // 159+183 = 342
  printf("%d\n",(p+1)->hab2);
  printf("%d\n",(p+1)->hab1+(p+1)->hab2);
  // 342+159
  // 501
}
