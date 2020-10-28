

# Persons Table

## General Information

- display all persons

```SQL
SELECT 
	*
FROM
	persons;

```

- count all persons + count with assigned gnd number
```SQL
SELECT 
	(SELECT COUNT(*) FROM persons) AS total_persons_count, 
 	COUNT(*) AS with_gnd_count
FROM
	persons
WHERE
	gndnummer != 0

```

## vorname 

```SQL
SELECT
	vorname,
    COUNT(*) AS count
FROM
	persons
GROUP BY
	vorname
HAVING
	count > 100
ORDER BY 
	count
DESC;
-- all persons have at least some value although field is nullable

```

## vornamenvarianten

```SQL
SELECT
	vornamenvarianten,
  COUNT(*) AS count
FROM 
	persons
GROUP BY
	vornamenvarianten
ORDER BY
	count
DESC;
-- empty field is by far most common = 70171

```


## familienname 

```SQL
SELECT 
	familienname,
    COUNT(*) AS count
FROM 
	persons
GROUP BY
	familienname
ORDER BY
	count
DESC;
-- 17341 have empty family name


```

## titel

```SQL
SELECT 
	COUNT(*) AS count,
	titel
FROM
	persons
GROUP BY
	titel
ORDER BY 
	count
DESC;
-- by far the most have no titel assigned: 78221


```

## orden

- group and count orden 
```SQL
SELECT
	orden,
  COUNT(*) AS count
FROM 
	persons
GROUP BY 
	orden
ORDER BY
	count
DESC;
-- 78511 have no orden value

```

- count occurence (from query before -- grouped by)

```SQL
SELECT
	count AS orden_occurence,
    COUNT(*) AS counted_orden_occurence
FROM ( 
	SELECT
		orden,
		COUNT(*) AS count
		FROM 
			persons
		GROUP BY 
			orden
		ORDER BY
			count
		DESC
	) AS grouped
GROUP BY 
	grouped.count
ORDER BY
	counted_orden_occurence
DESC;
-- most orden are just used once!

```

## belegdaten

```SQL

SELECT 
	belegdaten,
    COUNT(*) AS count
FROM 
	persons
GROUP BY
	belegdaten
ORDER BY 
	count
DESC;
-- most often assigned per person
-- but very diverse entry

```

## zeitraum_bis -- zeitraum_von

- Grouped after both and counted
```SQL
SELECT
	zeitraum_bis,
    zeitraum_von,
    COUNT(*) AS count
FROM
	persons
GROUP BY
	zeitraum_bis
ORDER BY 
	count
DESC;
-- both null is most common pair by far. 
-- BUT: not in absolute sense --- most of persons have dates assigned
-- 

```

## geburtstdatum

- as VARCHAR

```SQL
-- relative comparison pers-count vs total person_count
SELECT
	(SELECT COUNT(*) FROM persons) AS total_persons_count, 
	COUNT(geburtsdatum) AS with_birth_date
FROM
	persons
WHERE 
	geburtsdatum != 0;
-- 4844 / 79611 

SELECT
	geburtsdatum,
    COUNT(*) AS count
FROM
	persons
GROUP BY
	geburtsdatum
ORDER BY 
	count
DESC;

```


## sterbedatum

```SQL
SELECT 
	sterbedatum,
  COUNT(*) AS count
FROM
	persons
GROUP BY
	sterbedatum
ORDER BY
	count
DESC;
-- by far the most have no sterbedatum

```


## taetigkeit

```SQL

SELECT 
	taetigkeit,
    COUNT(taetigkeit) AS count
FROM
	persons
GROUP BY 
	taetigkeit
ORDER BY 
	count
DESC;
-- ~ 65000 have no tätigkeit assigned.
-- 'Ritter' is the second most common.

```

## verwandtschaften

```SQL
SELECT 
	verwandtschaften,
    COUNT(*) AS count
FROM
	persons
GROUP BY
	verwandtschaften
ORDER BY 
	count
DESC;
-- most have no verwandtschaften
-- very diverse entries.


```


## GND + cerlid + viaf

- count cerlid
```SQL
SELECT 
	(SELECT COUNT(*) FROM persons) AS total_persons_count,
	COUNT(cerlid) AS cerlid_count
FROM 
	persons
WHERE
	cerlid != '';
-- 16836/79611 have an assigned cerlid

```

- count viaf

```SQL

SELECT 
	(SELECT COUNT(*) FROM persons) AS total_persons_count,
	COUNT(viaf) AS viaf_count
FROM 
	persons
WHERE
	viaf != '';

-- 9 / 79611 have assigned viaf
-- there is also malformed data inside "von Münster" as VIAF

```

-- GND

```SQL

-- 
SELECT 
	(SELECT COUNT(*) FROM persons) AS total_persons_count, 
 	COUNT(*) AS with_gnd_count
FROM
	persons
WHERE
	gndnummer != ''


```