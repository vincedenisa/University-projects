import React, { useEffect } from 'react';
import { View, Alert, StyleSheet, TouchableOpacity, Text } from 'react-native';
import { useSelector, useDispatch } from 'react-redux';
import { deleteExerciseThunk, getAllExercisesThunk } from '../redux/exerciseSlice';
import { ExerciseList } from '../components/ExerciseList';
import Toast from 'react-native-toast-message';
import { useTheme } from "react-native-paper";


const MainScreen = ({ route, navigation }) => {
    //const exercises = useSelector((state) => state.exercises.exercises); // Access state
    const dispatch = useDispatch(); // Dispatch actions
    const theme = useTheme();

    // Retrieve the list of exercises from the Redux store
    const exercises = useSelector((state) => state.exercises.exercises);

    // Fetch exercises from the database when the screen mounts
    useEffect(() => {
        if (exercises.length === 0) {
            dispatch(getAllExercisesThunk());
        }
    }, [dispatch, exercises.length]);

    useEffect(() => {
        if (route.params?.successMessage) {
            Toast.show({
                type: 'success',
                position: 'bottom',
                text1: route.params.successMessage,
                visibilityTime: 4000,
                autoHide: true,
                style: {
                    backgroundColor: '#d579eb',
                }
            });
        }
    }, [route.params?.successMessage]);

    const handleDeleteExercise = (id) => {
        // Show a confirmation dialog before deleting
        Alert.alert(
            'Delete Exercise',
            'Are you sure you want to delete this exercise?',
            [
                {
                    text: 'Cancel',
                    onPress: () => console.log('Delete Cancelled'),
                    style: 'cancel',
                },
                {
                    text: 'Delete',
                    onPress: async () => {
                        try {
                            console.log('log1', id);
                            await dispatch(deleteExerciseThunk(exerciseId)).unwrap(); // Use thunk to delete exercise
                            Toast.show({
                                type: 'success',
                                text1: 'Exercise deleted successfully',
                                position: 'bottom',
                                visibilityTime: 1500,
                            });
                        } catch (error) {
                            console.log('error', error);
                            Toast.show({
                                type: 'error',
                                text1: 'Failed to delete exercise',
                                position: 'bottom',
                                visibilityTime: 1500,
                            });
                        }
                    },
                    style: 'destructive',
                },
            ],
            { cancelable: true } // Can be canceled by tapping outside the dialog
        );
    };

    const handleEditExercise = (exercise) => {
        navigation.navigate('EditExercise', { exercise });
    };

    return (
        <View style={styles.container}>
            {/* Display an empty state if no exercises exist */}
            {exercises.length === 0 ? (
                <Text style={styles.emptyStateText}>No exercises found. Tap "+" to add one!</Text>
            ) : (
                <ExerciseList
                    exercises={exercises}
                    onEdit={handleEditExercise}
                    onDelete={handleDeleteExercise}
                />
            )}

            {/* Floating Add Button */}
            <TouchableOpacity
                style={styles.fab}
                onPress={() => navigation.navigate('CreateExercise')}
            >
                <Text style={styles.fabText}>+</Text>
            </TouchableOpacity>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f7f7f7', // Light grey background for the container
    },
    fab: {
        position: 'absolute',
        bottom: 20,
        right: 20,
        width: 60,
        height: 60,
        borderRadius: 30, // Perfectly round button
        backgroundColor: '#FF4081', // Vibrant pink color for the button
        justifyContent: 'center',
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 4 },
        shadowOpacity: 0.3,
        shadowRadius: 8,
        elevation: 8, // Enhanced shadow for better visibility on Android
        borderWidth: 2, // Added a border to the button for a more defined look
        borderColor: '#F50057', // Matching border color to the button background
    },
    fabText: {
        fontSize: 28, // Larger font for a more prominent icon
        color: '#fff',
        fontWeight: 'bold',
        textAlign: 'center',
    },
});

export default MainScreen;

