import { io } from 'socket.io-client';

const socket = io( 'http://172.30.250.128:3000');

//ipconfig

export default socket;