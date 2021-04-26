import { Card, Image, Rate } from "antd";

import BookImg from "../../assets/images/book.jpg";

function Book({ book, showModal }) {
  return (
    <Card title={book.title} className="book">
      <Image width={150} height={150} src={BookImg} />
      <span className="add_button" onClick={showModal}>
        +
      </span>
      <p>Название: {book.title}</p>
      <p>Автор: {!book.author_name ? "Не указан" : book.author_name}</p>
      <p>Год: {book.year === "" || !book.year ? "Не указан" : book.year}</p>
      {book.rating ? <Rate disabled value={book.rating} /> : ""}
    </Card>
  );
}

export default Book;
