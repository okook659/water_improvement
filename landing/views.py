from django.shortcuts import render
import csv, os, folium, chardet, pandas as pd
from shapely.wkt import loads
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,template_name='index.html')

def dashboard(request):
    return render(request, template_name='dashboard.html')



def carte_agences_tde(request):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../media/agences_tde.csv')
    data = pd.read_csv(file_path)

    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

    for index, row in data.iterrows():
        try:
            geometry = loads(row['geometry'])
            longitude, latitude = geometry.coords[0]

            folium.Marker([latitude, longitude], popup=row['etab_nom']).add_to(m)
        except Exception as e:
            print(f"Error at {index}: {e}")
    map_filename = 'landing/static/iframe_agences_tde.html'
    map_path = os.path.join(settings.BASE_DIR, map_filename)
    m.save(map_path)

    return render(request, 'carte_agences_tde.html', {})

#bornes fontaines

def carte_bornes_fontaines(request):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../media/bornes_fontaines.csv')
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
    except Exception as e:
        return render(request, 'error.html', {"error": f"Erreur lors du chargement du fichier CSV : {e}"})
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
    for index, row in data.iterrows():
        try:
            geometry = loads(row['geometry'])
            longitude, latitude = geometry.x, geometry.y

            folium.Marker(
                [latitude, longitude],
                popup=row['borne_fontaine_organisme']
            ).add_to(m)
        except Exception as e:
            print(f"Erreur à l'index {index} : {e}")
    map_filename = 'landing/static/iframe_bornes_fontaines.html'
    map_path = os.path.join(settings.BASE_DIR, map_filename)
    m.save(map_path)
    return render(request, 'carte_bornes_fontaines.html', {})


#postes autonomes

def carte_poste_eau(request):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../media/poste_eau_autonome.csv')
    try:
        data = pd.read_csv(file_path, encoding='utf-8')
    except Exception as e:
        return render(request, 'error.html', {"error": f"Erreur lors du chargement du fichier CSV : {e}"})
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
    for index, row in data.iterrows():
        try:
            geometry = loads(row['geometry'])
            latitude, longitude = geometry.x, geometry.y

            folium.Marker(
                [longitude, latitude],
                popup=row['forage_nom']
            ).add_to(m)
        except Exception as e:
            print(f"Erreur à l'index {index} : {e}")
    map_filename = 'landing/static/iframe_poste_eau.html'
    map_path = os.path.join(settings.BASE_DIR, map_filename)
    m.save(map_path)
    return render(request, 'carte_poste_eau.html', {})


def graphe_tde(request):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../media/agences_tde.csv')
    data = pd.read_csv(file_path)
    data['region_nom_bdd'] = data['region_nom_bdd'].str.lower()
    region_counts = data['region_nom_bdd'].value_counts().to_dict()
    regions = ["maritime", "plateaux", "centrale", "kara", "savanes"]
    datapoints = [
        {"label": region.capitalize(), "y": region_counts.get(region, 0)}
        for region in regions
    ]
    return render(request, 'graphe_tde.html', {"datapoints": datapoints})


def graphe_toilette(request):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../media/toilettes_urbaines.csv')
    data = pd.read_csv(file_path)
        # return render(request, 'error.html', {"error": f"Erreur : {str(e)}"})
    data['region_nom_bdd'] = data['region_nom_bdd'].str.lower()
    region_counts = data['region_nom_bdd'].value_counts().to_dict()
    regions = ["maritime", "plateaux", "centrale", "kara", "savanes"]
    datatoilet = [
        {"label": region.capitalize(), "y": region_counts.get(region, 0)}
        for region in regions
    ]
    
    return render(request, 'graphe_toilettes.html',{"datatoilet": datatoilet})

def graphe_etablissement(request):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../media/traitement_dechets_etablissement.csv')
    data = pd.read_csv(file_path)
    data['region_nom_bdd'] = data['region_nom_bdd'].str.lower()
    region_counts = data['region_nom_bdd'].value_counts().to_dict()
    regions = ["maritime", "plateaux", "centrale", "kara", "savanes"]
    dataetablissement = [
        {"label": region.capitalize(), "y": region_counts.get(region, 0)}
        for region in regions
    ]
    
    return render(request, 'graphe_etablissement.html',{"dataetablissement": dataetablissement})