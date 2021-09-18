

#CALCULADORA DE IMPUESTOS 
print ('[1]INFORMACION')
print ('[2]CALCULADORA')
print("-"*50)

opcion=int(input("¿Qué opción deseas?"))
if(opcion==1):
 print ('INFORMACION SOBRE:')
 print ('[1]IVA')
 print ('[2]TENENCIA')
 print ('[3]IEPS')
 print ('[4]ISAN')
 print ('[5]IETU')
 print ('[6]IDE')
 print ('[7]ISN')
 print("-"*50)
 info=int(input('informacion sobre:'))
 if (info==1):
  print ('IVA. (Impuesto sobre el valor añadido) , es un incremento de un porcentaje en el precio de cada artículo que compramos y de cada servicio que recibimos')
 if (info==2):
  print ('Tenencia. Impuesto que tanto personas físicas como morales deben pagar al gobierno por el simple hecho de poseer un automóvil, independientemente del uso que se le dé a este.')
 if (info==3):
  print ('IEPS. (Impuesto Especial sobre Producción y Servicios),  impuesto indirecto que se cobra por la elaboración, venta o importación de gasolinas y lo paga el consumidor final, por lo que no lo vemos desglosado en el ticket de compra.')

 if (info==4):
  print ('ISAN. (Impuesto sobre automóviles nuevos), impuesto especial al consumo que grava la enajenación de automóviles nuevos de producción nacional, así como la importación definitiva de automóviles cuyo año modelo corresponde al año modelo en que se efectúa la importación, o a los 10 años modelo inmediatos anteriores.')

 if (info ==5):
  print ('IETU. (Impuesto Empresarial a Tasa Única), es un impuesto que grava la percepción efectiva de ingresos para las operaciones de enajenación de bienes, prestación de servicios independientes y por el otorgamiento del uso o goce temporal de bienes')

 if (info ==6):
  print ('IDE. (Entorno de Desarrollo Integrado), es un sistema de software para el diseño de aplicaciones que combina herramientas del desarrollador comunes en una sola interfaz gráfica de usuario (GUI).')

 if (info ==7):
  print ('ISN (Impuesto Sobre Nómina), es aplicado a los pagos en efectivo, en servicio o en especie por remuneración al trabajo realizado en una relación de subordinación (de un trabajador para un patrón). Este cobro es efectuado por parte de las entidades federativas y, por ser de carácter estatal, cada estado determina la tasa o porcentaje que se debe pagar.')


if (opcion==2):
 print ('[1]Calcular el IVA de un producto')
 print ('[2]Calcular tenencia')
 print ('[3]Calcular IEPS')
 print ('[4]Calcular ISAN')
 print ('[5]Calcular IETU')
 print ('[6]Calcular IDE')
 print ('[7]Calcular ISN')
 print("-"*50)
 cal=int(input("¿Qué opción deseas?"))
 ##IVA
 if (cal ==1):
  print ('[1] SI')
  print ('[2] NO')
  piva=int(input('el producto tiene IVA aplicado?'))

  if (piva==1):
      preciocniva=int(input('Cual es el precio del producto con IVA aplicado?'))
      iva1=preciocniva*0.16
      iva2=preciocniva-iva1
      print ('El precio sin iva es=')
      print (iva2)
      
  if (piva==2):
     preciosniva=int(input("Cual es el precio del producto o servicio?"))
     iva=preciosniva*0.16
     iva3=preciosniva+iva
     print ('el precio con iva es=') 
     print (iva3)


