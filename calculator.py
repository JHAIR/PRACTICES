class Calculator:
    def add(self, val1, val2):
        value = val1 + val2
        return value

    def age(self, val1):
        if (val1>0 and val1<101):
            return 1
        else:
            return 0


    def comparar(self, val1, val2):
        if(val1>=val2):
            return val1
        else:
            return val2

    def max(self, val1, val2, val3):
        aux = self.comparar(val1, val2)
        return self.comparar(aux, val3)

    def numero(self, val1):
         val1 = ord(val1)
         if (val1 >= 48 and val1 <= 57):
             return 1
         else:
             return 0


    def vocal(self, val1):
        return val1 == 'a' or val1 == 'e' or val1 =='i' or val1 =='u' or val1 == 'o' or val1 =='A' or val1 =='E' or val1 =='I' or val1 =='O' or val1 =='U'


    def letra (self, val1):
        val2 = ord(val1)
        if ((val2 >= 97 and val2 <= 122) or ( val2 >= 65 and val2 <= 90)):
            return self.vocal(val1)
        else:
            return 1


    def invertir(self, val1):
        aux = ''
        for i in range (len(val1)):
            aux = val1[i] + aux
        return aux

    def maxcadena(self, val1):
        tam = len(val1[0])
        cadaux = val1[0]
        for i in range (len(val1)):
            if(tam < len(val1[i])):
                tam = len(val1[i])
                cadaux = val1[i]
        return cadaux






