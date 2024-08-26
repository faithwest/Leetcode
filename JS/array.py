# # def sum_of_evens(numbers):
# #     # Initialize a variable to store the sum of even numbers
# #     total = 0
    
# #     # Iterate through the list of numbers
# #     for num in numbers:
# #         # Check if the number is even
# #         if num % 2 == 0:
# #             # Add the even number to the total sum
# #             total += num
    
# #     # Return the total sum of even numbers
# #     return total

# # # Example usage:
# # print(sum_of_evens([1, 2, 3, 4, 5]))  # Output should be 6 (2 + 4)
# # print(sum_of_evens([10, 15, 20, 25])) # Output should be 30 (10 + 20)
# // src/components/PuzzleBoard.js
# import React, { useState, useEffect } from 'react';
# import './PuzzleBoard.css';
# import PuzzlePiece from './PuzzlePiece';

# const PuzzleBoard = ({ size }) => {
#   const [pieces, setPieces] = useState([]);

#   useEffect(() => {
#     initializeBoard();
#   }, []);

#   const initializeBoard = () => {
#     let tempPieces = [];
#     for (let i = 0; i < size * size; i++) {
#       tempPieces.push(i);
#     }
#     setPieces(shuffleArray(tempPieces));
#   };

#   const shuffleArray = (array) => {
#     for (let i = array.length - 1; i > 0; i--) {
#       const j = Math.floor(Math.random() * (i + 1));
#       [array[i], array[j]] = [array[j], array[i]];
#     }
#     return array;
#   };

#   return (
#     <div className="puzzle-board">
#       {pieces.map((piece, index) => (
#         <PuzzlePiece key={index} number={piece} />
#       ))}
#     </div>
#   );
# };

# export default PuzzleBoard;
# Function to reverse an array in-place
def reverse_array_in_place(arr):
    arr.reverse()

# Example usage
arr = [1, 2, 3, 4, 5]
reverse_array_in_place(arr)
print("Reversed array (in-place):", arr)
# Function to reverse an array
def reverse_array(arr):
    return arr[::-1]

# Example usage
arr = [1, 2, 3, 4, 5]
reversed_arr = reverse_array(arr)
print("Reversed array:", reversed_arr)