##TENENCIA
 if (cal ==2):
  print ('[1]Automovil')
  print ('[2]Importado')
  print ('[3]Motocicletas')
  print ('[4]Transporte publico')
  print ('[5]Transporte de carga')
  tpvehiculo=int(input('Que tipo de vehiculo tiene?'))
  if (tpvehiculo==1):
       añovh=int(input('De de que año es el vehiculo?'))
       if (añovh >2004):
           valorvh=int(input('Cual es el valor total del vehiculo?'))
           if (valorvh <428768):
               tenA=valorvh*0.03
               print ('La tenencia es igual a=')
               print (tenA) 
           if (valorvh <825140 and valorvh>428769 ):
                tenB=valorvh-428769
                tenB1=tenB*0.08
                tenB2=tenB1+12863
                print ('La tenencia es igual a=')
                print (tenB2)
           if (valorvh <1109080 and valorvh>825140 ):
                tenC=valorvh-825140
                tenC1=tenC*0.13
                tenC2=tenC1+47347
                print ('La tenencia es igual a=')
                print (tenC2)
           if (valorvh <1393020 and valorvh>1109081 ):
                tenD=valorvh-1109081
                tenD1=tenD*0.16
                tenD2=tenD1+85111
                print ('La tenencia es igual a=')
                print (tenD2)
           if (valorvh >1396021):
                tenE=valorvh-1396020
                tenE1=tenE*19
                tenE2=tenE1+132813
                print ('La tenencia es igual a=')
                print (tenE2)

       if (añovh <2004 and añovh>1995 ):
           valorvh=int(input('Cual es el valor total del vehiculo?'))
           refrendo=int(input('Cual es el valor del refrendo'))
           if (valorvh <428768):
               tenA=valorvh*0.03
               tenA1=tenA+refrendo
               print ('La tenencia es igual a=')
               print (tenA1) 
           if (valorvh <825140 and valorvh>428769 ):
                tenB=valorvh-428769
                tenB1=tenB*0.08
                tenB2=tenB1+12863
                tenB3=tenB2+refrendo
                print ('La tenencia es igual a=')
                print (tenB3)
           if (valorvh <1109080 and valorvh>825140 ):
                tenC=valorvh-825140
                tenC1=tenC*0.13
                tenC2=tenC1+47347
                tenC3=tenC2+refrendo
                print ('La tenencia es igual a=')
                print (tenC3)
           if (valorvh <1393020 and valorvh>1109081 ):
                tenD=valorvh-1109081
                tenD1=tenD*0.16
                tenD2=tenD1+85111
                tenD3=tenD2+refrendo
                print ('La tenencia es igual a=')
                print (tenD3)
           if (valorvh >1396021):
                tenE=valorvh-1396020
                tenE1=tenE*19
                tenE2=tenE1+132813
                tenE3=tenE2+refrendo
                print ('La tenencia es igual a=')
                print (tenE3)
  if (tpvehiculo==2):
     print ('Los vehiculos importados pagan una cuota de $1,362.00')

  if (tpvehiculo==3):
     print ('Las motocicletas pagaran una cuota de $249.00')

  if (tpvehiculo==4): 
     print ('Los vehiculos destinados a transporte publuico pagan una cuota de $622.00')

  if (tpvehiculo==5):
     print ('los vehiculos destinados a transporte de carga pagan una cuota de $122.00')

          
 
