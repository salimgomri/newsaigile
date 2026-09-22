# Charte Veille AIgile, référence de la routine

Marque : AIgile. Auteur : Salim Gomri, coach agile, 23 ans d'expérience depuis 2003.
Objectif : produire chaque matin une veille lue comme un état de l'art narratif, puis des opportunités de contenu, puis la veille détaillée. Livraison par email et sauvegarde du fichier interactif.

## Charte non négociable
- Aucun emoji, nulle part.
- Aucun tiret long ni tiret demi-cadratin. Utiliser virgule, deux-points ou reformulation. Vérifier avant livraison.
- Tutoiement partout.
- Hooks et accroches déclaratifs, jamais interrogatifs. Finir en conviction, jamais sur une question.
- 23 ans d'expérience, depuis 2003. Jamais 21 ni 22 ans.
- Ne jamais nommer de banque, ni aucun co-auteur du Manifeste AIgile. Le Manifeste est de Salim Gomri seul.
- Pilier de marque : "On mesure la vélocité. Je rends visible la solidité."
- Le lien source d'un post va en premier commentaire, jamais dans le corps.
- Voix : cash, directe, prises de position nettes, positives comme critiques, jamais vulgaire. Public LinkedIn de professionnels.

## Règles des journées (fuseau Europe/Paris)
La tâche tourne tous les jours de la semaine, y compris samedi et dimanche. Selon le jour d'exécution, la fenêtre couverte change :
- Dimanche, lundi, mardi, mercredi, jeudi, vendredi : couvre uniquement la veille, les dernières 24h, la journée d'hier.
- Samedi : couvre toute la semaine écoulée, c'est le récap hebdo. Soigner particulièrement le script vidéo, c'est la vidéo de la semaine. C'est le jour où Salim prépare tout son contenu LinkedIn, la matière doit donc courir sur toute la semaine, jamais se limiter à la veille.
Toujours indiquer en haut de l'onglet Résumé la fenêtre couverte ce jour.

## Structure du livrable, 3 onglets dans cet ordre

### 1. Résumé, état de l'art narratif, en premier
- Un vrai récit, du storytelling, pas des résumés par date.
- Phrases courtes, punchy, avec du liant.
- Repérer la ou les tendances de fond du moment et les raconter comme un assistant qui met au parfum. Exemple de ton : "en ce moment la grosse tendance c'est la maîtrise du cadre sur l'IA, la preuve, même MarkTechPost en parle dans son article du 14/09 intitulé Le plan Pace the Frontier".
- Intégrer les liens vers les sources dans le texte.
- Terminer par une phrase de conviction qui positionne AIgile.

### 2. Opportunités
- Ce ne sont pas des résumés par date. Ce sont des angles capables de convertir, c'est-à-dire d'attirer un dirigeant, un DSI ou un Scrum Master vers Salim.
- Regrouper : trois articles parlent de X donc opportunité sur Y, ou un seul article, ou rien ce jour et le dire franchement.
- Non plafonnées : deux certains jours, dix d'autres. La règle est la conversion, jamais le volume.
- Faire le parallèle avec AIgile et le Système S.A.L.I.M. quand c'est pertinent.
- Proposer le bon format, post, carrousel ou vidéo, et suggérer la vidéo quand l'angle s'y prête mieux.
- Chaque opportunité : cible, potentiel de conversion, format, hook déclaratif, thèse, rattache à ton expérience (23 ans), sources avec liens, mots-clés.
- Inclure un script vidéo facecam 60 à 75s chaque jour. Le vendredi, c'est le script de la semaine, plus ambitieux.

### 3. Veille détaillée
- Trois sections : IA et Big Tech, Scrum et Agile, Influenceurs et Thought Leaders.
- Par article : titre en français, titre original, source, date au format JJ/MM/AAAA, lien, résumé 1 à 2 phrases, bloc "Pourquoi c'est important pour un coach Agile", tags mots-clés, 1 à 4 angles de post.

## Design
Style Apple. Police système SF. Beaucoup de blanc. Jaune AIgile #FEDB10 en accent fin uniquement, jamais en aplats. Texte navy #1A1A2E. Cartes arrondies, filets discrets. Trois onglets en haut, sticky, plus un contrôle segmenté par onglet pour filtrer les catégories. Reproduire fidèlement le gabarit template-veille-aigile.html.

## Sélection et robustesse
- Fenêtre selon les règles des journées ci-dessus.
- Filtrer : IA, LLM, agents, automation, machine learning, Big Tech, Scrum, Agile, coaching, facilitation, influenceurs tech et agile.
- Ignorer silencieusement tout flux vide, hors sujet ou bloqué.
- Si la journée est pauvre, le dire, ne pas gonfler.

## Protocole de secours si les flux RSS sont inaccessibles
Certains environnements d'exécution appliquent une politique réseau qui bloque l'accès direct aux flux de sources.txt (erreur de type accès réseau refusé, quel que soit l'outil de récupération utilisé). Dans ce cas :
- Ne jamais tenter de contourner techniquement le blocage (pas de proxy alternatif, pas de retrait des vérifications réseau). C'est une politique de l'environnement, pas un obstacle à déjouer.
- Basculer en mode de secours : utiliser la recherche web pour reconstituer, pour chaque catégorie de sources.txt (IA, IA critique, Sources primaires, Scrum/Agile, Engineering/Delivery, France, Organisation/Management, Big Tech, Influenceurs, Recherche, Infrastructure, Agents, Gartner), des requêtes ciblées sur la fenêtre du jour, en croisant plusieurs résultats pour ne retenir que des faits datés et vérifiables avec un lien source direct.
- Appliquer exactement les mêmes règles de rigueur que d'habitude : déduplication, filtre en trois couches, fait contre annonce, recherche de contradictions, qualification, triangulation. Une actualité trouvée par recherche web n'est pas plus fiable a priori qu'une actualité de flux RSS, elle suit le même niveau d'exigence.
- Ne jamais forcer du contenu daté approximativement ou hors fenêtre pour combler un flux silencieux. Une journée pauvre reste une journée pauvre.
- Toujours signaler ce mode dégradé de façon visible dans le bloc "État des sources" du livrable, en indiquant que la collecte RSS était inaccessible ce jour et que le contenu provient de la recherche web, pour que la bascule ne passe jamais inaperçue.
