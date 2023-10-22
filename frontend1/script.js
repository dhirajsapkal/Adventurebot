async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML += `<div><b>You:</b> ${userInput}</div>`;

    // Clear the input field
    document.getElementById('user-input').value = '';

    try {
        const response = await fetch('http://localhost:5000/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: userInput })
        });
        if (!response.ok) {
            throw new Error(`Network response was not ok ${response.statusText}`);
        }
        const responseData = await response.json();
        messagesDiv.innerHTML += `<div><b>Bot:</b> ${responseData.response}</div>`;
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
    }
}
