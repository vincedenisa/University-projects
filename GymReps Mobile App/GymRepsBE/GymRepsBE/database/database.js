const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const db = new sqlite3.Database(path.resolve(__dirname, 'gymReps.db'));

// Initialize the database
db.serialize(() => {
    db.run(`
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            reps TEXT NOT NULL,
            sets TEXT NOT NULL,
            restTime TEXT
        );
    `);
});

// Add an exercise
const addExercise = (exercise) => {
    return new Promise((resolve, reject) => {
        const query = `
            INSERT INTO exercises (name, reps, sets, restTime)
            VALUES (?, ?, ?, ?)
        `;
        db.run(query, [exercise.name, exercise.reps, exercise.sets, exercise.restTime], function (err) {
            if (err) reject(err);
            resolve({ ...exercise, id: this.lastID });
        });
    });
};

// Get all exercises
const getAllExercises = () => {
    return new Promise((resolve, reject) => {
        const query = `SELECT * FROM exercises`;
        db.all(query, [], (err, rows) => {
            if (err) reject(err);
            resolve(rows);
        });
    });
};

// Update a exercise
const updateExercise = (exercise) => {
    return new Promise((resolve, reject) => {
        const query = `
            UPDATE exercises
            SET name = ?, reps = ?, sets = ?, restTime = ?
            WHERE id = ?
        `;
        db.run(query, [exercise.name, exercise.reps, exercise.sets, exercise.restTime, exercise.id], (err) => {
            if (err) reject(err);
            resolve(exercise);
        });
    });
};

// Delete a exercise
const deleteExercise = (exerciseId) => {
    return new Promise((resolve, reject) => {
        const query = `DELETE FROM exercises WHERE id = ?`;
        db.run(query, [exerciseId], (err) => {
            if (err) reject(err);
            resolve();
        });
    });
};

module.exports = {
    addExercise,
    getAllExercises,
    updateExercise,
    deleteExercise,
};