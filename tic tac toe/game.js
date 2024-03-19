import React, { useState, useEffect } from "react";

  export default function TicTacToe() {
    const [board, setBoard] = useState(Array(9).fill(null));
    const [player, setPlayer] = useState("X");
    const [winner, setWinner] = useState(null);
  
    const handleClick = (index) => {
      if (winner) return;
      if (board[index]) return;
      const newBoard = [...board];
      newBoard[index] = player;
      setBoard(newBoard);
      setPlayer(player === "X" ? "O" : "X");
    };
  
    const checkWinner = () => {
      const possibleWins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
      ];
      possibleWins.forEach((win) => {
        const [a, b, c] = win;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
          setWinner(board[a]);
        }
      });
    };
  
    useEffect(() => {
      checkWinner();
    });
  
    const renderSquare = (index) => {
      return (
        <div
          className="border border-gray-400 w-16 h-16 flex items-center justify-center"
          onClick={() => handleClick(index)}
        >
          {board[index]}
        </div>
      );
    };
  
    return (
      <div className="flex flex-col items-center justify-center h-screen">
        <div className="flex flex-col items-center justify-center">
          <div className="flex flex-row">
            {renderSquare(0)}
            {renderSquare(1)}
            {renderSquare(2)}
          </div>
          <div className="flex flex-row">
            {renderSquare(3)}
            {renderSquare(4)}
            {renderSquare(5)}
          </div>
          <div className="flex flex-row">
            {renderSquare(6)}
            {renderSquare(7)}
            {renderSquare(8)}
          </div>
        </div>
        <div className="text-2xl">
          {winner ? {winner} + " wins!" : "It's " + {player} + "'s turn"}
        </div>
      </div>
    );
  }
  