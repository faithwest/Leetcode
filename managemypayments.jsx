import React, { useState } from "react";

const ManagePayment = () => {
  const [payments, setPayments] = useState([
    {
      id: 1,
      farmer: "John Doe",
      amount: 100,
      product: "Apples",
      isPaid: false,
      mpesaCode: "",
      phoneNumber: "0712345678",
    },
    {
      id: 2,
      farmer: "Jane Smith",
      amount: 50,
      product: "Oranges",
      isPaid: true,
      mpesaCode: "",
      phoneNumber: "0798765432",
    },
    {
      id: 3,
      farmer: "Alice Johnson",
      amount: 75,
      product: "Bananas",
      isPaid: false,
      mpesaCode: "",
      phoneNumber: "0723456789",
    },
  ]);

  let timeoutId = null;

  const handleMpesaCodeChange = (index, code) => {
    const updatedPayments = [...payments];
    updatedPayments[index].mpesaCode = code;
    updatedPayments[index].isPaid = code !== "";
    setPayments(updatedPayments);

    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      const unpaidFarmers = updatedPayments.filter(
        (payment) => !payment.isPaid
      );
      const paidFarmers = updatedPayments.filter((payment) => payment.isPaid);
      setPayments([...unpaidFarmers, ...paidFarmers]);
    }, 3000); // Move paid farmers to the last row after 3 seconds
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-white to-green-500 text-lg">
      <div className="flex justify-center items-start">
        <div className="w-full lg:w-3/4 xl:w-2/3 p-4">
          <div className="flex items-center justify-center mb-4">
            <img
              src="https://th.bing.com/th/id/OIG3.I6_l_BU_7LmLLfxkr3pH?pid=ImgGn"
              alt="Agri-soko Logo"
              className="h-12 mr-2"
            />
            <h2 className="text-2xl font-semibold underline text-green-900">
              Manage Payment
            </h2>
          </div>
          <div className="overflow-x-auto">
            <table className="table-auto w-full border-collapse border border-gray-300">
              <thead>
                <tr>
                  <th className="px-4 py-2">Farmer Name</th>
                  <th className="px-4 py-2">Amount Needed</th>
                  <th className="px-4 py-2">Product Sold</th>
                  <th className="px-4 py-2">M-Pesa Code</th>
                  <th className="px-4 py-2">Phone Number</th>
                  <th className="px-4 py-2">Is Paid</th>
                </tr>
              </thead>
              <tbody>
                {payments.map((payment, index) => (
                  <tr key={payment.id}>
                    <td className="border px-4 py-2 text-center">
                      {payment.farmer}
                    </td>
                    <td className="border px-4 py-2 text-center">
                      {payment.amount}
                    </td>
                    <td className="border px-4 py-2 text-center">
                      {payment.product}
                    </td>
                    <td className="border px-4 py-2 text-center">
                      <input
                        type="text"
                        value={payment.mpesaCode}
                        onChange={(e) =>
                          handleMpesaCodeChange(index, e.target.value)
                        }
                        className="border border-gray-300 p-1 w-full"
                      />
                    </td>
                    <td className="border px-4 py-2 text-center">
                      {payment.phoneNumber}
                    </td>
                    <td className="border px-4 py-2 text-center">
                      {payment.isPaid ? "Yes" : "No"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ManagePayment;
