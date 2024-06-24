-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT tv_shows.title, tv_show_genres.genre_id FROM hbtn_0d_tvshows;
INNER JOIN tv_show_genres ON hbtn_0d_tvshows.id = tv_show_genres.show_id
ORDER BY hbtn_0d_tvshows.title, tv_show_genres.genre_id ASC;