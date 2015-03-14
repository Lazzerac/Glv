#include "buttons.h"

int button_quantity = 8;

Button P1, P2, R1, R2, M1, M2, I1, I2;

Button buttons_set[8]={P1, P2, R1, R2, M1, M2, I1, I2};

int button_input[8] = {2,3,4,5,6,7,8,9};
char button_on[8] = {'a','b','c','d','e','f','g','h'};
char button_press[8] = {'1','2','3','4','5','6','7','8'};


void setup() {
  for(int i = 0; i < button_quantity; i++){
    buttons_set[i].setMode(MemoryTimer);
    buttons_set[i].setTimer(100);
    buttons_set[i].setRefresh(50);
    buttons_set[i].assign(button_input[i]);
  }
  Serial1.begin(9600);
  Serial1.println("Ready");
}

void loop(){
  for(int i = 0; i <= button_quantity; i++){
    switch(buttons_set[i].check()){
      case Pressed:
      	Serial1.println(button_press[i]);
        delay(5);
        break;
      case ON:
		Serial1.print('O');
        delay(5);
        break;
      case Hold:
        Serial1.print('H');
        delay(5);
        break;
      case OFF:
        break;
      case Released:
      	Serial1.print('R');
      	delay(5);
      	break;
    }
  }
}
  
