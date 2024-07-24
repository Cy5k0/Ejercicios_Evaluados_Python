# EL famoso juego de cachipun (piedra papel o tijera)



# Importación de galería
import random

score = 0
cpu_score = 0  

# Aspecto visual de la aplicación en el título
print("")
print("")
print("")

print('******************************************************************')
print('******************  Cachipun on Python  **************************')
print('******************************************************************')
print("")

# selección de idioma y validación del ingreso
while True:
  idioma = input('Escoge idioma EN para Inglés o ES para Español // Choose your language EN for English or ES for Spanish: ').upper()  # convierte a mayusculas

  if idioma in ["ES", "EN"]:  # COn el in verifica si el valor es válido, viendo que valor contiene la variable idioma
    break
  else:
    print('Por favor, ingresa "ES" para Español o "EN" para Inglés.')



def cachipun_game():
    if idioma in ['ES']:
          
        global score
        global cpu_score

        while True:
            mano = input('Ingresa tu juego, escribe: PIEDRA, PAPEL o TIJERA: ').upper()  # convierte a mayusculas

            if mano in ['PIEDRA', 'PAPEL' , 'TIJERA']:  # COn el in verifica si el valor es válido, viendo que valor contiene la variable mano
                break
            else:
                print('Por favor, escribe: PIEDRA, PAPEL o TIJERA.')

        
        opciones_cpu = ['PIEDRA', 'PAPEL', 'TIJERA']
        mano_cpu = random.choice(opciones_cpu)
        print("")
        if mano == mano_cpu:
            print('*****************************************************************************')
            print(f'Jugador escoge {mano} y CPU escoge {mano_cpu}, por lo tanto es un EMPATE -_-')
            print('-----------------------------------------------------------------------------')
        elif (mano =='PAPEL' and mano_cpu == 'PIEDRA') or (mano =='PIEDRA' and mano_cpu == 'TIJERA') or (mano =='TIJERA' and mano_cpu == 'PAPEL'):
            score = score + 1 # suma puntaje a favor del humano
            print('****************************************************************************')
            print(f'Jugador escoge {mano} y CPU escoge {mano_cpu}, por lo tanto JUGADOR GANA :)')
            print('----------------------------------------------------------------------------')
        elif (mano =='PAPEL' and mano_cpu == 'TIJERA') or (mano =='TIJERA' and mano_cpu == 'PIEDRA') or (mano =='PIEDRA' and mano_cpu == 'PAPEL'):
            cpu_score = cpu_score + 1 # suma puntaje a favor del cpu
            print('******************************************************************************')
            print(f'Jugador escoge {mano} y CPU escoge {mano_cpu}, por lo tanto JUGADOR PIERDE :(')
            print('------------------------------------------------------------------------------')
            # print(mano_cpu)
    

        
    elif idioma in ['EN']:
        
        while True:
            hand = input('Choose your game, write: STONE, PAPER or SCISSOR: ').upper()  # convierte a mayusculas

            if hand in ['STONE', 'PAPER' , 'SCISSOR']:  # COn el in verifica si el valor es válido
                break
            else:
                print('Please, you must write: STONE, PAPER or SCISSOR.')
        
        opciones_cpu = ['STONE', 'PAPER', 'SCISSOR']
        mano_cpu = random.choice(opciones_cpu)
        print(mano_cpu)


#mientras sea verdadero repetirá la función principal o cerrar el programa

while True:
    cachipun_game()
    
    while True:
        print(f'///Puntaje Jugador = {score} Puntaje CPU = {cpu_score}///')
        print('******************************************************************************')
        print('')
        
        repetir = input('¿Desea Continuar? (S/N): ').lower()
        print('')
        print('') #pasa de mayúscula a minúscula
        if repetir in ['s', 'n']: #'in' verifica lo que hay en repetir
            break
        else:
            print('Por favor, ingrese S para sí o N para no.')
    
    if repetir == 'n':
        
        if score < cpu_score:
            print('')
            print('*************************************************')
            print(f'PUNTAJE FINAL: Jugador {score} - CPU {cpu_score}')
            print('TU PIERDES!!!!   :(')
            print('*************************************************')
            print('')
        elif cpu_score < score:
            print('')
            print('*************************************************')
            print(f'PUNTAJE FINAL: Jugador {score} - CPU {cpu_score}')
            print('TU GANAS!!!!   :)')
            print('*************************************************')
            print('')
        else:
            print('')
            print('*************************************************')
            print(f'PUNTAJE FINAL: Jugador {score} - CPU {cpu_score}')
            print('EMPATE (-_-)')
            print('*************************************************')
            print('')
        print('El programa se cierra, Gracias Totales!')
        print('')
        break


