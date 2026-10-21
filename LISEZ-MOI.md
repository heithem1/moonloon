# FlashLab Dashboard 2.3.1 — Icône du lanceur
Heithem FlashLab · 0779 29 15 63

Installer FlashLab_Dashboard_2.3.1_Android9.apk par-dessus Dashboard 2.3. Conserver le module Commandes véhicule 1.3 déjà installé. Aucune désinstallation ni réinitialisation du widget n’est nécessaire.
Laisser le téléchargement se terminer avant de lancer l’installation. Si le lanceur conserve l’ancienne image après une installation réussie, redémarrer la tablette une fois.

## Correction
L’ancienne icône reposait sur un bitmap enveloppé dans un drawable. Le lanceur affichait une petite image dans une tuile blanche. La nouvelle version utilise une icône adaptative avec fond noir et un dessin vectoriel or, ainsi qu’une bannière paysage 320 × 180 déclarée dans l’application et son activité, suivant le format de Gestionnaire déjà fonctionnel.
Le symbole occupe davantage la tuile et conserve ses proportions. Une image de repli classique et l’icône ronde sont également fournies.

## Périmètre vérifié
Version 2.3.1, code 50, même package com.coolray.dash, même signature et Android 9/API 28.
Tous les DEX, bibliothèques natives, images de l’interface, dispositions de widgets et autres fichiers sont identiques à Dashboard 2.3. Les changements concernent le manifeste/version, la table de ressources, les icônes et les deux nouvelles ressources d’illustration.
Le rendu natif de l’icône adaptative, de sa variante ronde et de la bannière a été vérifié. Signature, alignement et intégrité ZIP contrôlés. L’affichage final dans le lanceur Flyme reste à confirmer sur la voiture après installation.
Les précédents résultats fonctionnels 2.3 sont conservés dans les sources historiques ; ils ne sont pas présentés comme de nouveaux tests véhicule 2.3.1.

## GitHub / Store
L’archive Dashboard_2.3.1_GitHub.zip contient le nouvel APK dashboard_50_<empreinte>.apk et catalog.json. Publier l’APK avant ou avec le catalogue pour éviter un HTTP 404.
Le catalogue fourni modifie uniquement l’entrée Dashboard du catalogue récupéré pendant cette préparation. Les autres applications et la mise à jour du Store sont conservées.
Si votre catalogue a changé entre-temps, utiliser catalog.entry.json et merge_catalog.py sur votre catalogue actuel, notamment si vous venez d’y ajouter Assistance :
 python merge_catalog.py votre_catalog.json --entry catalog.entry.json --output catalog.json
Aucun fichier n’a été publié automatiquement sur GitHub.

## Sources
source/dashboard_v23 conserve les sources historiques 2.3. source/dashboard_icon contient le correctif reproductible, ses ressources et le Dashboard 2.3 de base.
Reconstruire avec build.py --tools CHEMIN_OUTILS --key CLE --cert CERTIFICAT. Les clés privées ne sont pas incluses.

## Retour à l’original
Retour_Dashboard_Original_51.apk remplace l’ancien retour de code 48 : son code 51 permet une installation par-dessus cette mise à jour. Après ce retour, un futur Dashboard FlashLab devra utiliser un code supérieur à 51 pour une mise à jour normale.
