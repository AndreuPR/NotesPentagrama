import nota
import escala
class partitura:
    def __init__(self, nom):
        self.nom = nom
        self.escalaCromatica = [
        ['sol#', 0], ['sol', 0], ['la', 0], ['la#', 0], ['si', 0],
        ['do', 1], ['do#', 1], ['re', 1], ['re#', 1], ['mi', 1], ['fa', 1], ['fa#', 1], ['sol', 1], ['sol#', 1],  ['la', 1], ['la#', 1], ['si', 1],
        ['do', 2], ['do#', 2], ['re', 2], ['re#', 2], ['mi', 2], ['fa', 2], ['fa#', 2], ['sol', 2], ['sol#', 2],  ['la', 2], ['la#', 2], ['si', 2]]

    def combinar_llistes(self, *llistas):
        combinades = []
        combinadesStr = ""
        for elementos in zip(*llistas):
            combinades.append("".join(elementos))
            combinadesStr += "".join(elementos)
        return combinadesStr

    
    def ferLlistaNotes(self, args):
        final = ['  \n', ' - \n', '   \n', ' - \n', '   \n', '---\n', '   \n', '---\n', '   \n', '---\n',
                    '   \n', '---\n', '   \n', '---\n', '   \n', '   \n', '   \n'][::-1]
        
        llistaNotes = []
        for i in args:
            llista = nota(i[0], i[1]).getLlista()
            llistaNotes.append(llista)

        llistaNotes.append(final)
    
        return llistaNotes
    
    def crearPartitura(self, llistaNotes):
        return self.combinar_llistes(*self.ferLlistaNotes(llistaNotes))
    
    