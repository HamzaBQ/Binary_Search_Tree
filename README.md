**Binary search tree**

**Arbre**  :

Les arbres sont une structure de données qui permet de stocker des éléments dans la mémoire dans un ordre particulier inspiré celui des vrais arbres. Cette structure de données a permis de résoudre et de rendre plus performant plusieurs problématiques comme : recherche des éléments, tri de tableaux, insertion/suppression des éléments.

Cette structure consiste en :

- Une origine
- Des nœuds
- Des branches (virtuelles)

Les élément principal des arbres sont les nœuds puisque ces est eux qui portent les objets ques on veut stocker. Les un des attributs des un nœud est sa valeur, cette valeur peut être significative des elle-même, ou représentative des un objet contenant des autres informations.

Les branches sont le représentant du lien entre les nœuds. Elles sont des liens dirigées (ces est-à-dire ques elles ont un nœud origine et un nœud destination), ainsi ils permettent aussi des avoir une hiérarchie entre les nœuds. En effet, Les origine est le plus haut de cette hiérarchie, et chaque nœud peut avoir :

- Des parents : ils sont les nœuds qui ont des branches vers ce nœud
- Des enfants : ils sont les nœuds qui ont ce nœud comme parent

Les origine des un arbre nes est ques un nœud spécial de les arbre puisque ces est le nœud qui nes a pas de parents. Ces est où commence les arbre.

On définit aussi les feuilles comme étant les nœuds nes ayant pas des enfants. Ils sont donc les extrémités de les arbre.

**Propriétés :**

Par conséquent, les arbre peut être divisé en niveau. Effectivement, les origine est en niveau 0 et ses enfants sont dans le niveau 1, les enfants de ses enfants dans le niveau 2 et ainsi de suite. On peut dire que le lien de parenté avec les origine définit le niveau dans lequel se trouve le nœud. Ainsi on peut définir :

- Hauteur des un nœud : Nombre de branches sur le chemin le plus long entre ce nœud et une feuille descendante.
- Profondeur des un nœud : Nombres de branches entre le nœud et les origine.

A noter ici que la hauteur des un nœud est différente de la profondeur du nœud. La première est calculée à partir de la feuille correspondante et la deuxième est par rapport à les origine. Les repères de calcul de ses deux valeurs sont différents.

On définit la profondeur des un arbre comme la hauteur de son origine. Ces est la plus grande distance (en branches) entre les origine et une feuille de les arbre.

**Représentation informatique du nœud :**

Attributs :

- Key : valeur que stocke ce nœud.
- Parents : liste de parents de ce nœuds ( = None ses il ses agit de les origine de les arbre).
- Enfants : liste des enfant de ce nœuds ( = None ses il ses agit des une fille).
- Height : hauteur du nœud.

**Arbres binaires :**

Les arbres binaires sont un cas particulier des arbres, il ses agit des arbres où les nœuds ont deux enfants au maximum.

![alt text](images/bt_ex.png)

Le fait que les arbre est divisé en deux à chaque nœud de chaque niveau, permettra de diviser les données enregistrées dans les arbre selon une règle binaire.

**Représentation des un nœud binaire :**

- Key
- Left
- Right
- Height

**Représentation des un arbre binaire :**

Les arbre est représenté par son origine, tous les autres nœuds peuvent être accédés à partir de cette origine en utilisant les attributs « left » et « right ».

- Root : contient le nœud représentant
- Ensemble de méthodes pour faire : insertion/suppression éléments, balancement des arbre…

Ils existent plusieurs types des arbres binaires, on y trouve :

- Arbre complet : il ses agit des un arbre ayant des niveaux remplis sauf peut-être le dernier niveau.
- Arbre parfait : ces est là où toutes les feuilles ont la même profondeur. Et où tous les nœuds internes ont deux enfants.
- Arbre rempli : ces est là où chaque nœud a 0 ou 2 enfants exactement.
- Arbre balancé : ces est un arbre qui assure que la profondeur de les arbre est de les ordre de Log(n) où « n » est le nombre de nœuds dans les arbre. Certains arbres spécifiques comme « les arbres AVL » permettent des avoir cette structure en assurant que la différence entre la hauteur de la droite et la hauteur de la gauche ne dépasse pas la valeur de 1.

