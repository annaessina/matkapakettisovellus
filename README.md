# Matkapakettisovellus

Ideana on luoda sovellus, missä käyttäjä voi ostaa itselleen matkapaketin.

## Toiminnot ovat:

- Käyttäjä voi kirjautua sisään tai luoda uuden tunnuksen
- Käyttäjä voi kirjautua ulos 
- Käyttäjä voi valita itselleen matkapaketin ja tarkastella kuvia kohteesta 
- Käyttäjä pystyy näkemään tietoja yrityksestä 
- Käyttäjä voi arvioida itse matkakohteita ja lukea muiden arviointeja
- Matkakohteista on lyhyet kuvaukset 
- Matkakohteet on listattu paremmuusjärjestyksessä eli tähtien mukaan
- Kun käyttäjä valitsee matkakohteen, hän näkee oman tilauksen 


# Käynnistysohjeet

1. Aluksi kloonaa tämä repositorio koneellesi ja siirry sen juurikansioon.   

2. Luo .env-tiedosto ja määritä  sisältö on seuraavanlaiseksi:

> DATABASE_URL=\<tietokannan-paikallinen-osoite>   
> SECRET_KEY=\<salainen-avain>

3. Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:

`$ python3 -m venv venv`  
`$ source venv/bin/activate`  
`$ pip install -r ./requirements.txt`

4. Määritä tietokannan skeema komennolla

`$ psql < schema.sql`

5. Sovellus käynnistyy komennolla

`$ flask run`


