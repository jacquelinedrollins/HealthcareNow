
var pathArray = window.location.pathname.split('/');
var roomName = pathArray[pathArray.length-2];
var chatSocket = new WebSocket(
    'ws://' + window.location.host +
    '/ws/chat/' + roomName + '/');

chatSocket.onmessage = function(e) {
    var data = JSON.parse(e.data);
    var message = data['message'];
    var username = data['username'];
    document.querySelector('#chat-log').value += (username + ': ' + message + '\n');
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    var messageInputDom = document.querySelector('#chat-message-input');
    var usernameInputDom = document.querySelector('#chat-username-input');
    var message = messageInputDom.value;
    var username = usernameInputDom.value;
    console.log(username);
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': username
    }));

    messageInputDom.value = '';
};
