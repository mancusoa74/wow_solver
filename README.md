# Words of Wonder Solver

This simple tool helps to solve Words of Wonder puzle game on Android and IOS

This version is for Italian language. In order to use it for other languages just replace the txt dictionary file

## Syntax

```
usage: wow_solver.py [-h] -c C -l L [-cp CP] [-cc CC]

Help to solve Words of Wonders puzzle game

optional arguments:
  -h, --help  show this help message and exit
  -c C        characters of the puzzle
  -l L        length of the word <3..6>
  -cp CP      character constraint position
  -cc CC      character constraint
  ```

### Example

```python wow_solver.py -c emlneo -l 6```

generates all words of length 6

```
melone
menole
melone
menole
molene
molene
```


```python wow_solver.py -c emlneo -l 5 -cp 3 -cc e```

generates all the words of length 5 which have the character 'e' (-cc) in position number 3 (-cp)

```
eleno
moene
moene
eleno
oleme
oleme
```
