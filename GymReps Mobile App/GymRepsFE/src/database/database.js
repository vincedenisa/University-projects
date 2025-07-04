import * as SQLite from 'expo-sqlite';

let db;
export const openDatabase = async () => {
    try {
        db = await SQLite.openDatabaseAsync('gymReps.db');
        console.log('Database opened successfully:', db);
        return db;
    } catch (error) {
        console.error('Error opening database:', error);
    }
};

//await db.runAsync('UPDATE test SET intValue = ? WHERE value = ?', 999, 'aaa'); // Binding unnamed parameters from variadic arguments

export const addExercise = async (exercise) => {
    const db = await openDatabase();
    if (db) {
        try {
            await db.execAsync(
                `CREATE TABLE IF NOT EXISTS exercises (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    sets TEXT NOT NULL,
                    reps TEXT NOT NULL,
                    restTime TEXT
                );`
            );

            //console.log("aici", exercise.name, exercise.sets, exercise.reps, exercise.restTime);

            const result = await db.runAsync(
                'INSERT INTO exercises (name, sets, reps, restTime) VALUES (?, ?, ?, ?);',
                [exercise.name, exercise.sets, exercise.reps, exercise.restTime]
            );

            const insertedId = result.lastInsertRowId;
            exercise.id = insertedId;

            console.log('Exercise added successfully');
            return exercise;

        } catch (error) {
            console.error('Error adding exercise:', error);
        }
    }
};


export const updateExercise = async (exercise) => {
    const db = await openDatabase();
    if (db) {
        try {
            const result = await db.runAsync(
                'UPDATE exercises SET name = ?, sets = ?, reps = ?, restTime = ? WHERE id = ?;',
                [exercise.name, exercise.sets, exercise.reps, exercise.restTime, exercise.id]
            );

            console.log('Exercise updated successfully');
            return exercise;
        } catch (error) {
            console.error('Error updating exercise:', error);
        }
    }
};

export const getAllExercises = async () => {
    const db = await openDatabase();
    if (db) {
        try {
            // Create table if not exists (this will ensure the table is present)
            await db.execAsync(
                `CREATE TABLE IF NOT EXISTS exercises (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    sets TEXT NOT NULL,
                    reps TEXT NOT NULL,
                    restTime TEXT
                );`
            );

            // Now perform the select query
            const allExercises = await db.getAllAsync('SELECT * FROM exercises;');

            const exercises = [];

            for (const exercise of allExercises) {
                exercises.push(exercise);
            }

            return exercises;
        } catch (error) {
            console.error('Error retrieving exercises:', error);
            return [];
        }
    } else {
        console.error('Database not opened');
        return [];
    }
};


export const deleteExercise = async (exerciseId) => {
    try {
        console.log('log4', exerciseId);
        const db = await openDatabase();
        console.log('log5', exerciseId);

        await db.runAsync(
            'DELETE FROM exercises WHERE id = ?;',
            [exerciseId]
        );

        console.log(`Exercise with id ${exerciseId} deleted successfully`);
    } catch (error) {
        console.error('Error deleting exercise:', error);
    }
};