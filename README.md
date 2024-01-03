# Nombres Premiers

On calcule les nombres premiers entre 0 et N.

Pour cela on utilise le [crible d'Ératosthène](https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne)

![illustration](https://upload.wikimedia.org/wikipedia/commons/8/8c/New_Animation_Sieve_of_Eratosthenes.gif?20120214201729)

Pour rappel un nombre premier est un entier naturel ($\Bbb{N}$) qui a 2 diviseurs et ne peut être divisé que par lui-même et par 1.

note:

- 0 n'est pas premiers car on ne peut pas diviser par 0
- 1 n'est pas premiers car il n'a q'un diviseurs :1÷1

On a un tableau de nombre de 2 à N comme le montre le schéma en-haut.
On barre tous les multiples de 2,puis ceux de 3 et de 5 ... jusqu'à N.

Note: on ne barre pas les multiples de 4 car il est lui-même un multiple de 2 (ils sont déja barrés)

Sources: 

- wikipedia(l'image)
https://upload.wikimedia.org/wikipedia/commons/8/8c/New_Animation_Sieve_of_Eratosthenes.gif?20120214201729