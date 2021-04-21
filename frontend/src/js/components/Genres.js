import React, { useEffect, useState } from "react";
import { Pagination } from "antd";

import "../../styles/dialogBoxes.css";
import "../../styles/genres.css";
import AuthorizationHeader from "./AuthorizationHeader";
import requestService from "../services/requestService";
import history from "../history";
import { GENRES_PAGES_NUMBER, MIN_GENRES_NUMBER } from "../constants/constants";
import Genre from "./Genre";

function Genres() {
  const [genres, setGenres] = useState();
  const [page, setPage] = useState(1);
  const [genresIdList, setGenresIdList] = useState([]);

  useEffect(() => {
    if (page != null) {
      requestService
        .get(`/api/registration/genres?page=${page}`)
        .then((data) => {
          setGenres(data);
        });
    }
  }, [page]);

  function sendFormData(event) {
    event.preventDefault();
    genresIdList.length >= MIN_GENRES_NUMBER
      ? history.push("/main")
      : alert(`Минимальное количество жанров: ${MIN_GENRES_NUMBER}`);
  }

  function addGenreId(genreId) {
    setGenresIdList([...genresIdList, genreId]);
  }

  return (
    <div className="authorization">
      <AuthorizationHeader />
      <main className="main genresMain">
        <div className="form_wrapper">
          <form action="">
            <h2>Позвольте нам узнать о вас больше</h2>
            <h3>Какие жанры вас интересуют?</h3>
            <div className="genres">
              {genres
                ? genres.map((genre) => (
                    <Genre
                      key={genre.genre_id}
                      genre={genre}
                      addGenreId={() => addGenreId(genre.genre_id)}
                      genresIdList={genresIdList}
                    />
                  ))
                : ""}
            </div>
            <Pagination
              showSizeChanger={false}
              defaultCurrent={1}
              total={GENRES_PAGES_NUMBER * 10}
              className="pagination"
              current={page}
              onChange={(page) => setPage(page)}
            />
            <input
              type="submit"
              value="Продолжить"
              onClick={(event) => sendFormData(event)}
            />
          </form>
        </div>
      </main>
    </div>
  );
}

export default Genres;
