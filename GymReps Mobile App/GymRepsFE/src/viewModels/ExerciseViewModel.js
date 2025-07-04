import { useState } from 'react';
import { Exercise } from '../models/Exercise';

export function useExerciseViewModel() {
  const [exercises, setExercises] = useState([
           new Exercise(0, "Hip Thrusts", "10", "15", "10 seconds"),
           new Exercise(1, "Squats", "10", "15", "10 seconds"),
           new Exercise(2, "Lunges", "10", "15", "10 seconds"),
           new Exercise(3, "Deadlift", "10", "15", "10 seconds"),
           new Exercise(4, "Romanian Deadlift", "10", "15", "10 seconds"),
           new Exercise(5, "Sumo Squats", "10", "15", "10 seconds"),
           new Exercise(6, "Jumping Jacks", "10", "15", "10 seconds"),
           new Exercise(7, "Push Up", "10", "15", "10 seconds"),
           new Exercise(8, "Push Down", "10", "15", "10 seconds"),
           new Exercise(9, "Inclined Push Ups", "10", "15", "10 seconds"),
           new Exercise(10, "Tricep Dips", "10", "15", "10 seconds"),
           new Exercise(11, "Pull Ups", "10", "15", "10 seconds"),
           new Exercise(12, "Pull Downs", "10", "15", "10 seconds"),
           new Exercise(13, "Burpees", "10", "15", "10 seconds"),
           new Exercise(14, "Diamond Push Ups", "10", "15", "10 seconds"),
           new Exercise(15, "Sit Ups", "10", "15", "10 seconds"),
           new Exercise(16, "Crunches", "10", "15", "10 seconds"),
           new Exercise(17, "Russian Twist", "10", "15", "10 seconds"),
           new Exercise(18, "Bicycle Crunches", "10", "15", "10 seconds"),
           new Exercise(19, "Calf Raise", "10", "15", "10 seconds"),
             ]);

  const addExercise = (exercise) => {
    setExercises((prevExercises) => [...prevExercises, exercise]);
  };

  const updateExercise = (updatedExercise) => {
    setExercises((prevExercises) =>
      prevExercises.map(exercise => exercise.id === updatedExercise.id ? updatedExercise : exercise)
    );
  };

  const deleteExercise = (exerciseId) => {
    setExercises((prevExercises) => prevExercises.filter(exercise => exercise.id !== exerciseId));
  };

  return { exercises, addExercise, updateExercise, deleteExercise };
}



//look redux-state managenment in react native