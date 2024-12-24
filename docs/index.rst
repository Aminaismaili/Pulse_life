.. project1 documentation master file, created by
   sphinx-quickstart on Fri Nov 29 18:56:19 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to project1's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   Equipe
   Description
   Etapes
    
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
content :
==========================
Équipe du Projet Chatbot
==========================

Encadrant
---------

- *Nom de l'encadrant* : [Masrour Tawfik]
- *LinkedIn* : [https://www.linkedin.com/in/tawfik-masrour-43163b85/]
Équipe
-------

Voici les membres de l'équipe ayant travaillé sur le projet :

1. *Membre 1* : [Alae Boutarhat]
2. *Membre 2* : [Amina Ismaili]
   
   ==========
Chatbot des Maladies Cardiaques
==========

Description du Projet
==========

Le chatbot des maladies cardiaques est une solution intelligente et interactive élaborée pour aider à la prévention, à la sensibilisation et à la gestion des maladies cardiaques. Intégrant des technologies avancées d'intelligence artificielle, le chatbot fournit des réponses personnalisées et informatives basées sur les besoins des utilisateurs. 

Caractéristiques Principales
----------

- **Prise en charge des données médicales** : Analyse des dossiers médicaux et données personnelles pour offrir des conseils personnalisés.
- **Génération de réponses augmentées** : Utilisation de modèles à base de RAG (Retrieval-Augmented Generation) pour récupérer des informations fiables et précises.
- **Localisation des services** : Suggestions d'hôpitaux et services de santé à proximité.
- **Conseils sur la santé cardiaque** : Fournit des recommandations basées sur des données cliniques et des paramètres individuels.

Objectifs
----------

1. **Sensibilisation** : Informer les utilisateurs sur les risques des maladies cardiaques et promouvoir de meilleures habitudes de vie.
2. **Accès à l'information** : Rendre les informations médicales accessibles et compréhensibles pour tous.
3. **Support aux patients** : Offrir un accompagnement adapté aux patients souffrant de pathologies cardiaques.
4. **Interaction simple** : Permettre une interaction intuitive et fluide pour tous les types d'utilisateurs.

Technologies Clés
----------

- **Modèles de Langage** : Intégration de modèles avancés comme RAG, Mistral, et MXBAI pour une compréhension contextuelle optimale.
- **Pipeline IA** : Incorporation de la recherche dense avec Dense Passage Retriever et TransformersReader.
- **Interface Utilisateur** : Application créée avec Streamlit pour une expérience utilisateur fluide et interactive.

Public Cible
----------

Le projet s'adresse aux personnes cherchant à améliorer leur santé cardiaque, aux patients ayant des antécédents de maladies cardiovasculaires, ainsi qu'aux professionnels de santé souhaitant un outil pour orienter leurs patients.

==========================
Étapes de Création du Chatbot
==========================

Ce document décrit les étapes principales suivies pour créer notre chatbot sur les maladies cardiaques. Voici un résumé du processus :

1. *Collecte de Données depuis Hugging Face*
   -------------------------------------------------
   La première étape a consisté à récupérer des données pertinentes sur les maladies cardiaques à partir de la plateforme Hugging Face. Ces données incluent des jeux d'informations liées à la santé, comme les symptômes, les facteurs de risque et les traitements.

2. *Fusion des Données dans un Fichier Unique*
   -------------------------------------------------
   Toutes les données collectées ont été fusionnées dans un seul fichier PDF pour une gestion centralisée. Cela a permis une organisation optimale avant de procéder aux étapes suivantes.

3. *Nettoyage des Données*
   ----------------------------
   La qualité des données a été améliorée en supprimant les doublons, les informations inutiles et les incohérences. Cette étape garantit une précision accrue dans les réponses du chatbot.

4. *Création des Questions et Réponses*
   ------------------------------------------
   
   Des questions et réponses ont été générées à partir des données nettoyées. Ces dialogues ont été formatés dans un fichier PDF pour servir de référence et faciliter l'entraînement du chatbot.

5. *Création d'une Base de Vecteurs avec ChromaDB*
   --------------------------------------------------
   Une base de vecteurs a été créée en utilisant ChromaDB et le modèle mxbai-embed-large. Cette base permet de rechercher efficacement des informations pertinentes à partir des données indexées.

6. *Développement du Chatbot*
   ------------------------------
   Le chatbot a été développé en utilisant :

   - *Mistral* comme modèle LLM pour générer des réponses intelligentes et contextuelles.
   - *Streamlit* pour concevoir une interface conviviale et interactive, permettant une expérience utilisateur fluide.

Conclusion
-----------

Ces étapes combinées nous ont permis de construire un chatbot performant et éducatif, capable de répondre efficacement aux questions sur les maladies cardiaques tout en s'adaptant aux besoins des utilisateurs.