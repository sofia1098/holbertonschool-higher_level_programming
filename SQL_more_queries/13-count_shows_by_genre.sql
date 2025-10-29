-- JOIN, count y group by

SELECT tv_genre.name AS genre, COUNT(tv_show_genre.show_id) AS number_of_shows
FROM tv_genres 
JOIN tv_show_genre ON tv_show_genre.id = tv_show_genre.genre_id
GROUP BY tv_show_genres.name
ORDER BY number_of_shows DESC;
