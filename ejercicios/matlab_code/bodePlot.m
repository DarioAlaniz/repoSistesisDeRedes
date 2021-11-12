clc;close all;clear all;
%_____Compensador Cero-Polo(Adelanto-atrazo)
%_____Parametros__________
f1 = 200e3;f2 = 5.5e6;Ri=10e3;Rf=100e3;
fzc = f2; fpc = 60.5e6;
R1 = 1e3;R2 = 3.27e3;
s = tf('s');
%R1 = Ri;R2 = Rf;
K  = Ri/(Ri+Rf);
K_inv  =zpk((1/K))
w1 = 2*pi*f1;
w2 = 2*pi*f2;
Ad = db2mag(70);
Att_c = 1;
wzc   = w2;
wpc   = 2*pi*fpc;
Ac = zpk((Att_c * (1+s/wzc))/(1+s/wpc))
%Av = zpk( ((Rf/(Ri+Rf))*Ad) / ((1+s/w1)*(1+s/w2)))
Av = zpk( ((1)*Ad) / ((1+s/w1)*(1+s/w2)))
Av_c = Ac * Av 
%Avf = Av_c / (1-(K*Av_c))
Avf = feedback(Av_c,K)
%_____Plots________
op = bodeoptions;
op.FreqUnits = 'Hz';
figure(1)
bodeplot(Av_c,K_inv,op);grid on
figure(2)
bodeplot(Avf,op);grid on
%%
clc;close all;clear all;
%_____Compensador Polo-Cero (atrazo-adelanto)
%_____Parametros__________
f1 = 800e3;f2 = 4e6;R1=10e3;R2=100e3;
fzc = f1; fpc = 13.87e3;
Rx = 146;
s = tf('s');
K  = R1/(R1+R2);
K_inv  = zpk((1/K))
w1  = 2*pi*f1;
w2  = 2*pi*f2;
wzc = 2*pi*fzc;
wpc = 2*pi*fpc;
Ad  = db2mag(70);
%_____FunT__________
Av  = zpk( Ad / ((1+s/w1)*(1+s/w2)))
Ac  = zpk((1+s/wzc)/(1+s/wpc))
Av_c = Ac * Av
%_____Plot__________
op = bodeoptions;
op.FreqUnits = 'Hz';
bodeplot(Av,Av_c,K_inv,op);grid on;legend('Av','Avc','1/K');

%%
%________Compesador por polo dominante (atrazo)
clc;close all;clear all;
s = tf('s');
f1 = 800e3;f2 = 4e6;R1=10e3;R2=100e3;Mf=45;
fpc = 2e3;
K  = R1/(R1+R2);
K_inv  = zpk((1/K))
w1  = 2*pi*f1;
w2  = 2*pi*f2;
wpc = 2*pi*fpc;
Ad  = db2mag(70);
%_____FunT__________
Av  = zpk( Ad / ((1+s/w1)*(1+s/w2)))
Ac  = zpk(1/(1+s/wpc))
Av_c = Ac * Av
%_____Plot__________
op = bodeoptions;
op.FreqUnits = 'Hz';
bodeplot(Av,Av_c,K_inv,op);grid on;legend('Av','Avc','1/K');

%%
%Amplificador compuesto
clc;close all;clear all;
s = tf('s');
f1 =10.75;f2 = 6.4e6;Ri=10e3;Rf=100e3;R1=302;R2=1.58e3;
Ct = 4.8e-12; Rt=2.37e6;
fh = 1/(2*pi*Ct*R2);

K  = Ri/(Ri+Rf);
K_inv  = zpk((1-1/K))
w1  = 2*pi*f1;
w2  = 2*pi*f2;
wh = 2*pi*fh;
Ad  = db2mag(107);
Av    = zpk( Ad / ((1+s/w1)*(1+s/w2)))
Avf2  = zpk( (1+R2/R1) / (1+s/wh))
Av_c  = Avf2 * Av
Avf   = feedback(Av_c,K)
%_____Plot__________
op = bodeoptions;
op.FreqUnits = 'Hz';
bodeplot(Av,Av_c,K_inv,Avf2,Avf,op);grid on;legend('Av','Avc','1-1/K','Avf2','Avf');




