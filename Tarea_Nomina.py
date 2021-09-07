from datetime import date
import os

class Empresa:
    id=0
    def __init__(self, ruc='',direccion='' , tlfn='', rS='', empleado='', descrip=''):
        Empresa.id+=1
        self.id= Empresa.id
        self.ruc= ruc
        self.direccion=direccion
        self.telefono= tlfn
        self.razonSocial=rS
        self.empleados= empleado
        self.departamento= Departamento(descrip, empleado)

    def mostrarEmpresa(self):
        print("Empresa: {}\nId: {}\n Ruc: {}\nTelefono: {}\nDirección: {}".format(self.razonSocial, self.id, self.ruc, self.telefono, self.direccion))

class Departamento:
    id=0
    def __init__(self, descripcion,empleado):
        Departamento.id += 1
        self.id=Departamento.id
        self.descripcion= descripcion
        self.empleado=empleado

    def mostrarDepartamento(self):
        print("Id: {}\n Descripcion: {}" .format(self.id, self.descripcion))

class Empleado:
    id = 0 
    def __init__(self, nom='', sueldo='', tel='', fechaIng='', valorH=0):
        Empleado.id += 1
        self.id= Empleado.id
        self.nombre= nom
        self.sueldo= sueldo
        self.telefono= tel
        self.fechaIngreso= fechaIng
        self.valorHora= valorH
    
    def valorHor(self):
        self.valorHora= self.sueldo/240
        return self.valorHora

    def mostrarEmpleado(self):
        print("Empleado: {}\nID: {}\nTelefono: {}\nSueldo: {}\nFecha de Ingreso: {}".format(self.nombre, self.id, self.telefono,
                                                                                            self.sueldo, self.fechaIngreso))

class EmpleadoObrero(Empleado):
    id=0
    def __init__(self,nom='', sueldo=0, tel='', fechaIng='', valorH=0,sindicato= True, contratoColectivo= True):
        super().__init__(nom,sueldo,tel,fechaIng, valorH)
        EmpleadoObrero.id += 1
        self.id=EmpleadoObrero.id
        self.sindicato= sindicato
        self.__contratoColectivo= contratoColectivo
    
    @property
    def contraCole(self):
        return self.__contratoColectivo
    
    def valorHor(self):
        super().valorHora()

    def mostrarEmpleadoObrero(self):
        print("Empleado Obrero: {}\n Id: {}\n Sindicato: {}\n ContratoColectivo: {}".format(self.nombre, self.id, self.sindicato, self.__contratoColectivo))
    
class EmpleadoAdministrativo(Empleado):
    id=0
    def __init__(self, nom='', sueldo='', tel='', fechaIng='',valorH=0, comision=True):
        super().__init__(nom, sueldo, tel, fechaIng, valorH)
        EmpleadoAdministrativo.id += 1
        self.id=EmpleadoAdministrativo.id
        self.comision=comision
    
    def valorHor(self):
        super().valorHora()
    
    def mostrarEmpleadoAdministrativo(self):
        print("Empleado Oficina: {}\n Id: {}\n Comisión: {}%".format(self.nombre, self.id, self.comision))

class Prestamos:
    id=0
    def __init__(self, fecha='', valor=0, numPagos=0, empleado='', saldo=0, cuota=0, estado=True):
        Prestamos.id +=1
        self.id= Prestamos.id
        self.fecha= fecha
        self.valor= valor
        self.numPagos=numPagos
        self.cuota= cuota
        self.saldo= saldo
        self.estado= estado
        self.empleado= empleado
    
    def prestamo(self):
        self.cuota= self.valor/self.numPagos
        self.saldo= self.valor-self.cuota
        return self.cuota, self.saldo
    
    def mostrarPrestamos(self):
        print("Fecha de prestamos: {} \nValor prestado: {}\nNumero de Pagos: {}\nCuota: {}\nEstado:{}\nSaldo: {}" .format(self.fecha, self.valor, self.numPagos, 
                                                                                                                        self.cuota, self.estado, self.saldo))

class Sobretiempo:
    id=0
    def __init__(self, horRe=0, horExt=0, fecha='', empleado='', estado=False, totSobret=0):
        Sobretiempo.id += 1
        self.id= Sobretiempo.id
        self.horasRecargos= horRe
        self.horasExtraordinarias= horExt
        self.fecha= fecha
        self.estado= estado
        self.totalSobretiempo=totSobret
        self.empleado= empleado
    
    def sobretiempo(self):
        self.totalSobretiempo = round((self.empleado.valorHora + (horasRecargados*0.50+horasExtraordinaria*2)), 2)
        return self.totalSobretiempo

    def mostrarSobretiempo(self):
        print("Id: {}\n Horas Recargadas: {}\n Horas Extraordinarias: {}\n Estado: {}" .format(self.id, self.horasRecargos,
                                                                                        self.horasExtraordinarias, self.estado))

