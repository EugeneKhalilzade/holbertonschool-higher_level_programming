-- Select all genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres
-- Join genres to the link table
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Join the link table to the shows table
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- Filter for the specific show
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
