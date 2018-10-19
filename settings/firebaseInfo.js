// Initialize Firebase
var config = {
	apiKey: "AIzaSyBgefGNsaQtO5I3zpZuktQQtmPBsWfm0oY",
	authDomain: "q-sort-erasmusmc.firebaseapp.com",
	databaseURL: "https://q-sort-erasmusmc.firebaseio.com",
	projectId: "q-sort-erasmusmc",
	storageBucket: "q-sort-erasmusmc.appspot.com",
	messagingSenderId: "964868332513"
};
firebase.initializeApp(config);
var rootRef = firebase.database().ref();
