# medora
A smart pill organizer. A project that saves lives.

### Why medora?
Medication nonadherence is the failure to take medication as prescribed, whether by skipping doses, taking the wrong amount, or stopping treatment early.

* Medication nonadherence contributes to roughly 125,000 deaths every year in the U.S. (Kim and Sarah A.)
* Pill organizer users saw adherence rise from 65% to as high as 100% within months (Rathod et al.)
* Patients using a smart pill organizer were 60% more compliant than those without one, nearly double the 32% improvement seen with a standard pillbox (Godin)

In the status quo, there smart pill organizers are expensive costing an average of $150 - $200 with an added monthly subscription on top. For many Americans, this is simply too out-of-reach. Additionally, many of the apps that come with the organizers are outdated and hard to use. I wanted to fix this by creating a low-cost, modern, smart pill organizer. 

### PCB

The PCB was designed in KiCAD.

<img width="1327" height="263" alt="image" src="https://github.com/user-attachments/assets/d55f67c9-0b52-4dbc-b15a-4ef5547be7c1" />
<img width="866" height="423" alt="image" src="https://github.com/user-attachments/assets/ff4512f1-9926-4c13-b13b-70cec9a9396c" />
<img width="639" height="385" alt="image" src="https://github.com/user-attachments/assets/378f7308-d80d-4265-91e1-f34ab34a695c" />

### CAD

The CAD was designed in Onshape. You can view the link here: https://cad.onshape.com/documents/c1d6b76cfe1063ae9996d35d/w/b74057f0558c55e37de9882a/e/dce7fc6940c214e434cc5424?renderMode=0&uiState=6a616dc37022e90ea2108f99. There are magnets that hold together the lid and the case. 

<img width="595" height="513" alt="image" src="https://github.com/user-attachments/assets/60a44404-20b7-413a-8400-6fe3db22d747" />
<img width="1061" height="558" alt="image" src="https://github.com/user-attachments/assets/d291c3cd-82fa-4f34-b5f1-d671aaff43d8" />
<img width="609" height="490" alt="image" src="https://github.com/user-attachments/assets/821ff124-0c59-4dd7-9b43-0ef862123dba" />

### BOM 
A detailed bill of materials can be viewed here: https://docs.google.com/spreadsheets/d/15uKd0en9vIonSRlWCDsz52HICyDAk6iSbPfcEML8UvA/edit?usp=sharing.

### Credits
Big thanks to Hack Club for making this project possible!

### Sponsorship

This project's PCBs are sponsored by PCBWay, a leading manufacturer for PCB fabrication, assembly, 3D printing, and more.

#### About PCBWay

PCBWay offers PCB prototyping and manufacturing, PCB assembly, 3D printing, CNC machining, and other on-demand manufacturing services for makers, students, and engineers worldwide.

#### Project Background

This is a smart pill organizer — an 8-compartment device with LED indicators to help users track and remember their medication schedule. Building it required a custom PCB to house the microcontroller, LED drivers, and compartment sensors in a compact enclosure.

#### Order Process

1. **Download the Gerber files** from this repo.
2. **Go to [PCBWay.com](https://www.pcbway.com)** and click **"Instant Quote"** on the homepage.
3. **Upload the Gerber `.zip`** from this repo. PCBWay auto-detects your board dimensions, layer count, and other specs — verify these match: 190mm × 90mm, 2-layer.
4. **Set your order specs:**
   - Quantity (e.g. 5 or 10 boards)
   - Board thickness (1.6mm)
   - Copper weight (1oz standard)
   - Surface finish (HASL or ENIG)
   - Solder mask & silkscreen color
5. **Review the quote** and confirm cost/production time.
6. **Place the order** and confirm shipping address/method.
7. **Track production** — PCBWay provides status updates through fabrication and a tracking number once shipped.

#### Unboxing

Will be updated once I receive the boards!

#### Board Dimensions & Precision

Board size: 190 mm × 90 mm
Board thickness: 1.6 mm (standard)
Copper layers: 2-layer
Minimum trace width: 0.2 mm (KiCad default)
Minimum clearance: 0.2 mm (KiCad default)
Via diameter / drill: 0.6 mm / 0.3 mm (KiCad default)
Surface finish: HASL

#### End Application

The board powers the pill organizer's control system — driving LED indicators for each of the 8 compartments and interfacing with the microcontroller to track dosage timing.

#### Why PCBWay
* Fast turnaround for prototyping
* Reliable build quality at low cost for small-batch orders
* Easy Gerber upload and ordering process
* Good support for hobbyist and student projects
