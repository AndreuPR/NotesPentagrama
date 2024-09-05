import partitura
class escala:
    def __init__(self, nom):
        self.nom = nom
        self.escalaCromatica = [['sol#', 0], ['sol', 0], ['la', 0], ['la#', 0], ['si', 0],
        ['do', 1], ['do#', 1], ['re', 1], ['re#', 1], ['mi', 1], ['fa', 1], ['fa#', 1], ['sol', 1], ['sol#', 1],  ['la', 1], ['la#', 1], ['si', 1],
        ['do', 2], ['do#', 2], ['re', 2], ['re#', 2], ['mi', 2], ['fa', 2], ['fa#', 2], ['sol', 2], ['sol#', 2],  ['la', 2], ['la#', 2], ['si', 2]]
        
        
    def ordenarEscalaCromatica(self ,nota, octavica=False, bidireccional=False):
        try:
            posicioNota = self.escalaCromatica.index(nota)
            if octavica == True:
                escala_octava = self.escalaCromatica[posicioNota:posicioNota+13]
                escala_octava_rev = escala_octava[::-1]
                if bidireccional == True:
                    return escala_octava + escala_octava_rev
                return self.escalaCromatica[posicioNota:posicioNota+13]
            return self.escalaCromatica[posicioNota:]
        except:
            return self.escalaCromatica
        
    def ferEscala(self, nota, patro):
        # Un patro es T, T, S, T, T, S, T
        dic_patrons = {"T":2, "S":1}
        llistaIndexEscalaBuscada = []
        pos = 0
        for i in range(len(patro)):
            llistaIndexEscalaBuscada.append(pos)
            pos += dic_patrons[patro[i]]
            
        
        escalaPartir = self.ordenarEscalaCromatica(nota, False, False)
        
        return [escalaPartir[i] for i in llistaIndexEscalaBuscada]
    
    def retornarPartituraeEscala(self, nota, patro):
        return partitura.crearPartitura(self.ferEscala(nota,patro))
        
        