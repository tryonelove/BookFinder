import { Card, Image } from "antd";

import BookImg from "../../assets/images/book.jpg";

function Book({ book, showModal }) {
  // function changeRate(rating) {
  //   console.log(rating);
  //   const userId = jwt_decode(localStorage.getItem("token")).id;
  //   const data = {
  //     user_id: userId,
  //     book_id: book.book_id,
  //     rating,
  //     status: ALREADY_READ,
  //   };
  //   requestService
  //     .post("/api/user/books/", data)
  //     .then(() => alert("Спасибо за отзыв! :)"));
  // }

  return (
    <Card title={book.title} className="book">
      <Image width={150} height={150} src={BookImg} />
      <span className="add_button" onClick={showModal}>
        +
      </span>
      <p>Название: {book.title}</p>
      <p>Автор: {book.author_name}</p>
      <p>Год: {book.year === "" ? "Не указан" : book.year}</p>
      {/* <Rate
        value={rating}
        onChange={(value) => changeRate(value)}
      /> */}
    </Card>
  );
}

export default Book;
