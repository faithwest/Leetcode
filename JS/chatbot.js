function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();

    if (message === '') return;

    addMessage('user', message);
    userInput.value = '';

    setTimeout(() => {
        const botResponse = getBotResponse(message);
        addMessage('bot', botResponse);
    }, 500);
}

function addMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', sender);
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function getBotResponse(message) {
    message = message.toLowerCase();

    if (message.includes('hello') || message.includes('hi')) {
        return 'Hello! How can I help you today?';
    } else if (message.includes('how are you')) {
        return 'I am just a bot, but I am doing great! How about you?';
    } else if (message.includes('bye')) {
        return 'Goodbye! Have a great day!';
    } else {
        return 'I am sorry, I do not understand that.';
    }
}
