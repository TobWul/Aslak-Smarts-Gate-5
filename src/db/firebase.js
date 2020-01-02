import firebase from 'firebase/app';
import 'firebase/firestore';

import { firebaseConfig } from '../secret';

firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();

export default db;
