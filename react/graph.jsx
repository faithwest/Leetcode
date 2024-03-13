import React from 'react';
import { Pie } from 'react-chartjs-2';

const PieChart = () => {
  // Sample data for the pie chart
  const data = {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple'],
    datasets: [
      {
        data: [12, 19, 3, 5, 2],
        backgroundColor: [
          'red',
          'blue',
          'yellow',
          'green',
          'purple'
        ],
      },
    ],
  };

  return (
    <div>
      <h2>Colored Pie Chart</h2>
      <Pie data={data} />
    </div>
  );
};

export default PieChart;
 