import React, { useEffect, useState } from "react";
import jwt_decode from "jwt-decode";
import { Empty, Image } from "antd";

import GeneralHeader from "./GeneralHeader";
import Footer from "./Footer";
import BookWormImage from "../../assets/images/bookworm.svg";

import "../../styles/main.css";
import "../../styles/myLibrary.css";
import requestService from "../services/requestService";
import { bookStates } from "../constants/constants";
import Book from "./Book";
import StateModal from "./StateModal";

function MyLibrary() {
  const [books, setBooks] = useState(new Map());
  const [recBooks, setRecBooks] = useState([]);
  const [isModalVisible, setIsModalVisible] = useState(false);
  const [currentBook, setCurrentBook] = useState("");
  const [rerenderFlag, setRerenderFlag] = useState(true);

  useEffect(() => {
    let booksMap = new Map(initMap());
    const userId = jwt_decode(localStorage.getItem("token")).id;
    requestService.get(`/api/user/books/?user_id=${userId}`).then((data) =>
      data.forEach((element) => {
        requestService.get(`/api/books/${element.book_id}`).then((data) => {
          booksMap = groupBooks(data, element.status, element.rating, booksMap);
          setBooks(new Map(booksMap));
        });
      })
    );
  }, [rerenderFlag]);

  useEffect(() => {
    const userId = jwt_decode(localStorage.getItem("token")).id;
    requestService
      .get(`/api/user/recommendations/?user_id=${userId}`)
      .then((data) => setRecBooks(data.books));
  }, []);

  function initMap() {
    let booksMap = new Map();
    booksMap.set(bookStates.WANT_TO_READ, []);
    booksMap.set(bookStates.READING_NOW, []);
    booksMap.set(bookStates.ALREADY_READ, []);
    return booksMap;
  }

  function groupBooks(book, status, rating, booksMap) {
    console.log(status);
    switch (status) {
      case bookStates.WANT_TO_READ:
        booksMap.set(bookStates.WANT_TO_READ, [
          ...booksMap.get(bookStates.WANT_TO_READ),
          book,
        ]);
        break;
      case bookStates.READING_NOW:
        booksMap.set(bookStates.READING_NOW, [
          ...booksMap.get(bookStates.READING_NOW),
          book,
        ]);
        break;
      case bookStates.ALREADY_READ:
        booksMap.set(bookStates.ALREADY_READ, [
          ...booksMap.get(bookStates.ALREADY_READ),
          { ...book, rating },
        ]);
        break;
    }
    return booksMap;
  }

  const showModal = (book) => {
    setCurrentBook(book);
    setIsModalVisible(true);
  };

  const handleOk = () => {
    rerenderFlag === true ? setRerenderFlag(false) : setRerenderFlag(true);
    setIsModalVisible(false);
  };

  const handleCancel = () => {
    setIsModalVisible(false);
  };

  return (
    <>
      <StateModal
        isModalVisible={isModalVisible}
        currentBook={currentBook}
        handleOk={handleOk}
        handleCancel={handleCancel}
      />
      <GeneralHeader />
      <main className="library_main">
        <section className="general_user_info_wrapper">
          <div className="image_wrapper">
            <Image width={200} src={BookWormImage} />
          </div>
          <div className="user_info_wrapper">
            <p>{jwt_decode(localStorage.getItem("token")).name}</p>
            <div className="books_info_wrapper">
              <span>
                Прочитано:{" "}
                <strong>
                  {books.get(bookStates.ALREADY_READ)
                    ? books.get(bookStates.ALREADY_READ).length
                    : 0}
                </strong>
              </span>
              <span>
                Читаю сейчас:{" "}
                <strong>
                  {books.get(bookStates.READING_NOW)
                    ? books.get(bookStates.READING_NOW).length
                    : 0}
                </strong>
              </span>
              <span>
                Хочу прочитать:{" "}
                <strong>
                  {books.get(bookStates.WANT_TO_READ)
                    ? books.get(bookStates.WANT_TO_READ).length
                    : 0}
                </strong>
              </span>
            </div>
          </div>
        </section>
        <section className="week_selection_wrapper">
          <h1>Подборка недели</h1>
          <div className="week_selection_books_wrapper catalog">
            {recBooks ? (
              recBooks.map((book, index) => (
                <Book
                  key={index}
                  book={book}
                  showModal={() => showModal(book)}
                />
              ))
            ) : (
              <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} />
            )}
          </div>
        </section>
        <section className="already_read_wrapper">
          <h1>
            Прочитано -{" "}
            {books.get(bookStates.ALREADY_READ)
              ? books.get(bookStates.ALREADY_READ).length
              : 0}
          </h1>
          <div className="already_read_books_wrapper catalog">
            {books.get(bookStates.ALREADY_READ) &&
            books.get(bookStates.ALREADY_READ).length ? (
              books
                .get(bookStates.ALREADY_READ)
                ?.map((book, index) => (
                  <Book
                    key={index}
                    book={book}
                    showModal={() => showModal(book)}
                  />
                ))
            ) : (
              <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} />
            )}
          </div>
        </section>
        <section className="reading_now_wrapper">
          <h1>
            Читаю сейчас -{" "}
            {books.get(bookStates.READING_NOW)
              ? books.get(bookStates.READING_NOW).length
              : 0}
          </h1>
          <div className="reading_now_books_wrapper catalog">
            {books.get(bookStates.READING_NOW) &&
            books.get(bookStates.READING_NOW).length ? (
              books
                .get(bookStates.READING_NOW)
                .map((book, index) => (
                  <Book
                    key={index}
                    book={book}
                    showModal={() => showModal(book)}
                  />
                ))
            ) : (
              <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} />
            )}
          </div>
        </section>
        <section className="want_to_read_wrapper">
          <h1>
            Хочу прочитать -{" "}
            {books.get(bookStates.WANT_TO_READ)
              ? books.get(bookStates.WANT_TO_READ).length
              : 0}
          </h1>
          <div className="want_to_read_books_wrapper catalog">
            {books.get(bookStates.WANT_TO_READ) &&
            books.get(bookStates.WANT_TO_READ).length ? (
              books
                .get(bookStates.WANT_TO_READ)
                .map((book, index) => (
                  <Book
                    key={index}
                    book={book}
                    showModal={() => showModal(book)}
                  />
                ))
            ) : (
              <Empty image={Empty.PRESENTED_IMAGE_SIMPLE} />
            )}
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}

export default MyLibrary;
