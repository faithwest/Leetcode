// Define the card values
const cardValues = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E'];

// Shuffle function to randomize card positions
function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

// Initialize game state
let selectedCards = [];
let matchedCards = [];
let moves = 0;

// Render the game board
function renderBoard() {
  const board = document.getElementById('board');
  board.innerHTML = '';

  // Render each card element
  cardValues.forEach((value, index) => {
    const card = document.createElement('div');
    card.className = 'card';
    card.dataset.index = index;
    card.textContent = value;
    card.addEventListener('click', handleCardClick);
    board.appendChild(card);
  });
}

// Handle card click event
function handleCardClick(event) {
  const card = event.target;
  const index = parseInt(card.dataset.index);

  // Check if the card is already matched or selected
  if (!card.classList.contains('matched') && !card.classList.contains('selected')) {
    // Flip the card
    card.classList.add('selected');
    selectedCards.push(card);

    // Check if two cards are selected
    if (selectedCards.length === 2) {
      moves++;
      // Check if the selected cards match
      if (selectedCards[0].textContent === selectedCards[1].textContent) {
        // Mark the cards as matched
        selectedCards.forEach(card => card.classList.add('matched'));
        matchedCards.push(selectedCards[0], selectedCards[1]);
      } else {
        // Flip the cards back face down after a short delay
        setTimeout(() => {
          selectedCards.forEach(card => card.classList.remove('selected'));
        }, 1000);
      }
      // Clear the selected cards array
      selectedCards = [];
    }
  }

  // Check if all cards are matched
  if (matchedCards.length === cardValues.length) {
    // Game over, display victory message
    alert(`Congratulations! You won in ${moves} moves.`);
  }
}

// Initialize the game
function initializeGame() {
  shuffle(cardValues);
  renderBoard();
}

// Start the game
initializeGame();
F