---
sql:
    spotify: ./data/spotify-2023-limpo.csv
---

# Teste SQL
```sql id = histograma display
SELECT * FROM spotify
```

```sql id = histograma display
WITH SplitArtists AS (
    SELECT 
        unnest(regexp_split_to_array(artists_name, ', ')) AS artist,
        streams,
        released_year,
        track_name
    FROM 
        spotify
)
SELECT 
    artist AS artists,
    streams,
    track_name,
    released_year
FROM 
    SplitArtists;
```

