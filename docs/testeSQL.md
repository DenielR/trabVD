---
sql:
    spotify: ./data/spotify-2023-limpo.csv
---

# Teste SQL

```sql id = teste display
WITH TotalCount AS (
    SELECT COUNT(*) as total
    FROM spotify
)
SELECT mode, 
       COUNT(*) as count, 
       (COUNT(*) * 100.0 / (SELECT total FROM TotalCount)) as percentage
FROM spotify
GROUP BY mode
```