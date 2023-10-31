v {xschem version=3.4.3 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
C {madvlsi/nmos3.sym} 210 0 0 0 {name=M1
L=0.15
W=1
body=GND
nf=1
mult=1SSS
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {devices/iopin.sym} 210 -30 3 0 {name=p1 lab=VDD}
C {devices/iopin.sym} 210 30 1 0 {name=p2 lab=GND}
C {devices/iopin.sym} 180 0 2 0 {name=p3 lab=Vg}
