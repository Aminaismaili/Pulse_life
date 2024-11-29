import requests
from geopy.distance import geodesic

# Fonction pour récupérer la position de l'utilisateur
def get_user_position():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        loc = data["loc"].split(",")  # Coordonnées (latitude, longitude)
        return float(loc[0]), float(loc[1])  # Retourne (latitude, longitude)
    except Exception as e:
        st.write(f"Erreur lors de la récupération de la position : {e}")
        return None, None  # En cas d'erreur, retourne une position nulle

# Fonction pour obtenir les établissements les plus proches via Overpass API
def get_nearest_place(user_lat, user_lon, place_type):
    # Déterminer le tag en fonction du type de lieu
    if place_type == "pharmacy":
        tag = "amenity=pharmacy"
    elif place_type == "hospital":
        tag = "amenity=hospital"
    elif place_type == "doctor":
        tag = "amenity=doctor"
    else:
        return None

    # URL de l'API Overpass
    overpass_url = "http://overpass-api.de/api/interpreter"

    # Requête pour récupérer les établissements dans un rayon de 10 km
    overpass_query = f"""
    [out:json];
    (
      node[{tag}]({user_lat-0.1},{user_lon-0.1},{user_lat+0.1},{user_lon+0.1});
      way[{tag}]({user_lat-0.1},{user_lon-0.1},{user_lat+0.1},{user_lon+0.1});
      relation[{tag}]({user_lat-0.1},{user_lon-0.1},{user_lat+0.1},{user_lon+0.1});
    );
    out body;
    """

    # Faire la requête
    try:
        response = requests.get(overpass_url, params={'data': overpass_query})
        data = response.json()

        # Vérifier que la clé 'elements' existe et contient des données
        if 'elements' in data:
            places = []
            for element in data['elements']:
                name = element.get('tags', {}).get('name', 'Sans nom')
                lat = element['lat'] if 'lat' in element else (element['center']['lat'] if 'center' in element else None)
                lon = element['lon'] if 'lon' in element else (element['center']['lon'] if 'center' in element else None)
                if lat and lon:
                    places.append((name, lat, lon))

            # Trier les lieux par distance par rapport à l'utilisateur
            places.sort(key=lambda place: geodesic((user_lat, user_lon), (place[1], place[2])).km)

            # Limiter les résultats à 10 premiers établissements
            return places[:10]
        else:
            st.write("Aucun établissement trouvé dans les résultats.")
            return None
    except Exception as e:
        st.write(f"Erreur lors de la requête Overpass : {e}")
        return None


# --- Titre principal ---
st.title("Pulse Life 🫀")
st.write("This is a chatbot that can give you information about heart diseases")



# Sidebar avec le bouton "Position"
with st.sidebar:
    st.header("Options")
    
    
    if st.button("➕", help="new discussion"):
        # Lorsque le bouton est cliqué, réinitialiser la session des messages
        st.session_state.messages = []
        st.write("New discussion started.")
    # État pour sauvegarder la position de l'utilisateur
    if "user_position" not in st.session_state:
        st.session_state.user_position = None

    # Créer le bouton "Position"
    if st.sidebar.button('Position'):
        # Récupérer la position de l'utilisateur
        user_lat, user_lon = get_user_position()
        if user_lat is None or user_lon is None:
            st.sidebar.write("Position not available")
        else:
            # Sauvegarder la position dans l'état
            st.session_state.user_position = (user_lat, user_lon)
            st.sidebar.write(f"Position recovered : Latitude: {user_lat}, Longitude: {user_lon}")

    # Vérifier si la position est déjà récupérée
    if st.session_state.user_position is not None:
        # Afficher un menu pour choisir le type d'établissement
        place_type = st.radio("Choose a type of establishment", ["Pharmacy", "Hospital", "doctor"])

        # Lorsque l'utilisateur choisit un type d'établissement, afficher les résultats
        if place_type:
            st.sidebar.write(f"Search for the {place_type}s closest placements...")
            places = get_nearest_place(st.session_state.user_position[0], st.session_state.user_position[1], place_type.lower())
            if places:
                st.sidebar.write(f"The first 10 {place_type}s the closest are :")
                for place in places:
                    st.sidebar.write(f"{place[0]} - ({place[1]}, {place[2]})")
            else:
                st.sidebar.write(f"No {place_type} found nearby.")
    else:
        # Ne rien afficher avant que la position soit récupérée
        st.sidebar.write("Click on 'Position' to retrieve your location.")