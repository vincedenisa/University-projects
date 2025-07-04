import axios from 'axios';

const API_BASE_URL =  'http://192.168.1.137:3000';
//ipconfig

export const getAllExercises = async () => {
    try {
        console.log("Fetching all exercises...");
        const response = await axios.get(`${API_BASE_URL}/exercises`);
        console.log("Exercises fetched successfully.");
        return response.data;
    } catch (error) {
        console.error("Error fetching exercises: ", error.response ? error.response.data : error.message);
        throw new Error("Failed to fetch exercises. Please try again.");
    }
};

export const addExercise = async (exercise) => {
    try {
        console.log("Sending request to add exercise...");
        const response = await axios.post(`${API_BASE_URL}/exercises`, exercise);
        console.log("Exercise added successfully: ", response.data);
        return response.data;
    } catch (error) {
        console.error("Error adding exercise: ", error.response ? error.response.data : error.message);
        throw new Error("Failed to add exercise. Please check your input and try again.");
    }
};

export const updateExercise = async (exercise) => {
    try {
        console.log(`Sending request to update exercise with ID ${exercise.id}...`);
        const response = await axios.put(`${API_BASE_URL}/exercises/${exercise.id}`, exercise);
        console.log("Exercise updated successfully: ", response.data);
        return response.data;
    } catch (error) {
        console.error("Error updating exercise: ", error.response ? error.response.data : error.message);
        throw new Error("Failed to update exercise. Please try again.");
    }
};

export const deleteExercise = async (id) => {
    try {
        console.log(`Sending request to delete exercise with ID ${id}...`);
        await axios.delete(`${API_BASE_URL}/exercises/${id}`);
        console.log("Exercise deleted successfully.");
        return id;
    } catch (error) {
        console.error("Error deleting exercise: ", error.response ? error.response.data : error.message);
        throw new Error("Failed to delete exercise. Please try again.");
    }
};

