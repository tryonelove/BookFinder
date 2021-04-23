import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Spin, Pagination, Modal, Button, Rate } from "antd";
import jwt_decode from "jwt-decode";

import requestService from "../services/requestService";
import Book from "./Book";

import "../../styles/catalog.css";

import GeneralHeader from "./GeneralHeader";
import { addBooksAction } from "../redux/booksReducer";

import {
  ALREADY_READ,
  BOOKS_PAGES_NUMBER,
  NO_RATING,
  READING_NOW,
  WANT_TO_READ,
} from "../constants/constants";

function Catalog() {
  const [page, setPage] = useState(1);
  const dispatch = useDispatch();
  const books = useSelector((state) => state.books);
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [currentBook, setCurrentBook] = useState("");
  const [isRateVisible, setIsRateVisible] = useState(false);
  const [bodyData, setBodyData] = useState({});

  useEffect(() => {
    requestService.get(`/api/books?page=${page}`).then((data) => {
      dispatch(addBooksAction(data));
    });
  }, [page]);

  const showModal = (book) => {
    console.log(book);
    setCurrentBook(book);
    setIsModalVisible(true);
  };

  const handleOk = () => {
    requestService
      .post("/api/user/books/", bodyData)
      .then((data) => console.log(data));
    setIsModalVisible(false);
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  //выделение цветом при клике

  function changeBookStatus(status, rating) {
    const userId = jwt_decode(localStorage.getItem("token")).id;
    setBodyData({
      user_id: userId,
      book_id: currentBook.book_id,
      status,
      rating,
    });
  }

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
        <h4>{currentBook.title}</h4>
        <p
          onClick={() => changeBookStatus(WANT_TO_READ, NO_RATING)}
          onMouseOver={() => setIsRateVisible(false)}
        >
          Хочу прочитать
        </p>
        <div
          className="already_read_modal_wrapper"
          onMouseOver={() => setIsRateVisible(true)}
        >
          <p>
            Прочитал <br />
            Ваша оценка
          </p>
          <Rate
            className={isRateVisible === true ? "rate_visible" : ""}
            onChange={(value) => changeBookStatus(ALREADY_READ, value)}
          />
        </div>
        <p
          onClick={() => changeBookStatus(READING_NOW, NO_RATING)}
          onMouseOver={() => setIsRateVisible(false)}
        >
          Читаю сейчас
        </p>
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
                  showModal={() => showModal(book)}
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
