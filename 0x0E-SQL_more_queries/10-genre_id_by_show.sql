-- lists all shows contained in the hbtn_0d_tvshows with at least one
-- genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres
Group BY tv_shows.title, tv_show_genres.genre_id ORDER BY tv_shows.title ASC,
tv_show_genres.genre_id ASC
