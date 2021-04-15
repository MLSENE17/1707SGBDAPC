"""
Mamadou Lamine SENE
ML___SENE__17
"""
import module1
from tkinter import messagebox
import sys
import tweepy
import re
import bs4
import requests
import os
from io import BytesIO
from PIL import Image
import shutil
"""Fonction pour la AUTHENTIFICATION
   vers l API TWITTER
"""
def twitter_auth():
    try:
        costumer_key = "RLin4hhLDwdVuLznsOEHopZxm"
        costumer_secret = "2YmUVJjyUEhke1dtJ2CtKVhZbrwOEwPcH3p6qcDEL3CeyAlESl"
        access_token = "719520290242502656-K35or0oToHRGNO3NZBHnewAQVczu3ga"
        access_secret = "drsjWpWtChQ59ZIa3kh5uSbqVsV6iES4evxLi7AJXWI2W"
    except KeyError:
        sys.stderr.write("Twitter environnement variable  not set !\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(costumer_key,costumer_secret)
    auth.set_access_token( access_token,access_secret)
    return auth
"""Fonction pour recuperer l objet apres l authentification
"""
def get_twitter_client():
    auth = twitter_auth();
    client = tweepy.API(auth,wait_on_rate_limit=True)
    return client
"""Fonction pour recuperer
tous les tweets concernant les communicant
"""
def get_total_link(limite=0):
    user ="MinisteredelaS1"
    client = get_twitter_client()
    total_link = []
    i=1
    maxI=10
    if limite==0:
        tweetAll = tweepy.Cursor(client.user_timeline,screen_name=user,tweet_mode="extended",include_rts=False,lang="fr",exclude_replies=True).items()
    else:
        tweetAll = tweepy.Cursor(client.user_timeline,screen_name=user,tweet_mode="extended",include_rts=False,lang="fr",exclude_replies=True).items(1)
    for tweets in tweetAll:
        full_link={}
        if "Communiqué"  and "déclarés positifs" in tweets.full_text:
            try:
                if tweets.extended_entities :
                    #print(i,"tweets charges")
                    full_link["date_tweet"]=str(tweets.created_at.date().isoformat())
                    link = []
                    for t in tweets.extended_entities.get("media",[]):
                        link.append(t["media_url"])
                    full_link["link_image"]=link
                    total_link.append(full_link)
                    i=i+1
                    if i == maxI :
                        maxI=maxI+10   
                        os.system('cls')  
            except Exception as e :
                messagebox.showwarning("pas d`image",e)
    tw= str(i)+" tweets ont été bien chargés"
    messagebox.showinfo("Tweets charges",tw)
    return total_link
"""Fonction pour telecharger
 1 image apres recuperation des lien
"""
def telechargerImage(LIEN_DE_IMAGE,pourcentage,j):#cette fonction nous permet de telecharger les images
    if LIEN_DE_IMAGE :
        try:
            link_Extension = os.path.basename(LIEN_DE_IMAGE).split(".")
            extension = link_Extension[1]
            pour = "Téléchargement terminé : "+str(pourcentage)+"%"
            messagebox.showinfo("Progression  téléchargement",pour)
            print(extension)
            res =requests.get(LIEN_DE_IMAGE)
            imgFile = Image.open(BytesIO(res.content))
            imgFile.save(str(j)+'.'+extension)
        except Exception as e:
            pour = "Téléchargement terminé : "+str(pourcentage)+"%"
            messagebox.showinfo("Progression  téléchargement",pour)
"""Fonction pour stocker les images
 dans un dossier local
"""
def telechargerImageDuJour(tweets):
    Anne_Mois=tweets[0]["date_tweet"][:7]
    jour=tweets[0]["date_tweet"][8:]
    if not os.path.exists(Anne_Mois):
        try:
            os.mkdir(Anne_Mois)
        except:
            messagebox.showerror("Erreur","Impossible de creer le dossier")
    os.chdir(Anne_Mois)
    if not os.path.exists(jour):
        try:
            os.mkdir(jour)
        except: 
             messagebox.showerror("Erreur","Impossible de creer le dossier")
    else:
        os.chdir("..")
        return False
    os.chdir(jour)
    timage=1
    for Linkimage in  tweets[0]["link_image"]:
        telechargerImage(Linkimage,50*timage,timage)
        timage=timage+1
    os.chdir("..")
    os.chdir("..")
    return True
def telechargerAllImages(tweets):
    pos=1
    for itemTweet in tweets :
        pourcentage = int(pos*100/len(tweets))
        Anne_Mois=itemTweet["date_tweet"][:7]
        jour=itemTweet["date_tweet"][8:]
        if not os.path.exists(Anne_Mois):
            try:
                os.mkdir(Anne_Mois)
            except:
                messagebox.showerror("Erreur","Impossible de creer le dossier")
        os.chdir(Anne_Mois)
        if not os.path.exists(jour):
            try:
                os.mkdir(jour)
            except: 
                messagebox.showerror("Erreur","Impossible de creer le dossier")
        os.chdir(jour)
        timage=1
        for Linkimage in  itemTweet["link_image"]:
            telechargerImage(Linkimage,pourcentage,timage)
            timage=timage+1
        os.chdir("..")
        os.chdir("..")
        pos=pos+1
def fonctionMain(type="ALL"):
    Nom_Dossier= "TweetAllImage"
    print(os.chdir(os.path.abspath(".")))
    if not os.path.exists(Nom_Dossier):
        try:
            os.mkdir(Nom_Dossier)
        except:
            messagebox.showerror("Erreur","Impossible de creer le dossier")
    try:
            if(type=="ALL"):
                try:
                    shutil.rmtree(Nom_Dossier)
                    os.mkdir(Nom_Dossier)
                except:
                    messagebox.showerror("Erreur","Impossible de creer le dossier")
                os.chdir(Nom_Dossier)
                telechargerAllImages(get_total_link())
            else:
                os.chdir(Nom_Dossier)
                """Si on veut telecharger
                le dernier tweet(le communique du jour)"""
                if telechargerImageDuJour(get_total_link(1)):
                    os.chdir("..")
                    return True
                else :
                    os.chdir("..")
                    return False
    except Exception as e:
            messagebox.showerror("Probleme d ouverture du dossier ")
    os.chdir("..")
    return True

    