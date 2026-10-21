# Audio du podcast, à ajouter au prompt de la routine

Prérequis : variable d'environnement CARTESIA_API_KEY dans l'environnement de la routine, et api.cartesia.ai autorisé dans la politique réseau.

Paragraphe à coller dans le prompt, après la LIVRAISON :

AUDIO DU PODCAST :
Après avoir écrit le bloc "Version audio pour ton podcast", enregistre ce texte brut (sans HTML) dans podcast/aigile-AAAA-MM-JJ.txt, puis lance : python3 tools/podcast.py podcast/aigile-AAAA-MM-JJ.txt audio/aigile-AAAA-MM-JJ.mp3. Commit les deux fichiers et pousse-les sur la branche de la session. Dans le mail, juste sous le titre du bloc audio, ajoute le lien https://github.com/salimgomri/newsaigile/blob/NOM-DE-LA-BRANCHE/audio/aigile-AAAA-MM-JJ.mp3 (le lien n'est lisible que par les personnes ayant accès au dépôt). Si la clé est absente, si l'appel échoue ou si le push échoue, envoie quand même le mail avec le texte et écris en une phrase pourquoi l'audio manque. Ne mets jamais la clé dans un fichier, un commit ou le mail.
