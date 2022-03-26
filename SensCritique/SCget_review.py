
from selenium.webdriver.common.by import By
import pandas as pd



def getCommentaire(Liste_titre,liste_comm,driver):
    Liste_titre.append(driver.find_elements(By.CLASS_NAME,'ere-review-heading'))
    liste_comm.append(driver.find_elements(By.CLASS_NAME,'ere-review-excerpt'))


def merge_comms(liste_titre,liste_comm):
    Frame_commentaire = pd.DataFrame({"titre_comm":liste_titre,"commentaire":liste_comm})
    Frame_commentaire.to_csv('SensCritique.csv',sep = ";")
    return Frame_commentaire

def traitement_valeurs(Liste):
    for values in range (len(Liste[0])):
        Liste[0][values] = Liste[0][values].text
