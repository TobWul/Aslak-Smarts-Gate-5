import db from './firebase';

const lightRef = db.collection('lights');

const toggleLight = (lightId, newState) => {
  lightRef
    .doc(lightId)
    .update({ on: newState })
    .then(() => {
      console.log(`Switched ${lightId} ${newState ? 'on' : 'off'}`);
    })
    .catch(error => console.error(error));
};

const getLightState = identifier => {
  let result = false;
  db.collection('lights')
    .doc(identifier)
    .get()
    .then(doc => {
      if (doc.exists) {
        result = doc.data();
      } else {
        // doc.data() will be undefined in this case
        console.log('No such document!');
      }
    });
};

const getLights = new Promise((resolve, reject) => {
  lightRef
    .get()
    .then(querySnapshot =>
      resolve(
        querySnapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data()
        }))
      )
    )
    .catch(error => reject(error));
});

export { toggleLight, getLightState, getLights };
