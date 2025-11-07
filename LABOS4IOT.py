#labo 4 -

from ws2812 import WS2812
from machine import ADC, Pin
from utime import sleep
import urandom  # pour générer des couleurs aléatoires

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)

COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

led = WS2812(18,1)  #WS2812(pin_num,led_count)

#while True:
print("fills")
for color in COLORS:
    led.pixels_fill(color)
    led.pixels_show()
    sleep(0.2)  # A NE PAS METTRE #tempo cligno mettre un if avec un compteur de temps qui permet d'entrer dans la boulce if de condition
    print("coucou")

SOUND_SENSOR = ADC(1)

# while True:
#     light = LIGHT_SENSOR.read_u16()/256  #divise par 256 car les detecteurs sont relevé par 0 à  65535
#     noise = SOUND_SENSOR.read_u16()/256   #divise par 256 car les detecteurs sont relevé par 0 à  65535
#     print (noise)
#     print (light)
#     sleep(0.2)

#BOUCLE POUR VARIATION DE LUMI7RE SUR LE SON

# while True:
#     average = 0
#     for i in range (1000):
#         noise = SOUND_SENSOR.read_u16()/256
#         average += noise
#     noise = average/1000
#     print(noise)       #VERIF
#     indice=int(noise/8)   #indice pour la couleur suivante
#     led.pixels_fill(COLORS[indice])   #Affiche une couleur sur base du niveau de son relevé
#     led.pixels_show()
#     print(indice)     #VERIF
#     print("coucou22")

def Lecture_Son_Lissee(valeurs_son):
    
    #moyenne glissante pour evaluer le son de manière lisse
    son = SOUND_SENSOR.read_u16()/256
    if son > 1 :
        valeurs_son.append(son)
    if len(valeurs_son)>100:
        valeurs_son.pop(0)   #modifie et supprime les valeurs échantillonées sur 20 éléments
    moyenne= sum(valeurs_son)/len(valeurs_son)
    
    print("Dernière valeur :", son)   #VERIF
    print("Moyenne glissante :", moyenne)
    #print(valeurs_son)
    return moyenne

echanti = [1]
while True:
    moy=Lecture_Son_Lissee(echanti)
    indice=int(moy/31)   #indice pour la couleur suivante
    led.pixels_fill(COLORS[indice])   #Affiche une couleur sur base du niveau de son relevé
    led.pixels_show()


# # --- INITIALISATION ---
# led = WS2812(18, 1)       # LED RGB sur la broche GP18
# mic = ADC(1)              # Microphone sur la broche ADC1
# 
# # --- FONCTION : génère une couleur RGB aléatoire ---
# def random_color():
#     r = urandom.getrandbits(8)
#     g = urandom.getrandbits(8)
#     b = urandom.getrandbits(8)
#     return (r, g, b)
# 
# # --- VARIABLES DE DÉTECTION ---
# threshold = 50            # 🔺 Seuil plus haut = moins sensible
# previous_level = 0
# cooldown = 0
# alpha = 0.6               # Coefficient du filtre (entre 0 et 1) — lisse les variations rapides
# 
# # --- BOUCLE PRINCIPALE ---
# while True:
#     # Lecture du signal sonore (valeur entre 0 et 65535)
#     raw = mic.read_u16() / 256   # Normalisé entre 0 et ~255
# 
#     # Filtrage simple (lissage)
#     level = (alpha * previous_level) + ((1 - alpha) * raw)
# 
#     # Variation entre deux lectures
#     diff = abs(level - previous_level)
#     previous_level = level
# 
#     # Détection d'un pic sonore important
#     if diff > threshold and cooldown == 0:
#         color = random_color()
#         led.pixels_fill(color)
#         led.pixels_show()
#         print("🎵 Beat détecté ! Niveau:", int(level), "Diff:", int(diff), "→ Couleur:", color)
#         
#         cooldown = 15   # délai avant une nouvelle détection
# 
#     # Réduction du cooldown
#     if cooldown > 0:
#         cooldown -= 1
# 
#     sleep(0.02)
    