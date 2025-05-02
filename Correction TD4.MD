De la même manière que pour ton dernier retour, ton fichier est plutôt clair et bien écrit; une manière de le rendre encore plus propre est de mettre tes test pour la répartition (et de manière générale tous les petits tests que tu fais) dans la condition `if __name__ == "__main__"`.

Maintenant, même si ton code marche dans certains cas, il y a deux soucis: tu as une erreur quand tu veux récupérer la valeur d'une clé qui n'est pas dans la table, et les mises à jours ne marchent pas.
Sinon, pas de souci avec ta fonction `repartition`.
Pour le souci avec le commentaire quand tu appelles ta fonction horner, tu as juste oublié de renvoyer le résultat de ton calcul dans ta méthode de hachage.

Néanmoins, il y a plus de positif par rapport à la dernière fois, donc essaie de continuer dans cette direction !