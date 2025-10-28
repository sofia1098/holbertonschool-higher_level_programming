-- Subquery

SELECT id, name
FROM cities
where state_id = (
    select id
    from states
    where name = 'California'
)
