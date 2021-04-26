import { useEffect, useState } from "react";
import { Modal, Button, Rate } from "antd";
import { bookStates, NO_RATING } from "../constants/constants";
import jwt_decode from "jwt-decode";
import requestService from "../services/requestService";

function StateModal({ isModalVisible, currentBook, handleOk, handleCancel }) {
  const [bodyData, setBodyData] = useState({});
  const [currentState, setCurrentState] = useState("");
  const [defaultValue, setDefaultValue] = useState(0);

  useEffect(() => setDefaultValue(0), [isModalVisible]);

  function changeBookStatus(status, rating) {
    const userId = jwt_decode(localStorage.getItem("token")).id;
    setBodyData({
      user_id: userId,
      book_id: currentBook.book_id,
      status,
      rating,
    });
  }

  function saveState() {
    requestService.post("/api/user/books/", bodyData).then((data) => {
      setCurrentState("");
      handleOk();
    });
  }

  return (
    <Modal
      title="Выберите действие"
      visible={isModalVisible}
      onCancel={handleCancel}
      footer={[
        <Button key="submit" type="primary" onClick={saveState}>
          Сохранить
        </Button>,
      ]}
    >
      <h4>{currentBook ? currentBook.title : ""}</h4>
      <p
        onClick={() => {
          changeBookStatus(bookStates.WANT_TO_READ, NO_RATING);
          setCurrentState(bookStates.WANT_TO_READ);
        }}
        className={
          currentState === bookStates.WANT_TO_READ ? "selected_state" : ""
        }
      >
        Хочу прочитать
      </p>
      <div
        onClick={() => setCurrentState(bookStates.ALREADY_READ)}
        className={
          currentState === bookStates.ALREADY_READ
            ? "selected_state already_read_modal_wrapper"
            : "already_read_modal_wrapper"
        }
      >
        <p>Прочитал</p>
        <div className="rate_wrapper">
          <p>Ваша оценка</p>
          <Rate
            value={defaultValue}
            onChange={(value) => {
              changeBookStatus(bookStates.ALREADY_READ, value);
              setDefaultValue(value);
            }}
          />
        </div>
      </div>
      <p
        onClick={() => {
          changeBookStatus(bookStates.READING_NOW, NO_RATING);
          setCurrentState(bookStates.READING_NOW);
        }}
        className={
          currentState === bookStates.READING_NOW ? "selected_state" : ""
        }
      >
        Читаю сейчас
      </p>
    </Modal>
  );
}

export default StateModal;
