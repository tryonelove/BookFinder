import React, { useEffect, useState } from "react";
import { Pagination } from "antd";

import "../../styles/dialogBoxes.css";
import "../../styles/genres.css";
import AuthorizationHeader from "./AuthorizationHeader";
import requestService from "../services/requestService";
import history from "../history";
import { GENRES_PAGES_NUMBER } from "../constants/constants";

function Genres() {
  const [genres, setGenres] = useState();
  const [page, setPage] = useState(1);

  useEffect(() => {
    if (page != null) {
      requestService
        .get(`/api/registration/genres?page=${page}`)
        .then((data) => {
          setGenres(data);
        });
    }
  }, [page]);

  function sendFormData() {
    history.push("/main");
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
                ? genres.map((genre, index) => (
                    <span key={index}>{genre.genre_description}</span>
                  ))
                : ""}
            </div>
            <Pagination
              showSizeChanger={false}
              defaultCurrent={1}
              total={GENRES_PAGES_NUMBER*10}
              className="pagination"
              current={page}
              onChange={(page) => setPage(page)}
            />
            <input type="submit" value="Продолжить" onClick={sendFormData()} />
          </form>
        </div>
      </main>
    </div>
  );
}

export default Genres;
