document.addEventListener('DOMContentLoaded', () => {
    // Create and append the main chat container
    const container = document.createElement('div');
    container.classList.add('bg-white', 'rounded-lg', 'shadow-lg', 'p-6', 'w-96', 'flex', 'flex-col', 'items-center', 'justify-center', 'mx-auto', 'my-8');
    document.body.appendChild(container);

    // Create and append the chat box
    const chatBox = document.createElement('div');
    chatBox.id = 'chat-box';
    chatBox.classList.add('h-96', 'overflow-y-scroll', 'mb-4', 'p-4', 'border', 'border-gray-300', 'rounded-lg', 'flex', 'flex-col');
    container.appendChild(chatBox);

    // Create and append the user input field
    const userInput = document.createElement('input');
    userInput.type = 'text';
    userInput.id = 'user-input';
    userInput.placeholder = 'Type a message...';
    userInput.classList.add('w-full', 'p-2', 'border', 'border-gray-300', 'rounded-lg', 'mb-2');
    userInput.addEventListener('keydown', handleKeyDown);
    container.appendChild(userInput);

    // Create and append the control buttons container
    const controls = document.createElement('div');
    controls.id = 'controls';
    controls.classList.add('flex', 'justify-between', 'w-full');
    container.appendChild(controls);

    // Create and append the Send button
    const sendButton = document.createElement('button');
    sendButton.innerText = 'Send';
    sendButton.classList.add('bg-blue-500', 'text-white', 'px-4', 'py-2', 'rounded-lg');
    sendButton.addEventListener('click', sendMessage);
    controls.appendChild(sendButton);

    // Create and append the Clear Chat button
    const clearButton = document.createElement('button');
    clearButton.innerText = 'Clear Chat';
    clearButton.classList.add('bg-red-500', 'text-white', 'px-4', 'py-2', 'rounded-lg');
    clearButton.addEventListener('click', clearChat);
    controls.appendChild(clearButton);
});

function sendMessage() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();

    if (message === '') return;

    addMessage('user', message);
    userInput.value = '';

    addTypingIndicator();

    setTimeout(() => {
        removeTypingIndicator();
        const botResponse = getBotResponse(message);
        addMessage('bot', botResponse);
    }, 500);
}

function addMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', 'mb-2', 'p-2', 'rounded-lg');
    if (sender === 'user') {
        messageElement.classList.add('bg-blue-100', 'text-right', 'self-end');
    } else {
        messageElement.classList.add('bg-green-100', 'text-left');
    }
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
    } else if (message.includes('thanks') || message.includes('thank you')) {
        return 'You\'re welcome!';
    } else if (message.includes('help')) {
        return 'Sure, how can I assist you?';
    } else {
        return 'I am sorry, I do not understand that.';
    }
}

function handleKeyDown(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function addTypingIndicator() {
    const chatBox = document.getElementById('chat-box');
    const typingIndicator = document.createElement('div');
    typingIndicator.id = 'typing-indicator';
    typingIndicator.classList.add('message', 'mb-2', 'p-2', 'rounded-lg', 'bg-gray-100', 'italic');
    typingIndicator.innerText = 'Bot is typing...';
    chatBox.appendChild(typingIndicator);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typing-indicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

function clearChat() {
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML = '';
}
