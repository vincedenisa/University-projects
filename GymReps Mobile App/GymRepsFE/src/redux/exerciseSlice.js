import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as exerciseService from '../services/exerciseService.js';
import socket from '../services/socketService';
import Toast from 'react-native-toast-message';
import {addExercise, updateExercise, deleteExercise, getAllExercises} from '../database/database.js';

//here we have reducers and actions
//reducers: Functions that specify how the store's state changes in response to actions. They take the current state and an action, and return the new state
//actions: Plain JavaScript objects that describe what happened
//dispatch: A function used to send actions to the store
//selectors: Functions to retrieve specific pieces of state from the store

//thunk = function that can handle asynchronous logic

//exercise slice = state logic

// Initialize WebSocket listeners
export const initializeSocketListeners = (dispatch) => {
    socket.on('exercise_added', (exercise) => {
        if (exercise && exercise.id) {
            dispatch(addExerciseThunk.fulfilled(exercise));
        } else {
            console.error('Invalid exercise received from WebSocket on addExercise:', exercise);
        }
    });

    socket.on('exercise_updated', (exercise) => {
        if (exercise && exercise.id) {
            dispatch(updateExerciseThunk.fulfilled(exercise)); // Dispatch the fulfilled state of the update thunk
        } else {
            console.error('Invalid exercise received from WebSocket on updateExercise:', exercise);
        }
    });

    socket.on('exercise_deleted', ({ id }) => {
        dispatch(deleteExerciseThunk.fulfilled(id)); // Dispatch the fulfilled state of the delete thunk
    });
};

// Async thunks for API calls
export const getAllExercisesThunk = createAsyncThunk(
    'exercises/getAllExercises',
    async (_, { rejectWithValue }) => {
        try {
            const exercises = await exerciseService.getAllExercises();
            await getAllExercises(exercises);
            return exercises;      //the value returned becomes the payload of the action
        } catch (error) {
            console.error("Error fetching exercises:", error.message);
            const errorMessage = error.response?.data?.message || error.message;
            Toast.show({
                type: 'error',
                text1: 'Error Fetching Exercises',
                text2: errorMessage,
            });
            return rejectWithValue(error.message);
        }
    }
);

export const addExerciseThunk = createAsyncThunk(
    'exercises/addExercise',
    async (exercise, { rejectWithValue }) => {
        try {
            const newExercise = await exerciseService.addExercise(exercise);
            await addExercise(exercise);
            return newExercise;
        } catch (error) {
            console.error("Error adding exercise:", error.message);
            const errorMessage = error.response?.data?.message || error.message;
            Toast.show({
                type: 'error',
                text1: 'Error Adding Exercise',
                text2: errorMessage,
            });
            return rejectWithValue(error.message);
        }
    }
);

export const updateExerciseThunk = createAsyncThunk(
    'exercises/updateExercise',
    async (exercise, { rejectWithValue }) => {
        try {
            const updatedExercise = await exerciseService.updateExercise(exercise);
            await updateExercise(exercise);
            return updatedExercise;
        } catch (error) {
            console.error("Error updating exercise:", error.message);
            const errorMessage = error.response?.data?.message || error.message;
            Toast.show({
                type: 'error',
                text1: 'Error Updating Exercise',
                text2: errorMessage,
            });
            return rejectWithValue(error.message);
        }
    }
);

export const deleteExerciseThunk = createAsyncThunk(
    'exercises/deleteExercise',
    async (id, { rejectWithValue }) => {
        try {
            console.log('log2');
            await exerciseService.deleteExercise(id);
            await deleteExercise(id);
            return id;
            console.log('log3');
        } catch (error) {
            console.error("Error deleting exercise:", error.message);
            const errorMessage = error.response?.data?.message || error.message;
            Toast.show({
                type: 'error',
                text1: 'Error Deleting Exercise',
                text2: errorMessage,
            });
            return rejectWithValue(error.message);
        }
    }
);

// Slice definition
const exerciseSlice = createSlice({
    name: 'exercises',
    initialState: {
        exercises: [],
        error: null, // Track errors in the state
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            // Fulfilled cases
            .addCase(getAllExercisesThunk.fulfilled, (state, action) => {
                state.exercises = action.payload;
                state.error = null; // Clear any existing error
            })
            .addCase(addExerciseThunk.fulfilled, (state, action) => {
                const exerciseExists = state.exercises.some((exercise) => exercise.id === action.payload.id);
                if (!exerciseExists) {
                    state.exercises.push(action.payload);
                }
                state.error = null;
            })
            .addCase(updateExerciseThunk.fulfilled, (state, action) => {
                const index = state.exercises.findIndex((p) => p.id === action.payload.id);
                if (index !== -1) {
                    state.exercises[index] = action.payload;
                }
                state.error = null;
            })
            .addCase(deleteExerciseThunk.fulfilled, (state, action) => {
                state.exercises = state.exercises.filter((p) => p.id !== action.payload);
                state.error = null;
            })
        /*
        .addCase(getAllExercisesThunk.rejected, (state, action) => {
            state.error = action.payload || "Failed to fetch exercises.";
        })
        .addCase(addExerciseThunk.rejected, (state, action) => {
            state.error = action.payload || "Failed to add exercise.";
        })
        .addCase(updateExerciseThunk.rejected, (state, action) => {
            state.error = action.payload || "Failed to update exercise.";
        })
        .addCase(deleteExerciseThunk.rejected, (state, action) => {
            state.error = action.payload || "Failed to delete exercise.";
        });*/
    },
});

