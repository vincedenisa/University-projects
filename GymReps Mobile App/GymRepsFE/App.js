import React from 'react';
import { Provider } from 'react-redux';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import MainScreen from './src/screens/MainScreen';
import CreateExerciseScreen from './src/screens/CreateExerciseScreen';
import EditExerciseScreen from './src/screens/EditExerciseScreen';
import store from './src/redux/store';
import Toast from 'react-native-toast-message';

const Stack = createStackNavigator();

const App = () => {
    return (
        <Provider store={store}>
            <NavigationContainer>
                <Stack.Navigator initialRouteName="Main">
                    {/* MainScreen is the first screen */}
                    <Stack.Screen
                        name="Main"
                        component={MainScreen}
                        options={{ title: 'My Exercises' }} 
                    />
                    {/* The screen for creating an exercise */}
                    <Stack.Screen
                        name="CreateExercise"
                        component={CreateExerciseScreen}
                        options={{ title: 'Create Exercise' }}
                    />
                    {/* The screen for editing an exercise */}
                    <Stack.Screen
                        name="EditExercise"
                        component={EditExerciseScreen}
                        options={{ title: 'Edit Exercise' }}
                    />
                </Stack.Navigator>

                <Toast />
            </NavigationContainer>
        </Provider>
    );
};

export default App;