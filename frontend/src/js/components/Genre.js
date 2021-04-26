import jwt_decode from "jwt-decode";
import { useState } from "react";
import requestService from "../services/requestService";

function Genre(props) {
  const { genre, addGenreId, genresIdList } = props;

  const [assignedGenreFlag, setAssignedGenreFlag] = useState(false);

  function assignGenreToUser(genreId) {
    addGenreId();
    const userId = jwt_decode(localStorage.getItem("token")).id;
    requestService
      .post(`/api/registration/genres`, { user_id: userId, genre_id: genreId })
      .then((data) => {
        setAssignedGenreFlag(true);
      });
  }

  return (
    <span
      className={
        assignedGenreFlag === true || genresIdList.includes(genre.genre_id)
          ? "assigned_genre"
          : ""
      }
      onClick={() => assignGenreToUser(genre.genre_id)}
    >
      {genre.genre_description}
    </span>
  );
}

export default Genre;