##IEPS
 if (cal ==3):
  print ('[1]IMPORTACION')
  print ('[2]NACIONALES')
  origen=int(input('los productos son de venta o origen:'))
  if (origen==2):
     print ('[1]Combustibles')
     print ('[2]TABACO')
     print ('[3]BEBIDAS')
     print ('[4]PLAGUICIDAS')
     print ('[5]ALIMENTOS NO BASICOS')
     tp=int(input('Que tipo de producto es?'))
     if (tp==1):
         print ('[1]GASOLINA')
         print ('[2]PROPANO')
         print ('[3]BUTANO')
         print ('[4]GASAVIÓN')
         print ('[5]TURBOSINA')
         print ('[6]COMBUSTÓLEO')
         print ('[7]COQUE DE PETRÓLEO')
         print ('[8]COQUE DE CARBÓN')
         print ('[9]CARBON MINERAL')
         tpcom=int(input('Que tipo de combustible es?:'))
         if(tpcom==1):
           print ('[1]GASOLINA MAGNA')
           print ('[2]GASOLINA PREMIUM')
           tpgas=int(input('Que tipo de gasolina es?:'))
           if (tpgas==1):
             cantL=int(input('Cantidad de litros: '))
             IEPS=cantL*0.43
             print ('EL IEPS es igual a:')
             print (IEPS)
           if (tpgas==2):
             cantL=int(input('Cantidad de litros: '))
             IEPS=cantL*0.53
             print ('EL IEPS es igual a:')
             print (IEPS)
         if(tpcom==2):
            canG=int(input('Cantidad de litros:'))
            IEPSgas=canG*0.07
            print ('El IEPS es igual a:')
            print (IEPSgas)
         if (tpcom==3):
          canP=int(input('Cantidad de litros:'))
          IEPSbut=canP*0.09
          print ('El IEPS es igual a:')
          print (IEPSbut)
         if (tpcom==4):
          canAv=int(input('Cantidad de litros: '))
          IEPSav=canAv*0.13
          print ('El IEPS es igual a:')
          print (IEPSav)
         if (tpcom==5):
          canTur=int(input('Cantidad de litros:'))
          IEPStur=canTur*15
          print('El IEPS es igual a:')
          print (IEPStur)
         if (tpcom==6):
          canCOm=int(input('Cantidad de litros:'))
          IEPScom=canCOm*0.16
          print ('El IEPS es igual a:')
          print (IEPScom)
         if(tpcom==7):
          canPET=int(input('Cantidad de toneladas:'))
          IEPSpet=canPET*19
          print ('El IEPS es igual a:')
          print (IEPSpet)
         if (tpcom==8):
          canCAR=int(input('Cantidad de toneladas :'))
          IEPScar=canCAR*46
          print ('El IEPS es igual a:')
          print (IEPScar)
         if (tpcom==9):
          canCarM=int(input('Cantidad de toneladas:'))
          IEPScarm=canCarM*34
          print ('El IEPS es igual a:')
          print (IEPScarm)
     if(tp==2):
       print ('[1]CIGARRO')
       print ('[2]PUROS LABRADOS')
       print ('[3]PUROS HECHOS A MANO')
       Tpcigar=int(input('Tipo de tabaco'))
       if(Tpcigar==1):
         valcig=int(input('Cual es el valor del producto?'))
         IEPScig=valcig*0.6+valcig
         print('El IEPS es igual a:')
         print (IEPScig)
       if(Tpcigar==2):
         valpurol=int(input('Cual es el valor del producto?'))
         IEPSpurol=valpurol*0.6+valpurol
         print('El IEPS es igual a:')
         print (IEPSpurol)
       if(Tpcigar==3):
         valpuroM=int(input('Cual es el valor del producto?'))
         IEPSpuroM=valpuroM*0.30
         print('El IEPS es igual a:')
         print (IEPSpuroM)
     if(tp==3):
       print('[1]SABORIZADAS')
       print ('[2]AlCOHOLICAS')
       print('[3]ENERGETIZANTES')
       tpbebidas=int(input('Tipo de bebida:'))
       if(tpbebidas==1):
         cantLsab=int(input('Cantidad de litros:'))
         IEPSsab=cantLsab*1.26
         print('El IEPS es igual a:')
         print (IEPSsab)
       if(tpbebidas==2):
         cantgrados=int(input('Graduacion alcohólica'))
         if(cantgrados <15):
           valorbebida1=int(input('Valor de la bebida'))
           IEPSbebida1=valorbebida1*0.26
           print('El IEPS es igual a:')
           print (IEPSbebida1)
         if(cantgrados >14 and cantgrados<20):
           valorbebida2=int(input('Valor de la bebida'))
           IEPSbebida2=valorbebida2*0.3
           print('El IEPS es igual a:')
           print (IEPSbebida2)
         if(cantgrados >20):
           valorbebida3=int(input('Valor de la bebida'))
           IEPSbebida3=valorbebida3*0.53
           print('El IEPS es igual a:')
           print (IEPSbebida3)
       if(tpbebidas==3):
         valorener=int(input('Valor de la bebida:'))
         IEPSener=valorener*0.25
         print('El IEPS es igual a:')
         print (IEPSener)
     if(tp==4):
       catPla=int(input('Categoria:'))
       if(catPla==1 or 2):
         valPLa=int(input('Valor del plaguicida:'))
         IEPSplag=valPLa*0.09
         print('El IEPS es igual a:')
         print (IEPSplag)
       if(catPla==3):
         valPLa2=int(input('Valor del plaguicida:'))
         IEPSplag2=valPLa2*0.07
         print('El IEPS es igual a:')
         print (IEPSplag2)
       if(catPla==4):
         valPLa3=int(input('Valor del plaguicida:'))
         IEPSplag3=valPLa2*0.06
         print('El IEPS es igual a:')
         print (IEPSplag3)
     if(tp==5):
       VALalim=int(input('Valor del producto:'))
       pesoal=int(input('Peso en gramos:'))
       cientosal=pesoal/100
       IEPSpeso=VALalim*0.08
       IEPSaliment=cientosal*IEPSpeso
       print('EL valor IEPS es igual a:')
       print (IEPSaliment)

         
