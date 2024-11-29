Chatbot des Maladies Cardiaques
===============================

Introduction
------------

Ce projet est un chatbot intelligent destiné à fournir des informations et des conseils concernant les maladies cardiaques. Il utilise un modèle de type RAG (Retrieval-Augmented Generation) pour générer des réponses pertinentes à partir des données médicales et des documents indexés. Le chatbot peut fournir des conseils médicaux, suggérer des hôpitaux à proximité et offrir des informations en fonction de la localisation de l'utilisateur.

Objectifs du projet
-------------------

Le chatbot a pour objectif de :
- Fournir des informations sur les maladies cardiaques basées sur des données médicales.
- Recommander des hôpitaux en fonction de la localisation de l'utilisateur.
- Aider à la prise de décisions liées à la santé cardiaque en fonction des symptômes décrits par l'utilisateur.

Technologies Utilisées
----------------------

Les principales technologies utilisées dans ce projet incluent :
- **RAG (Retrieval-Augmented Generation)** : Pour générer des réponses pertinentes en utilisant un modèle pré-entraîné et des données récupérées.
- **Haystack** : Pour l'indexation des documents et la recherche d'information.
- **Streamlit** : Pour créer l'interface utilisateur interactive du chatbot.
- **Hugging Face** : Pour l'utilisation des modèles de langage pré-entraînés (ex. : GPT-2, mGPT-2).

Structure du Code
-----------------

Le projet est organisé en plusieurs fichiers et modules principaux :
- **pipeline_rag.py** : Le fichier contenant le pipeline RAG pour récupérer et générer des réponses.
- **indexation_documents.py** : Script pour indexer les documents de santé cardiaque.
- **interface_streamlit.py** : Fichier pour l'interface utilisateur Streamlit.

Exécution du Projet
-------------------

1. **Installation des dépendances** :
   Utilisez `pip` pour installer les bibliothèques nécessaires.
   
   ```bash
   pip install haystack transformers streamlit
