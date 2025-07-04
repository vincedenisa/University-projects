import React, { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import { TextInput, Button, Text, TouchableRipple, HelperText, useTheme } from 'react-native-paper';
import DateTimePicker from '@react-native-community/datetimepicker';
import { useDispatch } from 'react-redux';
import { addExerciseThunk } from '../redux/exerciseSlice';
import { Picker } from '@react-native-picker/picker';
import Toast from 'react-native-toast-message';

const CreateExerciseScreen = ({ navigation }) => {
    const [name, setName] = useState('');
    const [sets, setSets] = useState('');
    const [reps, setReps] = useState('');
    const [restTime, setRestTime] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const dispatch = useDispatch();
    const theme = useTheme();



    const handleCreateExercise = () => {
        if (!name || !sets || !reps) {
            setErrorMessage('Name, Sets, and Reps are required.');
            return;
        }

        const newExercise = {
            id: Date.now(),
            name,
            sets,
            reps,
            restTime,
        };

        dispatch(addExerciseThunk(newExercise));

        navigation.navigate('Main', { successMessage: 'Exercise Created successfully!' });

    };

    return (
        <View style={styles.container}>
            {/* Title */}
            <Text style={styles.title}>Create New Exercise</Text>

            {/* Exercise Name Input */}
            <TextInput
                label="Exercise Name"
                value={name}
                onChangeText={setName}
                mode="outlined"
                style={styles.input}
            />

            {/* Exercise Sets Input */}
            <TextInput
                label="Sets"
                value={sets}
                onChangeText={setSets}
                mode="outlined"
                multiline
                style={styles.input}
            />

            {/* Exercise Reps Input */}
            <TextInput
                label="Reps"
                value={reps}
                onChangeText={setReps}
                mode="outlined"
                multiline
                style={styles.input}
            />

            {/* Exercise Rest Time Input */}
            <TextInput
                label="Rest Time"
                value={restTime}
                onChangeText={setRestTime}
                mode="outlined"
                multiline
                style={styles.input}
            />


         

            {/* Error Message */}
            {errorMessage && (
                <HelperText type="error" style={styles.errorText}>
                    {errorMessage}
                </HelperText>
            )}

            {/* Create Button */}
            <Button
                mode="contained"
                onPress={handleCreateExercise}
                style={styles.createButton}
                buttonColor={theme.colors.primary}
            >
                Create Exercise
            </Button>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
        backgroundColor: '#f5f5f5', // Light grey background for a clean look
    },
    title: {
        fontSize: 28, // Larger title for better readability
        fontWeight: 'bold',
        color: '#333', // Dark color for text
        marginBottom: 30, // Added space below the title for better spacing
        textAlign: 'center', // Center-align the title
    },
    input: {
        marginBottom: 15, // Spacing between input fields
        backgroundColor: '#fff', // White background for inputs to stand out
        borderRadius: 8, // Rounded corners for inputs
        paddingHorizontal: 12, // Padding inside the input fields for better text placement
    },
    errorText: {
        fontSize: 14,
        color: '#d32f2f', // Red color for error messages
        marginBottom: 15, // Space below the error message
        textAlign: 'center', // Center-align error text
    },
    createButton: {
        marginTop: 20, // Space above the button
        paddingVertical: 12, // Increase button height for better tap area
        borderRadius: 8, // Rounded corners for the button
    },
});


export default CreateExerciseScreen;