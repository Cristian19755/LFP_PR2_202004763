import easygui
class AnalizadorSintactico:

    def __init__(self,tokens : list) -> None:
        self.errores = []
        self.tokens = tokens

    def agregarError(self,esperado,obtenido):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {}'''.format(obtenido,esperado)
        )

    def sacarToken(self):
        try:
            return self.tokens.pop(0)
        except:
            return None

    def observarToken(self):
        try:
            return self.tokens[0]
        except:
            return None
    
    def analizar(self):
        self.S()

    def S(self):
        self.INICIO()
    
    def INICIO(self):
        temp = self.observarToken()
        if temp == None:
            self.agregarError('reservada_RESULTADO | reservada_JORNADA | reservada_GOLES | reservada_TABLA | reservada_PARTIDOS | reservada_TOP | reservada_ADIOS ','EOF')
        elif temp.tipo == 'reservada_RESULTADO':
            self.RESULTADO()
        elif temp.tipo == 'reservada_JORNADA':
            self.JORNADA()
        elif temp.tipo == 'reservada_GOLES':
            self.GOLES()
        elif temp.tipo == 'reservada_TABLA':
            self.TABLA()
        elif temp.tipo == 'reservada_PARTIDOS':
            self.PARTIDOS()
        elif temp.tipo == 'reservada_TOP':
            self.TOP()
        elif temp.tipo == 'reservada_ADIOS':
            self.ADIOS()

    def RESULTADO(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_RESULTADO':
            token = self.sacarToken()
            if token.tipo == 'cadena':
                equipoA = token.lexema
                token = self.sacarToken()
                if token.tipo == 'reservada_VS':
                    token = self.sacarToken()
                    if token.tipo == 'cadena':
                        equipoB = token.lexema
                        token = self.sacarToken()
                        if token.tipo == 'reservada_TEMPORADA':
                            token = self.sacarToken()
                            if token.tipo == 'menorQue':
                                token = self.sacarToken()
                                if token.tipo == 'entero':
                                    temporadaI = token.lexema
                                    token = self.sacarToken()
                                    if token.tipo == 'guion':
                                        token = self.sacarToken()
                                        if token.tipo == 'entero':
                                            temporadaF = token.lexema
                                            token = self.sacarToken()
                                            if token.tipo == 'mayorQue':
                                                temporada = str(temporadaI) + '-' + str(temporadaF)
                                                ##################################################
                                            else:
                                                self.agregarError("mayorQue","EOF")
                                        else:
                                            self.agregarError("entero","EOF")
                                    else:
                                        self.agregarError("guion","EOF")
                                else:
                                    self.agregarError("entero","EOF")
                            else:
                                self.agregarError("menorQue","EOF")
                        else:
                            self.agregarError("reservada_TEMPORADA","EOF")
                    else:
                        self.agregarError("cadena","EOF")
                else:
                    self.agregarError("reservada_VS","EOF") 
            else:
                self.agregarError("cadena","EOF")
        else:
            self.agregarError("reservada_RESULTADO","EOF")

    def JORNADA(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_JORNADA':
            token = self.sacarToken()
            if token.tipo == 'entero':
                jornada = token.lexema
                token = self.sacarToken()
                if token.tipo == 'reservada_TEMPORADA':
                    token = self.sacarToken()
                    if token.tipo == 'menorQue':
                        token = self.sacarToken()
                        if token.tipo == 'entero':
                            temporadaI = token.lexema
                            token = self.sacarToken()
                            if token.tipo == 'guion':
                                token = self.sacarToken()
                                if token.tipo == 'entero':
                                    temporadaF = token.lexema
                                    token = self.sacarToken()
                                    if token.tipo == 'mayorQue':
                                        token = self.sacarToken()
                                        if token.tipo == 'guion':
                                            token = self.sacarToken()
                                            if token.tipo == 'bandera_f':
                                                token = self.sacarToken()
                                                if token.tipo == 'cadena':
                                                    Narchivo = token.lexema
                                                    temporada = str(temporadaI) + '-' + str(temporadaF)
                                                    ########################################     
                                                else:
                                                    self.agregarError("cadena","EOF")
                                            else:
                                                self.agregarError("bandera_f","EOF")
                                        else:
                                            temporada = temporadaI + '-' + temporadaF
                                            Narchivo = 'jornada.html'
                                            ########################################################
                                    else:
                                        self.agregarError("mayorQue","EOF")
                                else:
                                    self.agregarError("entero","EOF")
                            else:
                                self.agregarError("guion","EOF")
                        else:
                            self.agregarError("entero","EOF")
                    else:
                        self.agregarError("menorQue","EOF")
                else:
                    self.agregarError("reservada_TEMPORADA","EOF")
            else:
                self.agregarError("entero","EOF")
        else:
            self.agregarError("reservada_JORNADA","EOF")

    def GOLES(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_GOLES':
                token = self.sacarToken()
                if token.tipo in ['reservada_LOCAL','reservada_VISITANTE','reservada_TOTAL']:
                    condicion = token.lexema
                    token = self.sacarToken()
                    if token.tipo == 'cadena':
                        equipo = token.lexema
                        token = self.sacarToken()
                        if token.tipo == 'reservada_TEMPORADA':
                            token = self.sacarToken()
                            if token.tipo == 'menorQue':
                                token = self.sacarToken()
                                if token.tipo == 'entero':
                                    temporadaI = token.lexema
                                    token = self.sacarToken()
                                    if token.tipo == 'guion':
                                        token = self.sacarToken()
                                        if token.tipo == 'entero':
                                            temporadaF = token.lexema
                                            token = self.sacarToken()
                                            if token.tipo == 'mayorQue':
                                                temporada = str(temporadaI) + '-' + str(temporadaF)
                                                ########################################
                                            else:
                                                self.agregarError("cadena","EOF")
                                        else:
                                            self.agregarError("entero","EOF")
                                    else:
                                        self.agregarError("guion","EOF")
                                else:
                                    self.agregarError("entero","EOF")
                            else:
                                self.agregarError("menorQue","EOF")
                        else:
                            self.agregarError("reservada_TEMPORADA","EOF")
                    else:
                        self.agregarError("cadena","EOF")
                else:
                    self.agregarError('reservada_LOCAL | reservada_VISITANTE | reservada_TOTAL',"EOF")
        else:
            self.agregarError("reservada_GOLES","EOF")
    
    def TABLA(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_TABLA':
            if token.tipo == 'reservada_TEMPORADA':
                token = self.sacarToken()
                if token.tipo == 'menorQue':
                    token = self.sacarToken()
                    if token.tipo == 'entero':
                        temporadaI = token.lexema
                        token = self.sacarToken()
                        if token.tipo == 'guion':
                            token = self.sacarToken()
                            if token.tipo == 'entero':
                                temporadaF = token.lexema
                                token = self.sacarToken()
                                if token.tipo == 'mayorQue':
                                    token = self.sacarToken()
                                    if token.tipo == 'guion':
                                        token = self.sacarToken()
                                        if token.tipo == 'bandera_f':
                                            token = self.sacarToken()
                                            if token.tipo == 'cadena':
                                                Narchivo = token.lexema
                                                temporada = str(temporadaI)+'-'+str(temporadaF)
                                                ######################################################
                                            else:
                                                self.agregarError("cadena","EOF")
                                        else:
                                            self.agregarError("bandera_f","EOF")
                                    else:
                                        temporada = str(temporadaI) + '-' + str(temporadaF)
                                        Narchivo = 'temporada.html'
                                        ###############################################################
                                else:
                                    self.agregarError("mayorQue","EOF")
                            else:
                                self.agregarError("entero","EOF")
                        else:
                            self.agregarError("guion","EOF")
                    else:
                        self.agregarError("entero","EOF")
                else:
                    self.agregarError("menorQue","EOF")  
            else:
                self.agregarError("reservada_TEMPORADA","EOF")
                        
        else:
            self.agregarError("reservada_TABLA","EOF")

    def PARTIDOS(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_PARTIDOS':
            token = self.sacarToken()
            if token.tipo == 'cadena':
                jornada = token.lexema
                token = self.sacarToken()
                if token.tipo == 'reservada_TEMPORADA':
                    token = self.sacarToken()
                    if token.tipo == 'menorQue':
                        token = self.sacarToken()
                        if token.tipo == 'entero':
                            temporadaI = token.lexema
                            token = self.sacarToken()
                            if token.tipo == 'guion':
                                token = self.sacarToken()
                                if token.tipo == 'entero':
                                    temporadaF = token.lexema
                                    token = self.sacarToken()
                                    if token.tipo == 'mayorQue':
                                        token = self.sacarToken()
                                        if token.tipo == 'guion':
                                            token = self.sacarToken()
                                            if token.tipo == 'bandera_f':
                                                token = self.sacarToken()
                                                if token.tipo == 'cadena':
                                                    Narchivo = token.lexema
                                                    temporada = str(temporadaI) + '-' + str(temporadaF)
                                                    ######################################## 
                                                    self.sacarToken() 
                                                    if token.tipo == 'guion':
                                                        token = self.sacarToken()
                                                        if token.tipo == 'bandera_ji':
                                                            token = self.sacarToken()
                                                            
                                                        else:
                                                            self.agregarError("bandera_ji","EOF")
                                                    else:
                                                        self.agregarError("guion","EOF")   
                                                else:
                                                    self.agregarError("cadena","EOF")
                                            else:
                                                self.agregarError("bandera_f","EOF")
                                        else:
                                            temporada = temporadaI + '-' + temporadaF
                                            Narchivo = 'jornada.html'
                                            ########################################################
                                    else:
                                        self.agregarError("mayorQue","EOF")
                                else:
                                    self.agregarError("entero","EOF")
                            else:
                                self.agregarError("guion","EOF")
                        else:
                            self.agregarError("entero","EOF")
                    else:
                        self.agregarError("menorQue","EOF")
                else:
                    self.agregarError("reservada_TEMPORADA","EOF")
            else:
                self.agregarError("cadena","EOF")
        else:
            self.agregarError("reservada_PARTIDOS","EOF")
    
    def TOP(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_TOP':
            token = self.sacarToken()
            if token.tipo in ['reservada_INFERIOR','reservada_SUPERIOR']:
                condicion = token.lexema
                token = self.sacarToken()
                if token.tipo == 'reservada_TEMPORADA':
                    token = self.sacarToken()
                    if token.tipo == 'menorQue':
                        token = self.sacarToken()
                        if token.tipo == 'entero':
                            temporadaI = token.lexema
                            token = self.sacarToken()
                            if token.tipo == 'guion':
                                token = self.sacarToken()
                                if token.tipo == 'entero':
                                    temporadaF = token.lexema
                                    token = self.sacarToken()
                                    if token.tipo == 'mayorQue':
                                        token = self.sacarToken()
                                        if token.tipo == 'guion':
                                            token = self.sacarToken()
                                            if token.tipo == 'bandera_n':
                                                token = self.sacarToken()
                                                if token.tipo == 'entero':
                                                    numero = token.lexema
                                                    temporada = str(temporadaI) + '-' + str(temporadaF)
                                                    ##########################################################
                                                else:
                                                    self.agregarError("entero","EOF")
                                            else:
                                                self.agregarError("bandera_n","EOF")
                                        else:
                                            numero = 5
                                            temporada = str(temporadaI) + '-' + str(temporadaF)
                                            #############################################################
                                    else:
                                        self.agregarError("mayorQue","EOF")
                                else:
                                    self.agregarError("entero","EOF")
                            else:
                                self.agregarError("guion","EOF")
                        else:
                            self.agregarError("entero","EOF")
                    else:
                        self.agregarError("menorQue","EOF")
                else:
                    self.agregarError("reservada_TEMPORADA","EOF")
            else:
                self.agregarError("cadena","EOF")
        else:
            self.agregarError("reservada_TOP","EOF")
    
    def ADIOS(self):
        token = self.sacarToken()
        if token.tipo == 'reservada_ADIOS':
            print(easygui.msgbox('ADIOS','ADIOS'))
            exit()
        else:
            self.agregarError("reservada_ADIOS","EOF")
    