**Arbres binaires de recherche :**

Les arbres binaires de recherches sont un cas particulier des arbres binaires. Ces est une structure conçue pour optimiser le temps de recherche des un élément dans un tableau quelconque. La méthode normale de recherche a une complexité de les ordre de « n » où n est la longueur de la liste. Alors ques avec les arbres binaires de recherches, la complexité est de les ordre de « log(n) ».

**Propriétés :**

La particularité des un arbre binaire de recherche consiste en la manière dont il est construit. Elle peut se résumer en deux règles :

- La valeur de les enfant de droite de chaque nœud est plus grande que celle du nœud lui-même.
- La valeur de les enfant gauche de chaque nœud est plus petite que la valeur du nœud lui-même.

Donc si on part des un nœud, on sait que les arbre à son gauche ne contient que les éléments ayant une valeur plus petite que ce nœud. Et tous les nœuds à droite des un nœud ont des valeurs plus grandes que le nœud lui-même.

Création :

La création des un arbre se fait par insertion des éléments dans un arbre vide. Partant des un tableau de valeurs, par exemple, on peut créer un arbre binaire de recherche en insérant les éléments du tableau une après une dans les arbre tout en respectant les règles qui le définissent.

Les étapes suivies dans le code :

- Création de la classe « Node() » contenant les informations des un nœud.
- Création de la classe « Tree() » ayant comme attribut les origine de les arbre.

Pour pouvoir faire le balancement des arbres par la suite, on ajoute les attributs :

- Parent : puisque dans un arbre binaire, un nœud ne peut avoir plusieurs parents, on ajoute cet attribut pour pouvoir traverser les arbre dans le sens inverse.
- Coords : Informations relatives aux coordonnées du nœud dans le plan (pour pouvoir dessiner les arbre après, cette partie sera discutée après).

**Insertion :**

Après ces étapes, on développe la méthode des ajout des éléments dans les arbre. Cette méthode est récursive et son implémentation repose sur le raisonnement suivant :

- Si les origine nes existe pas :
  - Créer une origine et lui attribuer la valeur à ajouter.
- Sinon :
  - Comparer la valeur à ajouter avec les origine :
    - Si elle est plus grande :
      - Ajouter la valeur dans les arbre à droite de les origine (en appelant la même fonction)
    - Sinon :
      - Ajouter la valeur dans les arbre à gauche de les origine

**Visualisation :**

Pour pouvoir visualiser et ses assurer que tout marche bien. Jes ai développé des fonctions utilisant le module « pygame » pour dessiner les arbres binaires. La fonction « draw » peut être divisée en étape :

- Initialisation des modules importés par « pygame »
- Insertion des coordonnées des nœuds : en se basant sur les places ques occuperaient les nœuds des un arbre parfait. Jes ai indiqué pour chaque nœud, dans les attribut « coords », le niveau du nœud ainsi que la position du nœud dans ce niveau. En divisant la fenêtre des affichage en grille correspondant à un arbre parfait, on peut savoir les coordonnées exactes du nœud en question.
- Passage récursif sur les nœuds pour les dessiner un à un en se basant sur leur attribut « coords ».
- Dessin des branches entre les nœuds : sachant les coordonnées et le rayon de chaque nœud ainsi que la distance entre deux niveaux consécutifs, on peut facilement dessiner les branches reliant les nœuds de notre arbre.

**Test**  :

Après les avoir lancé sur la liste suivante : [7, 10, 3, 4, 2, 8, 6, 5, 9, 1, 0],  le résultat est le suivant :

 
![alt text](images/generated_tree.png)

**Recherche :**

