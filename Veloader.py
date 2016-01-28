import sqlalchemy
from sqlalchemy import create_engine
from datetime import datetime
from geopandas import GeoDataFrame
import geopandas as gpd
import urllib
from Veloader_datastruct import *  ##Entraine la declaration du schema de la table velovmaxenc


## Methode de remplacement des valeurs vides par -1
def replaceMissingDataByNegate1(data):
    try:
        if not data:
            return '-1'
        else:
            return data
    except:
        return data


##Parametrage SGBD et creation de la table si absente grace a la couche ORM
engine = create_engine("postgresql://postgres:P@nd0s+@vps234953.ovh.net:5432/velovDB", echo=True)
Base.metadata.create_all(engine)

## Recuperation fichier json et ecriture sur le disque
geojsonfile=urllib.URLopener()
geojsonfile.retrieve("https://download.data.grandlyon.com/wfs/rdata?SERVICE=WFS&VERSION=2.0.0&outputformat=GEOJSON&maxfeatures=400&request=GetFeature&typename=jcd_jcdecaux.jcdvelov&SRSNAME=urn:ogc:def:crs:EPSG::4171",'velov.json')


## Lecture fichier json en memoire
velovGeoDataFrame=gpd.read_file('velov.json')           ##Charge le contenu du Json dans un GeoDataFrame (herite de  et surcharge pandas.DataFrame)
velovGeoDataFrame['dateinsert']=datetime.today()        ##Ajoute une colonne avec le timestamp actuel

## Nettoyage des donnees en memoire
velovGeoDataFrame.drop('geometry', axis=1, inplace=True)                    ## Suppression colonne inutile
velovGeoDataFrame=velovGeoDataFrame.applymap(replaceMissingDataByNegate1)   ## Remplacement des valeurs vides par -1 necessaire a la methode to_sql surchargee

##Insertion en base
velovGeoDataFrame.to_sql(name='velovmaxence',con=engine,if_exists='append',dtype=velovTableColumnTypes)