##ISAN
if (cal ==4):
  valorvh1=int(input('Cual es el valor total del vehiculo?'))
  if (valorvh1 <283241):
   ISANa=valorvh1*0.02
   print ('El ISAN es igual a=')
   print (ISANa) 
  if (valorvh1 <339889 and valorvh1>283240):
   ISANb=valorvh1-283239
   ISANb1=ISANb*0.05
   ISANb2=ISANb1+5664
   print ('El ISAN es igual a=')
   print (ISANb2)
  if (valorvh1 <396537 and valorvh1>339889 ):
   isanC=valorvh1-339888
   isanC1=isanC*0.10
   isanC2=isanC1+8497
   print ('El ISAN es igual a=')
   print (isanC2)
  if (valorvh1 <509833 and valorvh1>396537 ):
   isanD=valorvh1-396535
   isanD1=isanD*0.15
   isanD2=isanD1+14162
   print ('El ISAN es igual a=')
   print (tenD2)
  if (valorvh1 >509834):
   isanE=valorvh1-509830
   isanE1=isanE*17
   isanE2=isanE1+31156
   print ('El ISAN es igual a=')
   print (tenE2)
##IETU
if (cal ==5):
  ingresosTP=int(input('Cuales fueron sus ingresos totales percibidos'))
  deducciones=int(input('Monto de deducciones autorizadas:'))
  isrretenidos=int(input('ISR retenido:'))
  basegravable=ingresosTP-deducciones
  subtotal=basegravable*0.175
  subtotal2=subtotal+basegravable+isrretenidos
  print ('EL IETU es igual a:')
  print (subtotal2)

##IDE
if (cal ==6):
  monto=int(input('Cantidad que se deposito:'))
  if (monto <15000):
    print ('No se aplica IDE')
  if (monto >15000):
    excedente=monto-15000
    ide=excedente*0.03
    print ('El IDE es igual a:')
    print (ide)
##ISN
if (cal ==7):
  print ('[1]AGUAS CALIENTES')
  print ('[2]BAJA CALIFORNIA NORTE')
  print ('[3]BAJA CALIFORNIA SUR')
  print ('[4]CAMPECHE')
  print ('[5]CHIAPAS')
  print ('[6]CHIHUAHUA')
  print ('[7]COAHUILA')
  print ('[8]COLIMA')
  print ('[9]CIUDAD DE MEXICO')
  print ('[10]DURANGO')
  print ('[11]ESTADO DE MEXICO')
  print ('[12]GUANAJUATO')
  print ('[13]GUERRERO')
  print ('[14]HIDALGO')
  print ('[15]JALISCO')
  print ('[16]MICHOACAN')
  print ('[17]MORELOS')
  print ('[18]NAYARIT')
  print ('[19]NUEVO LEON')
  print ('[20]OAXACA')
  print ('[21]PUEBLA')
  print ('[22]QUERETARO')
  print ('[23]QUINTANA ROO')
  print ('[24]SAN LUIS')
  print ('[25]SINALOA')
  print ('[26]SONORA')
  print ('[27]TABASCO')
  print ('[28]TAMAULIPAS')
  print ('[29]TLAXCALA')
  print ('[30]VERACRUZ')
  print ('[31]YUCATAN')
  print ('[32]ZACATECAS')
  estado=int(input('En que estado se laboro?'))
  if (estado==1):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.025
    print ('El ISN es igual a:')
    print (isn)
  if (estado==2):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==3):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.025
    print ('El ISN es igual a:')
    print (isn)
  if (estado==4):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==5):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==6):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==7):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==8):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==9):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==10):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==11):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==12):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.023
    print ('El ISN es igual a:')
    print (isn)
  if (estado==13):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==14):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==15):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==16):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==17):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==18):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==19):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==20):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==21):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==22):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==23):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==24):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.025
    print ('El ISN es igual a:')
    print (isn)
  if (estado==25):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.024
    print ('El ISN es igual a:')
    print (isn)
  if (estado==26):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.02
    print ('El ISN es igual a:')
    print (isn)
  if (estado==27):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.025
    print ('El ISN es igual a:')
    print (isn)
  if (estado==28):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==29):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==30):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==31):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.03
    print ('El ISN es igual a:')
    print (isn)
  if (estado==32):
    sueldo=int(input('Sueldo en nomina:'))
    isn=sueldo*0.025
    print ('El ISN es igual a:')
    print (isn)
  


