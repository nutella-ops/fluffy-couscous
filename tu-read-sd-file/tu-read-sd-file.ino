//audio.play("filename");    plays a file
//audio.play("filename",30); plays a file starting at 30 seconds into the track
//audio.speakerPin = 11;     set to 5,6,11 or 46 for Mega, 9 for Uno, Nano, etc.
//audio.disable();           disables the timer on output pin and stops the music
//audio.stopPlayback();      stops the music, but leaves the timer running
//audio.isPlaying();         returns 1 if music playing, 0 if not
//audio.pause();             pauses/unpauses playback
//audio.quality(1);          Set 1 for 2x oversampling
//audio.volume(0);           1(up) or 0(down) to control volume
//audio.setVolume(0);        0 to 7. Set volume level
//audio.loop(1);             0 or 1. Can be changed during playback for full control of looping. 

#include <pcmRF.h>
#include <pcmConfig.h>
#include <TMRpcm.h>
#include <SD.h>
#include <SPI.h>

TMRpcm audio;
File myFile;

// set up variables using the SD utility library functions:
Sd2Card card;
SdVolume volume;
SdFile root;
const int chipSelect = 10;

// user input pin, output of choreography switch goes here
int inputA = 2;
int outputA = 3;

 
void setup()
{
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

pinMode(3, OUTPUT);
audio.speakerPin = 9;
audio.setVolume(7);
audio.loop(1);
audio.quality(1);
 audio.play("tree.wav");
 
}
 
void loop()
{
    bool logic = LOW;
  // listen on userPin for input; ATmega pins are set to INPUT by default
  if (digitalRead(inputA) == logic) {
    digitalWrite(3, HIGH);
  } else {
    digitalWrite(3, logic);
  }
 
}
