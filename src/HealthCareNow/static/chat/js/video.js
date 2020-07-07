var video = document.querySelector('video');
var constraints = { video: true, audio: true };
var peerConnectionConfig = {'iceServers': [{'url': 'stun:stun.services.mozilla.com'}, {'url': 'stun:stun.l.google.com:19302'}]};
var isCaller = true;
var localVideo;
var localStream;
var remoteVideo;
var peerConnection;
var uuid;
var serverConnection;


navigator.mediaDevices.getUserMedia(constraints)
  .then(stream => video.srcObject = stream)
  .catch(e => console.error(e));
//console.log(connection)

function start() {
    peerConnection = new RTCPeerConnection(peerConnectionConfig);
    console.log(peerConnection)
    //peerConnection.onicecandidate = gotIceCandidate;
    //peerConnection.onaddstream = gotRemoteStream;
    peerConnection.addStream(video.srcObject);

    if(isCaller) {
        peerConnection.createOffer(gotDescription, createOfferError);
    }
}
start();
