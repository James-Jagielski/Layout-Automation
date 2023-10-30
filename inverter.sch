v {xschem version=3.4.3 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 100 -120 100 -30 {
lab=A}
N 140 -90 140 -60 {
lab=Y}
N 140 -80 190 -80 {
lab=Y}
N 100 -120 110 -120 {
lab=A}
N 100 -30 110 -30 {
lab=A}
N 40 -80 100 -80 {
lab=A}
N 140 -160 140 -150 {
lab=VP}
N 140 -150 140 -120 {
lab=VP}
N 140 -30 140 0 {
lab=VN}
C {devices/ipin.sym} 40 -80 0 0 {name=p2 lab=A}
C {devices/iopin.sym} 140 -160 3 0 {name=p3 lab=VP}
C {devices/iopin.sym} 140 0 1 0 {name=p4 lab=VN}
C {devices/opin.sym} 190 -80 0 0 {name=p5 lab=Y}
C {madvlsi/pmos4.sym} 140 -120 0 0 {name=M2
L=0.15
W=2
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {madvlsi/nmos4.sym} 140 -30 0 0 {name=M1
L=0.15
W=1
nf=1 
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
