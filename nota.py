class nota:
    def __init__(self, nota, octava):
      self.octava = octava
      self.nota = nota
      
      """  ♩   ♪    ♭   ♮   ♯  """
      simbol = "O"
      final = ["\n"] * 17
                    ##         1       2     3     4     5       6     7     8      9      10    11     12    13     14   15    16      17
      self.dic_notes = { 0:{
                      "sol": [f" {simbol} ", " - ","   ", " - ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "sol#":[f"#{simbol} ", " - ","   ", " - ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "solb":[f"b{simbol} ", " - ","   ", " - ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "la":  ["   ", f"-{simbol} ","   ", " - ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "la#": ["   ", f"#-{simbol}","   ", " - ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "lab": ["   ", f"b-{simbol}","   ", " - ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "si":  ["   ", "   ",f" {simbol} ", " - ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "si#": ["   ", "   ",f"#{simbol} ", " - ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "sib": ["   ", "   ",f"b{simbol} ", " - ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1]},
                    ##         1       2     3     4     5       6     7     8      9      10    11     12    13     14   15    16      17
                    
                    1:{
                      "do":  ["   ", "   ","   ", f"-{simbol} ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "do#": ["   ", "   ","   ", f"#-{simbol}","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "dob": ["   ", "   ","   ", f"b-{simbol}","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "re":  ["   ", "   ","   ", "   ",f" {simbol} ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "re#": ["   ", "   ","   ", "   ",f"#{simbol} ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "reb": ["   ", "   ","   ", "   ",f"b{simbol} ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "mi":  ["   ", "   ","   ", "   ","   ", f"-{simbol}-","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "mi#": ["   ", "   ","   ", "   ","   ", f"#{simbol}-","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "mib": ["   ", "   ","   ", "   ","   ", f"b{simbol}-","   ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "fa":  ["   ", "   ","   ", "   ","   ", "---",f" {simbol} ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "fa#": ["   ", "   ","   ", "   ","   ", "---",f"#{simbol} ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "fab": ["   ", "   ","   ", "   ","   ", "---",f"b{simbol} ", "---","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "sol": ["   ", "   ","   ", "   ","   ", "---","   ", f"-{simbol}-","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "sol#":["   ", "   ","   ", "   ","   ", "---","   ", f"#{simbol}-","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "solb":["   ", "   ","   ", "   ","   ", "---","   ", f"b{simbol}-","   ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "la":  ["   ", "   ","   ", "   ","   ", "---","   ", "---",f" {simbol} ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "la#": ["   ", "   ","   ", "   ","   ", "---","   ", "---",f"#{simbol} ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "lab": ["   ", "   ","   ", "   ","   ", "---","   ", "---",f"b{simbol} ", "---","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "si":  ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", f"-{simbol}-","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "si#": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", f"#{simbol}-","   ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "sib": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", f"b{simbol}-","   ", "---","   ", "---","   ", "   ", "   "][::-1]},
                    
                    ##         1       2     3     4     5       6     7     8      9      10    11     12    13     14      15    16      17   
                    2:{
                      "do":  ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---",f" {simbol} ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "do#": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---",f"#{simbol} ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "dob": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---",f"b{simbol} ", "---","   ", "---","   ", "   ", "   "][::-1],
                      "re":  ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", f"-{simbol}-","   ", "---","   ", "   ", "   "][::-1],
                      "re#": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", f"#{simbol}-","   ", "---","   ", "   ", "   "][::-1],
                      "reb": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", f"b{simbol}-","   ", "---","   ", "   ", "   "][::-1],
                      "mi":  ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---",f" {simbol} ", "---","   ", "   ", "   "][::-1],
                      "mi#": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---",f"#{simbol} ", "---","   ", "   ", "   "][::-1],
                      "mib": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---",f"b{simbol} ", "---","   ", "   ", "   "][::-1],
                      "fa":  ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", f"-{simbol}-","   ", "   ", "   "][::-1],
                      "fa#": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", f"#{simbol}-","   ", "   ", "   "][::-1],
                      "fab": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", f"b{simbol}-","   ", "   ", "   "][::-1],
                      "sol": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---",f" {simbol} ", "   ", "   "][::-1],
                      "sol#":["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---",f"#{simbol} ", "   ", "   "][::-1],
                      "solb":["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---",f"b{simbol} ", "   ", "   "][::-1],
                      "la":  ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", f"-{simbol} ", "   "][::-1],
                      "la#": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", f"#-{simbol}", "   "][::-1],
                      "lab": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", f"b-{simbol}", "   "][::-1],
                      "si":  ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", " - ", f" {simbol} "][::-1],
                      "si#": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", " - ", f"#{simbol} "][::-1],
                      "sib": ["   ", "   ","   ", "   ","   ", "---","   ", "---","   ", "---","   ", "---","   ", "---","   ", " - ", f"b{simbol} "][::-1]}
                    ##         1       2     3     4     5       6     7     8      9      10    11     12    13     14   15    16      17
                      }
        
        
    def veureDic(self, octava):
      return self.dic_notes[octava]
    
    def getOctava(self):
      return self.octava
    def getNota(self):
      return self.nota
    
    def getLlista(self):
      return self.dic_notes[self.octava][self.nota]
    