class Deducciones:
    id= 0
    def __init__(self, iess, comision=0, antiguedad=0):
        Deducciones.id += 1
        self.id= Deducciones.id
        self.iess= iess 
        self.__comision= comision
        self.__antiguedad= antiguedad
    
    @property
    def comision(self):
        return self.__comision
    
    @property
    def antiguedad(self):
        return self.__antiguedad

    def mostrarDeducciones(self):
        print("Id: {}\n Iees: {}\n Comisión: {}\n Antiguedad: {}" .format(self.id, self.iess, self.comision, self.antiguedad))

class Nomina:
    id= 0
    def __init__(self, fecha='', sueldo=0, comision=0, antiguedad=0, iess=0, empleado='', sobret=0, prest=0):
        Nomina.id += 1
        self.id= Nomina.id
        self.fecha= fecha
        self.sueldo= sueldo
        self.comision= round((comision * sueldo), 2)
        self.antiguedad= self.calculoAnti(antiguedad, self.fecha, empleado.fechaIngreso, self.sueldo)
        self.iess= round((iess*(self.sueldo+sobret.totalSobretiempo)), 2)
        self.totIngreso= self.sueldo + sobret.totalSobretiempo + self.comision + self.antiguedad
        self.totDes= round((self.iess + prest.cuota), 2)
        self.liquidoRecibir= self.totIngreso - self.totDes
        self.empleado= empleado
    
    def calculoAnti(self, anti=0, fechaNomina=0, fechaIngreso=0, sueldo=0):
        fechas = str(fechaNomina - fechaIngreso)
        numeroDiasStr = []
        dias = ''
        # OBTENGO EL NUMERO DE DIAS DE DIFERENCIA EN STR.
        for num in fechas:
            try:
                int(num)
                numeroDiasStr.append(num)
            except ValueError:
                break
        # OBTENGO EL NUMERO DE DIAS DE DIFERENCIA EN INT.
        for numeroDia in numeroDiasStr:
            dias += numeroDia
        dias = int(dias)
        return round(((anti*dias)/(365*sueldo)), 2)

    def mostrarNomina(self):
        print("Id: {}\nFecha Nomina: {}\nSueldo: {}\nTotal Ingreso: {}\nComision: {}\nAntiguedad: {}\nIess: {}\nTotal Descuento: {}\nLiquido a Recibir: {}" .format(
              self.id, self.fecha, self.sueldo, self.totIngreso, self.comision, self.antiguedad, self.iess, self.totDes, self.liquidoRecibir))


os.system("cls")
print("---DATOS DE LA EMPRESA---")
razonsocial= input("Ingrese la razón social de la empresa: ")
ruc= int(input("Ingrese el R.U.C de la empresa: "))
direccion= input("Ingrese la dirección donde se encuentra la empresa: ")
tlfn= int(input("Ingrese el número telefonico de la empresa: "))
print("")
print("---DATOS EMPLEADO---")
nombre= input("Ingrese el nombre del empleado: ")
telefono= int(input("Ingrese el número celular del empleado {}: ".format(nombre)))
sueldo= float(input("Ingrese el sueldo del empleado {}: ".format(nombre)))
año= int(input("Ingrese el año que ingreso el empleado {}: ".format(nombre)))
mes= int(input("Ingrese el mes que ingreso el empleado {}: ".format(nombre)))
dia= int(input("Ingrese el dia que ingreso el empleado {}: ".format(nombre)))
fechaIngreso= date(año,mes,dia)
descripcion= input("El empleado a que departamento pertenece [Administrativo, Obrero]: ").capitalize()
descripcionDepa = input("Descripción del departamento: ")
if descripcion=="Administrativo":
    comision=float(input("Ingrese la comision que posee el empleado: "))
    pres= input("El empleado {} va a realizar prestamos [Si, No]: ".format(nombre)).capitalize()
    if pres=="Si":
        añoP= int(input("Ingrese el año que hizo el prestamo el empleado {}: ".format(nombre)))
        mesP= int(input("Ingrese el mes que hizo el prestamo el empleado {}: ".format(nombre)))
        diaP= int(input("Ingrese el dia que hizo el prestamo el empleado {}: ".format(nombre)))
        fechaP= date(añoP,mesP,diaP)
        valor= float(input("Ingrese el valor del prestamo: "))
        numPagos= int(input("Ingrese los numeros de pago que va realizar: "))
    sobret= input("El empleado {} realizo sobretiempo [Si, No]: ".format(nombre)).capitalize()
    if sobret=="Si":
        añoS= int(input("Ingrese el año que hizo el sobretiempo el empleado {}: ".format(nombre)))
        mesS= int(input("Ingrese el mes que hizo el sobretiempo el empleado {}: ".format(nombre)))
        diaS= int(input("Ingrese el dia que hizo el sobretiempo el empleado {}: ".format(nombre)))
        fechaS= date(añoS,mesS,diaS)
        horasRecargados= float(input("Ingrese las horas recargadas que hizo el empleado {}: ".format(nombre)))
        horasExtraordinaria= float(input("Ingrese las horas extraordinarias que hizo el empleado {}: ".format(nombre)))
    iess= float(input("Ingrese el porcentaje del Iess: "))
    añoN= int(input("Ingrese el año que se realizo el pago al empleado {}: ".format(nombre)))
    mesN= int(input("Ingrese el mes que se realizo el pago al empleado {}: ".format(nombre)))
    diaN= int(input("Ingrese el dia que se realizo el pago al empleado {}: ".format(nombre)))
    fechaN= date(añoN,mesN,diaN)
