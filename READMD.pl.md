[![pl](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Ciastelix/Python-Algorithms/README.pl.md)
[![en](https://img.shields.io/badge/lang-en-green.svg)](https://github.com/Ciastelix/Python-Algorithms/README.md)

# Spis treści

1. [Rekurencja](#rekurencja)
   1. [Silnia](#silnia)
   2. [Fibonacci](#fibonacci)
   3. [Liczenie potęg](#liczenie-potęg)
   4. [Liczby pierwsze](#liczby-pierwsze)
   5. [Usuwanie duplikatów](#usuwanie-duplikatów)
2. [Lista jednokierunkowa](#lista-jednokierunkowa)
   1. [Węzeł](#węzeł)
   2. [Lista jednokierunkowa](#lista-jednokierunkowa-1)
3. [Struktury danych](#struktury-danych)
   1. [Graf](#graf)
   2. [Drzewo binarne](#drzewo-binarne)
      1. [Węzeł binarny](#węzeł-binarny)
      2. [Drzewo binarne](#drzewo-binarne-1)
   3. [Stos](#stos)
4. [Szyfry](#szyfry)
   1. [Szyfr Cezara](#szyfr-cezara)

<a name="rekurencja"></a>

## Rekurencja

Rekurencja to technika programowania, w której funkcja wywołuje samą siebie w celu rozwiązania problemu. Poniżej znajdują się różne przykłady zastosowania rekurencji w algorytmach.

<a name="silnia"></a>

### Silnia

Silnia to funkcja matematyczna, która dla danego liczbę całkowitą `n` oblicza produkt wszystkich liczb całkowitych od 1 do `n`. Oto implementacja funkcji silni za pomocą rekurencji:

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

<a name="fibonacci"></a>

### Fibonacci

Sekwencja Fibonacciego to ciąg liczb, w którym każda liczba jest sumą dwóch poprzednich liczb. Oto implementacja obliczania `n`-tej liczby Fibonacciego za pomocą rekurencji:

```python
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

<a name="liczenie-potęg"></a>

### Liczenie potęg

Obliczanie potęgi liczby to mnożenie liczby przez siebie określoną liczbę razy. Oto implementacja rekurencyjna obliczania potęgi liczby:

```python
def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return number * power(number, n - 1)
```

<a name="liczby-pierwsze"></a>

### Liczby pierwsze

Liczba pierwsza to liczba całkowita większa od 1, która dzieli się tylko przez 1 i przez siebie. Oto rekurencyjna implementacja sprawdzania, czy dana liczba jest liczbą pierwszą:

```python
def prime(n: int, i: int = 2) -> bool:
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return prime(n, i + 1)
```

<a name="usuwanie-duplikatów"></a>

### Usuwanie duplikatów

Usuwanie duplikatów to proces usuwania kolejnych powtarzających się znaków z ciągu znaków. Oto rekurencyjna implementacja usuwania duplikatów:

```python
def remove_duplicates(txt: str, idx: int = 0) -> str:
    if not txt:
        return ""
    if idx == len(txt) - 1:
        return txt[idx]

    if txt[idx] == txt[idx + 1]:
        return remove_duplicates(txt, idx + 1)
    else:
        return txt[idx] + remove_duplicates(txt, idx + 1)
```

<a name="lista-jednokierunkowa"></a>

## Lista jednokierunkowa

Lista jednokierunkowa to struktura danych składająca się z węzłów, które zawierają element danych oraz wskaźnik na następny węzeł w sekwencji. Oto implementacja listy jednokierunkowej:

<a name="węzeł"></a>

### Węzeł

Węzeł to podstawowy element listy jednokierunkowej, który przechowuje dane oraz wskaźnik na następny węzeł:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

<a name="lista-jednokierunkowa-1"></a>

### Lista jednokierunkowa

Implementacja listy jednokierunkowej, która używa węzłów do przechowywania danych:

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
```

<a name="struktury-danych"></a>

## Struktury danych

Poniżej znajdują się różne struktury danych, takie jak grafy, drzewa binarne i stosy.

<a name="graf"></a>

### Graf

Graf to struktura danych składająca się z węzłów (wierzchołków) połączonych krawędziami. Grafy mogą być skierowane lub nieskierowane, ważone lub nieważone.

<a name="drzewo-binarne"></a>

### Drzewo binarne

Drzewo binarne to struktura danych, która składa się z węzłów, z których każdy może mieć co najwyżej dwóch potomków. Drzewo binarne jest zorganizowane hierarchicznie z korzeniem na szczycie.

<a name="węzeł-binarny"></a>

#### Węzeł binarny

Węzeł binarny to podstawowy element drzewa binarnego, który przechowuje dane oraz wskaźniki na lewego i prawego potomka:

```python
class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

<a name="drzewo-binarne-1"></a>

#### Drzewo binarne

Implementacja drzewa binarnego, które używa węzłów binarnych do przechowywania danych:

```python
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BinaryNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = BinaryNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = BinaryNode(data)
            else:
                self._insert_recursive(node.right, data)
```

<a name="stos"></a>

### Stos

Stos to kolekcja elementów, w której elementy są dodawane i usuwane zgodnie z zasadą "ostatni na wejściu, pierwszy na wyjściu" (LIFO). Poniżej znajduje się implementacja stosu:

```python

class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        return self._storage.remove_last()

    def __str__(self) -> str:
        ret = self._storage.__str__().split(" -> ")
        ret = [str(i) for i in ret]
        return "\n".join(ret[::-1])

    def __len__(self) -> int:
        return len(self._storage)
```

<a name="szyfry"></a>

## Szyfry

Szyfry to metody szyfrowania i deszyfrowania tekstu za pomocą kluczy. Poniżej znajduje się implementacja szyfru Cezara.

<a name="szyfr-cezara"></a>

### Szyfr Cezara

Szyfr Cezara to technika szyfrowania, która polega na zamianie każdej litery tekstu jawnego na inną literę przesuniętą o stałą liczbę pozycji w alfabecie. Oto implementacja szyfru Cezara:

```python
from string import ascii_lowercase as alphabet

alphabet = [letter for letter in alphabet]

class Ceasar:
    @staticmethod
    def encrypt(text: int, key: int) -> str:
        encrypted_text = ""
        text = text.lower()
        for letter in text:
            if letter in alphabet:
                encrypted_text += alphabet[
                    (alphabet.index(letter) + key) % len(alphabet)
                ]
            else:
                encrypted_text += letter
        return encrypted_text

    @staticmethod
    def decrypt(text: str, key:int) -> str:
        text = text.lower()
        return Ceasar.encrypt(text, -key)

    @staticmethod
    def brute_force(text: str) -> None:
        text = text.lower()
        for key in range(len(alphabet)):
            print(f"Key: {key} - {Ceasar.decrypt(text, key)}")
```
