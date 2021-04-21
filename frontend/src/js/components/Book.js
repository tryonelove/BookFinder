import { Card, Image, Rate } from "antd";

import BookImg from "../../assets/images/book.jpg";

function Book(props) {
  const { data } = props;
  return (
    <Card title={data.title} className="book">
      <Image width={150} height={150} src={BookImg} />
      <span className="add_button">+</span>
      <p>Название: {data.title}</p>
      <p>Автор: {data.author_name}</p>
      <p>Год: {data.year === "" ? "Не указан" : data.year}</p>
      <Rate />
    </Card>
  );
}

export default Book;
