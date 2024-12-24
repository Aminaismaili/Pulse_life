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