export default exerciseSlice.reducer;



/*
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import * as exerciseService from '../services/exerciseService.js';
import socket from '../services/socketService';


export const initializeSocketListeners = (dispatch) => {
    socket.on('exercise_added', (exercise) => {
        if (exercise && exercise.id) {
            dispatch(addExerciseThunk.fulfilled(exercise));
        } else {
            console.error('Invalid exercise received from WebSocket on addExercise:', exercise);
        }
    });


    socket.on('exercise_updated', (exercise) => {
        if (exercise && exercise.id){
            dispatch(updateExerciseThunk.fulfilled(exercise)); // Dispatch the fulfilled state of the update thunk
        } else {
            console.error('Invalid exercise received from WebSocket on updateExercise:', exercise);

        }
    });

    socket.on('exercise_deleted', ({ id }) => {
        dispatch(deleteExerciseThunk.fulfilled(id)); // Dispatch the fulfilled state of the delete thunk
    });
};


export const getAllExercisesThunk = createAsyncThunk(
    'exercises/getAllExercises',
    async () => {
        const exercises = await exerciseService.getAllExercises();
        return exercises;
    }
);

export const addExerciseThunk = createAsyncThunk(
    'exercises/addExercise',
    async (exercise) => {
        const newExercise = await exerciseService.addExercise(exercise);
        return newExercise;
    }
);

export const updateExerciseThunk = createAsyncThunk(
    'exercises/updateExercise',
    async (exercise) => {
        const updatedExercise = await exerciseService.updateExercise(exercise);
        return updatedExercise;
    }
);

export const deleteExerciseThunk = createAsyncThunk(
    'exercises/deleteExercise',
    async (id) => {
        await exerciseService.deleteExercise(id);
        return id;
    }
);


const exerciseSlice = createSlice({
    name: 'exercises',
    initialState: {
        exercises: [],
    },
    reducers: {},
    extraReducers: (builder) => {
        builder
            .addCase(getAllExercisesThunk.fulfilled, (state, action) => {
                state.exercises = action.payload;
            })
            .addCase(addExerciseThunk.fulfilled, (state, action) => {
                const exerciseExists = state.exercises.some((exercise) => exercise.id === action.payload.id);
                if (!exerciseExists) {
                    state.exercises.push(action.payload);
                }
            })
            .addCase(updateExerciseThunk.fulfilled, (state, action) => {
                const index = state.exercises.findIndex((p) => p.id === action.payload.id);
                if (index !== -1) {
                    state.exercises[index] = action.payload;
                }
            })
            .addCase(deleteExerciseThunk.fulfilled, (state, action) => {
                state.exercises = state.exercises.filter((p) => p.id !== action.payload);
            });
    },
});

export default exerciseSlice.reducer;






/!*
import { createSlice, createAsyncThunk  } from '@reduxjs/toolkit';
import { getAllExercises, addExercise, deleteExercise, updateExercise } from '../database/database';

//here we have reducers and actions
//reducers: Functions that specify how the store's state changes in response to actions. They take the current state and an action, and return the new state
//actions: Plain JavaScript objects that describe what happened
//dispatch: A function used to send actions to the store
//selectors: Functions to retrieve specific pieces of state from the store

//thunk = function that can handle asynchronous logic

//exercise slice = state logic

export const getAllExercisesThunk = createAsyncThunk(
    'exercises/getAllExercises',   // we ensure that the generated action types are unique and descriptive
    async () => {
        const exercises = await getAllExercises();
        return exercises;    //payload of the fulfilled action
    }
);

export const addExerciseThunk = createAsyncThunk(
    'exercises/addExercise',
    async (exercise) => {
        const returnedExercise = await addExercise(exercise);
        return returnedExercise;      //payload of the fulfilled action
    }
);

export const deleteExerciseThunk = createAsyncThunk(
    'exercises/deleteExercise',
    async (id) => {
        await deleteExercise(id);
        return id;              //payload of the fulfilled action
    }
);

export const updateExerciseThunk = createAsyncThunk(
    'exercises/updateExercise',
    async (exercise) => {
        const returnedExercise = await updateExercise(exercise);
        return returnedExercise;         //payload of the fulfilled action
    }
);

const exerciseSlice = createSlice({
    name: 'exercises',
    initialState: {
        exercises: [],
    },
    reducers: {},
    extraReducers: (builder) => {  // extra reducers are a feature used to handle actions that are not directly created by the slice itself
        builder
            .addCase(getAllExercisesThunk.fulfilled, (state, action) => {
                state.exercises = action.payload;
            })
            .addCase(addExerciseThunk.fulfilled, (state, action) => {
                state.exercises.push(action.payload);
            })
            .addCase(updateExerciseThunk.fulfilled, (state, action) => {
                const index = state.exercises.findIndex((p) => p.id === action.payload.id);
                if (index !== -1) {
                    state.exercises[index] = action.payload;
                }
            })
            .addCase(deleteExerciseThunk.fulfilled, (state, action) => {
                state.exercises = state.exercises.filter((p) => p.id !== action.payload);
            });
    },
});

export default exerciseSlice.reducer;



*!/
*/