else:
    sindicato= input("Ingrese el sindicato que pertenece el empleado Obrero: ")
    pres= input("El empleado {} va a realizar prestamos [Si, No]: ".format(nombre)).capitalize()
    if pres=="Si":
        añoP= int(input("Ingrese el año que hizo el prestamo el empleado {}: ".format(nombre)))
        mesP= int(input("Ingrese el mes que hizo el prestamo el empleado {}: ".format(nombre)))
        diaP= int(input("Ingrese el dia que hizo el prestamo el empleado {}: ".format(nombre)))
        fechaP= date(añoP,mesP,diaP)
        valor= float(input("Ingrese el valor del prestamo: "))
        numPagos= int(input("Ingrese los numeros de pago que va realizar: "))
    sobret= input("El empleado {} realizo sobretiempo [Si, No]: ".format(nombre)).capitalize()
    if sobret=="Si":
        añoS= int(input("Ingrese el año que hizo el sobretiempo el empleado {}: ".format(nombre)))
        mesS= int(input("Ingrese el mes que hizo el sobretiempo el empleado {}: ".format(nombre)))
        diaS= int(input("Ingrese el dia que hizo el sobretiempo el empleado {}: ".format(nombre)))
        fechaS= date(añoS,mesS,diaS)
        horasRecargados= float(input("Ingrese las horas recargadas que hizo el empleado {}: ".format(nombre)))
        horasExtraordinaria= float(input("Ingrese las horas extraordinarias que hizo el empleado {}: ".format(nombre)))
    iess= float(input("Ingrese el porcentaje del Iess: "))
    antiguedad = float(input("Por antiguedad, cuanto es el recargo: $"))
    añoN= int(input("Ingrese el año que se realizo el pago al empleado {}: ".format(nombre)))
    mesN= int(input("Ingrese el mes que se realizo el pago al empleado {}: ".format(nombre)))
    diaN= int(input("Ingrese el dia que se realizo el pago al empleado {}: ".format(nombre)))
    fechaN= date(añoN,mesN,diaN)


os.system("cls")
print("")
print("---EMPRESA---")
if descripcion == 'Administrativo': emp = EmpleadoAdministrativo(nombre,sueldo,telefono,fechaIngreso,0,comision)
else: emp= EmpleadoObrero(nombre,sueldo,telefono,fechaIngreso, 0,sindicato, True)
empresa= Empresa(ruc, direccion, tlfn, razonsocial, emp, descripcionDepa)
if pres=="Si":
    prest= Prestamos(fechaP, valor, numPagos, emp, 0,0, True)
else: prest=Prestamos()
if sobret=="Si":
    sobret= Sobretiempo(horasRecargados, horasExtraordinaria, fechaS, emp, True, 0)
else: sobret = Sobretiempo()
if descripcion == 'Administrativo':
    deduc= Deducciones(iess, comision)
    nomin= Nomina(fechaN, sueldo, deduc.comision, 0, iess, emp, sobret, prest)
else:
    deduc= Deducciones(iess=iess, antiguedad=antiguedad)
    nomin= Nomina(fechaN, sueldo, deduc.comision, deduc.antiguedad, iess, emp, sobret,prest)

print("")
empresa.mostrarEmpresa()
print("")
print("-----DEPARTAMENTO-----")
empresa.departamento.mostrarDepartamento()
print("")
print("-----EMPLEADO-----")
emp.mostrarEmpleado()
print("")
if isinstance(emp, EmpleadoAdministrativo): emp.mostrarEmpleadoAdministrativo()
else: emp.mostrarEmpleadoObrero()
print("")
print("-----PRESTAMO-----")
prest.mostrarPrestamos()
print("")
print("-----SOBRETIEMPO-----")
sobret.mostrarSobretiempo()
print("")
print("-----DEDUCCIONES-----")
deduc.mostrarDeducciones()
print("")
print("-----PAGO DE NOMINA-----")
nomin.mostrarNomina()
print("")
