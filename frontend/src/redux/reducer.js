import * as types from "./actionTypes.js";

const initialState = {
  // authActions
  loggedIn: true,
  userId: null,
  quizList:[],
  quizView:{},
  lessonsList:[],
  lessonView:{},
};

const DataReducers = (state = initialState, action) => {
  switch (action.type) {
    case types.LOGIN:
      return {
        ...state,
        loggedIn:  action?.payload?.userId && true,
        userCred: action?.payload,
      };
      case types.QUIZ_LIST:
        return {
          ...state,
          quizList:action?.payload
        }
      case types.LESSON_LIST :
        {
          return {
            ...state,
            lessonsList:action?.payload?.data
          }
        }
        case types.LESSON_VIEW :
        {
          return {
            ...state,
            lessonView:action?.payload?.data
          }
        }
        case types.QUIZ_DATA :
        {
          return {
            ...state,
            quizView:action?.payload
          }
        }
    default:
      return state;
  }
};
export default DataReducers;