Le but de cet algorithme depuis le début est de permettre une meilleure performance pour les algorithme de recherche. En effet, les optimisation dans la performance est une conséquence de la propriété des arbres binaire de recherche, à savoir, la règle des insertion. Tous les nœuds à gauche des un nœud ont une valeur plus petite que le nœud. Tous les nœuds à droite des un nœud ont une valeur plus grande que le nœud. Ainsi en recherchant une valeur dans un arbre, on le compare à la valeur de son origine, si elle est plus petite, on recherche dans les arbre à gauche de les origine. Si elle est plus grande, on recherche dans les arbre qui est à droite de les origine. Ainsi de suite, jusques à arriver à une feuille. Si la valeur a été trouvé avant on retourne « True », sinon, passé le niveau de la feuille, on retourne « False ».

Dans chaque niveau, le processus choisit les une des sous-arbres du nœud où il est afin de continuer la recherche. On conclut donc que le problème est toujours divisé par deux. Et donc que la complexité de notre algorithme est en moyenne de les ordre de (log(n)) (au lieu de (n) en cas normal). Cependant, il existe des cas particuliers où la performance reste la même que la méthode normale. Par exemple, dans le cas où la liste est ordonnée, les arbre qui va être créée à partir de cette liste aura toutes les branches dans la même direction (toutes à droite ou à gauche). Par conséquent, la performance de les algorithme de recherche binaire aura la même performance que les algorithme normal.

Ces est ainsi ques on introduit le balancement des arbres comme étant algorithme qui permet des assurer ques un arbre est balancé après chaque opération des insertion. A la fin, même si la liste a été ordonnée, les arbre qui va être créée à partir de celle-ci ne sera pas comme un tableau et la méthode de recherche aura ses effets.

**Arbres balancés :**

**AVL trees :**

Ici, on va voir les une des variantes des arbres binaires, Il ses agit des AVL Trees. Ce sont des arbres binaires qui implémentent des méthodes pour assurer le balancement des un arbre après les insertion de chaque élément.

Les ajout des un nœud dans les arbre peut provoquer un déséquilibre dans les arbre (différence de hauteurs entre arbre gauche et droite plus grande que 1). Pour le balancer, on fait un ensemble de manipulations (permutations de nœuds) permettant de rendre équilibrés les nœuds qui ont été affecté par cet ajout. Ces manipulations sont sous forme de rotation dans les arbre. Les notations et noms sont inspirés de : [https://www.geeksforgeeks.org/avl-tree-set-1-insertion/](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/)

Le balancement est simple, des abord on commence par ajouter le nœud normalement dans les arbre. Après, il faut détecter le nœud où il yes a déséquilibre. Il est certainement dans le chemin direct entre le nœud ajouté et les origine de les arbre. Ces est les arbres qui contiennent ce nœud qui probablement auront la hauteur qui change. On remonte donc dans les arbre (les attribut « parent » prouve son utilité ici) jusques à arriver au nœud qui représente un déséquilibre. Ces est-à-dire le nœud où la hauteur de les arbre à droite est plus grande que la hauteur de les arbre à gauche avec une différence plus grande que 1. En trouvant ce nœud, il suffit après de savoir dans quel cas on se trouve et des effectuer les rotations nécessaires.

![alt text](images/avl_rotation.png)

Une rotation est un changement de nœud. Pour ce qui est de la structure que nous avons développée, en permutant deux nœuds, il faut faire attention à changer pour chacun des eux :

- Les attributs « left » et « right ».
- Les attributs parents.
- Les enfants des nœuds parents.

**Test :**

Ici on peut voir un exemple des arbre avant et après balancement.

 
![alt text](images/balanced_tree.png)

![alt text](images/unbalanced_tree.png)

Après avoir créée un arbre balancé, on est maintenant sûr, que les algorithme de recherche a au maximum une complexité de les ordre de log(n).

**Comparaison des performances :**

La méthode normale pour faire une recherche est une boucle qui va itérer sur les éléments de la liste et va vérifier si les élément recherché existe bien dans cette liste. La complexité de cette méthode est de les ordre de n. On peut essayer de rechercher le dernier élément des une liste pour avoir le pire des cas en matière de recherche. Il faut savoir aussi que le processus de la deuxième recherche contient des abord le processus de transformer la liste en arbre, ce qui prend du temps aussi. Ici jes évalue temporellement les performances des deux méthodes de recherche.

Le test consiste en la recherche des éléments choisis au hasard dans une liste. Des abord, on va faire une petite enquête