import * as types from "./actionTypes";
import axios from "axios";
import GLOBAL_CONSTANTS from "../../GlobalConstants.js";

// utils
import { toast } from "react-toastify";

export const user_login = (data, callback) => {
    return function (dispatch) {
      var headers = {
        "Content-type": "application/json",
      };
      axios
        .post(`${GLOBAL_CONSTANTS.backend_url}auth/login`, JSON.stringify(data), {
          headers,
        })
        .then((resp) => {
         
          if(! resp?.data?.status)
          {
            toast.error(resp?.data?.message);  
          }
          else
          {
            toast.success("Logged in");
            localStorage.setItem("user_data",JSON.stringify(resp?.data));  
            dispatch({
              type: types.LOGIN,
              payload: resp?.data,
            });

            sessionStorage.setItem("user_data",JSON.stringify(resp?.data))
            callback(resp?.data);
          }

        })
        .catch((error) => {

          toast.error(
            error ?? "Something went wrong",
            {
              autoClose: 2000,
            }
          );
        });
    };
  };

  export const user_signup = (data, callback) => {
    return function () {
      var headers = {
        "Content-type": "application/json",
      };
      axios
        .post(`${GLOBAL_CONSTANTS.backend_url}auth/register`, JSON.stringify(data), {
          headers,
        })
        .then((resp) => {
          if(resp?.data?.error)
          {
            toast.error(resp?.data?.error);  
          }
          else
          {
            toast.success("User Created Sucessfully");  

          }
          callback(resp?.data);
        })
        .catch((error) => {
          toast.error(
            error ?? "Something went wrong",
            {
              autoClose: 2000,
            }
          );
        });
    };
  };


  const getQuizList = (data) => ({
    type: types.QUIZ_LIST,
    payload: data,
  });
  
  export const loadQuizList = () => {
    return function (dispatch) {
      var headers = {
        "Content-type": "application/json",
        };
        axios.get(`${GLOBAL_CONSTANTS?.backend_url}/quiz/full_list`, {headers})
        .then((resp) => {
          dispatch(getQuizList(resp?.data?.data));
        })
        .catch((error) => console.log(error));
    };
  };

  const getQuizView = (data) => ({
    type: types.QUIZ_DATA,
    payload: data,
  });
  
  export const loadQuizQuestions = (id) => {
    return function (dispatch) {
      var headers = {
        "Content-type": "application/json",
        };
        axios.get(`${GLOBAL_CONSTANTS?.backend_url}/quiz/${id}/questions`, {headers})
        .then((resp) => {
          dispatch(getQuizView(resp?.data));
        })
        .catch((error) => console.log(error));
    };
  };


  const getLessonList = (data) => ({
    type: types.LESSON_LIST,
    payload: data,
  });
  
  export const loadLessonList = () => {
    return function (dispatch) {
      var headers = {
        "Content-type": "application/json",
        };
        axios.get(`${GLOBAL_CONSTANTS?.backend_url}/lesson/${GLOBAL_CONSTANTS?.user_cred?.user_id}/list`, {headers})
        .then((resp) => {
          dispatch(getLessonList(resp?.data));
        })
        .catch((error) => console.log(error));
    };
  };


  const getLessonView = (data) => ({
    type: types.LESSON_VIEW,
    payload: data,
  });
  
  export const loadLessonView = (id) => {
    return function (dispatch) {
      var headers = {
        "Content-type": "application/json",
        };
        axios.get(`${GLOBAL_CONSTANTS?.backend_url}/lesson/${id}/get`, {headers})
        .then((resp) => {
          dispatch(getLessonView(resp?.data));
        })
        .catch((error) => console.log(error));
    };
  };


  export const quizSubmit = (data, callback) => {
    return function () {
      var headers = {
        "Content-type": "application/json",
      };
      axios
        .post(`${GLOBAL_CONSTANTS.backend_url}result/submit_answer`, JSON.stringify(data), {
          headers,
        })
        .then((resp) => {
          callback(resp?.data);
        })
        .catch((error) => {

          toast.error(
            error ?? "Something went wrong",
            {
              autoClose: 2000,
            }
          );
        });
    };
  };

  export const quizCreate = (data, callback) => {
    return function () {
      var headers = {
        "Content-Type ": "multipart/form-data",
      };
      axios
        .post(`${GLOBAL_CONSTANTS.backend_url}quiz/upsert_quiz`, data, {
          headers,
        })
        .then((resp) => {
          callback(resp?.data);
        })
        .catch((error) => {

          toast.error(
            error ?? "Something went wrong",
            {
              autoClose: 2000,
            }
          );
        });
    };
  };