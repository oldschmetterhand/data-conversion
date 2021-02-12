

# 1. Konkordanz Personen

```SQL

SELECT 
	vorname,
	familienname,
	viaf,
	gndnummer,
	-- gs_datenbank.items.id AS joined_item_id,
	gs_datenbank.gsn.nummer AS gsn_nummer,
	'http://germania-sacra-datenbank.uni-goettingen.de/index/gsn/' || gs_datenbank.gsn.nummer AS GSN_LINK
FROM
	gs_datenbank.persons
JOIN
	gs_datenbank.offices
	ON
	gs_datenbank.offices.person_id = gs_datenbank.persons.id
JOIN
	gs_datenbank.items
	ON
	gs_datenbank.persons.item_id = gs_datenbank.items.id 
JOIN
	gs_datenbank.gsn
	ON
	gs_datenbank.items.id = gs_datenbank.gsn.item_id 
WHERE
	gs_datenbank.offices.art = 'geistlich'



```

# 2. Konkordanz Klöster

```SQL
-- Klöster mit url
SELECT
	monastery_name,
	id_gsn,
	'https://adw-goe.de/forschung/forschungsprojekte-akademienprogramm/germania-sacra/klosterdatenbank/datenbankabfrage/gsn/' || id_gsn AS Kloster_url
FROM
	gs_klosterdatenbank.gs_monastery


-- klöster mit orte mit gnd / wikidata etc.
-- recht viele
SELECT
	monastery_name,
	id_gsn,
	'https://adw-goe.de/forschung/forschungsprojekte-akademienprogramm/germania-sacra/klosterdatenbank/datenbankabfrage/gsn/' || id_gsn AS Kloster_url,
	location_name,
	place_name,
	geonames_id,
	wikidata_qid
FROM
	gs_klosterdatenbank.gs_monastery
JOIN
	gs_klosterdatenbank.gs_monastery_location
	ON
	gs_klosterdatenbank.gs_monastery_location.gsn_id = gs_klosterdatenbank.gs_monastery.id_gsn
JOIN
	gs_klosterdatenbank.gs_places
	ON
	gs_klosterdatenbank.gs_monastery_location.place_id = gs_klosterdatenbank.gs_places.id_places


```

# 3.Officeskonkordanz


```SQL

SELECT
	bezeichnung,
	weihegrad,
	vorname,
	persons.id AS person_id
FROM
	gs_datenbank.offices
JOIN
	gs_datenbank.persons
	ON
	gs_datenbank.offices.person_id = gs_datenbank.persons.id
WHERE
	art = 'geistlich'
	


-- mit verbundenem Kloster!
SELECT
	bezeichnung,
	weihegrad,
	vorname,
	persons.id AS person_id,
	monastery_name
FROM
	gs_datenbank.offices
JOIN
	gs_datenbank.persons
	ON
	gs_datenbank.offices.person_id = gs_datenbank.persons.id
JOIN
	gs_klosterdatenbank.gs_monastery
	ON
	gs_datenbank.offices.klosterid = gs_klosterdatenbank.gs_monastery.id_gsn
WHERE
	art = 'geistlich'
	
-- unique offices ordered by count
SELECT
	bezeichnung,
	COUNT(*) AS occurence
FROM
	gs_datenbank.offices
JOIN
	gs_datenbank.persons
	ON
	gs_datenbank.offices.person_id = gs_datenbank.persons.id
WHERE
	art = 'geistlich'
GROUP BY 
	bezeichnung
ORDER BY
	occurence
DESC


```