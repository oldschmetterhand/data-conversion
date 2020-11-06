
## Items Table

### GENERAL

- same number of persons as items

```SQL
-- total item and perosn count count
SELECT
	(SELECT COUNT(*) FROM persons) AS person_count,
	COUNT(*) AS total_item_count
FROM
	items;

```


### gruppe column

- used some kind of controlled vocabulary
    e.g. NF - DF - AF
    multiple assignments per cell
    by far the most just have "NF"
    most have assignement (only 194 withpout group)
```SQL
-- grouped and counted by group 
SELECT
	COUNT(*) AS count,
	gruppe
FROM 
	items
GROUP BY 
	gruppe
ORDER BY 
	count
DESC;

```


### book_id column

- references a book

```SQL
-- group by book_id
SELECT 
	COUNT(*) id_occ_count,
	book_id
FROM
	items
GROUP BY
	book_id
ORDER BY 
	id_occ_count
DESC;

```


### art count

- count + group for art

```SQL
--
SELECT
	art,
  COUNT(*) AS count
FROM
	items
GROUP BY
	art;
-- only two things are not persons in terms of "art"


```

### zusaetze

```SQL
--
SELECT 
	COUNT(*) AS COUNT,
	zusaetze
FROM
	items
GROUP BY
	zusaetze;

-- most have no zusaetze 
-- free text to describe db entry for item
--  

```


### seiten

```SQL
SELECT 
	seiten,
	COUNT(*) AS total_count
FROM
	items
GROUP BY
	seiten
ORDER BY 
	total_count
DESC;

-- all items have seiten assigned
-- partly strange artefacts/html bode in database <b>348<b>

```


### dateiname

```SQL

SELECT 
	dateiname,
    COUNT(*) AS total_count,
    (SELECT COUNT(*) FROM items) AS total_item_count
FROM
	items
GROUP BY
	dateiname
ORDER BY 
	total_count
DESC;

-- by far the most have a dateiname
-- most pointing to the same file

```



### 