import undetected_chromedriver as uc
import time
import time  # Importe le module time pour utiliser des fonctions liées au temps
from selenium import webdriver  # Importe la classe webdriver du module selenium
from selenium.webdriver.chrome.options import Options  # Importe la classe Options du module chrome_options
import requests  # Importe le module requests pour effectuer des requêtes HTTP
from selenium.webdriver.common.by import By  # Importe la classe By du module common


chrome_options = uc.ChromeOptions()
#chrome_options.add_argument("--headless")  # Exécute le navigateur en mode headless (sans interface graphique)
# Instanciation du navigateur avec les options
driver = uc.Chrome(options=chrome_options)
driver.get("https://www.paraphraser.io/fr/resume-de-texte")
input("Last Page ready")
acceptCookie = driver.find_element(By.XPATH, """//*[@id="accept-choices"]""")
acceptCookie.click()
time.sleep(20)
def enter():
    entrer = driver.find_element(By.NAME, """input_content""")
    entrer.clear()
    entrer.send_keys("""Vous êtes une personne remarquable, dotée d'une personnalité unique et captivante. Votre curiosité insatiable vous pousse à explorer de nouvelles idées, de nouveaux horizons. Vous êtes constamment en quête de connaissances et vous vous épanouissez dans l'apprentissage continu. Votre passion pour la vie se reflète dans votre détermination à relever les défis avec grâce et résilience. Votre esprit ouvert et votre empathie naturelle vous permettent de tisser des liens authentiques avec les autres. Votre présence radieuse illumine les pièces où vous entrez, et vous inspirez ceux qui vous entourent. Vous êtes un(e) leader charismatique, guidé(e) par des valeurs fortes et une vision claire de votre avenir. Votre désir de créer un impact positif dans le monde est profondément enraciné en vous. Vous êtes un(e) source d'inspiration pour ceux qui cherchent à vous connaître et à marcher à vos côtés. Votre parcours est rempli de réalisations et de succès, mais vous gardez toujours une humilité admirable. Vous êtes un(e) être humain extraordinaire et le monde est meilleur grâce à votre présence. fffffffffff""")#Marquer le texte du livre
    time.sleep(4)
    surmazier_now = driver.find_element(By.ID, "summarize_now")
    surmazier_now.click()
    time.sleep(20)
    texte = driver.find_element(By.CLASS_NAME, """col-sm-12""").text
    
enter()
time.sleep(1000)    
driver.quit()
