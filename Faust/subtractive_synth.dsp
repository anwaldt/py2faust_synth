 

import("stdfaust.lib");  


//////////////////////////////////////////////////////////////////
// oscillators
//////////////////////////////////////////////////////////////////

// some basic stuff
sr = SR;
twopi = 2.0*PI;

// define the waveform
ts =  1<<16 ;
time = (+(1) ~ _ ) , 1 : - ;
sawwave =  ((float(time) / float(ts)) *2 -1)*-1;
sqaurewave = sawwave : >(0.0);
 
phase = os.hs_phasor(ts,midifreq,trig);

saw_osc( freq) = rdtable ( ts , sawwave , int ( phase  ) ) ;
square_osc( freq) = rdtable ( ts , sqaurewave , int ( phase  ) ) ;

mix = hslider("mix", 0, 0, 1, 0.01);

oscillo(fre) =  saw_osc(fre) *mix + square_osc(fre)*(1-mix);

//////////////////////////////////////////////////////////////////
// ENV
//////////////////////////////////////////////////////////////////

env1 = en.adsre(att1,dec1,sus1,rel1,gater);
att1 = 0.01 * (hslider ("att1[style:knob]",0.1,0.1,400,0.001));
dec1 = 0.01 * (hslider ("dec1[style:knob]",60,0.1,400,0.001));
sus1 = hslider ("sus1[style:knob]",0.2,0,1,0.001); 
rel1 = 0.01 * (hslider ("rel1[style:knob]",100,0.1,400,0.001));

env2 = en.adsre(att2,dec2,sus2,rel2,gater);
att2 = 0.01 * (hslider ("att2[style:knob]",0.1,0.1,400,0.001));
dec2 = 0.01 * (hslider ("dec2[style:knob]",60,0.1,400,0.001));
sus2 =         hslider ("sus2[style:knob]",0.2,0,1,0.001); 
rel2 = 0.01 * (hslider ("rel2[style:knob]",100,0.1,400,0.001));


gater = button ("gater");
midifreq = hslider("freq", 440, 20, 20000, 1);
midigain = hslider("gain", 0.5, 0, 0.5, 0.01); 

 

//////////////////////////////////////////////////////////////////
// VCF
//////////////////////////////////////////////////////////////////

res = hslider("resonnance",0.5,0,1,0.001):si.smoo;
fr  = hslider("fc", 10, 10, 12000, 0.001):si.smoo;
envMod = hslider("envMod",0,0,12000,0.01):si.smoo;

 
cutoff = fr + (envMod * env2) : min(ma.SR/8);



trig =  pm.impulseExcitation(gater);
//oscillo(f) = os.hs_phasor(2048,f);

// VCA
volume = midigain * env1;

 
// SYNTH ////////////////////////////////////////////////
synth = (oscillo(midifreq) :ve.moog_vcf(res,cutoff)) * volume;

// PROCESS /////////////////////////////////////////////
process = synth <: _,_ ;