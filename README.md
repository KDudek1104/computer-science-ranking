# Badanie perspektyw zawodowych absolwentów kierunku informatyka na polskich uczelniach

## Spis treści

1. [Tytuł pracy](#tytuł-pracy)
2. [Autorzy](#autorzy)
3. [Streszczenie](#streszczenie)
4. [Słowa kluczowe](#Słowa-Kluczowe)
5. [Wprowadzenie](#wprowadzenie)
6. [Przedmiot badania](#przedmiot-badania)
   - [Cel i zakres badania](#cel-i-zakres-badania)
   - [Przegląd literatury](#przegląd-literatury)
   - [Zmienne wybrane do analizy](#zmienne-wybrane-do-analizy)
   - [Wstępna analiza danych](#wstępna-analiza-danych)
     - [Statystyki opisowe](#statystyki-opisowe)
     - [Podstawowa wizualizacja](#podstawowa-wizualizacja)
     - [Braki danych](#braki-danych)
     - [Obserwacje odstające](#obserwacje-odstające)
7. [Opis metod](#opis-metod)
   - [Wzory wraz z opisami oznaczeń](#wzory-wraz-z-opisami-oznaczeń)
   - [Cytowanie pracy z metodą](#cytowanie-pracy-z-metodą)
8. [Rezultaty](#rezultaty)
   - [Tabele i/lub grafiki](#tabele-i/lub-grafiki)
   - [Omówienie wyników](#omówienie-wyników)
9. [Podsumowanie](#podsumowanie)
   - [Ocena realizacji celu](#ocena-realizacji-celu)
   - [Odniesienie do pozycji z przeglądu literatury](#odniesienie-do-pozycji-z-przeglądu-literatury)
10. [Bibliografia](#bibliografia)
    
# Tytuł pracy
Badanie perspektyw zawodowych absolwentów kierunku informatyka na polskich uczelniach

# Autorzy
- Katarzyna Dudek 217369
- Jakub Czabok 217293
- Karolina Dekajło 217482
- Mateusz Chudowolski 217330

# Streszczenie
Niniejsza analiza prezentuje badanie ekonomicznej sytuacji absolwentów studiów informatycznych w Polsce. Wykorzystując metody statystyczne do porządkowania danych, zostanie stworzony ranking, umożliwiający porównanie uśrednionej sytuacji ekonomicznej po ukończeniu poszczególnych programów studiów.

# Słowa kluczowe
Porządkowanie obiektów, statystyki zarobków i zatrudnienia, perspektywy zawodowe absolwentów

# Wprowadzenie
Absolwenci kierunku informatyka odgrywają kluczową rolę w dzisiejszym społeczeństwie opartym na technologii. Jednakże, ich ekonomiczne losy po ukończeniu studiów mogą znacząco się różnić w zależności od wielu czynników. Niniejsza praca ma na celu zbadanie tych różnic oraz stworzenie rankingów porównujących sytuację ekonomiczną absolwentów poszczególnych uczelni i programów studiów informatycznych w Polsce.

# Przedmiot badania
Celem badania jest zastosowanie metod statystycznych porządkowania obiektów w celu utworzenia rankingów porównujących uśrednione sytuacje ekonomiczne absolwentów studiów informatycznych w Polsce. Analiza obejmuje zmienne takie jak zarobki po ukończeniu studiów, stopień zatrudnienia, lokalizacja zatrudnienia oraz ewentualne dodatkowe kwalifikacje. W literaturze istnieją badania pokazujące, że wybór konkretnej uczelni czy specjalizacji może mieć istotny wpływ na karierę zawodową i zarobki absolwentów.

## Cel i zakres badania

## Przegląd literatury






## Zmienne wybrane do analizy:

| Skrót zmiennej         | Opis                                                                                                                                       | Rodzaj zmiennej   |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| P_CZY_BEZR_P1          | Procent absolwentów, którzy mieli doświadczenie bycia bezrobotnym w pierwszym roku po uzyskaniu dyplomu                                   | Destymulanta       |
| P_CZY_BEZR_P4          | Procent absolwentów, którzy mieli doświadczenie bycia bezrobotnym w czwartym roku po uzyskaniu dyplomu                                      | Destymulanta       |
| P_ME_ZAR_STUD_P1       | Mediana średnich miesięcznych wynagrodzeń absolwentów ze wszystkich źródeł w pierwszym roku po uzyskaniu dyplomu w okresach, gdy studiowali po uzyskaniu dyplomu | Stymulanta         |
| P_ME_ZAR_STUD_P4       | Mediana średnich miesięcznych wynagrodzeń absolwentów ze wszystkich źródeł w czwartym roku po uzyskaniu dyplomu w okresach, gdy studiowali po uzyskaniu dyplomu    | Stymulanta         |
| P_IF_2st               | Procent osób, które po ukończeniu studiów I stopnia podjęły studia II stopnia w pierwszym roku po uzyskaniu dyplomu                        | Stymulanta         |
| P_IF_2st_ucz           | Procent osób kontynuujących studia I stopnia na studiach II stopnia kiedykolwiek w badanym okresie, które kontynuują je na tej samej uczelni | Stymulanta         |
| P_ME_ZAR_ETAT_DOSW_P4 | Mediana średnich miesięcznych wynagrodzeń z tytułu umów o pracę w czwartym roku po uzyskaniu dyplomu absolwentów wśród absolwentów z doświadczeniem pracy przed uzyskaniem dyplomu | Stymulanta         |
| P_ME_ZAR_ETAT_NDOSW_P4| Mediana średnich miesięcznych wynagrodzeń z tytułu umów o pracę w czwartym roku po uzyskaniu dyplomu absolwentów nie wśród absolwentów z doświadczeniem pracy przed uzyskaniem dyplomu | Stymulanta         |


**Uzasadnienie:**

- **Destymulanty:** Zmienne `P_CZY_BEZR_P1` i `P_CZY_BEZR_P4` są istotne, ponieważ odzwierciedlają procent absolwentów, którzy mieli doświadczenie bycia bezrobotnym w pierwszym i czwartym roku po uzyskaniu dyplomu. Stanowią istotne wskaźniki niepewności ekonomicznej po ukończeniu studiów.

- **Stymulanty:** Pozostałe zmienne, takie jak `P_ME_ZAR_STUD_P1`, `P_ME_ZAR_STUD_P4`, `P_ME_ZAR_ETAT_DOSW_P4` oraz `P_ME_ZAR_ETAT_NDOSW_P4`, odzwierciedlają różne aspekty sytuacji ekonomicznej absolwentów, takie jak poziom wynagrodzeń, czy mediany wynagrodzeń w zatrudnieniu etatowym z i bez doświadczenia pracy przed uzyskaniem dyplomu. Pozwalają one na zrozumienie różnic w zarobkach wśród absolwentów kierunku informatyka na polskich uczelniach. Aby wyniki były jak najbardzie obiektywne, rozdzieliliśmy czas (1 rok- zaraz po studiach i 4 lata- po zdobyciu pierwszych doświadczeń na rynku), co zmiejsza znacząco losowość analizy. Użyliśmy do analizy rówenież `P_IF_2st`, `P_IF_2st_ucz`, które mówią o kontynuacji nauki na wyższym poziomie na danej uczelni. Zakładamy, że im lepsza uczelnia, tym częściej jej studenci zdecydują się na kontynuacje tam studiów drugiego stopnia, zamiast podejmować te studia na innej uczelni.

### Wstępna analiza danych
### Statystyki opisowe
### Podstawowa wizualizacja
### Braki danych
Braki danych były ważnym problemem w analizie, który należało obsłużyć. Wszystkie uczelnie miały pełne dane dotyczące bezrobocia i procentu osób kontynujących studia 2. stopnia na tej samej uczelni. Niestety, nie dysponowaliśmy przy niektórych pozycjach informacjami odnośnie zarobków (zarówno rok jak i 4 lata po dyplomie). Pozycje, w których brakowało obu kolumn w danym roku po uzyskaniu dyplomu (1 lub 4) zarówno w medianie zarobków z tytułu o prace, jak i medianie zarobków ze wszystkich źródeł, były usuwane. Uważamy, że symulacja tak ważnych kolumn w naszej analizie nie byłaby wystarczająco obiektywna. Jeśli jednak mieliśmy dane odnośnie co najmniej jednej kolumny (patrząc osobno na rok 1. i rok 4.), symulowliśmy dane w kolumnie z tym samym rokiem po uzyskaniu dyplomu. Odpowiednio:
1. Gdy brakowało danej w kolumnie 'P_ME_ZAR_STUD_P1', ale mieliśmy tą daną w kolumnie 'P_ME_ZAR_STUD_P4', mnożyliśmy wartość dla tego wiersza z kolumny 'P_ME_ZAR_STUD_P4' przez współczynnik przejścia między średnią ze wszystkich wartości z kolumny 'P_ME_ZAR_STUD_P1', a 'P_ME_ZAR_STUD_P4'
2. Analogicznie w odwrotnym przypadku (gdy brakowało danej w kolumnie 'P_ME_ZAR_STUD_P4', ale mieliśmy tą daną w kolumnie 'P_ME_ZAR_STUD_P1')
3. Gdy brakowało danej w kolumnie `P_ME_ZAR_ETAT_DOSW_P4`, ale mieliśmy tą daną w kolumnie `P_ME_ZAR_ETAT_NDOSW_P4`, mnożyliśmy wartość dla tego wiersza z kolumny `P_ME_ZAR_ETAT_NDOSW_P4` przez współczynnik przejścia między średnią ze wszystkich wartości z kolumny `P_ME_ZAR_ETAT_DOSW_P4`, a `P_ME_ZAR_ETAT_NDOSW_P4`.
4. 
#### Dzialanie programu uzupełniającego puste dane:
1. Program oblicza średnie wartości dla określonych kolumn, które są używane jako współczynniki w symulacji.
2. Tworzy maski dla komórek, które zawierają brakujące dane w poszczególnych kolumnach.
3. Na podstawie tych maski oraz wcześniej obliczonych średnich wartości, program przeprowadza mnożenie wartości w pustych komórkach przez odpowiednie współczynniki. Te współczynniki są stosowane proporcjonalnie do danych w innych kolumnach lub na podstawie innych czynników, które są istotne dla analizy.
4. Wartości te są używane do uzupełnienia brakujących danych, co pozwala zachować spójność i logiczność danych w analizie.

#### Fragmenty kodu:

```python
mean_P_ME_ZAR_STUD_P4 = df['P_ME_ZAR_STUD_P4'].mean()
mean_P_ME_ZAR_STUD_P1 = df['P_ME_ZAR_STUD_P1'].mean()
```
Obliczamy średnie wartości dla kolumn `P_ME_ZAR_STUD_P4` i `P_ME_ZAR_STUD_P1`.

```python
mask_P1 = df['P_ME_ZAR_STUD_P1'].isnull()
df.loc[mask_P1, 'P_ME_ZAR_STUD_P1'] = df.loc[mask_P1, 'P_ME_ZAR_STUD_P4'] * (mean_P_ME_ZAR_STUD_P1 / mean_P_ME_ZAR_STUD_P4)
```
Tworzymy maskę (`mask_P1`), która wskazuje, które wartości w kolumnie `P_ME_ZAR_STUD_P1` są puste. Używamy tej maski do znalezienia odpowiednich wierszy w kolumnie `P_ME_ZAR_STUD_P4`, aby uzyskać wartości, które wykorzystamy do uzupełnienia pustych miejsc w kolumnie `P_ME_ZAR_STUD_P1`. Wartości są uzupełniane na podstawie proporcji między średnimi wartościami `P_ME_ZAR_STUD_P4` i `P_ME_ZAR_STUD_P1`.

Analogiczne operacje wykonywane są dla pozostałych kolumn i wartości.

```python
df.to_excel('uzupelnione.xlsx', index=False)
```
Po uzupełnieniu pustych wartości, zapisujemy zmodyfikowane dane do nowego pliku Excel, który można wykorzystać do dalszych analiz.

### Obserwacje odstające
W naszej analizie ekonomicznych losów absolwentów kierunku informatyka na polskich uczelniach nie było potrzeby obsługiwać obserwacji odstających. Wynika to głównie z charakteru danych oraz sposobu ich zbierania. Dane te są agregatami liczbowymi, takimi jak procent absolwentów w różnych kategoriach, mediany wynagrodzeń i inne miary podobne, które zostały zebrane na poziomie grupy absolwentów. Usunięcie takich obserwacji mogłoby zniekształcić rzeczywisty obraz sytuacji ekonomicznej absolwentów. Jednocześnie, po wstępnej analizie nie zauważyliśmy wyników, które można byloby uznać za nieprawidłowe- a odchylenia- zarówno te większe, jak i mniejsze, są w naszej analizie bardzo ważne i pokazują jak bardzo różnią się losy absolwentów po różnych uczelniach. Dlatego też zdecydowaliśmy się na pozostawienie danych w ich pierwotnej formie, bez dalszego przetwarzania w celu obsługi ewentualnych obserwacji odstających.

# Opis metod

### Analiza metodą TOPSIS
Jako jedną z metod analizy danych wykorzystaliśmy TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) zaproponowaną przez Ching-Lai Hwang'a oraz Yoon'a w pracy "Multiple Attribute Decision Making: Methods and Applications" z 1981 roku. TOPSIS polega na utworzeniu wzorca jako zestaw najbardziej porządanych wartości cech oraz antywzorca jako przeciwieństwo reprezentowane przez wektor najmniej porządanych wartości. Po znormalizowaniu danych wejściowych i utworzeniu wzorca oraz antywzorca wynik analizy TOPSIS to iloraz odległości euklidesowej od antywzorca oraz sumy odległości od wzorca i antywzorca.

### Analiza metodą Hellwiga
W ramach naszej analizy danych skorzystaliśmy z metody Hellwiga, która została opracowana przez Leo A. Hellwiga w 1972 roku. Jest to jedna z najczęściej stosowanych technik analizy danych, zwłaszcza w kontekście porządkowania liniowego. Metoda ta bazuje na minimalizacji kryteriów skrajnych, co umożliwia wyłonienie istotnych cech lub zmiennych decyzyjnych. Poprzez dokładne porównanie poszczególnych zmiennych, analiza przy użyciu metody Hellwiga pozwala na ich uporządkowanie z uwzględnieniem ich znaczenia w kontekście badanych danych.

### Analiza metodą MUZ
W naszym badaniu danych wykorzystaliśmy Metodę Ujednoliconego Zmniejszania (MUZ) do uporządkowania liniowego danych. MUZ, będąca techniką minimalizacji kryteriów skrajnych, umożliwia wyodrębnienie kluczowych cech lub zmiennych decyzyjnych. Poprzez dokładne porównanie poszczególnych zmiennych, analiza za pomocą MUZ pozwoliła nam na ich hierarchiczne uporządkowanie, uwzględniając ich istotność w badanym kontekście.

### Wyniki


# Podsumowanie
Praca skupiła się na badaniu ekonomicznych losów absolwentów studiów informatycznych w Polsce. Uzyskane wyniki potwierdzają istotność wyboru programu studiów i uczelni dla przyszłych perspektyw zawodowych i zarobków absolwentów. Odniesienie do literatury wskazuje na zgodność uzyskanych wyników z wcześniejszymi badaniami w dziedzinie.
## Ocena realizacji celu
## Odniesienie do pozycji z przeglądu literatury
# Bibliografia
