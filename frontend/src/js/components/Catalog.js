import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Spin } from "antd";
import { Pagination } from "antd";

import requestService from "../services/requestService";
import Book from "./Book";

import "../../styles/catalog.css";

import GeneralHeader from "./GeneralHeader";
import { addBooksAction } from "../redux/booksReducer";

import { BOOKS_NUMBER, BOOKS_PAGES_NUMBER } from "../constants/constants";

function Catalog() {
  const [page, setPage] = useState(1);
  const dispatch = useDispatch();
  const books = useSelector((state) => state.books);

  useEffect(() => {
    requestService.get(`/api/books?page=${page}`).then((data) => {
      dispatch(addBooksAction(data));
    });
  }, [page]);

  return (
    <>
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
                <Book key={index} data={book} />
              ))}
            </div>
          </>
        )}
      </main>
    </>
  );
}

export default Catalog;
