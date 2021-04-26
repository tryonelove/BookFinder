import { Card, Image } from "antd";

import BookImg from "../../assets/images/book.jpg";

function Book(props) {
  const { data } = props;
  return (
    <Card title={data.title} className="book">
      <Image width={150} height={150} src={BookImg} />
      <p>Название: {data.title}</p>
      <p>Автор: {data.author_name}</p>
      <p>Год: {data.year === "" ? "Не указан" : data.year}</p>
    </Card>
  );
}

export default Book;
