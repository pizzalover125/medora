# journal

### 5/24 (90 min)
- i started this project a while back
- the idea is to create a smart pill organizer
- lots of seniors die due to improper medication
- the status quo is filled with overpriced solutions
- my previous work can be viewed here: https://docs.google.com/document/d/1gj0a-iJIHle2tvecCM2r5ncjlf6axlyIEGGkNLvfImo/edit?tab=t.5onzl3533ios
- i've alr made the schematic... time for PCB!

<img width="648" height="501" alt="image" src="https://github.com/user-attachments/assets/fd3ca182-f26d-4b24-bffe-01a373564474" />

- ill research some dimensions
- ok did some more research on the problem
- ill start with CAD because I need to visualize the exact design
- The EllieGrid dimensions in millimeters are approximately 197 mm × 108 mm × 32 mm. (thing below)

<img width="524" height="551" alt="image" src="https://github.com/user-attachments/assets/5476010a-f3b3-4874-846e-7bcf200eb520" />

- used Claude to calculate dimensions

<img width="757" height="144" alt="image" src="https://github.com/user-attachments/assets/f1977ccd-3310-4a33-85b7-d4a314afe62e" />
<img width="1028" height="676" alt="image" src="https://github.com/user-attachments/assets/ea2d911d-0123-449d-beb1-8e3db41ac840" />

- looks pretty decent!
- ok i made the general design

<img width="710" height="466" alt="image" src="https://github.com/user-attachments/assets/c629c70e-e828-4123-a21b-babe488e905a" />
<img width="460" height="345" alt="image" src="https://github.com/user-attachments/assets/e4f93abf-4512-457f-b1f1-94e40801946e" />

- renders are sooooo awesome
- going to watch https://www.youtube.com/watch?v=kKsVUTRPM3k to learn more
- built a lid!

<img width="1187" height="631" alt="image" src="https://github.com/user-attachments/assets/e3829367-802c-44f7-bad6-6bd978c0d9dd" />

- added the cutout

<img width="196" height="123" alt="image" src="https://github.com/user-attachments/assets/f35e7f90-fb8f-4a79-984e-3877e50eefe6" />

- seems like printing PETG/PLA is not food-safe so i'll need containers
- might redesign the case to add the containers
- but that shouldn't be a problem for v1 of this

### 6/6 (started 4:30)
- going to work on PCB now!
- seems like some of the footprints got corrupted
- will fix!

<img width="175" height="282" alt="image" src="https://github.com/user-attachments/assets/59f5a634-67b5-4229-afa4-2e73cd114753" />

- fixed!
- calculated these values:

Top row (y = 28):
(26.13, 28)
(74.38, 28)
(122.63, 28)
(170.88, 28)

Bottom row (y = 80):
(34.17, 80)
(98.50, 80)
(162.83, 80)

- these took a while lol
- did not think id use mean function this much back when i was in like 4th grade

<img width="789" height="381" alt="image" src="https://github.com/user-attachments/assets/62701cad-b85f-4988-bf6a-189f2ae4c4af" />

- looks pretty good

<img width="224" height="172" alt="image" src="https://github.com/user-attachments/assets/487a1f45-853c-40db-8c3b-0b41a12a037b" />

- added 3d model of Xiao!

<img width="757" height="367" alt="image" src="https://github.com/user-attachments/assets/4a485e3f-2b7e-4fea-a3ed-79bddd85f46a" />

- routing done!

### 6/7: 1hr
- ok first things first imma add mounting holes

<img width="708" height="342" alt="image" src="https://github.com/user-attachments/assets/852bcfdc-7fb4-44ea-bb52-2f475dd988ef" />

- voila!
- before i modify the CAD, i want to create a quick BOM
- ok its $31.18 for the parts at a quantity of 5
- 5 PCBs comes out to 26.65 at quantity of 5
- ok 11.56 / PCB + CAD costs
- SEEED Studio kinda broken rn but
- so hopefully under ~$20!
- thats great to hear
- time to start up CAD!

<img width="778" height="585" alt="image" src="https://github.com/user-attachments/assets/221da533-639b-4f9c-bed6-910730446704" />

- super quick iteration!

### 6/19 (2 hours)
- okay haven't worked on this in a hot minute
- have been working on other projects
- time to lock in for this!
- first thing: delete m2 holes and add m3
- bruh i have to reroute because i have to move microcontroller down

<img width="836" height="111" alt="image" src="https://github.com/user-attachments/assets/6bc2b674-2936-4664-9ba3-fd1921aa5cc0" />

- asked that question in Slack to make sure

<img width="815" height="384" alt="image" src="https://github.com/user-attachments/assets/1fbab844-2351-4123-a742-864c1a2e21a7" />

- going to do what alex recommended and just work with a rough sketch in CAD of the PCB
- i think ill make it battery powered cause it shouldnt be too hard to?
- i could just easily wire up a lipo to the thing

<img width="1242" height="456" alt="image" src="https://github.com/user-attachments/assets/70b1a30f-e366-4f37-a09b-6ac31a8bac24" />

- redesigned it
- going to look up what mates are
- added screws
- watching https://www.youtube.com/watch?v=0hI57MksVyk

<img width="1489" height="683" alt="image" src="https://github.com/user-attachments/assets/b0875dbd-b353-436e-947d-d3f5fe479de3" />

- works pretty well!

<img width="125" height="154" alt="image" src="https://github.com/user-attachments/assets/7785ebc3-4d4d-4a93-aaff-c00b341638a2" />

- added USB-C hole

<img width="1292" height="604" alt="image" src="https://github.com/user-attachments/assets/ec8aac60-5991-4aff-9ab9-6ba52d3b54e7" />

- added mounting holes for top
- i have to make this less thick some way
- going to add holes for LEDs

<img width="819" height="621" alt="image" src="https://github.com/user-attachments/assets/80fbf9a1-f07b-469d-bb1f-91ded448ff24" />

- added the holes!

<img width="411" height="518" alt="image" src="https://github.com/user-attachments/assets/42d0c2d1-63c8-4437-b66b-f83b40d8a0b5" />

- added display hole
- realized actual display isn't even centered

<img width="250" height="310" alt="image" src="https://github.com/user-attachments/assets/b99252dd-8881-47d2-b06d-8abc4c0385a5" />

- ok im going to add an actuall border cause i'm using exact dimensions

<img width="856" height="446" alt="image" src="https://github.com/user-attachments/assets/b00939cb-bb04-435b-8aea-f9c9b04c71c9" />
