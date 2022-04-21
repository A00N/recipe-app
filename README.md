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

## Nykytilanne
- Sovelluksessa toimii yllämainitut ominaisuudet. Kuitenkin vaikka kategorioita voi valita reseptiin useita, toimii ainoastaan yksi valituista.
- Sovelluksen ulkoasu on hyvin pelkistetty, ja siihen on myöhemmin tulossa parannuksia.
- Lisäksi kategorioita on varsin rajoitetusti, ja niitä tullaan lisäämään jatkossa.
- Sovellus tallentaa reseptit psql tietokantaan toistaiseksi kuitenkin ilman, että se pitää kirjaa reseptin lisääjästä.
- Reseptejä ei voi toistaiseksi muokata jälkikäteen.
- Reseptejä voi luoda ainoastaan kirjautuneena.
- Reseptiin tulee asettaa nimi, valita 1 kategoria (useampi ei tee mitään), hintaluokka sekä aika tai nettisivu kaatuu.

## Testaaminen
Alla olevasta linkistä sovelluksen nykyversiota voi kokeilla.
https://reseptiverkko.herokuapp.com
