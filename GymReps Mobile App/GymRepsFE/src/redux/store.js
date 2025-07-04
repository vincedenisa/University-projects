import { configureStore } from '@reduxjs/toolkit';
import exerciseReducer from './exerciseSlice';


//store = a single source of truth for the state (global state of the app)


const store = configureStore({
    reducer: {
        exercises: exerciseReducer,
    },
});

export default store;