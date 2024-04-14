# Ekonomiczne losy absolwentów kierunku informatyka na polskich uczelniach

## Autorzy
- Katarzyna Dudek 217369
- Jakub Czabok 217293
- Karolina Dekajło 217482
- Mateusz Chudowolski 217330

## Streszczenie pracy
Poniższa praca przedstawia badanie ekonomicznych losów absolwentów studiów informatycznych w Polsce. Poprzez zastosowanie metod statystycznych porządkowania obiektów utworzony zostanie swego rodzaju ranking porównujący uśrednioną sytuację ekonomiczną po ukończeniu poszczególnych studiów.

## Słowa kluczowe
Porządkowanie obiektów, statystyki zarobków i zatrudnienia, ekonomiczne losy absolwentów

## Wprowadzenie
Absolwenci kierunku informatyka odgrywają kluczową rolę w dzisiejszym społeczeństwie opartym na technologii. Jednakże, ich ekonomiczne losy po ukończeniu studiów mogą znacząco się różnić w zależności od wielu czynników. Niniejsza praca ma na celu zbadanie tych różnic oraz stworzenie rankingów porównujących sytuację ekonomiczną absolwentów poszczególnych uczelni i programów studiów informatycznych w Polsce.

## Przedmiot badania
Celem badania jest zastosowanie metod statystycznych porządkowania obiektów w celu utworzenia rankingów porównujących uśrednione sytuacje ekonomiczne absolwentów studiów informatycznych w Polsce. Analiza obejmuje zmienne takie jak zarobki po ukończeniu studiów, stopień zatrudnienia, lokalizacja zatrudnienia oraz ewentualne dodatkowe kwalifikacje. W literaturze istnieją badania pokazujące, że wybór konkretnej uczelni czy specjalizacji może mieć istotny wpływ na karierę zawodową i zarobki absolwentów.

### Zmienne wybrane do analizy:

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





## Opis metod
### Uzupełnienie pustych danych:
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

### Wartości odstające
W naszej analizie ekonomicznych losów absolwentów kierunku informatyka na polskich uczelniach nie było potrzeby obsługiwać obserwacji odstających. Wynika to głównie z charakteru danych oraz sposobu ich zbierania. Dane te są agregatami liczbowymi, takimi jak procent absolwentów w różnych kategoriach, mediany wynagrodzeń i inne miary podobne, które zostały zebrane na poziomie grupy absolwentów. Usunięcie takich obserwacji mogłoby zniekształcić rzeczywisty obraz sytuacji ekonomicznej absolwentów. Jednocześnie, po wstępnej analizie nie zauważyliśmy wyników, które można byloby uznać za nieprawidłowe- a odchylenia- zarówno te większe jak i mniejsze, są w naszej analizie bardzo ważne i pokazują jak bardzo różne są losy absolwentów po różnych uczelniach. Dlatego też zdecydowaliśmy się na pozostawienie danych w ich pierwotnej formie, bez dalszego przetwarzania w celu obsługi ewentualnych obserwacji odstających.

### Analiza metodą TOPSIS
Jako jedną z metod analizy danych wykorzystaliśmy TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) zaproponowaną przez Ching-Lai Hwang'a oraz Yoon'a w pracy "Multiple Attribute Decision Making: Methods and Applications" z 1981 roku. TOPSIS polega na utworzeniu wzorca jako zestaw najbardziej porządanych wartości cech oraz antywzorca jako przeciwieństwo reprezentowane przez wektor najmniej porządanych wartości. Po znormalizowaniu danych wejściowych i utworzeniu wzorca oraz antywzorca wynik analizy TOPSIS to iloraz odległości euklidesowej od antywzorca oraz sumy odległości od wzorca i antywzorca.

## Wyniki


## Podsumowanie
Praca skupiła się na badaniu ekonomicznych losów absolwentów studiów informatycznych w Polsce. Uzyskane wyniki potwierdzają istotność wyboru programu studiów i uczelni dla przyszłych perspektyw zawodowych i zarobków absolwentów. Odniesienie do literatury wskazuje na zgodność uzyskanych wyników z wcześniejszymi badaniami w dziedzinie.

## Bibliografia
