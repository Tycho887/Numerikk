# -*- coding: utf-8 -*-
"""
Created on Sat May 20 16:39:49 2023

@author: Michael Johansen
"""

from math import *
import matplotlib.pyplot as plt
import numpy as np

InntektStudie = 137905

TimeLønnMG  = 180   ;   TimerMG  = 3.75*52
TimeLønnMN  = 185    ;   TimerMN  = 10
TimeLønnHOM = 225    ;   TimerHOM = 20

InntektJobb = TimeLønnHOM*TimerHOM + TimeLønnMG*TimerMG + TimeLønnMN*TimerMN

Ekstra_inntekt = 0

Total_Inntekt = InntektStudie + InntektJobb + Ekstra_inntekt

# Utgifter

Utgift_Mat = 80*31*12
Utgift_subscription = 12*(70+70)
Utgift_Ekstra = 12*(400)
Utgift_Leie = 12*5200

Total_utgift = Utgift_Ekstra+Utgift_Leie+Utgift_Mat+Utgift_subscription

# Netto

Netto = Total_Inntekt - Total_utgift

# Sparinger

BSU_sparing = 27500
Ekstra_sparing = 700*12
Fond_sparing = Netto-BSU_sparing

# renter

BSU_rente = 1.0545
Fond_rente = 1.1

def BSU(år):
    return BSU_sparing*np.ceil(år)*BSU_rente**år

def Fond(år):
    return Fond_sparing*np.ceil(år)*Fond_rente**år
    
def HusSparing(år):
    return BSU(år)+Fond(år)-Ekstra_sparing*år

def Total_sparing(år):
    return BSU(år)+Fond(år)

# StudieLån

def Lån(år):
    return år*82400

# Visualisering
    
SpareVindu = np.linspace(0,7,200)

plt.scatter(SpareVindu,HusSparing(SpareVindu),color='blue',s=3)
plt.scatter(SpareVindu,BSU(SpareVindu),color='green',s=1)
plt.scatter(SpareVindu,Fond(SpareVindu),color='red',s=1)

plt.savefig('data/graf.png', dpi=1024)

plt.show()

print(f"""
--------------------Inntekt---------------------
    
    Årlig
    
    SL:  {InntektStudie:.0f}
    HoM: {TimeLønnHOM*TimerHOM:.0f} kr
    MN:  {TimeLønnMN*TimerMN:.0f} kr
    MG:  {TimeLønnMG*TimerMG:.0f} kr
    Ekstra: {Ekstra_inntekt:.0f} kr
    
    Total: {Total_Inntekt:.0f} kr
    
    Månedlig
    
    Jobb: {InntektJobb/12:.1f} kr
    Studielån: {InntektStudie/12:.1f} kr
    
    Total: {Total_Inntekt/12:.1f} kr

--------------------utgift---------------------
    
Årlig
    
    Mat: {Utgift_Mat:.0f} kr
    Leie: {Utgift_Leie:.0f} kr
    Subscriptions: {Utgift_subscription:.0f} kr
    Ekstra: {Utgift_Ekstra:.0f} kr
    
    Total: {Total_utgift:.0f} kr
    
Månedlig
    
    Mat: {Utgift_Mat/12:.1f} kr
    Leie: {Utgift_Leie/12:.1f} kr
    Subscriptions: {Utgift_subscription/12:.1f} kr
    Ekstra: {Utgift_Ekstra/12:.1f} kr
    
    Total: {Total_utgift/12:.0f} kr
    
--------------------Sparing---------------------
    
    Årlig: {Netto:.0f} kr
    Månedlig: {Netto/12:.1f} kr

Antatt hussparesum i 2030: {HusSparing(7):.0f} kr
Ekstra sparing hvert år: {800*12} kr

Maksimal lånesum ved 15% egenkapital: {(HusSparing(7)/0.15*10e-7):.3f} millioner kr""")