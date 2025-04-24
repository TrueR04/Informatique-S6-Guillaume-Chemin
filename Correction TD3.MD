D'un point de vue global, ton fichier est plutôt propre et bien écrit, avec quelque tests, et la plupart des méthodes ont la bonne idée.

Maintenant, il y a un gros souci, c'est que quasiment 80% de tes méthodes ont des erreurs de compilation de Python, c'est-à-dire que si je les appelle, elles donnent une erreur.
Par exemple, `is_leaf` ne marche pas car ta variable est `__children`, la fonction `depth` non plus car tu n'appelles pas la méthode (tu devrais écrire `self.if_leaf()`), le code ensuite est récursif et ne finit pas, etc.
C'est dommage car tu as pourtant écrit des tests, mais tout le but des tests est de pouvoir vérifier par toi même si tes fonctions marchent.
D'autant plus qu'ici, il n'y a même pas un souci de logique, mais un souci de syntaxe, ce qui veut dire que tu n'a pas du tout essayé d'appeler tes fonctions pour voir si ca donnait quelque chose de cohérent.
Pour les prochains TP, il vaut mieux avoir que quelques méthodes, mais qui au moins n'ont pas d'erreur syntaxique, et où tu as vérifié via 1 ou 2 tests qu'elle donnaient un bon résultat, plutôt que d'écrire pleins de fonctions qui ne marchent pas.

Je te remets le lien du corrigé si tu veux jeter un coup d'oeil: https://github.com/thomas-vinet/Mines-TD-PSD

Sinon, essaie les prochaines fois d'écrire moins de code mais au moins de l'appeler, puis de vérifier que les tests passent.
