#include <SD.h>                      // need to include the SD library
//#define SD_ChipSelectPin 53  //example uses hardware SS pin 53 on Mega2560
#define SD_ChipSelectPin 10  //using digital pin 4 on arduino nano 328, can use other pins
#include <TMRpcm.h>           //  also need to include this library...
#include <pcmRF.h>
#include <pcmConfig.h>
#include <SPI.h>

TMRpcm audio;   // create an object for use in this sketch
// set up variables using the SD utility library functions:
Sd2Card card;
SdVolume volume;
SdFile root;

void setup(){

  audio.speakerPin = 9; //5,6,11 or 46 on Mega, 9 on Uno, Nano, etc

  Serial.begin(9600);
  if (!SD.begin(SD_ChipSelectPin)) {  // see if the card is present and can be initialized:
    Serial.println("SD fail");  
    return;   // don't do anything more if not
  }
//   audio.play("tree.wav"); //the sound file "music" will play each time the arduino powers up, or is reset
}



void loop(){  

  if(Serial.available()){    
    if(Serial.read() == 'p'){ //send the letter p over the serial monitor to start playback
      audio.play("tree.wav");
    }
  }

}