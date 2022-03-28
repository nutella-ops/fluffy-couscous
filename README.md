# ZK/U Arduino Tree Music

**Short Story:**
	I was trying to play a 16-bit audio file using an Arduino because I was not aware of Data Bus Widths.
**Long Story:**
	I had previously made two personal projects with an Arduino, so it was familiar and comfortable. I had no expereince in the design considerations for this sort of project. I created something I thought would work given the platform I was using. The idea was to manipulate a multiplexer using the arduino as a means of selecting different responses. The project was to personify trees and have each action (approaching the tree, watering the tree, etc) give a different response, hence the multiplexer. Near the end of the project I discovered Data Bus Width and then I knew the Arduino was the wrong platform to use. I switched to a Raspberry Pi Zero and completed the project (found in folder: "rpi-zero" in this repo). Yes, I probably should have branched it, but my git experience level was so low that branching would add complexity I didn't want to deal with as time was of the essence.
