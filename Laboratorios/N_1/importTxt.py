def abrir_datos (): # nombre , alias , correo
    " Abrir un archivo que tiene guardada la info [ key ], [ Val[0]] ,[ Val [1] ... ]"
    vec =[]
    dicc = {}
    # f = open ( input (" nombre ")+'.txt', 'rt')
    f =  open ('Draft3.txt', 'rt') #cambiar path
    for line in f:
        vec = line.strip('\n').split('\t')
        dicc [str(vec[0])]= list(vec [1:])
    f.close()
    # print(dicc)
    Planilla_ = dict(dicc)
    return Planilla_

planilla        = abrir_datos()
frequency       = []
mod             = []
phase           = []

for key in planilla:
    if(key != 'Freq.'):
        frequency.append(float(key))
        data = planilla[key][0].strip('()').split(',')
        mod.append(float(data[0].strip('dB')))
        phase.append(float(data[1].strip('°')))


data = {'Freq': frequency,'Mod': mod,'Phase':phase}

