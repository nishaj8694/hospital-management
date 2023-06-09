
var openChatBtn = document.getElementsByClassName("open-chat-btn");
var chatPopup = document.getElementById("chat-popup");



    var closeChatBtn = document.getElementById("close-chat-btn");

    // When the user clicks the close button, close the chat popup
    closeChatBtn.onclick = function() {
      chatPopup.style.display = "none";
    }

// var onoff = document.getElementById("user-onoff");

var userList = document.getElementById('user-list').children;        
const user = JSON.parse(document.getElementById('username').textContent);
const roomName = JSON.parse(document.getElementById('id').textContent);
                const chatSocket = new WebSocket(
                    'ws://'
                    + window.location.host
                    + '/ws/'
                    + roomName
                    + '/'
                );

                chatSocket.onmessage = function(e) {
                    const data = JSON.parse(e.data);
                    console.log(data.message)
                    const chatLog = document.querySelector('#chat-log');
                    const onoff = document.getElementById("user-onoff");
                    // const chat = document.querySelector('#chat-message-input');
                    if (data.message !=undefined){
                        console.log(data.message);                 
                        const msge = document.createElement('p');
                        msge.innerText = data.message;
                        if (data.css_class === "current-user") {
                            msge.style.textAlign = 'right';
                            msge.style.marginRight='50px'
                            msge.style.color = 'blue';
                        } else {
                            msge.style.textAlign = 'left';
                            msge.style.color = 'red';
                            msge.style.marginleft='50px'

                          
                        }
                    chatLog.appendChild(msge);
                   
                    }
                    if (data.is_online) {
                        onoff.innerHTML = 'online';
                        onoff.style.color = 'green';
                    } else {
                        console.log(data.is_online);
                        onoff.innerHTML = 'offline';
                        onoff.style.color = 'red';
                    } 
                };
                chatSocket.onopen = function(e){
                    console.log("CONNECTION ESTABLISHED");
                }
                
                chatSocket.onerror = function(e){
                    console.log("ERROR OCCURED");
                }   
                chatSocket.onclose = function(e) {
                    console.error('Chat socket closed unexpectedly');
                };
                window.addEventListener('beforeunload', function () {
                    chatSocket.close();
                });

                
                
                
                
                

                document.querySelector('#chat-message-input').focus();

                document.querySelector('#chat-message-input').addEventListener('keyup', function(e) {
                    if (e.keyCode === 13) {  
                        document.querySelector('#chat-message-submit').click();
                    }
                });

                document.querySelector('#chat-message-submit').addEventListener('click', function(e) {
                    const messageInputDom = document.querySelector('#chat-message-input');
                    const message = messageInputDom.value;
                    chatSocket.send(JSON.stringify({
                        'message': message
                    }));
                    messageInputDom.value = '';
                });
                