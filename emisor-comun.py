#Location: /mnt/HDD/Universidad/EleApl2/03LAB

import numpy as np

#------------------------------------------------------------------------------
#FUNCIONES:
#------------------------------------------------------------------------------
#Paralelo entre dos resistores:
def shunt(R1,R2):
    return (R1*R2)/(R1+R2)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#PARAMETROS DE DISEÑO:
#------------------------------------------------------------------------------
hfe = 253
Ic  = 1e-3       #[A]
Ib  = Ic / hfe   #[A]
Ie  = (hfe+1)*Ib #[A]

Vcc = 12         #[V]
Vbe = 0.7        #[V]
Vt  = 26e-3      #[V]
VRC = 0.45 * Vcc #[V]
VCE = 0.45 * Vcc #[V]

Rs  = 50         #[Ohm]
RL  = 10e3       #[Ohm]

C1  = 1e-6       #[F]
C2  = 10*C1      #[F]
CE  = (hfe+1)*C1 #[F]

Tf  = 409.5e-9   #[s]
Cb  = Tf*Ic/Vt   #[F]
Cje = 11.5e-9    #[F]

Cmu0= 0.5e-9     #[F]
vje = 0.5        #[V]

gm  = Ic / Vt    #[S]
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#POLARIZACION:
#------------------------------------------------------------------------------
RC  = VRC / Ic
RE  = Vcc * (1 - 0.45 - 0.45) / (((hfe+1)/hfe) * Ic)

Rth = hfe * RE / 10
RB  = Rth
Vth = Ib * Rth + Vbe + Ie * RE

fact_R1 = (Vcc - Vth) / Vth
R2 = ((fact_R1 + 1) / fact_R1) * Rth
R1 = fact_R1 * R2

Rpi = hfe * Vt / Ic

#Imprimir:
print('R1 = ', R1)
print('R2 = ', R2)
print('RC = ', RC)
print('RE = ', RE)
print('Rth = ', Rth)
print('Vth = ', Vth)
print('IB = ', Ib)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#RESPUESTA EN FRECUENCIA:
#------------------------------------------------------------------------------
Rpi = hfe * Vt / Ic
Bf  = Rpi * gm

#Frecuencia de corte inferior:
RC1 = Rs + shunt(RB,Rpi)
FC1 = 1 / (2 * np.pi * RC1 * C1)

RC2 = RC + RL
FC2 = 1 / (2 * np.pi * RC2 * C2)

RCE = shunt(RE, (Rpi + shunt(Rs,RB))/(1+Bf))
FCE = FC2 = 1 / (2 * np.pi * RCE * CE)

print('FC1 = ', FC1)
print('FC2 = ', FC2)
print('FCE = ', FCE)

#Frecuencia de corte superior:
RCpi = shunt(Rpi, shunt(Rs,RB))
RCmu = shunt(RL,RC) + RCpi * (1 + gm*shunt(RL,RC))

Cpi  = Cb + Cje

VC   = VCE + Ie*RE
VB   = Vbe + Ie*RE
VCB  = VC - VB
Cmu  = Cmu0 / (1 + VCB/vje)**(1/3)

FH   = 1 / (2 * np.pi *(RCpi*Cpi + RCmu*Cmu))

print('Cpi = ', Cpi)
print('Cmu = ', Cmu)
print('FH = ', FH)
#------------------------------------------------------------------------------
