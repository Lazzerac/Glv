/*

MinIMU-9-Arduino-AHRS
Pololu MinIMU-9 + Arduino AHRS (Attitude and Heading Reference System)

Copyright (c) 2011 Pololu Corporation.
http://www.pololu.com/

MinIMU-9-Arduino-AHRS is based on sf9domahrs by Doug Weibel and Jose Julio:
http://code.google.com/p/sf9domahrs/

sf9domahrs is based on ArduIMU v1.5 by Jordi Munoz and William Premerlani, Jose
Julio and Doug Weibel:
http://code.google.com/p/ardu-imu/

MinIMU-9-Arduino-AHRS is free software: you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

MinIMU-9-Arduino-AHRS is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for
more details.

You should have received a copy of the GNU Lesser General Public License along
with MinIMU-9-Arduino-AHRS. If not, see <http://www.gnu.org/licenses/>.

*/

unsigned int p,y,r;
byte buff[10];
void printdata(void)
{    
      Serial.print("!");

      #if PRINT_EULER == 1
      Serial.print("ANG:");
      Serial.print(ToDeg(roll));
      Serial.print(",");
      Serial.print(ToDeg(pitch));
      Serial.print(",");
      Serial.print(ToDeg(yaw));
      #endif      
      #if PRINT_ANALOGS==1
      Serial.print(",AN:");
      Serial.print(AN[0]);  //(int)read_adc(0)
      Serial.print(",");
      Serial.print(AN[1]);
      Serial.print(",");
      Serial.print(AN[2]);  
      Serial.print(",");
      Serial.print(AN[3]);
      Serial.print (",");
      Serial.print(AN[4]);
      Serial.print (",");
      Serial.print(AN[5]);
      Serial.print(",");
      Serial.print(c_magnetom_x);
      Serial.print (",");
      Serial.print(c_magnetom_y);
      Serial.print (",");
      Serial.print(c_magnetom_z);
      #endif
      /*#if PRINT_DCM == 1
      Serial.print (",DCM:");
      Serial.print(convert_to_dec(DCM_Matrix[0][0]));
      Serial.print (",");
      Serial.print(convert_to_dec(DCM_Matrix[0][1]));
      Serial.print (",");
      Serial.print(convert_to_dec(DCM_Matrix[0][2]));
      Serial.print (",");
      Serial.print(convert_to_dec(DCM_Matrix[1][0]));
      Serial.print (",");
      Serial.print(convert_to_dec(DCM_Matrix[1][1]));
      Serial.print (",");
      Serial.print(convert_to_dec(DCM_Matrix[1][2]));
      Serial.print (",");
      Serial.print(convert_to_dec(DCM_Matrix[2][0]));
      Serial.print (",");
      Serial.print(convert_to_dec(DCM_Matrix[2][1]));
      Serial.print (",");
      Serial.print(convert_to_dec(DCM_Matrix[2][2]));
      #endif*/
      Serial.println();    
      
}

void Print_Data_Binary(void)
{
      
      p =  (int) 100*pitch;
      y =  (int) 100*yaw;
      r =  (int) 100*roll;
      buff[0] = B00100001;
      buff[1] = lowByte(p);
      buff[2] = highByte(p);
      buff[3] = lowByte(y);
      buff[4] = highByte(y);
      buff[5] = lowByte(r);
      buff[6] = highByte(r);
      buff[7] = lowByte(sender);
      buff[8] = highByte(sender);      
//      Serial.write(sender);
      buff[9] = B00100100;
      Serial.write(buff, 10);
      Serial.flush();
      //Serial.print(buff);
}

//void printdatabinary(void)
//{
//      p = int(pitch);
//      y = int(yaw);
//      r = int(roll);
//      Serial.write("!");
//      Serial.write(p >> 8);
//      Serial.write(p & 0xFF);
//      Serial.write(y >> 8);
//      Serial.write(y & 0xFF);
//      Serial.write(r >> 8);
//      Serial.write(r & 0xFF);
//      Serial.write(sender >> 8);
//      Serial.write(sender & 0xFF);      
////      Serial.write(sender);
//      Serial.write("$");
//      Serial.flush();
//
//}
void printdata2(void)
{    
      Serial.print("!");
      Serial.print("ANG:");
      Serial.print(roll);
      Serial.print(",");
      Serial.print(pitch);
      Serial.print(",");
      Serial.print(yaw);
      Serial.println();
      
}
long convert_to_dec(float x)
{
  return x*10000000;
}

