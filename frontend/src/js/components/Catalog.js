import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Spin, Pagination, Modal, Button } from "antd";

import requestService from "../services/requestService";
import Book from "./Book";

import "../../styles/catalog.css";

import GeneralHeader from "./GeneralHeader";
import { addBooksAction } from "../redux/booksReducer";

import { BOOKS_PAGES_NUMBER } from "../constants/constants";

function Catalog() {
  const [page, setPage] = useState(1);
  const dispatch = useDispatch();
  const books = useSelector((state) => state.books);
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [bookTitle, setBookTitle] = useState("");

  useEffect(() => {
    requestService.get(`/api/books?page=${page}`).then((data) => {
      dispatch(addBooksAction(data));
    });
  }, [page]);

  const showModal = (title) => {
    console.log(title);
    setBookTitle(title);
    setIsModalVisible(true);
  };

  const handleOk = () => {
    setIsModalVisible(false);
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  return (
    <>
      <Modal
        title="Выберите действие"
        visible={isModalVisible}
        onCancel={handleCancel}
        footer={[
          <Button key="submit" type="primary" onClick={handleOk}>
            Сохранить
          </Button>,
        ]}
      >
        <h4>{bookTitle}</h4>
        <p>Хочу прочитать</p>
        <p>Прочитал</p>
        <p>Читаю сейчас</p>
      </Modal>
      <GeneralHeader />
      <main className="catalog_main">
        {books == null ? (
          <Spin className="spin" id="spin" size="large" />
        ) : (
          <>
            <Pagination
              showSizeChanger={false}
              defaultCurrent={1}
              total={BOOKS_PAGES_NUMBER * 10}
              className="pagination"
              current={page}
              onChange={(page) => setPage(page)}
            />
            <div className="catalog">
              {books.map((book, index) => (
                <Book
                  key={index}
                  book={book}
                  showModal={() => showModal(book.title)}
                />
              ))}
            </div>
          </>
        )}
      </main>
    </>
  );
}

export default Catalog;
