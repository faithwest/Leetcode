// src/components/PuzzleBoard.js
import React, { useState, useEffect } from 'react';
import './PuzzleBoard.css';
import PuzzlePiece from './PuzzlePiece';

const PuzzleBoard = ({ size }) => {
  const [pieces, setPieces] = useState([]);

  useEffect(() => {
    initializeBoard();
  }, []);

  const initializeBoard = () => {
    let tempPieces = [];
    for (let i = 0; i < size * size; i++) {
      tempPieces.push(i);
    }
    setPieces(shuffleArray(tempPieces));
  };

  const shuffleArray = (array) => {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  };

  return (
    <div className="puzzle-board">
      {pieces.map((piece, index) => (
        <PuzzlePiece key={index} number={piece} />
      ))}
    </div>
  );
};

export default PuzzleBoard;
