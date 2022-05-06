# Reseptiverkko

## Kuvaus
Reseptiverkko on nettisivu, jonka tarkoituksena on antaa käyttäjien jakaa omia reseptejään sivulla.

## Ominaisuudet
- Rekisteröinti (nimi väh 4 merkkiä, salasana väh 5)
- Kirjautuminen
- Reseptien lisääminen
- Reseptien selaaminen listana
- Reseptien haku hakukentässä
- Reseptiä luodessa on sille mahdollista asettaa hinta- että aikaarvio, sekä otsikko, ohje ja kategoria.
- Virhe ilmoitukset rekisteröidyttäessä sekä kirjauduttaessa.
- Reseptin luonnisa, mikäli reseptin nimi on jo varattu, pysyy kirjoitetut tiedot silti lomakkeessa.

## Nykytilanne
- Sovelluksessa toimii yllämainitut ominaisuudet.
- Sovelluksella on maltillinen mutta tyylikäs ja selkeä ulkoasu
- Sovellus tallentaa reseptit psql tietokantaan, sekä toiseen tietokantaa reseptin nimen ja luojan
- Reseptejä ei voi toistaiseksi muokata jälkikäteen.
- Reseptejä voi luoda ainoastaan kirjautuneena.
- Reseptiin tulee asettaa nimi, valita 1 kategoria, hintaluokka, aika sekä itse ohje.
- Reseptiä tarkastellessa näkyy myös reseptin luojan käyttäjänimi

## Testaaminen
Alla olevasta linkistä sovelluksen nykyversiota voi kokeilla.
https://reseptiverkko.herokuapp.com
