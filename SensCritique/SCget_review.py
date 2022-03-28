
from selenium.webdriver.common.by import By
import pandas as pd



def getCommentaire(Liste_titre,liste_comm,driver):
    titre2 = driver.find_elements(By.CLASS_NAME,'ere-review-heading')
    commentaire = driver.find_elements(By.CLASS_NAME,'ere-review-excerpt')
    for i in range(len(titre2)):
        titre2[i] = titre2[i].text
    Liste_titre.append(titre2)
    for j in range(len(commentaire)):
        commentaire[j] = commentaire[j].text
    liste_comm.append(commentaire)


def merge_comms(liste_titre,liste_comm):
    Frame_commentaire = pd.DataFrame({"titre_comm":liste_titre,"commentaire":liste_comm})
    Frame_commentaire.to_csv('SensCritique.csv',sep = ";")
    return Frame_commentaire
