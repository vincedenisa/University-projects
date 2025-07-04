const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const { addExercise, getAllExercises, updateExercise, deleteExercise } = require('./database/database');
const { setupWebSocket } = require('./sockets/websocket');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

app.use(express.json());

setupWebSocket(io);

// API Endpoints
app.get('/exercises', async (req, res) => {
    try {
        const exercises = await getAllExercises();
        console.log("Exercises fetched");
        res.json(exercises);
    } catch (error) {
        console.error('Error fetching exercises:', error);
        res.status(500).json({ message: "Failed to fetch exercises" });
    }
});


app.post('/exercises', async (req, res) => {
    try {
        const exercise = req.body;
        const newExercise = await addExercise(exercise);
        io.emit('exercise_added', newExercise);
        console.log("New exercise added");
        res.json(newExercise);
    } catch (error) {
        console.error('Error adding exercise:', error);
        res.status(500).json({ message: "Failed to add exercise" });
    }
});

app.put('/exercises/:id', async (req, res) => {
    try {
        const exercise = req.body;
        exercise.id = parseInt(req.params.id);
        const updatedExercise = await updateExercise(exercise);
        io.emit('exercise_updated', updatedExercise);
        console.log("Exercise updated");
        res.json(updatedExercise);
    } catch (error) {
        console.error('Error updating exercise:', error);
        res.status(500).json({ message: "Failed to update exercise" });
    }
});

app.delete('/exercises/:id', async (req, res) => {
    try {
        const exerciseId = parseInt(req.params.id);
        await deleteExercise(exerciseId);
        io.emit('exercise_deleted', { id: exerciseId });
        console.log("Exercise deleted");
        res.status(200).json({ message: "Exercise deleted successfully" });
    } catch (error) {
        console.error('Error deleting exercise:', error);
        res.status(500).json({ message: "Failed to delete exercise" });
    }
});

// Start server
const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});


//node server.js