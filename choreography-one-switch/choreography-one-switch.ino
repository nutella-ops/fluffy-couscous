// choose a high and low frequency to stand in as dialog words  
int dialogWord[2] = {207, 414};


// user input pin, output of choreography switch goes here
int inputA = 0;
int outputA = 1;

int inputB = 2;
int outputB = 3;

int inputC = 4;
int outputC = 5;

int inputD = 6;
int outputD = 7;

int inputE = 8;
int outputE = 9;


// function to create placeholder phrases; 4 possible phrases; tone(Pin, Frequency, Duration); audioPin = audio output on specified pin
int dialogPhrase(int x, int y, int audioPin) {
    tone(audioPin, x, 145); 
    delay(150);       
    tone(audioPin, y, 125);
    delay(150);
    tone(audioPin, y, 100);
    delay(1300);
  }

// list of unused pins
int unused[18] = {10, 11, 12, 13, A0, A1, A2, A3, A4, A5};
// size of unused pins list
int unused_length = sizeof(unused) / sizeof(int);

// pull-up on all unused pins
void pullup() {
  int i;
  for (i = 0; i < unused_length; i++) {
    pinMode(unused[i], INPUT_PULLUP);
  }
}

// setup for values which only need to be set once and remain unchanged; things need to all be defined globally (outside all loops) to work; it's beacuse the function is there so anything the function uses needs to be outside with the function
void setup() {
// set up pins because best practices
pinMode(inputA, INPUT);
pinMode(outputA, OUTPUT);

pinMode(inputB, INPUT);
pinMode(outputB, OUTPUT);

pinMode(inputC, INPUT);
pinMode(outputC, OUTPUT);

pinMode(inputD, INPUT);
pinMode(outputD, OUTPUT);

pinMode(inputE, INPUT);
pinMode(outputE, OUTPUT);
pullup();
}

// main code loop, runs repeatedly
void loop() {   
  bool logic = LOW;
  // listen on userPin for input; ATmega pins are set to INPUT by default
  if (digitalRead(inputA) == logic) {
    dialogPhrase(dialogWord[0], dialogWord[1], outputA);
  }
  if (digitalRead(inputB) == logic) {
    dialogPhrase(dialogWord[1], dialogWord[0], outputB);
  }
  if (digitalRead(inputC) == logic) {
    dialogPhrase(dialogWord[1], dialogWord[1], outputC);
  }
  if (digitalRead(inputD) == logic) {
    dialogPhrase(dialogWord[0], dialogWord[0], outputD);
  }
  if (digitalRead(inputE) == logic) {
    dialogPhrase(dialogWord[1], dialogWord[1], outputE);
  }
}