import React from 'react';
import { View, Text, FlatList, StyleSheet, TouchableOpacity } from 'react-native';

export const ExerciseList = ({ exercises, onEdit, onDelete }) => {
    const renderItem = ({ item }) => {
        

        return (
            <TouchableOpacity
                style={styles.card}
                onPress={() => onEdit(item)} // Clicking a card navigates to edit
            >
                <View style={styles.content}>
                    <Text style={styles.title}>{item.name}</Text>
                    
                    <Text style={styles.description}>{item.sets}</Text>
                    <Text style={styles.description}>{item.reps}</Text>
                    <Text style={styles.description}>{item.restTime}</Text>
                </View>
                <TouchableOpacity
                    style={styles.smallDeleteButton}
                    onPress={() => onDelete(item.id)}
                >
                    <Text style={styles.deleteButtonText}>X</Text>
                </TouchableOpacity>
            </TouchableOpacity>
        );
    };

    return (
        <FlatList
            data={exercises}
            renderItem={renderItem}
            keyExtractor={(item) => item.id.toString()}
            contentContainerStyle={styles.list}
        />
    );
};

const styles = StyleSheet.create({
    list: {
        paddingHorizontal: 20,
        paddingVertical: 12,
    },
    card: {
        backgroundColor: '#fff', // White background for a cleaner look
        borderRadius: 16, // Slightly more rounded corners
        marginBottom: 16,
        padding: 18,
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 4 },
        shadowOpacity: 0.3,
        shadowRadius: 6,
        elevation: 5, // Enhanced shadow for Android
        position: 'relative',
        borderWidth: 1, // Added subtle border
        borderColor: '#ddd', // Light border color
    },
    content: {
        marginBottom: 12, // Increased margin for better spacing
    },
    title: {
        fontSize: 20, // Larger font for title
        fontWeight: '600', // Slightly lighter weight for a modern look
        color: '#6A1B9A', // Rich purple color
        textTransform: 'uppercase', // Uppercase for a bold statement
    },
    sets: {
        fontSize: 14, // Slightly bigger font for better visibility
        color: '#FF4081', // Soft pink color for urgency
        fontStyle: 'italic',
    },
    reps: {
        fontSize: 14, // Slightly bigger font for better visibility
        color: '#FF4081', // Soft pink color for urgency
        fontStyle: 'italic',
    },
    restTime: {
        fontSize: 14, // Slightly bigger font for better visibility
        color: '#FF4081', // Soft pink color for urgency
        fontStyle: 'italic',
    },
    smallDeleteButton: {
        backgroundColor: '#D32F2F', // Strong red color for delete button
        paddingVertical: 6,
        paddingHorizontal: 12,
        borderRadius: 8,
        position: 'absolute',
        top: 10,
        right: 10, // Positioned at the top-right corner of the card
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.2,
        shadowRadius: 4,
        elevation: 4, // Added shadow to button for emphasis
    },
    deleteButtonText: {
        color: '#fff', // White text
        fontSize: 14, // Larger font size
        fontWeight: 'bold',
        textTransform: 'uppercase', // Uppercase for a stronger look
    },
});
