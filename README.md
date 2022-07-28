# Human Resource Machine Python Editor
<img src="http://cdn.akamai.steamstatic.com/steam/apps/375820/ss_7b564936dfb8f9b7b76f2141a79fa3cea8fd6fc7.1920x1080.jpg?t=1450110253" 
     alt="Quelle http://store.steampowered.com/app/375820/?l=german" 
     style="width: 600px;"/>

<img src="img.png" style="width: 600px;"/>

## Introduction
This project started as an interpreter for the human resource machine format, but after some done stuff I started to create a gui and the target changed.

So the goal is now to create an editor/ ide for the human resource machine format. Supporting editing, executing and debugging the hrm-format.

## Description

Drag operation from op box to code box.

Double click block in code box to set parameter if it needs parameter.

Click the right button in code box to delete one or all code.

Click 'start' button to run your program and use other 4 button to debug.

'Flash speed' slider is used to adjust animation speed. 

## Available operators

Operator               | Effect
---                    |---
INBOX                  |Pop next value from INBOX to POINTER 
OUTBOX                 |Put value from POINTER to OUTBOX 
COPYFROM `<REF>`       |Copy value to POINTER        
COPYTO   `<REF>`       |Copy value to referenced register
ADD      `<REF>`       |Adds value from REF to POINTER
SUB      `<REF>`       |Subtracts value from REF to POINTER
BUMPUP   `<REF>`       |Increment value of REF and copy it into POINTER
BUMPDN   `<REF>`       |Decrement value of REF and copy it into POINTER
LABEL                  |A flag will be jumped 
JUMP     `<LABEL>`     |Jump to LABEL
JUMPZ    `<LABEL>`     |Jump to LABEL if POINTER is zero
JUMPN    `<LABEL>`     |Jump to LABEL if POINTER is negative


## REF
REF declares which register to use for operator, there are two types available:
- Direct access: `1`
- Indirect access: `[1]`
-- Accesses the register, defined by the value of declared register 

Example:
```
INBOX //1
COPYTO 1
BUMPUP [1]
COPYFROM 1
OUTBOX //2
```

## JUMP/LABEL
With a JUMP operator the PC (program counter - defines which position in code should be interpreted)
will set to the given LABEL

Example:
```
INBOX //1
COPYTO 1
JUMP a
BUMPUP 1 //Skipped
a:
OUTBOX //1
```

## POINTER
The machine is able to keep one value on the "BUS" (keep it active).
This value is used in operations like outbox or inbox.

## Roadmap

### Backend
[x] Return new state from tick <br>
[x] Create level module holding state, messages and check 1-4<br>
[x] Support character as values (only subtraction with two chars allowed)<br>
[ ] Create level module holding state, messages and check 4-...<br>


### GUI
[x] Undo Button to go back to previos state <br>
[x] Reset button setup first state <br>
[x] En- and disable buttons <br>
[x] Editable code window <br>
[x] Highlight code and mark errors<br>
[x] Load menu for Level <br>
[x] Load code from file<br>
[x] Add scrollbar to code editor<br>
[x] Center window
[-] Show when program finishes <br>
[x] Show errors when they occur <br>
[x] Add disabled state buttons
[x] Show level check result <br>
[x] Hotkeys: Duplicate Line (Ctrl/CMD-D) <br>
[x] Editable inbox window <br>
[x] Editable regs window <br>
[x] Add help for syntax in some way<br>
[x] Automatic timer for tick (Slider 1s-5s) (With "Play" and "Pause" button?)<br>
[ ] Use icons <br>
[ ] Save code to file<br>
[ ] Copy solution to clipboard <br>
[ ] Paste solution from clipboard <br>
[ ] Hotkeys: Move Up   (Ctrl/CMD-Up) <br>
[ ] Hotkeys: Move Down (Ctrl/CMD-Down) <br>
[ ] Hotkeys: Delete Line (Ctrl/CMD-BackSpace) <br>
[ ] Add statistics about execution <br>
[-] Redesign gui (remove borders, add colors, backgrounds, ...)<br>
[ ] Experiment: Use pymitter events to manage gui state and updates <br>


Icon Sources:
[Icon8](https://icons8.com/web-app/category/all/Very-Basic)