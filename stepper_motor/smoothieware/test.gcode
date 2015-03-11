; Start at X/Y Zero
G0 X0 Y0
; Make a regular move with an arbitrary  speed
; 1.885 s
G1 X200 Y200 F9000 
; Move one axis a long distance, another axis a short distance AND change the speed.
; 0.500 s
G1 X190 Y0 F24000
; Move back to Zero
; 0.475 s
G0 X0 Y0

