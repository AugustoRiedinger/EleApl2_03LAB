%% LABORATORIO 3 - APII: Cálculos de polarización, resistencias y capacitancias
%% Datos:
hfe = 100   ;   % [ ]
Ic  = 2e-3  ;   % [A] 
Ib  = Ic/hfe;   % [A]
%--------------------
Vcc = 12;       % [V]
Vce = Vcc/2 - 1;% [V]
Vbe = 0.7;      % [V]
Vb  = Vcc/2 + 2;% [V]
Vje = 0.8;      % [V]
Vjc = 0.8;      % [V]
Vt  = 26e-3;    % [V]
%--------------------
RS = 50;        % [O]
RL = 10e3;      % [O]
%--------------------
C1 = 1e-6;      % [F]
C2 = 1e-6;      % [F]
CE = 1e-6;      % [F]
Cj0 = 1e-12;    % [F]
Cu0 = 1e-12;    % [F]
tf  = 1e-6;     % [?]
%--------------------

%% Cálculos
R1 = Vcc / (20 * Ib);            % [O]         
R2 = R1;                         % [O]
RE = (Vcc - Vb - Vbe) / Ic;      % [O]
RC = (Vcc - Vce) / (2 * Ic) - RE;% [O]
RB = shunt(R1,R2);               % [O]
hie = Vt*hfe/Ic;                 % [O]
gm  = hfe/hie;                   % [M]
%------------------------------------
Cj  = Cj0/(1 - Vbe/Vje)^(1/3);   % [F] 
Cb  = tf * Ic/Vt;                % [F]
CP  = Cj + Cb;                   % [F]
CU  = Cu0/(1 + Vce/Vjc)^(1/3);   % [F]
%------------------------------------

%% EMISOR COMÚN
RC1 =  shunt(RB, hie) + RS;                 % [O]
RC2 = RC + RL;                              % [O]
RCE = shunt(RE, (hie+shunt(RB,RS))/(hfe+1));% [O]
RCP = three_shunt(hie,RB,RS);               % [O]
RCU = three_shunt(hie, RB, RS) + shunt(RC,RL)*(1+gm*three_shunt(hie,RB,RS));
%------------------------------------------------
fC1 = 1/(2*pi*RC1*C1);                      % [Hz]
fC2 = 1/(2*pi*RC2*C2);                      % [Hz]
fCE = 1/(2*pi*RCE*CE);                      % [Hz]
fL  = fC1 + fC2 + fCE;                      % [Hz]
fH  = 1/(2*pi*(RCP*CP + RCU*CU));            % [Hz]
%-------------------------------------------------




%% FUNCIONES 
function R = shunt(R1,R2)
    R = R1*R2/(R1+R2);
end

function R = three_shunt(R1, R2, R3)
    R = 1/(1/R1+1/R2+1/R3);
end
