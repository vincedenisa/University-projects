import React, { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import { TextInput, Button, Text, TouchableRipple, useTheme, HelperText } from 'react-native-paper';
import DateTimePicker from '@react-native-community/datetimepicker';
import { useDispatch } from 'react-redux';
import { updateExerciseThunk } from '../redux/exerciseSlice';
import { Picker } from '@react-native-picker/picker';
import Toast from 'react-native-toast-message';

const EditExerciseScreen = ({ route, navigation }) => {
    const { exercise } = route.params;

    const [name, setName] = useState(exercise.name);
    const [sets, setSets] = useState(exercise.sets);
    const [reps, setReps] = useState(exercise.reps);
    const [restTime, setRestTime] = useState(exercise.restTime);

    const dispatch = useDispatch();
    const theme = useTheme();

    const handleSaveChanges = () => {
        const updatedExercise = {
            ...exercise,
            name,
            sets,
            reps,
            restTime,
        };

        dispatch(updateExerciseThunk(updatedExercise));

        navigation.navigate('Main', { successMessage: 'Exercise Edited successfully!' });
    };

    return (
        <View style={styles.container}>
            {/* Title */}
            <Text style={styles.title}>Edit Exercise</Text>

            {/* Name Input */}
            <TextInput
                label="Exercise Name"
                value={name}
                onChangeText={setName}
                mode="outlined"
                style={styles.input}
            />

            {/* Sets Input */}
            <TextInput
                label="Sets"
                value={sets}
                onChangeText={setSets}
                mode="outlined"
                multiline
                style={styles.input}
            />

            {/* Reps Input */}
            <TextInput
                label="Reps"
                value={reps}
                onChangeText={setReps}
                mode="outlined"
                multiline
                style={styles.input}
            />

            {/* Rest Time Input */}
            <TextInput
                label="Rest Time"
                value={restTime}
                onChangeText={setRestTime}
                mode="outlined"
                multiline
                style={styles.input}
            />

            

            {/* Save Button */}
            <Button
                mode="contained"
                onPress={handleSaveChanges}
                style={styles.saveButton}
                buttonColor={theme.colors.primary}
            >
                Save Changes
            </Button>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 20,
        backgroundColor: '#f5f5f5', // Light grey background for the screen
    },
    title: {
        fontSize: 28, // Larger font for the title to make it stand out
        fontWeight: 'bold',
        color: '#333', // Dark color for the title
        marginBottom: 20, // Space below title for clean separation
        textAlign: 'center', // Center align the title
    },
    input: {
        marginBottom: 15, // Space between each input field
        backgroundColor: '#fff', // White background for inputs for better contrast
        borderRadius: 8, // Slightly rounded corners for a modern look
        paddingHorizontal: 12, // Padding inside the input fields
        fontSize: 16, // Increase font size for better readability
    },
    saveButton: {
        marginTop: 20, // Space above the button
        paddingVertical: 12, // More padding for better tap area
        borderRadius: 8, // Rounded corners for the button
    },
});


export default EditExerciseScreen;